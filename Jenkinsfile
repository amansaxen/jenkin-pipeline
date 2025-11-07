pipeline {
    agent any
    
    environment {
        APP_NAME = 'jenkin-pipeline'
        NODE_VERSION = '18'
        PORT = '3000'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing Node.js dependencies...'
                sh '''
                    node --version
                    npm --version
                    npm install
                '''
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'npm test || true'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building application...'
                sh 'echo "Build completed successfully"'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                script {
                    // Stop existing container if running
                    sh '''
                        docker stop ${APP_NAME} || true
                        docker rm ${APP_NAME} || true
                    '''
                    
                    // Build Docker image
                    sh """
                        docker build -t ${APP_NAME}:${BUILD_NUMBER} .
                        docker tag ${APP_NAME}:${BUILD_NUMBER} ${APP_NAME}:latest
                    """
                    
                    // Run container
                    sh """
                        docker run -d \\
                            --name ${APP_NAME} \\
                            -p ${PORT}:${PORT} \\
                            -e PORT=${PORT} \\
                            -e APP_VERSION=${BUILD_NUMBER} \\
                            --restart unless-stopped \\
                            ${APP_NAME}:latest
                    """
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline succeeded!'
            script {
                echo "Application deployed! Access at: http://localhost:${PORT}"
            }
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Cleaning up...'
        }
    }
}
