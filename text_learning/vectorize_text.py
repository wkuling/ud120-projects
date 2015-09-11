#!/usr/bin/python
for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        #temp_counter += 1
        if temp_counter < 200:
            path = os.path.join('..', path[:-1])
            print temp_counter, path
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            
            words = parseOutText(email)

            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            
            for ii in ["sara", "shackleton", "chris", "germani", "sshacklensf"]:
                words = words.replace(ii, " ")

            ### append the text to word_data
            
            word_data.append(words)
            
            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris

            if name == "sara":
                from_data.append(0)
            elif name == "chris":
                from_data.append(1)

            email.close()

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

