# Installation of splash on Windows Home

- Install Oracle VirtualBox 
- Install docker toolbox exe from 
[here](https://github.com/docker/toolbox/releases)
- During installation uncheck virtual box and the install 
- Open CMD with admin right and type
```
bcdedit

bcdedit /set hypervisorlaunchtype off
```

- And then start docker-terminal 

```
docker pull scrapinghub/splash
docker run scrapinghub/splash
```

open another cmd and type
```
docker-machine ip
```

And the type 
```
http://ip_docker_machine:8050
```
on the web browser Splash starts running 