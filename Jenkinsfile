pipeline {
    agent any
    
    environment {
        APP_NAME = 'hello-world-app'
        PORT = '5000'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 --version
                    pip3 install -r requirements.txt
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    sh '''
                        docker stop ${APP_NAME} || true
                        docker rm ${APP_NAME} || true
                    '''
                    
                    sh """
                        docker build -t ${APP_NAME}:${BUILD_NUMBER} .
                        docker tag ${APP_NAME}:${BUILD_NUMBER} ${APP_NAME}:latest
                    """
                    
                    sh """
                        docker run -d \\
                            --name ${APP_NAME} \\
                            -p ${PORT}:5000 \\
                            --restart unless-stopped \\
                            ${APP_NAME}:latest
                    """
                }
            }
        }
    }
    
    post {
        success {
            echo "Application deployed! Access at: http://localhost:${PORT}"
        }
    }
}
