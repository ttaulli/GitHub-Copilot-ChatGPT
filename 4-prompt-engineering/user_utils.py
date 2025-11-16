import json
from typing import Any, Dict, List


def map_user_ids_to_names(users: List[Dict[str, Any]]) -> str:
    """
    Convert a list of user objects into a JSON string that maps user IDs to names.

    Each user object should contain an ID and a name. Common key names are
    supported: 'id' or 'user_id' for the identifier and 'name' or
    'full_name' for the display name. IDs are converted to strings in the
    resulting JSON object.

    Args:
        users: List of dict-like user objects.

    Returns:
        A JSON-formatted string mapping user IDs to names.

    Example:
        >>> users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        >>> map_user_ids_to_names(users)
        '{"1": "Alice", "2": "Bob"}'
    """
    mapping: Dict[str, str] = {}

    for user in users:
        if not isinstance(user, dict):
            # skip entries that aren't mapping-like
            continue

        # find id
        uid = None
        for id_key in ("id", "user_id"):
            if id_key in user:
                uid = user[id_key]
                break

        # find name
        name = None
        for name_key in ("name", "full_name"):
            if name_key in user:
                name = user[name_key]
                break

        if uid is None or name is None:
            # skip incomplete user objects
            continue

        # use string keys for JSON consistency
        mapping[str(uid)] = str(name)

    return json.dumps(mapping)


def map_user_ids_to_names_pretty(users: List[Dict[str, Any]], indent: int = 2) -> str:
    """Return a pretty-printed JSON string (with indentation)."""
    mapping_json = json.loads(map_user_ids_to_names(users))
    return json.dumps(mapping_json, indent=indent)


__all__ = ["map_user_ids_to_names", "map_user_ids_to_names_pretty"]
