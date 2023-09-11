from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.general import InternetGateway



with Diagram("HA cluster", show=False, direction="TB"):
    dns = Route53("dns")    
    igw = InternetGateway("this-igw")
    with Cluster("this (VPC)"):
      lb = ELB("collabra-alb-01")
      with Cluster("ap-south-1a (AZ)"):
        with Cluster("app-1-public-1 (subnet)"):
            lb >> Edge(color="firebrick", style="dashed") >> EC2("app-server-1")
      with Cluster("ap-south-1b (AZ)"):
        with Cluster("app-1-public-2 (subnet)"):
            lb >> Edge(color="firebrick", style="dashed") >> EC2("app-server-2")
             
  
    

    dns >> igw >> lb

