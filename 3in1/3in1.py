from flask import Flask, request, redirect, render_template_string, send_file

app = Flask(__name__)

@app.route('/')
def check_ua():
    user_agent = request.headers.get('User-Agent', '').lower()

    if 'micromessenger' in user_agent:
        return send_file('wechat.png', mimetype='image/jpeg')
    elif 'alipayclient' in user_agent:
        return redirect("https://qr.alipay.com/fkx19092rwrfit8qoafzl50")
    elif 'QQ' in user_agent:
        return send_file('QQ.png', mimetype='image/jpeg')
    else:
        html_content = f'''
        <html>
            <head>
                <title>扫码提示</title>
                <style>
                    body {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-family: Arial, sans-serif;
                    }}
                    .container {{
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>请使用微信/支付宝/QQ扫码</h1>
                    <h1>您的UA:{user_agent}</h1>
                </div>
            </body>
        </html>
        '''
        return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True, port=677)