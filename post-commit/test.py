import commands

status, output = commands.getstatusoutput("curl -s -S -i -X POST http://builds-for-managers-ykezyp-post-commit.apps.eu46a.prod.ole.redhat.com/api/build -f -d 'developer=Dev&git=Git&project=proj'")

print(output)
print("This line will be printed.")
