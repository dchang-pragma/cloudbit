docker --version
docker run hello-world
docker run -d -p 80:80 --name webserver nginx
docker ps
docker ps -a #(show running & stopped)
docker
docker rmi nginx.
# ------------containers ------------------- #
docker build -t friendlyhello
docker images
docker run -p 4000:80 friendlyhello
docker login
docker tag friendlyhello dchangtech/cloudsense:newbie
docker push dchangtech/cloudsense:newbie


# -------- basic docker commands 1 & 2 --------- #
docker build -t friendlyname . # Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyname # Run "friendlyname" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyname # Same thing, but in detached mode
docker container ls # List all running containers
docker container ls -a # List all containers, even those not running
docker container stop <hash> # Gracefully stop the specified container
docker container kill <hash> # Force shutdown of the specified container
docker container rm <hash> # Remove specified container from this machine
docker container rm $(docker container ls -a -q) # Remove all containers
docker image ls -a # List all images on this machine
docker image rm <image id> # Remove specified image from this machine
docker image rm $(docker image ls -a -q) # Remove all images from this machine
docker login # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag # Tag <image> for upload to registry
docker push username/repository:tag # Upload tagged image to registry
docker run username/repository:tag # Run image from a registry



# ----------------services ----------------------- #
docker swarm init # initiate swarm from mac itself
docker stack deploy -c docker-compose.yml getstartedlab
docker container ls -q
docker stack rm getstartedlab
docker swarm leave --force

# --------------basic commands # 3 ------------#
docker stack ls                                            # List stacks or apps
docker stack deploy -c <composefile> <appname>  # Run the specified Compose file
docker service ls                 # List running services associated with an app
docker service ps <service>                  # List tasks associated with an app
docker inspect <task or container>                   # Inspect task or container
docker container ls -q                                      # List container IDs
docker stack rm <appname>                             # Tear down an application
docker swarm leave --force      # Take down a single node swarm from the manager


# -------------------swarms ------------------- #

# sudo lsof -PiTCP -sTCP:LISTEN
# netstat -ap tcp | grep -i "listen"


docker-machine create --driver virtualbox myvm1
docker-machine create --driver virtualbox myvm2
docker-machine ls
docker-machine ssh myvm1 "docker swarm init --advertise-addr 192.168.99.100" # initialize the swarm (cluster) and add myvm1 as the manager (first machine)

# to join as a manager; you will need to have myvm1 to leave the swarms
docker-machine ssh myvm1 "docker swarm join-token manager" # get information you need to join the swarm; the output should look like following

# to get token to join as a worker
docker-machine ssh myvm1 "docker swarm join-token worker"

docker-machine ssh myvm2 "docker swarm leave"

docker-machine ssh myvm2 "docker swarm join --token SWMTKN-1-0lhs05j4xxg7dqf4smxl2eiklgfd1ue5nop45sh8e4zg76w9nd-3jmllpj7jmq0wu28yslei5ido 192.168.99.100:2377"

docker-machine ssh myvm1 "docker node ls"

docker-machine env myvm1 # to get following output then run them to configure your shell to talk to myvm1 - swarm manager;

export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/Users/bunmaster/.docker/machine/machines/myvm1"
export DOCKER_MACHINE_NAME="myvm1"

eval $(docker-machine env myvm1)

# ----- deploy the app -------
docker stack deploy -c docker-compose.yml getstartedlab
docker stack ps getstartedlab

#Alternatively, you can wrap Docker commands in the form of docker-machine ssh <machine> "<command>", which logs directly into the VM but doesn’t give you immediate access to files on your local host.

docker stack rm getstartedlab
docker-machine ssh myvm2 "docker swarm leave"
docker-machine ssh myvm1 "docker swarm leave"

#unset environment variable
eval $(docker-machine env -u)

docker-machine stop $(docker-machine ls -q)               # Stop all running VMs
docker-machine rm $(docker-machine ls -q) # Delete all VMs and their disk images


# ------------------- commands #4 ---------------------#
docker-machine create --driver virtualbox myvm1 # Create a VM (Mac, Win7, Linux)
docker-machine create -d hyperv --hyperv-virtual-switch "myswitch" myvm1 # Win10
docker-machine env myvm1                # View basic information about your node
docker-machine ssh myvm1 "docker node ls"         # List the nodes in your swarm
docker-machine ssh myvm1 "docker node inspect <node ID>"        # Inspect a node
docker-machine ssh myvm1 "docker swarm join-token -q worker"   # View join token
docker-machine ssh myvm1   # Open an SSH session with the VM; type "exit" to end
docker node ls                # View nodes in swarm (while logged on to manager)
docker-machine ssh myvm2 "docker swarm leave"  # Make the worker leave the swarm
docker-machine ssh myvm1 "docker swarm leave -f" # Make master leave, kill swarm
docker-machine ls # list VMs, asterisk shows which VM this shell is talking to
docker-machine start myvm1            # Start a VM that is currently not running
docker-machine env myvm1      # show environment variables and command for myvm1
eval $(docker-machine env myvm1)         # Mac command to connect shell to myvm1
& "C:\Program Files\Docker\Docker\Resources\bin\docker-machine.exe" env myvm1 | Invoke-Expression   # Windows command to connect shell to myvm1
docker stack deploy -c <file> <app>  # Deploy an app; command shell must be set to talk to manager (myvm1), uses local Compose file
docker-machine scp docker-compose.yml myvm1:~ # Copy file to node's home dir (only required if you use ssh to connect to manager and deploy the app)
docker-machine ssh myvm1 "docker stack deploy -c <file> <app>"   # Deploy an app using ssh (you must have first copied the Compose file to myvm1)
eval $(docker-machine env -u)     # Disconnect shell from VMs, use native docker
docker-machine stop $(docker-machine ls -q)               # Stop all running VMs
docker-machine rm $(docker-machine ls -q) # Delete all VMs and their disk images

# ------------------ stack ----------------------- #
docker-machine create --driver virtualbox myvm1
docker-machine create --driver virtualbox myvm2
docker-machine ls
docker-machine ssh myvm1 "docker swarm init --advertise-addr 192.168.99.100"
docker-machine ssh myvm2 "docker swarm join --token SWMTKN-1-5zmv5gtva6oo4e64l30b985brhleg9se9iqdyvmzpdkozepifl-7jz3oilwosdvd3rmy0101c7zk 192.168.99.100:2377"
docker-machine env myvm1
eval $(docker-machine env myvm1)
docker stack deploy -c docker-compose.yml getstartedlab
docker-machine ssh myvm1 "mkdir ./data"
docker stack deploy -c docker-compose.yml getstartedlab
docker service ls # wait for 5 seconds

# ---------------------- cloud ---------------------- #
# create role arn: arn:aws:iam::410094167485:role/dockercloud-swarm-role
# create swarm from docker cloud
# wait 5-10 minutes until ec2 are provisioned and online
# set security grou to allo 80/8080

#docker run -ti --rm -v /var/run/docker.sock:/var/run/docker.sock dockercloud/registration

#docker run --rm -ti -v /var/run/docker.sock:/var/run/docker.sock -e DOCKER_HOST dockercloud/client dchangtech/swarm-mark-1

# error Unable to query docker version: Get https://192.168.99.100:2376/v1.15/version: x509: cannot validate certificate for 192.168.99.100 because it doesn't contain any IP SANs


# AWS swarm
# connect to AWS swarm via docker manager
docker node ls
cd /Users/bunmaster/python/aws/docker
ssh -i /Users/bunmaster/dchangtech.pem docker@54.91.241.198
mkdir ./data
docker stack deploy -c /Users/bunmaster/python/aws/docker/docker-compose.yml getstartedlab
docker stack services getstartedlab # list all services
docker stack ps getstartedlab # List the tasks in the stack
# ID                  NAME                         IMAGE                             NODE                            DESIRED STATE       CURRENT STATE           ERROR               PORTS
# vk4c8h19u2kb        getstartedlab_redis.1        redis:latest                      ip-172-31-29-231.ec2.internal   Running             Running 2 minutes ago                       
# naf29n2vswhz        getstartedlab_visualizer.1   dockersamples/visualizer:stable   ip-172-31-29-231.ec2.internal   Running             Running 2 minutes ago                       
# zgi7n2n6vtgi        getstartedlab_web.1          dchangtech/cloudsense:newbie      ip-172-31-20-70.ec2.internal    Running             Running 2 minutes ago                       
# 0f3dnw7tnkcn        getstartedlab_web.2          dchangtech/cloudsense:newbie      ip-172-31-20-70.ec2.internal    Running             Running 2 minutes ago                       
# 1838s7ce3vb4        getstartedlab_web.3          dchangtech/cloudsense:newbie      ip-172-31-29-231.ec2.internal   Running             Running 2 minutes ago                       
# ur4lx37c6w49        getstartedlab_web.4          dchangtech/cloudsense:newbie      ip-172-31-20-70.ec2.internal    Running             Running 2 minutes ago                       
# byk18yyzxuo7        getstartedlab_web.5          dchangtech/cloudsense:newbie      ip-172-31-29-231.ec2.internal   Running             Running 2 minutes ago                       

# stack - getstartedlab
# service - getstartedlab_web, getstartedlab_redis, getstartedlab_visualizer



# on each ec2
docker container ls # list all containers running

# from wokrer node
docker swarm leave
# from manager node
docker swarm rm ndfl2nxemkbf30f56cqiq8lkv

# from worker node

docker swarm join --token SWMTKN-1-1w9ydyr58h0fjhv7emr0bwapl4i2f61uwe3wavqadr57rip8tj-5lih1kgrd3kk0s584y1c6jxov 172.31.29.231:2377


# -------------- pet shop sample ----------------------
docker ps
docker stop cf8bc7cc1d3e















