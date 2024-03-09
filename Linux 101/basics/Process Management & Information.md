## `ps` Process Information
The `man ps` page has lots of example commands.

Reccomended: Pipe the info with `| less -S` 

`ps` Print all process of current user

BSD and Unix options:

BSD: `ps aux` Show process of all users

Unix: `ps -ef` Show process of all users

`ps -eH` Show process of all users in Hierachy. (usefull)

`pstree` To show the process hierachy.

## `top` Process monitor 
Default order: CPU. Change refresh rate with `d`.

# Foreground and Background Process
There can be only __one foreground process__ at a time.
Multiple background processes.
### Suspend foreground process  `ctrl`**+**`Z`
This pauses the foreground process.
`jobs` will show that the process is stoped.
### Make foreground -> background process with `&`
Example: `xeyes &`
### Move background -> foreground. `fg`
Use the `fg` with the jobs process id (find it using `jobs`)
### Move foreground -> background. `bg`
Use the `bg` with the jobs process id (find it using `jobs`)

#### Quick Tip `| &> /dev/null`
When starting GUI apps, they may generate lots of stdout and stderr.
Simply redirect these to the blackhole: `| &> /dev/null` 

# Managing Processes
| Process State | relationship | Process State |
|-|-|-|
| [New] | **-->** | Running |
| Running | **<-->** | Stopped |
| Running | **<-->** | Sleeping |
| Running | **-->** | [Terminated] |
| Running | **-->** | Zombie |
| Zombie | **-->** | [Terminated] |

## `kill` (`kill -l` for list of kill commands) 

1 `kill -SIGHUP` process re-read config. Update without shutdown. (think busy web server)
`kill -1 PID`

19 `kill -SIGSTOP` stops process. 
`kill -19 PID`

15 `kill -SIGTERM` default. Process terminate. (polite)
`kill -5 PID`

9 `kill -SIGKILL` Terminate, without cleanup. (last resort)
`kill -9 PID`
__Example:__

`xeyes &` Start xeyes in the background 

`ps -ef | grep xeyes` List processes and filter for xeyes.

Find it's PID. (e.g. 69420)

Typically, you'd use this: `kill 69420`

## `pkill` kill with grep instead of PID. (kills all grep matches!!)
`pkill xeyes`

## Sleep
Pauses exec. for amound of time (in seconds).
E.g. `sleep 5`
