import json

with open('users.json') as json_file:
    jsonDict = json.load(json_file)
    #print(jsonDict) #dictionary
    try:
    	print("in trying before")
    	print(jsonDict.len) #will cause exception
    	#print(jsonDict)
    	print("in trying after") #skipped
    except (TypeError):
    	print("TypeError is caught") 
    # except (AttributeError):
    # 	print("AttributeError is caught") 

    except (AttributeError): #skipped if there is no exception
    	print("AttributeError is caught")
    	for k, v in jsonDict.items():
     		print(k, v)

# all exception types - https://docs.python.org/3/library/exceptions.html#exception-hierarchy