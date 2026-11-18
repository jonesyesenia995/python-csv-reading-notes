# Read quoted CSV records: implementation

## What the example does

The csv reader handles embedded commas and quoted newlines. It returns strings and does not infer types or validate row widths.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"name,city\nAda,London\n"
```

Expected result:

```json
[
  [
    "name",
    "city"
  ],
  [
    "Ada",
    "London"
  ]
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
