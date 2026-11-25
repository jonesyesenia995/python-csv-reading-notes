# Ordered batch processing for Read quoted CSV records

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
```json
"name,city\nAda,London\n"
```

Result:
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

## Case 2

Input:
```json
"a,\"b,c\"\n"
```

Result:
```json
[
  [
    "a",
    "b,c"
  ]
]
```

## Case 3

Input:
```json
"\"line\nbreak\",x\n"
```

Result:
```json
[
  [
    "line\nbreak",
    "x"
  ]
]
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

The csv reader handles embedded commas and quoted newlines. It returns strings and does not infer types or validate row widths.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.
