import requests, hashlib

email = raw_input('Enter your email address: ');
response = requests.get("https://en.gravatar.com/" + hashlib.md5(email.lower()).hexdigest() + ".json")
# defaultJson = {"entry":[{"id":"44429977","hash":"49f5ccb1c81597a64e1ca5783b9bb270","requestHash":"ParvJain","profileUrl":"http:\/\/gravatar.com\/parvjain","preferredUsername":"parvjain","thumbnailUrl":"http:\/\/0.gravatar.com\/avatar\/49f5ccb1c81597a64e1ca5783b9bb270","photos":[{"value":"http:\/\/0.gravatar.com\/avatar\/49f5ccb1c81597a64e1ca5783b9bb270","type":"thumbnail"}],"name":{"givenName":"Parv","familyName":"Jain","formatted":"Parv Jain"},"displayName":"Parv Jain","aboutMe":"I am a Python, Django Developer, Security enthusiast. and loves to help people around me. I am also a web-app security enthusiast. there is an another personal blog where you can find all my write-ups about researches. i have found security vulnerabilities on websites like Feedly, Vodafone, Truecaller, Shiksha, Digital Inspiration, AndPictures and many more. i also have security acknowledgement on ebay.","currentLocation":"India","emails":[{"primary":"true","value":"parv.wutizup@gmail.com"}],"accounts":[{"domain":"blogger.com","display":"blogger.com","url":"http:\/\/www.blogger.com\/profile\/g116069047783016990964","userid":"g116069047783016990964","verified":"true","shortname":"blogger"},{"domain":"profiles.google.com","display":"profiles.google.com","url":"http:\/\/profiles.google.com\/116069047783016990964","userid":"116069047783016990964","verified":"true","shortname":"google"},{"domain":"linkedin.com","display":"n3g4tiv3element","url":"http:\/\/www.linkedin.com\/in\/n3g4tiv3element","username":"n3g4tiv3element","verified":"true","shortname":"linkedin"},{"domain":"tumblr.com","display":"parv-jain","url":"http:\/\/parv-jain.tumblr.com\/","username":"parv-jain","verified":"true","shortname":"tumblr"},{"domain":"twitter.com","display":"@p4rv_j","url":"http:\/\/twitter.com\/p4rv_j","username":"p4rv_j","verified":"true","shortname":"twitter"}],"urls":[{"value":"http:\/\/about.me\/parv_jain","title":"About Me"},{"value":"http:\/\/parv-jain.tumblr.com","title":"Personal Blog"}]}]}

if response.text == "\"User not found\"":
	alresponse = requests.get("https://en.gravatar.com/767fc9c115a1b989744c755db47feb60.json")
	defaultJson = alresponse.text
	print "email not assosicated with htttp://www.gravatar.com, sample portfolio app created though."

else:
	fo = open('assets/js/main.js', 'w')
	defaultJson = response.text

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