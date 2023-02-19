$ oc new-app redis:6.2 --name=my-redis


$ oc expose deployment/my-redis --port=6379 --name=my-redis-service

$ oc get svc my-redis-service

$ redis-cli -h <IP address of the Redis service>
