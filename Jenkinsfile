pipeline {
    agent any
    stages {
        stage('Getting Git Repo') {
            steps {
                git url: 'https://github.com/kartikeyametikoti/java_project', credentialsId: 'mycredentials'
            }
        }
        stage('Docker Image Build') {
            steps {
                script {
                    docker.build('my-python-app:latest')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run the Docker container
                    def app = docker.image('my-python-app:latest')
                    app.withRun('-d -p 5000:5000') { c ->
                        // Implement your test steps here
                        // For example, you might use a curl command to check if the app is running
                        sh 'curl http://localhost:5000'
                    }
                }
            }
        }
    }
}
