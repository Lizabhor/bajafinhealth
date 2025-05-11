import requests

url = 'https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdjaTIyMTA4MyIsIm5hbWUiOiJMaXphIEJob3IiLCJlbWFpbCI6ImxpemFiaG9yMjIwMzg3QGFjcm9wb2xpcy5pbiIsInN1YiI6IndlYmhvb2stdXNlciIsImlhdCI6MTc0Njk2NTI4NSwiZXhwIjoxNzQ2OTY2MTg1fQ.5jVn_oF5MzDBVhC3gfrPLYg14riv1MzutipDf75TcAk'
}

data = {
    'finalQuery': 'SELECT p.AMOUNT AS SALARY,CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,FLOOR(DATEDIFF(CURDATE(), e.DOB) / 365.25) AS AGE, d.DEPARTMENT_NAME FROM PAYMENTS p JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID WHERE DAY(p.PAYMENT_TIME) != 1 ORDER BY p.AMOUNT DESC LIMIT 1'
}

response = requests.post(url, headers=headers, json=data)

print('Response Body:', response.json())