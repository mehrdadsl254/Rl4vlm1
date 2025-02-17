import torch
import random
from typing import List

def get_prompt(env_name, action_only, infos = None):
    """
        This function defines the prompt for the text-to-action task, depending on the environments
        env_name: determines the prompts for each environment
        info: additional information that can be added to the prompt, if none, then use the default prompt
    """
    if env_name == 'gym_cards/NumberLine-v0':
        qs = "You are playing a game called number line. You will see a target number and a current number in the image. "
        qs = qs + "And your goal is to move the current number closer to the target by choosing either adding or subtracting one to the current number. "
        qs = qs + "Your response should be a valid json file in the following format: \n{\n "
        if not action_only:
            qs = qs + "\"current number\": \"x\", \n"
            qs = qs + "\"target number\": \"x\", \n"
            qs = qs + "\"thoughts\": \"{first read out the current and target number, then think carefully about which action to choose}\", \n"
        qs = qs + "\"action\": \"-\" or \"+\" \n}"
    elif env_name == 'gym_cards/Blackjack-v0':
        qs = "You are a blackjack player. You are observing the current game state, you can choose between ['stand', 'hit']. "
        qs = qs + "Your response should be a valid json file in the following format: \n{\n "
        if not action_only:
            qs = qs + "\"thoughts\": \"{first describe your total points and the dealer's total points then think about which action to choose}\", \n"
        qs = qs + "\"action\": \"stand\" or \"hit\" \n}"
    elif env_name == 'gym_cards/EZPoints-v0': 
        try:
            text_formula = ''.join(str(element) for element in infos[0]['Formula'])
        except:
            text_formula = ''
        qs = "You are an expert card game player. You are observing two cards in the image. "
        qs = qs + f"You are observing the current formula: {text_formula}. "
        qs = qs + "You can choose between ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '+', '*', '=']. "
        qs = qs + "The number or operator you choose will be appended to the current formula. "
        qs = qs + "Note that 'J', 'Q', and 'K' count as '10'. "
        qs = qs + "Your goal is to output a formula that evaluates to 12, and each number can only be used once. "
        qs = qs + "Your response should be a valid json file in the following format: \{\n"
        if not action_only:
            qs = qs + " \"cards\": [x, y], \n"
            qs = qs + f"\"current formula\": {text_formula}, \n"
            qs = qs + "\"thoughts\": {First check whether the current formula 'z' is complete. "
            qs = qs + "If the current formula 'z' is complete, output '='. "
            qs = qs + "Otherwise consider which number or operator should be appended to the current formula to make it equal 12.} \n"
        qs = qs + "\"action\": \"{number}\" or \"{operator}\" \n \}"    
            
            
            
            
            
            
            
        # print(f"-------------------text fomula:{text_formula}--------------")
        # #what to do if it is invalid like +3 adn
        # qs = "You are an expert card game player. You are observing two cards in the image. "
        # qs += f"You are given the current formula as: '{text_formula}'. if {text_formula} that is invilid fomula like +4 or ++ , give the action: \"=\" "
        # qs += "You can choose between the following options: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '+', '*', '='] but note tha the number you choose should be between t cards. "
        # qs += "The number or operator you choose will be appended to the current formula and note that after an operator should be a number and after a number should be an operator. "
        # qs += "Note that 'J', 'Q', and 'K' count as '10'. "
        # qs += f"Your goal is to create a formula that evaluates to 12, with each number used only once and if the current formula that is :{text_formula} evalutes 12 you should just respose the action:\"=.\" "
        # qs += "Your response must be a valid JSON object with exactly the following keys: "
        # qs += "\"cards\": a list of two numbers representing the cards, "
        # if text_formula == "":
        #     qs += f"\"formula\":\"\"(this is now empty) "
        # else:
        #     qs += f"\"formula\": {text_formula} note that till now the cuurent formula you should set is {text_formula},"
        # qs += "\"thoughts\": a string explaining your reasoning (e.g., what the current formula is and why you chose the next move), "
        # qs += "and \"action\": a string representing the number or operator you choose to append. "
        # qs += "Do not include any extra text outside of the JSON object. "
        # qs += "Here are two examples of valid responses:\n\n"
        # qs += "Example 1:\n"
        # qs += "{\"cards\": [4, 3], \"formula\": \"3\", \"thoughts\": \"'3' is incomplete; appending '*' gives '3*4'=12.\", \"action\": \"*\"}\n\n"
        # qs += "Example 2:\n"
        # qs += "{\n  \"cards\": [2, 6],\n  \"formula\": \"\",\n  \"thoughts\": \"The current formula is empty, so I choose '2' to start.\",\n  \"action\": \"2\"\n}"
        # qs += "Example 3:\n"
        # qs += "{\n  \"cards\": [2, 10],\n  \"formula\": \"10\",\n  \"thoughts\": \"'10' is an incomplete formula, since '10+2=12', I should append '+' to the current formula\",\n  \"action\": \"+\"\n}"
        # qs += "Example 4:\n"
        # qs += "{\n  \"cards\": [7, 5],\n  \"formula\": \"5\",\n  \"thoughts\": \"'5' is an incomplete formula, since '5+7=12', I should append '+' to the current formula\",\n  \"action\": \"+\"\n}"

        # try:
        #     text_formula = ''.join(str(element) for element in infos[0]['Formula'])
        #     qs = (
        #     "You are a skilled card player and mathematician. In the image, two cards are shown. "
        #     "First, identify their values (J, Q, K count as 10) as [<card1>, <card2>]. "
        #     f"Next, thoroughly examine the current formula provided: {text_formula}. Analyze every part of it—its structure, completeness, and current numerical value if it can be evaluated. "
        #     "If the formula is complete and equals 12, simply respond the actoin with '='. Otherwise, consider how the card values and the available operators ('+', '*') can be appended to extend the formula towards a final expression equal to 12. Remember, each card can be used only once. "
        #     "Your response must be a JSON object in the following format:\n\n"
        #     "{\n"
        #     "  \"cards\": [<card1>, <card2>],\n"
        #     f"  \"current formula\": \"{text_formula}\",\n"
        #     "  \"current number\": \"<evaluated value if available>\",\n"
        #     "  \"target number\": \"12\",\n"
        #     "  \"thoughts\": \"<detailed reasoning about the current formula, its structure, and how your next step advances the formula towards 12>\",\n"
        #     "  \"action\": \"<the operator or number you choose to append to the current formula>\"\n"
        #     "}\n"
        #     "For example: {\"cards\": [4, 3], \"formula\": \"3\", \"thoughts\": \"'3' is incomplete; appending '*' gives '3*4'=12.\", \"action\": \"*\"}"
        #     "Another example:{\n  \"cards\": [2, 6],\n  \"formula\": \"\",\n  \"thoughts\": \"The current formula '' is empty, I should start with any number in cards randommly, hence I choose '2'\",\n  \"action\": \"2\"\n}"
        # )
        # except:
        #     text_formula = ''

        #     qs = (
        #     "You are a skilled card player and mathematician. In the image, two cards are shown. "
        #     "First, identify their values (J, Q, K count as 10) as [<card1>, <card2>]. "
        #     "Next, thoroughly examine the current formula provided: \"\". Analyze every part of it—its structure, completeness, and current numerical value if it can be evaluated. "
        #     "If the formula is complete and equals 12, simply respond the actoin with '='. Otherwise, consider how the card values and the available operators ('+', '*') can be appended to extend the formula towards a final expression equal to 12. Remember, each card can be used only once. "
        #     "Your response must be a JSON object in the following format:\n\n"
        #     "{\n"
        #     "  \"cards\": [<card1>, <card2>],\n"
        #     "  \"current formula\": \"\",\n"
        #     "  \"current number\": \"<evaluated value if available>\",\n"
        #     "  \"target number\": \"12\",\n"
        #     "  \"thoughts\": \"<detailed reasoning about the current formula, its structure, and how your next step advances the formula towards 12>\",\n"
        #     "  \"action\": \"<the operator or number you choose to append>\"\n"
        #     "}\n"
        #     "For example: {\"cards\": [4, 3], \"formula\": \"3\", \"thoughts\": \"'3' is incomplete; appending '*' gives '3*4'=12.\", \"action\": \"*\"}"
        #     "Another example:{\n  \"cards\": [2, 6],\n  \"formula\": \"\",\n  \"thoughts\": \"The current formula '' is empty, I should start with any number in cards randommly, hence I choose '2'\",\n  \"action\": \"2\"\n}"
        # )
        
        




    elif env_name == 'gym_cards/Points24-v0':
        try:
            text_formula = ''.join(str(element) for element in infos[0]['Formula'])
        except:
            text_formula = ''
        qs = "You are an expert 24 points card game player. You are observing thee four cards in the image. "
        qs = qs + f"You are observing the current formula: {text_formula}. "
        qs = qs + "You can choose between ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '+', '-', '*', '/', '(', ')', '=']. "
        qs = qs + "The number or operator you choose will be appended to the current formula. "
        qs = qs + "Note that 'J', 'Q', and 'K' count as '10'. "
        qs = qs + "Your goal is to output a formula that evaluates to 24, and each number can only be used once. "
        qs = qs + "Your response should be a valid json file in the following format: \{\n"
        if not action_only:
            qs = qs + " \"cards\": [x, y, z, w], \n"
            qs = qs + f"\"current formula\": {text_formula}, \n"
            qs = qs + "\"thoughts\": {First check whether the current formula equals 24. "
            qs = qs + "If the current formula equals 24, output '='. "
            qs = qs + "Otherwise consider which number or operator should be appended to the current formula to make it equal 24.} \n"
        qs = qs + "\"action\": \"{number}\" or \"{operator}\" \n \}"
    return qs

# Define the function that processes the list of strings according to the specified rules
def text_projection(text_actions: List[str], env_name):
    output_indices = []
    if env_name == 'gym_cards/NumberLine-v0':
        action_list = ["-", "+"]
    elif env_name == 'gym_cards/Blackjack-v0':
        action_list = ["stand", "hit"]
    elif env_name == 'gym_cards/EZPoints-v0':
        action_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                       "+", "*", "="]
    elif env_name == 'gym_cards/Points24-v0':
        action_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                       "+", "-", "*", "/", "(", ")", "="]
    else:
        raise NotImplementedError("Action list not implemented for this env!")
    for string in text_actions:
        if not isinstance(string, str):
            # directly output a random action if the string is not a string
            output_indices.append(random.randint(0, len(action_list) - 1))
            continue
        string = string.lower()
        action_index = string.find('"action":')
        # Extract everything after "action":
        string = string[action_index:]
        contained_actions = []
        # For the 'gym_cards/Points24-v0' environment, handle '10' separately
        if 'points' in env_name.lower() and '10' in string:
            contained_actions.append('10')
            string = string.replace('10', '')  # Remove '10' to prevent it from being counted as '1'
        # Find all actions that are contained in the string
        for action in action_list:
            if action in string:
                contained_actions.append(action)
        # Remove duplicates by converting to a set and back to a list
        contained_actions = list(set(contained_actions))
        if len(contained_actions) == 1 and contained_actions[0] in action_list:
            # Only one keyword from action_list is in the string
            print("************HERE1****************")
            output_indices.append(action_list.index(contained_actions[0]))
        else:
            # The string contains none or multiple keywords, randomly select an index from action_list
            output_indices.append(random.randint(0, len(action_list) - 1))
            print("************HERE2****************")
        # print(text_actions)
        # print(output_indices)
        # exit()
    return torch.Tensor([output_indices]).long().reshape(-1, 1)

