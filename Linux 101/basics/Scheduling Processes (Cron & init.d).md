## cron
crontab: system-wide cron tab. (system maintence)
Example: `ll /etc/crontab.daily`

`crontab -l` List of personal crontab jobs.

`crontab -e` Open personal crontab.
You will be promted for text editor.

| m | h | dom | mon | dow | command |
|-|-|-|-|-|-|
| minute | hour | day-of-month | month | day-of-week (Sunday = 0) | Command to exec. at time |

Use `*` for every: min, hour, mon, dow.

m: `*/5` every 5 minutes.

`crontab -r` delete personal crontab.

