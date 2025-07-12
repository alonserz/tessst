# tessst
Application searches for a given substring in a randomly generated string CSV file.

# Quick start
```
docker compose up -d --build
```

# Web
Go to: http://localhost:8000/

# Usage
```
$ curl localhost:8000/find_substring/acccccc
["851e4bcb-d524-4d99-bc96-7504e2e83e23",false,"acccccc"]

$ curl localhost:8000/get_data_by_task_id/851e4bcb-d524-4d99-bc96-7504e2e83e23
{"52":{"string":"tgatgtgtgtacgttcctgaggattgaggaacctgagattattccagtgcttctagaagttaccttcacgtaccccccctcttttaactatcgctt","start":71,"end":78}}
```

# Endpoints
| Endpoint                         | Description  |
| --------------                   | ------------ | 
| `/find_substring/{substring}`    | Return json with created task id, task status and given substring |
| `/get_data_by_task_id/{task_id}` | Return json like `{string_index: {"string": string, "start": int1, "end": int2}}`. `string_index` is index of string in file, string is string which contains given substring, `start` and `end` are integer indexes where substring starts and ends        |
| /                                | Return html page                                                  |

# Generate new file
Use src/backend/generate_csv.py to generate new file
