# Docker-Infra
IIEC RISE 1.0 DOCKER PROJECT 

ONJECTIVES :-
 -> This project is based on the implementation of Docker Infrastructure through Docker Compose.
 -> It lets user create the whole Docker Infrastructure for Wordpress , Jenkins just in one click.

WORK FLOW :-
 -> First the wordpress and mysql images launche containers.
 -> Both the containers are mounted by their respective persistent storage.
 -> Wordpress container gets connected to mysql container.
 -> For the connectivity of outside world to container , PAT is enabled.

REQUIREMENTS :-
 -> Redhat linux OS
 -> Internet Connectivity 
