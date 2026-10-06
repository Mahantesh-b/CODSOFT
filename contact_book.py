# Contact Information: Store name, phone number, email, and address for each contact.
#  Add Contact: Allow users to add new contacts with their details.
#  View Contact List: Display a list of all saved contacts with names and phone numbers.
#  Search Contact: Implement a search function to find contacts by name or phone number.
#  Update Contact: Enable users to update contact details.
#  Delete Contact: Provide an option to delete a contact.
#  User Interface: Design a user-friendly interface for easy interaction


contacts={
              "rolex":{
        
        "phone":8967437876,
        "email":"rolex@gmail.com",
        "address":"#123,kuvempunagar,mysuru"

                },
              "ajmal":{
         
        "phone":9346428967,
        "email":"rolex@gmail.com",
        "address":"rajeevnagara,mysuru"
                },
              "tara":{
        
        "phone":  9874657873,
        "email":"tara@gmail.com",
        "address":"gunduravnagara@gmail.com"
        
              },
              "amruth":{
        
        "phone":8792340588,
        "email":"amruth@gmail.com",
        "address":"nanjumlige, mysuru"
        
              }
}
while True:
   print("1.view contacts")
   print("2.add contacts")
   print("3.search contacts")
   print("4.delete contacts")
   select=input("select one ")


   if select=="1":
    print(contacts)

   elif select=="2":
    def add_contacts():
        name=input("Enter the  contact name ")
        if name in contacts:
           print("contact is already saved")
        else:
           phone=input("enter the number ") 
           email=input("enter the   email ")
           address=input("enter the  address ")   

           contacts[name]={
               "phone":phone,
               "email":email,
               "address":address
            }
 
    add_contacts()
    print("contact added successfully")

   elif select=="3":
    search_contact=input("enter the contact which you want ")
    if search_contact in  contacts:
        print( contacts[search_contact])
    else:
        print("contact is not in phonebook")

   elif select=="4":
    delete_contact=input("which contact do you want to delete? ")
    contacts.pop(delete_contact)
    print("contact delete successfully")

   else:
    print("Invalid search")

    happy=input("back to menu,yes or no? ")
    if happy!="no":
      continue
    else:
      print("Thankyou")
      break
     
    



        
