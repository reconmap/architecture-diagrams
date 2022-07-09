
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.database import MySQL
from diagrams.onprem.compute import Server
from diagrams.onprem.client import Client, User
from diagrams.onprem.inmemory import Redis
from diagrams.programming.language import PHP, Go, Typescript, Python
from diagrams.custom import Custom
from diagrams.generic.os import Android

with Diagram("Reconmap system architecture", show=True, direction="LR"):
    user = User("Pentester")

    with Cluster("Database"):
        apiDb = MySQL("API database")
        keycloakDb = MySQL("Keycloak database")
        apiDb - Edge(color="brown", style="dotted") - keycloakDb
    restApi = PHP("Rest API")
    webClient = Client("Web client")
    webClient >> restApi
    cli = Go("CLI")
    redis = Redis("Cache")
    keycloak = Custom("Keycloak", "resources/keycloak_icon_512px.png")
    agent = Go("Agent")
    mobileClient = Android("Mobile client")

    user >> webClient
    user >> cli
    user >> mobileClient
    
    with Cluster("Tools"):
        nmap = Custom("Nmap", "resources/nmap-2x.png")
        zap = Custom("OWASP Zap", "resources/owasp-zap.png")
        tools = [nmap, zap]

    cli >> tools
    agent >> tools

    keycloak >> restApi
    keycloak >> keycloakDb
    webClient >> keycloak
    restApi >> apiDb
    cli >> restApi
    mobileClient >> restApi
    restApi >> redis
    agent >> restApi

