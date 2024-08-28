from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data Policy</title>
        <script>
            function handleSubmit(event) {
                event.preventDefault(); // Prevent the default form submission

                const userAcceptance = document.getElementById('userAcceptance').value;

                fetch('/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ user_acceptance: userAcceptance }),
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('responseMessage').innerText = data.message;
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }
        </script>
    </head>
    <body>
        <h1>Data Policy Acceptance</h1>
        <form id="acceptanceForm" onsubmit="handleSubmit(event)">
            <label for="userAcceptance">Do you accept the data policy?</label>
            <input type="text" id="userAcceptance" name="userAcceptance" required>
            <button type="submit">Submit</button>
        </form>
        <p id="responseMessage"></p>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    user_acceptance = data.get('user_acceptance', '').lower()
    if user_acceptance == 'yes':
        return jsonify(message='User accepted the data policy. The user can continue with the application.')
    else:
        return jsonify(message='User rejected the data policy. The user cannot continue with the application.')

if __name__ == '__main__':
    app.run()
