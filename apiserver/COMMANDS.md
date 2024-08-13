How to modify and test backend code. 


python manage.py shell

python manage.py runserver 0.0.0.0:8000 --settings=plane.settings.local

python manage.py create_dummy_data

From the root of `plane`, run `./setup.sh`

From `plane/web`, run `yarn dev` to modify front edit code. 

To modify backend code. 

curl http://localhost:8000/auth/get-csrf-token/

python manage.py show_urls

all_workspaces = Workspace.objects.all()

Similar endpoints to the one I want. 

Docker Compose and `docker run` are both tools for managing Docker containers, but they serve different purposes and have distinct features:

### Docker Run
- **Command-Line Utility**: `docker run` is a command-line tool used to start a single Docker container. It allows you to specify the container's configuration, such as environment variables, volumes, ports, and networks, directly in the command line.
- **Single Container Focus**: It is typically used for running one container at a time, though you can run multiple containers with separate `docker run` commands.
- **Ephemeral Configuration**: The configuration provided with `docker run` is usually ephemeral, meaning it is not stored persistently. Once the container stops, you need to re-specify the configuration if you want to run the container again.

### Docker Compose
- **Multi-Container Application**: Docker Compose is designed for defining and running multi-container Docker applications. It uses a YAML file (`docker-compose.yml`) to specify the configuration for all the containers in an application, including their images, environment variables, volumes, networks, and dependencies.
- **Orchestration and Management**: With Docker Compose, you can manage the entire lifecycle of an application, including starting, stopping, and scaling containers, in a more coordinated way. It is particularly useful for microservices architectures where multiple services need to interact.
- **Persistent Configuration**: The configuration is stored in the `docker-compose.yml` file, making it easier to version control and share among different environments or teams. This file provides a convenient way to document the architecture and configuration of your application.

### Key Differences
1. **Scope**: `docker run` is more suited for simple, single-container setups, while Docker Compose is designed for complex applications involving multiple containers.
2. **Ease of Use**: Docker Compose simplifies the management of multi-container applications, allowing you to start all services with a single command (`docker-compose up`), whereas `docker run` requires individual commands for each container.
3. **Configuration Management**: Docker Compose provides a more structured and persistent way to manage container configurations, making it easier to maintain and replicate environments.

In summary, `docker run` is best for straightforward, single-container deployments, while Docker Compose is ideal for orchestrating complex, multi-container applications.