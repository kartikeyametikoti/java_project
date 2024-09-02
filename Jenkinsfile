pipeline{
    agent any
    environment {
        DOCKER_IMAGE = 'my-python-app'
        DOCKER_TAG = 'latest'
        DOCKER_IMAGE_NAME = "${DOCKER_IMAGE}:${DOCKER_TAG}"
    stages{
        stage('getting git repo')
        {
            steps{
                git branch: 'main', credentialsId: 'mycredentials', url: 'https://github.com/kartikeyametikoti/java_project'
            }
        }
        stage('docker image build ')
        {
            steps{
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}")
                }
            }
        }
        stage('test')
        {
            steps
            {
                script{
                def container = docker.run(
                        "${DOCKER_IMAGE_NAME}"),
                        '-d -p 5000:5000',
                    }
            }
        }
       
    }
}
