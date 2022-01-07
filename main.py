import requests

def get_data():
    url = 'https://mach-eight.uc.r.appspot.com/' #endpoint
    response = requests.get(url) #Get the response from server
    #print(response)

    if response.status_code == 200:
        payload = response.json() #Dic
        results = payload.get('values', [])

        if results:
            return results.copy()

            #for player in results:
                #name = player['first_name']

def sort_players(data): #This function used to sort data by h_in 
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
        if left_side[left_index]['h_in'] < right_side[right_index]['h_in']:
            data[data_index] = left_side[left_index]
            left_index += 1
        else: #if left-side data is >= to right-side
            data[data_index] = right_side[right_index]
            right_index += 1
        data_index += 1

    if left_index < len(left_side):
        del data[data_index:] #delete all data after data-index
        data += left_side[left_index:]
    elif right_index < len(right_side):
        del data[data_index:]
        data += right_side[right_index:]

def search_pairs(data):
    data_len = len(data) #Get data length
    min_value = int(data[0]['h_in']) + int(data[1]['h_in']) #calculate min posible value
    max_value = int(data[data_len - 1]['h_in']) + int(data[data_len - 2]['h_in']) #calculate max posible value

    print("min:",min_value," & ","max:", max_value) #BORRAR ESTA MONDA ********************

    option = "y"
    while(option == "y"):

        #Input validation
        user_input = input("Integer Input: ")
        try:
            user_input = int(user_input)
        except:
            user_input = (-1)

        
        if user_input < 0:
            print("Just positive integer numbers")

        elif user_input < min_value or user_input > max_value: #check if input is out of limits
            print("No matches found.")

        else: #if input is between the limits
            left_index = 0
            right_index = data_len - 1 


            while left_index < right_index: #left-index must be smaller than right-index
                if int(data[left_index]['h_in']) + int(data[right_index]['h_in']) > user_input: #if the sum is grater than input
                    right_index -= 1
                    continue 

                elif int(data[left_index]['h_in']) + int(data[right_index]['h_in']) < user_input: #if the sum is smaller than input
                    left_index += 1
                    continue

                elif int(data[left_index]['h_in']) + int(data[right_index]['h_in']) == user_input: #if the sum is equal to imput
                    print(
                        data[left_index]['first_name'],data[left_index]['last_name'],left_index #print left player
                        ,"<--->",
                        data[right_index]['first_name'],data[right_index]['last_name'],right_index #print right player
                    )

                    if int(data[left_index]['h_in']) + int(data[right_index - 1]['h_in']) == user_input and right_index - left_index > 1:
                        aux_index = right_index - 1 #auxiliary index
                        while(True):
                            print(
                            data[left_index]['first_name'],data[left_index]['last_name'],left_index
                            ,"<--->",
                            data[aux_index]['first_name'],data[aux_index]['last_name'],aux_index
                            )
                            aux_index -= 1
                            if int(data[left_index]['h_in']) + int(data[aux_index]['h_in']) != user_input or aux_index - left_index <= 1:
                                break
                        

                    elif int(data[left_index + 1]['h_in']) + int(data[right_index]['h_in']) == user_input and right_index - left_index > 1:
                        print(
                            data[left_index + 1]['first_name'],data[left_index + 1]['last_name'],left_index + 1
                            ,"<--->",
                            data[right_index]['first_name'],data[right_index]['last_name'],right_index
                            )
            
                    right_index -= 1
                    left_index += 1


        while True:
            option = input("Again? [Y/N]").lower()
            
            if option == "y" or option == "n":
                break
            elif option != "y" or option != "n":
                print("Please write just [Y/N]")
                continue



if __name__ == '__main__':

    nba_players = get_data()
    sort_players(nba_players)
    search_pairs(nba_players)
