import requests, hashlib

email = raw_input('Enter your email address: ');

response = requests.get("https://en.gravatar.com/" + hashlib.md5(email.lower()).hexdigest() + ".json") 

fo = open('assets/js/main.js', 'w')
fo.write("""
	var source = document.getElementById("myTemplate").innerHTML;
var template = Handlebars.compile(source);
var data = """+ response.text +"""

document.getElementById("placeholder").innerHTML = template(data);
	""")
fo.close()