testcaseID = input("Enter testcase ID: ")
if testcaseID.startswith("TC-"):
    if testcaseID[3:].isdigit() and len(testcaseID) == 6:
        print("Testcase ID is valid,All good")
    else:
        print("Testcase ID is invalid, must start with TC- followed by 3 digits")
else:
    print("Testcase ID is invalid")

