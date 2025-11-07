pipeline {
    agent any
    
    environment {
        APP_NAME = 'jenkin-pipeline'
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
                    python3 -m pip --version || python3 -m ensurepip --upgrade
                    python3 -m pip install -r requirements.txt
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
        failure {
            echo 'Pipeline failed!'
        }
    }
}
