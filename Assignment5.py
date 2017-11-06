import ui

import random

#number_to_card = random.ranint(1,10)
#print(number_to_card)

#number_to_card2 = random.ranint(1,10)
#print(number_to_card2)

#number_to_card3 = random.ranint(1,10)
#print(number_to_card3)

#number_to_card4 = random.ranint(1,10)
#print(number_to_card4)

#number_to_card5 = random.ranint(1,10)
#print(number_to_card5)

#number_to_card6 = random.ranint(1,10)
#print(number_to_card6)

card = 0
card2 = 0
card3 = 0
card4 = 0
card5 = 0
card6 = 0
user_card_total = card + card2 + card3

computer_card_total = card4 + card5 + card6


def deal_my_card_touch_up_inside(sender):
    global card
    card = random.randint(1,10)
    view['textfield1'].text = str(card)
    global card
    card2 = random.randint(1,10)
    view['textfield2'].text = str(card2)
    # view['deal_my_card'].enabled = False

def deal_third_card_touch_up_inside(sender):

    global card3
    card3 = random.randint(1,10)
    view['textfield3'].text = str(card3)

def check_touch_up_inside(sender):
    
    global card4
    card4 = random.randint(1,10)
    view['textfield4'].text = str(card4)
    global card5
    card5 = random.randint(1,10)
    view['textfield5'].text = str(card5)
    global card6
    card6 = random.randint(1,10)
    view['textfield6'].text = str(card6)
    
    view['user_card_total_textfield'].text = str(card + card2 + card3)
    
    view['computer_card_total_textfield'].text = str(card4 + card5 + card6)
    
    user_card_total = card + card2 + card3
    computer_card_total = card4 + card5 + card6
    if all((user_card_total > 21,computer_card_total >21)):
         view['final_textfield'].text = 'Tie'
    elif user_card_total > 21:
         view['final_textfield'].text = 'computer win!'
    elif computer_card_total > 21:
         view['final_textfield'].text = 'you win!'
    elif user_card_total < computer_card_total:
         view['final_textfield'].text = 'computer win!'
    elif user_card_total > computer_card_total:
         view['final_textfield'].text = 'you win!'
    else:
       user_card_total == computer_card_total
       view['final_textfield'].text = 'tie!'


view = ui.load_view()
view.present('full_screen')
