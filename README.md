## Readme

### Description
A simple function to classify email by checking the diagnostic value


### Usage

```
from check_error_codes import classify_by_error_code
error = classify_by_error_code(diag_code)
print error
```

returns a dictionary with details below if found otherwise empty

```
{'code': '550 5.1.1', 'description': 'The mailbox specified in the address does not exist.', 'flag_as': 'bounced'}
```

### TODO
Edit the `basic_error_codes.csv` and `smtp-enhanced-status-codes-3.csv` to set the flag values