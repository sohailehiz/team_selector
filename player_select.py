from string import digits
import random
import streamlit as st
import pandas as pd

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3
# callback function to change the random number stored in state
def change_player_numbers():
    st.session_state["random_nos"] = random.sample(range(len_of_refined_list),len_of_refined_list)
    return
colstitle1,colstitle2,colstitle3 = st.columns(3)
colstitle2.title("PMP v1.0")
colstitle2.text("Pick My Players")
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)

get_players_names = st.text_area("Enter Player Names: ","")#
if get_players_names != "":
    get_players_names_raw = get_players_names.split('.')[1:]
    #print(get_players_names_raw)
    get_players_names_refined = []
    for player_name_raw in get_players_names_raw:
        remove_digits = str.maketrans('', '', digits)
        res = player_name_raw.translate(remove_digits)
        get_players_names_refined.append(res.replace(" ",""))
    print(get_players_names_refined)
    if len(get_players_names_refined) >= 10:
        len_of_refined_list = len(get_players_names_refined)
        if int(len(get_players_names_refined)/2) <= 7:
            game = st.selectbox('Football Type',['7 v 7','6 v 6','5 v 5'])
        elif int(len(get_players_names_refined)/2) <= 6:
            game = st.selectbox('Football Type',['6 v 6','5 v 5'])
        else:
            game = st.selectbox('Football Type',['5 v 5'])

        if game == '7 v 7':
            game_no = 7
        elif game == '6 v 6':
            game_no = 6
        elif game == '5 v 5':
            game_no = 5
            
        col1button, col2button, col3button = st.columns(3)
        if game_no*2 > len(get_players_names_refined):
            col2button.write("Select a different Football Type Players are Less")
        else:
            ## button to generate a new random player_numbers
            col2button.button("Generate Team Captain and Player Numbers", on_click=change_player_numbers)
            # initializing with a random number
            #if "random_nos" not in st.session_state:
                #st.session_state["random_nos"] = []#random.sample(range(len_of_refined_list),len_of_refined_list)
        
            try:
                random_nos = st.session_state.random_nos
                generate_player_number_random = {}
                for idx,player_name in enumerate(get_players_names_refined):
                    generate_player_number_random[random_nos[idx]] = player_name
                remove_list = [1,2]

                get_players_key = [i for i in list(generate_player_number_random.keys()) if i not in remove_list]#list(generate_player_number_random.keys())

                p1 = []
                p2 = []
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Team 1 Captain : "+generate_player_number_random[1])
                    p1 = st.multiselect(generate_player_number_random[1]+" Pick "+str(game_no-1)+" Player #'s",get_players_key, key = "p1")
                    #st.write('You selected:', p1)

                with col2:
                    st.subheader("Team 2 Captain : "+generate_player_number_random[2])
                    if len(p1) == game_no-1:
                        p2 = st.multiselect(generate_player_number_random[2]+" Pick "+str(game_no-1)+" Player #'s",intersection(get_players_key,p1), key = "p2")
                    else:
                        p2 = st.multiselect(generate_player_number_random[2]+" Pick "+str(game_no-1)+" Player #'s",[], key = "p2")
                        #st.write('You selected:', p2)
                get_selected_player_1_team = {}
                get_selected_player_2_team = {}
                for p_1 in p1:
                    get_selected_player_1_team[p_1] = generate_player_number_random[p_1]
                for p_2 in p2:
                    get_selected_player_2_team[p_2] = generate_player_number_random[p_2]
                if len(p1) == len(p2):
                    col1show, col2show, col3show = st.columns(3)
                    if col2show.button("Show Players"):
                        team1 = pd.DataFrame(get_selected_player_1_team.items(), columns=['Players #', 'Players Names'])
                        col1.table(team1)
                        team2 = pd.DataFrame(get_selected_player_2_team.items(), columns=['Players #', 'Players Names'])
                        col2.table(team2)
                    else:
                        col2show.text("")
            except:
                st.write("Click On Generating Team Captain and Players #s")
    else:
        st.write("Please Enter @ Least 10 Players")
st.text("\n\n\n\n How to Use the App")
colstep1, colstep2, colstep3 = st.columns(3)
colstep1.text("Copy Final List\nFrom WhatsApp Group and\npaste in the text area, as shown below: \nSunday 6-8pm \nPlace - Turfside - booked\n1. player I \n2. player II \n3. player III \n4. player IV \n5. player V \n6. player VI \n7. player VII \n8. player VIII \n9. player IX \n10. player X \n11. player XI \n12. player XII \n13. player XIII \n14. player XIV +I \n15. player XV \n\nWaitlist \n1. player M")
colstep3.text("Delete\nDate, Waitlist Location Just Keep\nthe Main Players, as shown below: \n1. player I \n2. player II \n3. player III \n4. player IV \n5. player V \n6. player VI \n7. player VII \n8. player VIII \n9. player IX \n10. player X \n11. player XI \n12. player XII \n13. player XIII \n14. player XIV +I \n15. player XV")
st.text("Click on Button to Generate Captain and Player Numbers")
st.text("Team Captain 1 can pick his/her Players based on the football Type")
st.text("Team Captain 2 Can ONLY pick his/her Players\nafter Team Captain 1 [Option will be available then]")
