import requests, hashlib

email = raw_input('Enter your email address: ');
response = requests.get("https://en.gravatar.com/" + hashlib.md5(email.lower()).hexdigest() + ".json")
defaultJson = response.text

if response.text == "\"User not found\"":
	alresponse = requests.get("https://en.gravatar.com/22bd03ace6f176bfe0c593650bcf45d8.json")
	defaultJson = alresponse.text
	print "email not assosicated with htttp://www.gravatar.com, sample portfolio app created though."

script = """
Handlebars.registerHelper("ifvalue", function(conditional, options) {
    if (conditional == options.hash.equals) {
        return options.fn(this);
    } else {
        return options.inverse(this);
    }
});
var source = document.getElementById("myTemplate").innerHTML;
var template = Handlebars.compile(source);
var data = """+ defaultJson +"""
document.getElementById("placeholder").innerHTML = template(data);
"""

fo = open('assets/js/main.js', 'w')
fo.write(script)
fo.close()