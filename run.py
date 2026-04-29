from flask import Flask, render_template, request, flash
from website import create_app

app = create_app()
app.secret_key = 'supersecretkey'  # Needed for flashing messages
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    email = "imadaarab46@gmail.com"
    name = "Imad Aarab"
    number = "+212 6 14 97 02 93"
    if request.method == 'POST':
        # Here you would typically send an email or save to a database
        flash(f"Thank you {name}, your message has been sent!", "success")
    return render_template('contact.html', email=email, name=name, number=number)
if __name__ == '__main__':
    app.run(debug=True)