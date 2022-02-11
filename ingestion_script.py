# Time spent: 90 min
import json
from models import Dataset


def read_data_file(filename: str) -> list:
    """Reads a data file - formatted as a newline separated list of JSON formatted records

    Args:
        filename: Name of file to read
    
    Returns:
        list of lines in the data file
    
    """
    raw_data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            raw_data.append(json.loads(line))

    return raw_data


def main():
    raw_data = read_data_file('sample_payload.txt')

    # Employee Company Position Job

    mapping = {
        'Employee': Dataset('Employee'),
        'Company': Dataset('Company'),
        'Position': Dataset('Position'),
        'Job': Dataset('Job')
    }

    for line in raw_data:
        source_table = line.pop('source_table')
        action = line.pop('action')
        timestamp = line.pop('timestamp')

        mapping[source_table].process_line(line, action, timestamp)
    
    for k, v in mapping.items():
        print(f'{k} Table:')
        for line in v._cache:
            print(line)


if __name__ == "__main__":
    main()

# Open Questions:

### 1

# Do we want to hard delete (completely remove from cache) or soft delete (fill in a 'deleted_at')
# --> At the cost of storage space, I think we should do soft deletes - you never know when you might need some data again.

### 2

# Record "40a36493-f450-4331-874c-5ef01aabe1d5" was not inserted before the 'UPDATE' was given
# In these situations - do we prefer the record to be inserted anyways or ignored?
# --> I think we should insert them anyways, then clean the duplicates later
# --> This means that for cases like the above (update comes before the insert) - there will be duplicate records.