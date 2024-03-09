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

## init.d (On startup)
`cd /etc/init.d` Scripts for starting processes related to cron.
These scripts are added by system.

`ls -d /etc/rc*.d` list of all "rc" run level. On boot a run level is chosen. 

Example:

__rc5__, (Desktop) run level 5 with GUI and networking enabled.

__rc3__, (Servers) networking enabled without GUI. 

All files in *rc* directory are symbolic links to scripts in /etc/init.d/...__s__ _or_ __k__

__s__ means the script exec. when service is started.

__k__ means the script exec. when service is killed.

Number is the hiearchy of service start. (1 is first). Since some processes are dependent.
