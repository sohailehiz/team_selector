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

get_players_names = st.text_area("Enter Player Names: "," ")#
get_players_names_raw = get_players_names.split('.')[1:]
#print(get_players_names_raw)
get_players_names_refined = []
for player_name_raw in get_players_names_raw:
    remove_digits = str.maketrans('', '', digits)
    res = player_name_raw.translate(remove_digits)
    get_players_names_refined.append(res.replace(" ",""))
print(get_players_names_refined)

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

st.write("Number of players per team:",game_no)


    
# initializing with a random number
if "random_nos" not in st.session_state:
    st.session_state["random_nos"] = random.sample(range(len_of_refined_list),len_of_refined_list)

## button to generate a new random player_numbers
st.button("generate player numbers", on_click=change_player_numbers)

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
    st.header("Team 1 Captain : "+generate_player_number_random[1])
    p1 = st.multiselect("Pick a number",get_players_key, key = "p1")
    #st.write('You selected:', p1)

with col2:
    st.header("Team 2 Captain : "+generate_player_number_random[2])
    if len(p1) == game_no:
        p2 = st.multiselect("Pick a number",intersection(get_players_key,p1), key = "p2")
        #st.write('You selected:', p2)
get_selected_player_1_team = {}
get_selected_player_2_team = {}
for p_1 in p1:
    get_selected_player_1_team[p_1] = generate_player_number_random[p_1]

for p_2 in p2:
    get_selected_player_2_team[p_2] = generate_player_number_random[p_2]

if len(p1) == len(p2):
    
    team1 = pd.DataFrame(get_selected_player_1_team.items(), columns=['Players #', 'Players Names'])
    col1.table(team1)

    team2 = pd.DataFrame(get_selected_player_2_team.items(), columns=['Players #', 'Players Names'])
    col2.table(team2)
