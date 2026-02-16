"""Simple PubMed fetcher with improved filtering and error handling.

This module provides `fetch_pubmed_articles` which queries NCBI E-utilities
(`esearch` + `esummary`) and applies basic filters (year range, required
keywords in title/abstract). It includes clear error handling and logging.

Note: network calls to NCBI may be rate-limited; callers should respect
NCBI usage policies and provide an API key if needed.
"""
from typing import List, Dict, Optional, Any
import logging
import requests

logger = logging.getLogger(__name__)

class PubMedFetchError(Exception):
    pass

ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


def _safe_get(url: str, params: Dict[str, Any], timeout: int = 10) -> requests.Response:
    try:
        resp = requests.get(url, params=params, timeout=timeout)
        resp.raise_for_status()
        return resp
    except requests.RequestException as exc:
        logger.exception("Network error when contacting PubMed: %s", exc)
        raise PubMedFetchError(f"Network error when contacting PubMed: {exc}") from exc


def fetch_pubmed_ids(query: str, retmax: int = 100, api_key: Optional[str] = None) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": str(retmax),
        "retmode": "json",
    }
    if api_key:
        params["api_key"] = api_key

    resp = _safe_get(ESEARCH_URL, params)
    try:
        data = resp.json()
    except ValueError as exc:
        logger.exception("Invalid JSON from esearch: %s", exc)
        raise PubMedFetchError("Invalid JSON response from PubMed esearch") from exc

    try:
        idlist = data.get("esearchresult", {}).get("idlist", [])
        return [str(i) for i in idlist]
    except Exception as exc:
        logger.exception("Unexpected esearch response structure: %s", exc)
        raise PubMedFetchError("Unexpected esearch response structure") from exc


def fetch_pubmed_summaries(id_list: List[str], api_key: Optional[str] = None) -> List[Dict[str, Any]]:
    if not id_list:
        return []
    params = {
        "db": "pubmed",
        "id": ",".join(id_list),
        "retmode": "json",
    }
    if api_key:
        params["api_key"] = api_key

    resp = _safe_get(ESUMMARY_URL, params)
    try:
        data = resp.json()
    except ValueError as exc:
        logger.exception("Invalid JSON from esummary: %s", exc)
        raise PubMedFetchError("Invalid JSON response from PubMed esummary") from exc

    results = []
    try:
        result_map = data.get("result", {})
        for pid in id_list:
            entry = result_map.get(pid)
            if not entry:
                # skip missing entries
                continue
            results.append({
                "id": pid,
                "title": entry.get("title", ""),
                "pubdate": entry.get("pubdate", ""),
                "source": entry.get("source", ""),
                "summary": entry.get("sortfirstauthor", ""),
            })
        return results
    except Exception as exc:
        logger.exception("Unexpected esummary response structure: %s", exc)
        raise PubMedFetchError("Unexpected esummary response structure") from exc


def _year_from_pubdate(pubdate: str) -> Optional[int]:
    if not pubdate:
        return None
    # pubdate can be like '2020 Jan 15' or '2020'
    try:
        year = int(pubdate.strip().split()[0])
        return year
    except Exception:
        return None


def filter_articles(articles: List[Dict[str, Any]], year_from: Optional[int] = None,
                    year_to: Optional[int] = None, required_keywords: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    if not articles:
        return []
    required_keywords = [k.lower() for k in (required_keywords or [])]

    def keep(a: Dict[str, Any]) -> bool:
        year = _year_from_pubdate(a.get("pubdate", ""))
        if year_from and (year is None or year < year_from):
            return False
        if year_to and (year is None or year > year_to):
            return False
        if required_keywords:
            text = (a.get("title", "") + " " + a.get("summary", "")).lower()
            for kw in required_keywords:
                if kw not in text:
                    return False
        return True

    return [a for a in articles if keep(a)]


def fetch_pubmed_articles(query: str, retmax: int = 100, filters: Optional[Dict[str, Any]] = None,
                          api_key: Optional[str] = None) -> List[Dict[str, Any]]:
    """Fetch and filter PubMed articles.

    filters supported:
      - year_from: int
      - year_to: int
      - required_keywords: List[str]

    Raises `PubMedFetchError` on network or parsing errors.
    """
    filters = filters or {}
    ids = fetch_pubmed_ids(query, retmax=retmax, api_key=api_key)
    if not ids:
        return []
    summaries = fetch_pubmed_summaries(ids, api_key=api_key)
    try:
        return filter_articles(
            summaries,
            year_from=filters.get("year_from"),
            year_to=filters.get("year_to"),
            required_keywords=filters.get("required_keywords"),
        )
    except PubMedFetchError:
        raise
    except Exception as exc:
        logger.exception("Error when filtering articles: %s", exc)
        raise PubMedFetchError("Error when filtering PubMed articles") from exc


__all__ = [
    "fetch_pubmed_articles",
    "PubMedFetchError",
]
