def fetch_one_record(db, sql, params):
    return db.execute(sql, params, fetch_one=True)


def fetch_all_records(db, sql, params):
    return db.execute(sql, params)


def execute_record(db, sql, params=None):
    db.execute(sql, params, commit=True)


def convert_records(columns, records):
    if isinstance(records, list):
        record_list = []
        for record in records:
            new_record = {}
            for idx, column in enumerate(columns):
                new_record.update({
                    column.name: record[idx]
                })
            record_list.append(new_record)

        return record_list
    elif isinstance(records, tuple):
        new_record = {}
        for idx, column in enumerate(columns):
            new_record.update({
                column.name: records[idx]
            })

        return new_record
