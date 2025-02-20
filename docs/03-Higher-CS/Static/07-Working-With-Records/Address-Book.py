def populateContacts():
    from dataclasses import dataclass

    @dataclass
    class contact:
        Name : str
        Age : int
        PhoneNum : str
        WhatsApp : bool
        OutOfTen : float
    
    contacts = [contact] * 4 
    
    contacts[0] = contact("Bruce Taylor", 15,  "01123298567", True, 7.6)
    contacts[1] = contact("Gina Williams", 13, "01234567897", False, 4.9)
    contacts[2] = contact("Trevor Youngson", 18, "02222222222", False, 6.1)
    contacts[3] = contact("Tyler Ice", 12, "07777777777", True, 8.2)
    
    return contacts