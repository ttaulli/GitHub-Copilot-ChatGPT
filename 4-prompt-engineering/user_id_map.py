"""Utility: map user IDs to names and return JSON-formatted output.

Example usage:
    users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    json_str = map_user_ids_to_names(users)
    print(json_str)  # {"1": "Alice", "2": "Bob"}
"""

from typing import Iterable, Mapping, Any, Optional
import json


def map_user_ids_to_names(users: Iterable[Mapping[str, Any]], *, indent: Optional[int] = 2) -> str:
    """Return a JSON string mapping user IDs to names.

    Args:
        users: Iterable of mappings (each must contain 'id' and 'name').
        indent: Number of spaces for JSON indentation. Use ``None`` for compact output.

    Returns:
        A JSON-formatted string where keys are user IDs (converted to strings) and
        values are the corresponding user names.

    Notes:
        - Entries missing an 'id' or 'name' are skipped.
        - IDs are converted to strings so the resulting JSON object has string keys.
    """
    mapping = {}
    for u in users:
        try:
            uid = u['id']
            name = u['name']
        except Exception:
            # skip entries that are not mappings or missing required keys
            continue
        mapping[str(uid)] = name

    return json.dumps(mapping, ensure_ascii=False, indent=indent)


if __name__ == "__main__":
    sample_users = [
        {'id': 1, 'name': 'Alice'},
        {'id': '2', 'name': 'Bob'},
        {'id': 3, 'name': 'Carol'},
        {'name': 'NoID'},  # this entry will be skipped
    ]

    print(map_user_ids_to_names(sample_users))
