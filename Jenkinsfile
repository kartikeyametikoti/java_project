pipeline{
    agent any
    stages{
        stage('getting git repo')
        {
            steps{
                git branch: 'main', credentialsId: 'mycredentials', url: 'https://github.com/kartikeyametikoti/java_project'
            }
        }
        stage('build and run')
        {
            steps{
                bat 'javac main.java'
                
            }
        }
        stage('test')
        {
            steps
            {
                bat 'java main'
            }
        }
       
    }
}
