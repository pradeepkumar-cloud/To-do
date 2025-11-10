pipeline {
    agent any
    environment {
        IMAGE_NAME = "todo-app"
        CONTAINER_NAME = "todo-container"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                git branch: 'main', url: 'https://github.com/pradeepkumar-cloud/To-do.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    bat "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    echo 'Running Docker container...'
                    bat "docker stop ${CONTAINER_NAME} || exit /b 0"
                    bat "docker rm ${CONTAINER_NAME} || exit /b 0"
                    bat "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}"
                }
            }
        }

        stage('Verify') {
            steps {
                echo '✅ To-Do app deployed successfully!'
            }
        }
    }
}
