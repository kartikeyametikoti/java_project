pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-python-app'
        DOCKER_TAG = 'latest'
        DOCKER_IMAGE_NAME = "${DOCKER_IMAGE}:${DOCKER_TAG}"
    }

    stages {
        stage('Getting Git Repo') {
            steps {
                git branch: 'main', credentialsId: 'mycredentials', url: 'https://github.com/kartikeyametikoti/java_project'
            }
        }

        stage('Docker Image Build') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run Docker container
                    def container = docker.run(
                        "${DOCKER_IMAGE_NAME}",
                        '-d -p 5000:5000', // Run detached and map port 5000
                        true // Bind the container to the pipeline
                    )
                    
                    // Optional: Add a sleep time to allow the container to start
                    sleep(10)
                    
                    // Optionally, you can run tests against your container
                    sh 'curl http://localhost:5000'
                    
                    // Stop and remove the container after the tests
                    container.stop()
                }
            }
        }
    }
}
