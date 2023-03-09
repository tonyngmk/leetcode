"""Python demo for sorting using VS Code Debug Visualizer."""

# https://hediet.github.io/visualization/docs/visualization-data-schema.json

def serialize(arr, compare_idx=0, target_idx=0):
    """Serialize an array into a format the visualizer can understand."""
    formatted = {
        "kind": {"grid": True},
        "rows": [
            {
                "columns": [
                    {"content": str(value), "tag": str(value)} for value in arr
                ],
            }
        ],
         "markers": [
        {
            "row": 0,
            "column": compare_idx,
            "id": "compare_idx",
            "id": "compare_idx"
        },
        {
            "row": 0,
            "column": target_idx,
            "id": "target_idx",
            "id": "target_idx"
        }
    ]
    }
    return formatted


arr = [6, 9, 3, 12, 1, 11, 5, 13, 8, 14, 2, 4, 10, 0, 7]

# Put serialized into the Debug Visualizer console
serialized = serialize(arr)

# Set a breakpoint on the line below and go through the code in debug mode to
# watch it update
for target_idx in range(1, len(arr)):
    target_value = arr[target_idx]
    compare_idx = target_idx - 1

    while compare_idx >= 0 and arr[compare_idx] > target_value:
        arr[compare_idx + 1] = arr[compare_idx]
        serialized = serialize(arr, compare_idx, target_idx)
        compare_idx -= 1

    arr[compare_idx + 1] = target_value
    serialized = serialize(arr, compare_idx, target_idx)

assert arr == sorted(arr)