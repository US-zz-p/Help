# Flask CSRF Problem

Hi everyone,

I have a weird problem with CSRF validation.

Running my app with "http://0.0.0.0:5001/" the Form CSRF validation Works Fine.

But when I changed to "http://192.168.0.106:5001/" the CSRF become invalid. (this is my Wi-Fi IP, I use it to access my laptop site with my smartphone)

I believe that the problem is because Flask won't set cookies for IP based domains.

I added to /etc/hosts : "192.168.0.106 myapp.dev" and I add to Config file: SERVER_NAME = 'myapp.dev:5001'

But the cookies still not working and therefore CSRF still invalid.

I'll appreciate if someone run my code in a different domain or IP to figure out what is wrong.

Code: https://github.com/USP/Flask

Running:  http://2gm8ql-flask-staging-usp.runnableapp.com:5001/

(refresh 2 times to get cookies)


Screenshots: https://github.com/USP/Flask/tree/master/static/img

Thank you very much,
John
