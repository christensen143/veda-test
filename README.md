# This is a sample CDK project

This project builds an api with Lambdas to do the following:

- GET - List of all locks
- GET /{id} - Information about a specific lock
- POST /{id} - Create a lock with the name provided in the path
- DELETE /{id} - Delete the lock specified in the path

### Example api calls:

Get all locks:

```
curl -X GET https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod
{"locks":["bar","foo","hello"]}
```

Get information about a specific lock:

```
curl -X GET https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/hello
"hello created: Wed Nov 17 2021 21:29:31 GMT+0000 (Coordinated Universal Time)"
```

Create a new lock:

```
curl -X POST https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/hello
The lock hello acquired.
```

Attempt to create a lock that is already taken:

```
curl -X POST https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/hello
Lock hello is in-use.
```

Delete a lock:

```
curl -X DELETE https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/hello
Successfully deleted lock hello.
```

Attempt to delete a lock that does not exist:

```
curl -X DELETE https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/hello
Lock hello does not exist.
```

This project is based heavily on the AWS example at this link https://docs.aws.amazon.com/cdk/latest/guide/serverless_example.html
