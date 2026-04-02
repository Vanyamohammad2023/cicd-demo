pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vanyamhd/todo-api"
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build & Test') {
            steps {
                echo 'Installing dependencies and running tests...'
                sh '''
                    pip install -r requirements.txt
                    pytest test_app.py -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed! To-Do API is live on Docker Hub!'
        }
        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}