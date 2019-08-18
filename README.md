AWS Serverless Notes

1. Globally install npm on your machine.
2. Create a local package.json for the project to pin the serverless version.
3. Then run `npm install` in the project folder.
4. You will be able to pin the serverless version because when you create package.json and run `npm install` a local node_modules folder will be created. That folder will have a path to serverless like this:
```
$ pwd
/Users/ankur/lambda_serverless_tutorial

$ ls -l ./node_modules/serverless/bin/serverless
-rwxr-xr-x  1 aagarwal  staff  1812 Oct 26  1985 ./node_modules/serverless/bin/serverless
```
5. Once you create a package.json, package-lock.json will also be created. You will be prompted to checkin that file.
The process will look like this:
```
$ npm install
npm notice created a lockfile as package-lock.json. You should commit this file.
```
You should commit package-lock.json as well. Please see:
[npm-install documentation](https://docs.npmjs.com/cli/install)

6.	Also create a Makefile (see the project Makefile) to do a cleaner deploy every time.
7. To deploy, run:
```
make deploy stage=<stage> accountid=<accountid>
```


Other references:

1. See [Issues using logging.basicConfig in AWS Lambda function](https://stackoverflow.com/questions/37703609/using-python-logging-with-aws-lambda)
