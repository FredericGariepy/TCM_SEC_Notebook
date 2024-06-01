import subprocess
#subprocess.call("calc")
# SAME AS
out =  subprocess.check_call(["cmd","/c","calc"])

out_whoami =  subprocess.check_output(["cmd","/c","whoami"])
# under the hood makes use of the create process function
print(out_whoami.decode())

out_ipconfig =  subprocess.check_output(["cmd","/c","ipconfig"])
ipconfig_arr = out_ipconfig.decode().split('\n')
for l in ipconfig_arr:
    if ('IP' in l):
        print(l)

print("end of Subprocess.py")
