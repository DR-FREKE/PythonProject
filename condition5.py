def which_prize(score):
    wood_rabbit = "wooden rabbit";
    no_prize = "No prize";
    wafer_thin_mint = "wafer-thin mint";
    penguin = "penguin";
    if score > 0 and score <= 50:
        return "Congratulations! You have won a {}".format(wood_rabbit);
    elif score >= 51 and score <= 150:
        return "{}".format(no_prize);
    elif score >=151 and score <=180:
        return "Congratulations! You have won a {}".format(wafer_thin_mint);
    elif score >= 181 and score <= 200:
        return "Congratulations! You have won a {}".format(penguin);
    else:
        return "Oh dear, no prize this time";

print(which_prize(53));
        
        
        