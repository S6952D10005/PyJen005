pipeline {
    agent any

    // เช็ค GitHub ทุก 1 นาที ถ้ามี commit ใหม่จะ build อัตโนมัติ
    triggers {
        pollSCM('* * * * *')
    }

    environment {
        PYTHON     = 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
        DEPLOY_DIR = 'C:\\deploy\\PyJen005'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building PyJen005...'
                bat '"%PYTHON%" --version'
                bat '"%PYTHON%" -m py_compile calculator.py test_calculator.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                bat '"%PYTHON%" -m unittest -v test_calculator.py'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying to ${env.DEPLOY_DIR}..."
                bat 'if not exist "%DEPLOY_DIR%" mkdir "%DEPLOY_DIR%"'
                bat 'copy /Y calculator.py "%DEPLOY_DIR%\\calculator.py"'
                bat '"%PYTHON%" "%DEPLOY_DIR%\\calculator.py" 10 20'
            }
        }
    }

    post {
        success { echo 'Build, Test, Deploy สำเร็จ' }
        failure { echo 'Pipeline ล้มเหลว กรุณาตรวจสอบ log' }
    }
}
