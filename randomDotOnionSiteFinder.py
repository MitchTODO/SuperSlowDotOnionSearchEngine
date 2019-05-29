# Two imports random and requests
import random
import requests

# generates dot onion urls
class onionGenerator:
    listofACII = []
    def __init__(self):
        # create a list of acii charaters only found in .onion urls "1-7 a-z"
        # more info go https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
        for a in range(49,56):
            self.listofACII.append(chr(a))
        for b in range(97,123):
            self.listofACII.append(chr(b))

    def generator(self):
        url = "http://"
        # loop sixteen times to generate a random number between 0 and the length of acii list
        for sixteen in range(16):
            arePick = self.listofACII[random.randint(0,(len(self.listofACII) - 1))]
            url += arePick
        url += ".onion/"
        return (url)

# test onion url
class Tor:
    # returns a bool wether the url was successful
    def trySite(self,siteToTest):
        # tor needs to be running for python to hop through local proxy
        # if tor is not running false urls will be return
        session = requests.session()
        session.proxies = {}
        session.proxies['http'] = 'socks5h://localhost:9150'
        session.proxies['https'] = 'socks5h://localhost:9150'
        # make the request, timeout is set to 10 seconds
        try:
            r = session.get(siteToTest,verify=False,timeout=10)
            return True
        except:
            return False


#Known tor url's
knownUrl = 'https://www.facebookcorewwwi.onion/'
duckduckGoUrl = "http://3g2upl4pq6kufc4m.onion/"
torSearch = "http://xmh57jrzrnw6insl.onion/"

#save file of good onion urls
f = open("dotOnionSites.txt", "w")


def main():
    # create dot onion objects
    onionURL = onionGenerator()
    SendToTor = Tor()
    # ask user how many urls to test
    AmountToTest = input("How many urls do you want to test? ")
    # test user input
    try:
        AmountToTest = int(AmountToTest)
    except:
        raise ValueError('Please enter a Integer!')
    print ("Testing "+str(AmountToTest)+"!")
    # loop through user amount
    for urlAmount in range(AmountToTest):
        onionGeneratedUrl = (onionURL.generator()) # generate the url
        print ("Trying "+onionGeneratedUrl)
        response = SendToTor.trySite(onionGeneratedUrl) # try the url
        if (response == True):        # test the response
            f.write(onionGeneratedUrl)# if successful save the url
            print (onionGeneratedUrl+" is valid!")
            print ('\n')
        else:
            print (onionGeneratedUrl+" is Invalid!")
            print ('\n')
            pass
    f.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        f.close()
