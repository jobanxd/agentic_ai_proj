import time
import logging
from typing import Dict, Any
from hrmanager_agent.database.database import db

logger = logging.getLogger(__name__)

def execute_query(sql_query: str, query_type: str = "general") -> Dict[str, Any]:
    try:
        start_time = time.time()
        results = db.execute_query(sql_query)
        execution_time = (time.time() - start_time)*1000
        return {
            "query_succesful": True,
            "data": results,
            "record_count": len(results),
            "query_type": query_type,
            "execution_time_ms": round(execution_time, 2),
            "error": None
        }
    except Exception as e:
        logger.error("SQL query execution error: %s", e)
        logger.error("Query: %s", sql_query)
        return {
            "query_succesful": False,
            "data": [],
            "record_count": 0,
            "query_type": query_type,
            "execution_time_ms": 0,
            "error": f"Query executon failed: {str(e)}"
        }
    