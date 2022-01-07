import requests

def get_data(): #STEP 1: Get data from server

    """
    This function get the data from server using the Requests library. If the status code of response is [200]
    save JSON data as a dictionary and finaly return a copy.
    """


    url = 'https://mach-eight.uc.r.appspot.com/' #endpoint
    response = requests.get(url) #Get the response from server

    if response.status_code == 200:
        payload = response.json() #Dic
        results = payload.get('values', [])#Save just the data in results variable 

        if results:
            return results.copy()

def sort_players(data): #STEP 2: Arrange from lowest to highest according to height in inches

    """
    This function uses the Merge-Sort algorithm to arrange the data from lowest yo highest according
    to height in inches. This algo divide que whole problem in pieces and then put the parts together 
    already ordered.
    """

    if len(data) <= 1: #Look if data can be sorted
        return
    
    mid = len(data) // 2 #Floor division
    left_side = data[:mid] #Left side data
    right_side = data[mid:] #Right side data

    #recursion for both data sides
    sort_players(left_side)
    sort_players(right_side)

    #Help Index
    left_index = 0 #left Index
    right_index = 0 #right Index
    data_index = 0 #merged data Index

    
    while left_index < len(left_side) and right_index < len(right_side): #Side-index must be less than side-length
        if left_side[left_index]['h_in'] < right_side[right_index]['h_in']: #if left-side data is < to right-side
            data[data_index] = left_side[left_index] #Merged-data in that index will be the left side data value
            left_index += 1 #increment left index
        else: #if left-side data is >= to right-side
            data[data_index] = right_side[right_index]#Merged-data in that index will be the right side data value
            right_index += 1 #increment right index
        data_index += 1 #increment data index

    if left_index < len(left_side):
        del data[data_index:] #delete all data after data-index
        data += left_side[left_index:] #add left side value to data
    elif right_index < len(right_side):
        del data[data_index:] #delete all data after data-index
        data += right_side[right_index:]#add right side value to data

def search_pairs(data): #STEP 3: Search pairs according to user input

    """
    Here we take the user input and then search the pairs according to that input. We have some while loops
    to ask the user if want to make another try and validate some inputs.
    """

    data_len = len(data) #Get data length
    min_value = int(data[0]['h_in']) + int(data[1]['h_in']) #calculate min posible value 
    max_value = int(data[data_len - 1]['h_in']) + int(data[data_len - 2]['h_in']) #calculate max posible value

    option = "y"
    while(option == "y"): #This loop asks if user want another try. if option is "y" loop continues if option "n" loop breaks

        #Input validation
        user_input = input("Integer Input: ")
        try:
            user_input = int(user_input) #if input is a number, updates the user_input variable
        except:
            user_input = (-1) #if input is not a number, updates the user_input variable to -1

        
        if user_input < 0: #If input is less than 0
            print("Just positive integer numbers")

        elif user_input < min_value or user_input > max_value: #check if input is out of limits
            print("No matches found.")

        else: #if input is between the limits
            left_index = 0
            right_index = data_len - 1 


            """
            The search algorithm start evaluating from the limits of the dictionary (left and right) and make the sum and compare
            with the input.

            CASE 1: If the sum is greater than the input, subtract 1 from the right index

            CASE 2: If the sum is less than the input, subtract 1 from the left index

            CASE 3: If the sum is equal to the input, print the pair and check the following data by subtracting 1 from the right
                    index until the sum is different from the input. Then it performs the sum of the next left index and the right 
                    index, if it is equal to the input it prints the pair. If not, add one to the left index and subtract one from 
                    the right index.

            The loop ends when left_index is equal or grater than right_index
            """

            while left_index < right_index: #left-index must be smaller than right-index
                if int(data[left_index]['h_in']) + int(data[right_index]['h_in']) > user_input: #if the sum is grater than input
                    right_index -= 1
                    continue 

                elif int(data[left_index]['h_in']) + int(data[right_index]['h_in']) < user_input: #if the sum is smaller than input
                    left_index += 1
                    continue

                elif int(data[left_index]['h_in']) + int(data[right_index]['h_in']) == user_input: #if the sum is equal to imput
                    print(
                        data[left_index]['first_name'],data[left_index]['last_name'] #print left player
                        ,"<--->",
                        data[right_index]['first_name'],data[right_index]['last_name'] #print right player
                    )

                    if int(data[left_index]['h_in']) + int(data[right_index - 1]['h_in']) == user_input and right_index - left_index > 1:
                        aux_index = right_index - 1 #auxiliary index
                        while(True): #This loop checks the sum of the current left index with the next indexes on the right
                            print(
                            data[left_index]['first_name'],data[left_index]['last_name']
                            ,"<--->",
                            data[aux_index]['first_name'],data[aux_index]['last_name']
                            )
                            aux_index -= 1
                            if int(data[left_index]['h_in']) + int(data[aux_index]['h_in']) != user_input or aux_index - left_index <= 1:
                                break #when the sum is different from the input it is interrupted
                        

                    elif int(data[left_index + 1]['h_in']) + int(data[right_index]['h_in']) == user_input and right_index - left_index > 1:
                        print(
                            data[left_index + 1]['first_name'],data[left_index + 1]['last_name']
                            ,"<--->",
                            data[right_index]['first_name'],data[right_index]['last_name']
                            )
            
                    right_index -= 1
                    left_index += 1


        while True: #This loop validates the input to repeat the code or close it
            option = input("Again? [Y/N]").lower()
            
            if option == "y" or option == "n":
                break
            elif option != "y" or option != "n":
                print("Please write just [Y/N]")
                continue


if __name__ == '__main__':

    nba_players = get_data()  #STEP 1: Get data from server

    if nba_players:
        sort_players(nba_players) #STEP 2: Arrange from lowest to highest according to height in inches
        search_pairs(nba_players) #STEP 3: Search pairs according to user input
    else:
        print("There is not data")