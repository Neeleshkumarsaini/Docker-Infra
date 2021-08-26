
IIEC RISE 1.0 PROJECT 

OBJECTIVES :-
 -> This project is based on the implementation of Docker Infrastructure through Docker Compose.
 -> It lets user create the whole Docker Infrastructure for Wordpress , Jenkins just in one click.
 -> It can also run linux commands.
 -> It lets user to install and start the webserver easily in one click.
WORK FLOW FOR DOCKER INFRA :-
 -> First the wordpress and mysql images launch containers.
 -> Both the containers are mounted by their respective persistent storage.
 -> Wordpress container gets connected to mysql container.
 -> For the connectivity of outside world to container , PAT is enabled.

REQUIREMENTS :-
 -> Redhat linux OS
 -> Internet Connectivity 
