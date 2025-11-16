"""Small demo for `map_user_ids_to_names`.

Run this file to see an example mapping printed as JSON.
"""
from user_utils import map_user_ids_to_names_pretty


def main() -> None:
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"user_id": "3", "full_name": "Charlie"},
        {"id": 4, "name": None},  # incomplete -> skipped
        "invalid",
    ]

    print(map_user_ids_to_names_pretty(users))


if __name__ == "__main__":
    main()
