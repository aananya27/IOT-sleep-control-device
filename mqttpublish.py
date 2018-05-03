import paho.mqtt.publish as publish

publish.single("Anan/one" , "Hello" , hostname="test.mosquitto.org")
publish.single("Anan/two" , "World!" , hostname="test.mosquitto.org")

print("Done")
