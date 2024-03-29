import os
import getpass

print("""-------------------------------------------------------------  Password Authentication !! -----------------------------------------------------------------
""")


apass = "neelesh"
count=0



def yum_configure():
	os.system("sudo cp epel.repo dock.repo  epel-playground.repo epel-testing.repo root.repo rpmfusion-free-updates.repo rpmfusion-free-updates-testing.repo /etc/yum.repos.d/ ")
	print("Your yum is configured now check it by 'yum repolist' command.")
	x=input("Enter to continue...")

def webserver_configure():
	os.system("sudo yum install httpd")
	os.system("sudo systemctl start httpd")
	print("Webserver is configured successfully. ")
	x=input("Enter to continue...")

def date():
	os.system("date")
	x=input("Enter to continue...")
def cal():
	os.system("cal")
	x=input("Enter to continue...")
def ls():
	os.system("ls")
	x=input("Enter to continue...")

def docker_install():
	os.system("sudo yum install docker-ce --nobest -y")
	os.system("sudo systemctl start docker")
	os.system("sudo systemctl enable docker")
	os.system("sudo firewall-cmd --zone=public --add-masquerade --permanent")
	os.system("sudo firewall-cmd --zone=public --add-port=80/tcp")
	os.system("sudo firewall-cmd --zone=public --add-port=443/tcp")
	os.system("sudo firewall-cmd --reload")
	os.system("sudo systemctl restart docker")
	os.system("sudo yum install httpd")
	os.system("sudo systemctl enable httpd")
	print("Docker-CE successfully installed.")
	x=input("Enter to continue...")

def docker_pull():
	imgname=input("Enter image with version. for ex- centos:7 : ")
	os.system("sudo docker pull {}".format(imgname))
	print("{} image downloaded successfully.".format(imgname))
	x=input("Enter to continue...")

def docker_images():
	print("""
								Available Images
""")
	os.system("sudo docker images")
	x=input("Enter to continue...")

def docker_create_image():
	print("""
								Available Containers
""")
	os.system("sudo docker ps -a")
	own_image = input("Give name to your own image with version. for ex- myimage:v1 : ")
	which_cont = input("Container Name : ")
	os.system("sudo docker commit {0}{1}".format(which_cont,own_image))	
	x=input("Enter to continue...")

def docker_remove_image():
	print("""
								Available Images
""")
	os.system("sudo docker images")
	rem_image = input("Image name with version. for ex- myimage:v1 : ")
	os.system("sudo docker rmi {}".format(rem_image))
	print("{} image successfully removed.".format(rem_image))
	x=input("Enter to continue...")

def docker_running_container():
	os.system("sudo docker ps")
	x=input("Enter to continue...")

def docker_all_container():
	print("""
								All Containers
""")
	os.system("sudo docker ps -a")
	x=input("Enter to continue...")

def docker_start():
	print("""
								Available Containers
""")
	os.system("sudo docker ps -a")
	start = input("Container Name : ")
	os.system("sudo docker start {}".format(start))
	print("{} container start successfully.".format(start))
	x=input("Enter to continue...")

def docker_stop():
	print("""
								Running Containers
""")
	os.system("sudo docker ps")
	stop = input("Container Name : ")
	os.system("sudo docker stop {}".format(stop))
	print("{} container stopped successfully.".format(stop))
	x=input("Enter to continue...")

def docker_terminate():
	print("""
								All Containers
""")
	os.system("sudo docker ps -a")
	terminate = input("Container Name : ")
	os.system("sudo docker stop {}".format(terminate))
	print("{} container terminated successfully.".format(terminate))
	x=input("Enter to continue...")

def new_container():
	print("""
								Available Images
""")
	os.system("sudo docker images")
	cont_name=input('Container Name : ')
	img_name = input('Enter image name with version. for ex- centos:7 : ')
	os.system("sudo docker run -dit --name {} {}".format(cont_name,img_name))
	print("{} container created successfully.".format(cont_name))
	##print("press 'left ctrl' and hold 'p' and 'q' to deattach.")
	x=input("Enter to continue...")

def docker_attach():
	print("""
								Available Containers
Note : You can only attach to the running container.
""")
	os.system("sudo docker ps")
	attach = input("Container name to attach.")
	os.system("sudo docker attach {}".format(attach))
	print("press 'left ctrl' and hold 'p' and 'q' to detach.")
	x=input("Enter to continue...")

def remove_container():
	print("""
								Available Containers
""")
	os.system("sudo docker ps -a")
	remove = input("Container Name or ID : ")
	os.system("sudo docker rm -f {}".format(remove))
	print("{} container removed successfully.".format(remove))
	x=input("Enter to continue...")

def remove_all_container():
	print("""
								Available Containers
""")
	os.system("sudo docker ps -a")
	print("Warning not recommended.")
	os.system("sudo docker rm -f $(docker ps -a)")
	print("successfully removed all containers.")
	x=input("Enter to continue...")

def show_volume():
	os.system("sudo docker volume ls")
	x=input("Enter to continue...")

def create_volume():
	vol=input("volume name.")
	os.system("sudo docker create volume {}".format(vol))
	print("successfully created volume. {}".format(vol))
	x=input("Enter to continue...")

def remove_volume():
	print("""
								Available Volumes
""")
	os.system("sudo docker volume ls")
	rem_vol=input("volume name.")
	os.system("sudo docker volume rm {}".format(rem_vol))
	print("successfully removed volume. {}".format(rem_vol))
	x=input("Enter to continue...")
	
def container_ip():
	con_name=input("Container name.")
	os.system("sudo docker inspect --format {{.NetworkSteetings.IPAddress}} {}".format(con_name))
	x=input("Enter to continue...")

def docker_cpu():
	print("If you stuck in between press 'left ctrl' + 'c' + os.system('watch -n 1 free -m')")
	os.system("watch -n 1 free -m")
	x=input("Enter to continue...")

def active_port():
	os.system("sudo netstat -tnlp")
	x=input("Enter to continue...")

def wordpress():
	os.system('sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
	os.system("sudo chmod +x /usr/local/bin/docker-compose")
	os.system("sudo cp docker-compose.yml /") 
	os.system("sudo cd / ")
	os.system("sudo mkdir /infrastructure")
	os.system("sudo cd /infrastructure/")
	os.system("sudo pwd")
	os.system("sudo mv ../docker-compose.yml .")
	os.system("sudo docker-compose up -d")
	print("Wordpress is ready to use. Run Wordpress in browser with Base OS IP and port no. : 8080. for ex- 192.168.43.139:8080")
	x=input("""
Details :
	MYSQL_ROOT_PASSWORD : rootpass
	MYSQL_USER : neelesh
	MYSQL_PASSWORD : redhat
	MYSQL_DATABASE : db
	Container : neelesh
	Image : mysql:5.7
Press Enter to continue...""")

def docker_jenkins():
	print("""
								Available Images
""")
	os.system("sudo docker images")
	jen_name=input('\nContainer Name : ')
	img_name = input('Enter image name with version. for ex- centos:7 : ')
	os.system("sudo docker run -dit --name {} {}".format(jen_name,img_name))
	print("downloading jenkins....")
	os.system("sudo sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat/jenkins.repo")
	os.system("sudo rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key")
	os.system("sudo yum install jenkins")
	print("Jenkins is ready to use. Run Jenkins in browser with Container IP and port no. : 8080. for ex- 192.168.43.139:8080")
	print("""
Details :
	Container : {0}
	Image : {1}	""".format(jen_name,img_name))

	print("{} container created successfully.".format(jen_name))
	x=input("Enter to continue...")
	



while count < 3:
	passwd = getpass.getpass("								Enter Password : ")
	if apass != passwd:
		print("Try Again!!")
		count+=1
	else:
		while True:	
			os.system("clear")
			os.system("tput setaf 2")

			print("""
							   Welcome to Menu
							  ________________________
								  Images
								  ------
			1 Docker Install		2 Available Docker Images	3 Download Docker Image
			4 Create Image			5 Remove Image
								 Containers
								 ----------
 			6 Show Running Containers	7 Attach Container 		8 All Containers
			9 Launch Container		10 Stop Container Service	11 Start Container Service
			12 Delete Container 		13 Delete All Containers	14 Show Container IP
								Infrastructure
								--------------
			15 Launch Wordpress		16 Launch Jenkins			
								   Volume
								   ------
			17 Create Volume		18 See Volumes			19 Remove Volume
								  
								  Settings
								  --------
			20 Yum Configuration 		21 Monitor Docker CPU		22 Active Ports
								  Webserver
								  ---------

23 Install and Configure webserver 
								Basic Linux Commands
								--------------------
24 See Date			25 See Calendar		26 List of files and folders
			
			27 Exit""")
			
			os.system("tput setaf 7")
			ch=int(input("Enter your choice. "))


			if ch == 1:
				docker_install()
				continue
			elif ch == 2:
				docker_images()
				continue				
			elif ch == 3:
				docker_pull()
				continue
			elif ch == 4:
				docker_create_image()
				continue
			elif ch == 5:
				docker_remove_image()
				continue
			elif ch == 6:
				docker_running_container()
				continue			
			elif ch == 7:
				docker_attach()
				continue
			elif ch == 8:
				docker_all_container()
				continue
			elif ch == 9:
				new_container()
				continue
			elif ch == 10:
				docker_stop()
				continue
			elif ch == 11:
				docker_start()
				continue
			elif ch == 12:
				remove_container()
				continue			
			elif ch == 13:
				remove_all_container()
				continue
			elif ch == 14:
				container_ip()
				continue
			elif ch == 15:
				wordpress()
				continue
			elif ch == 16:
				docker_jenkin()
				continue
			elif ch == 17:
				create_vumeol()
				continue
			elif ch == 18:				
				show_volume()
				continue
			elif ch == 19:
				remove_volume()
				continue
			elif ch == 20:
				yum_configure()
				continue
			elif ch == 21:
				docker_cpu()
				continue			
			elif ch == 22:
				active_port()
				continue
			elif ch == 23:
				webserver_configure()
				continue
			elif ch == 24:
				date()
				continue
			elif ch == 25:
				cal()
				continue
			elif ch == 26:
				ls()
				continue
			elif ch == 27:
				exit()
		else:
			print("Not Found.")
			x=input("Retry...")
else:
	print("Try again !", end="")
	x=input("Enter to exit...")
