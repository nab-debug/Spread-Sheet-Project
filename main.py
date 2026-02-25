import datetime 
import streamlit  as st 

st.set_page_config(page_title="SpreadSheet")

st.header("Kizzy Balance Spreadsheet", divider='rainbow')
st.subheader("Use This To Keep Track Of Payments") 

tab1, tab2 = st.tabs(["Money Recieved", "Total Balance"])

with tab1:
    money = st.text_input("How Much Money Did You Recieve?")

    button_clicked = st.button("click me") 
    date = st.date_input("When did you recieve payment: ", value=None)

    if money and date != None:
        try:
            clean_int = float(money)

            #date 
            if button_clicked:
                st.write(f"Payment of ${money} was recieve ", date)
                with open("payment.txt", "a") as file:
                    date_file = str(date) + " " +  str(money) + "\n"
                    file.write(date_file) 
        except ValueError:
            print("VALUEE ERROR")
with tab2:

    st.header("Total")


    balance_list = []
    price_list = []

    show_button = st.button("Show Total")
    if show_button:
        with open("payment.txt", "a") as file:
            for line in file:
                numbers = line.split()
                balance_list.append(numbers[0])
                balance_list.append(numbers[1] + "\n") 
                price_list.append(numbers[1])
            for number in range(0, len(balance_list), 2):
                #print(f"{balance_list[number]} ${balance_list[number+1]}")
                st.write(f"{balance_list[number]} ${balance_list[number+1]}")
            
            int_list = [float(price) for price in price_list]
            print(sum(int_list)) 

            st.header(f" Total Amount Recieved: ${sum(int_list)}")
            st.header(f"Total Amount Owed: ${50000-sum(int_list)}")
        
