# Automatic updater script for goin-up-the-country
# by Pugduddly

import os, subprocess, pickle

# Main function
def main():
    print "goin-up-the-country auto updater"
    
    # Check if git is installed
    try:
        # Pipe output to /dev/null for silence
        null = open("/dev/null", "w")
        subprocess.Popen("git", stdout=null, stderr=null)
        null.close()

    except OSError:
        print("Error: git is not installed!\nPlease install git for automatic updating to work and then clone this repository.\nThis won't work if you use the downloaded zip file.\nTip: If you don't know how to do any of this, Google is your best friend.")
        exit(0)
    
    # Get origin URL of repository
    p = subprocess.Popen(["git", "config", "--get", "remote.origin.url"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    originURL = stdout.split("\n")[0]
    
    print "Origin URL: %s" % originURL
    
    # Get latest commit ID of repository
    p = subprocess.Popen(["git", "ls-remote", originURL], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = subprocess.check_output(["grep", "refs/heads/master"], stdin=p.stdout)
    p.wait()
    latestCommit = output.split("\t")[0]
    
    print "Latest commit: %s" % latestCommit
    
    dataFile = "../../latestversion.dat"
    
    # Check if update version file thingy doesn't exist
    if os.path.isfile(dataFile):
        # Load last checked commit and origin URL from file
        print "Loading file..."
        fileObject = open(dataFile, "r")
        fileData = pickle.load(fileObject)
        fileObject.close()
        print "Done!"
        
        # Compare last checked origin URL and current URL
        if fileData["originURL"] != originURL:
            print "Warning: origin URL has changed! This might be a problem!"
        
        if fileData["latestCommit"] != latestCommit:
            # We found a new commit!
            # Let's download it!
            print "New commit found, downloading..."
            os.system("git pull")
            print "Done!"
    
    # Save latest commit ID and origin URL to file
    print "Saving file..."
    fileObject = open(dataFile, "wb")
    pickle.dump({"originURL": originURL, "latestCommit": latestCommit}, fileObject)
    fileObject.close()
    print "Done!"
    
    print "Auto updater has finished"

# main() won't be called if this file is loaded as a library for some weird reason
if __name__ == "__main__":
    main();
