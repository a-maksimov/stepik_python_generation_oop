def log_for(logfile, date_str):
    with (
        open(logfile, 'r', encoding='utf-8') as log,
        open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as output
    ):
        [
            output.write(line.replace(date_str, '').lstrip())
            for line in log.readlines() if line.startswith(date_str)
        ]