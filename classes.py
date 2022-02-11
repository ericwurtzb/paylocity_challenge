class Dataset:
    
    def __init__(self, name):
        self.name = name
        self._cache = []

    def process_line(self, record, action, timestamp):
        if action == 'INSERT':
            self.insert(record, timestamp)
        if action == 'UPDATE':
            self.update(record, timestamp)
        if action == 'DELETE':
            self.soft_delete(record, timestamp)

    def insert(self, record, timestamp):
        record['created_at'] = timestamp
        self._cache.append(record)
    
    def update(self, new_record, timestamp):
        for i, old_record in enumerate(self._cache):
            if old_record['guid'] == new_record['guid']:
                new_record['updated_at'] = timestamp
                self._cache[i] == new_record
                return

        print(f"Could not find guid {new_record['guid']} to update")
    
    def hard_delete(self, new_record):
        for i, old_record in enumerate(self._cache):
            if old_record['guid'] == new_record['guid']:
                self._cache.pop(i)
                return

        print(f"Could not find guid {new_record['guid']} to delete")
    
    def insert_or_update(self, record):
        for i, old_record in enumerate(self._cache):
            if old_record['guid'] == record['guid']:
                self._cache[i] == record
                return

        print(f"Could not find guid {record['guid']} to update - inserting now")
        self.insert(record)

    def soft_delete(self, new_record, timestamp):
        for old_record in self._cache:
            if old_record['guid'] == new_record['guid']:
                old_record['deleted_at'] = timestamp

        print(f"Could not find guid {new_record['guid']} to soft delete")