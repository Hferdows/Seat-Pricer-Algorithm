import math

def compute_seat_price(row, col, total_rows, total_cols, base_p):
    #comparison coordinates for calculating the ideal seat
    center_col = (total_cols - 1) / 2
    screen_row =  0 #since the screen is at the top/front, marking it 0
    base_price = base_p
    speakers = [ #speaker positions
        (screen_row, 0),      #left
        (screen_row, center_col),    #center
        (screen_row, total_cols - 1) #right
    ]
    legroom_rows = {total_rows - 1, total_rows // 2} #back row and center row will have extra leg room
    aisle_cols = {0, total_cols - 1} #the left of the seats and to the right of the seats will have an aisle
    if total_cols > 6:
        aisle_cols.add(total_cols // 2) #if a theater is large enough, this will account for a center aisle as well

    #calculate distances and scores for the seat to be totaled at the end 
    max_col_dist = center_col
    if (max_col_dist == 0.0):
        col_score = 1.0
    else :
        col_score = 1 - abs(col - center_col) / max_col_dist
    col_score = max(0.0, min(1.0, col_score))
    dx = col - center_col   #angle to screen center score
    dy = row - screen_row
    angle = abs(math.atan2(dx, dy))  #gives you the angle where the two points intersect, abs value to make sure not negative

    #calculate angle score2
    max_angle = math.atan2(center_col, total_rows)  #farthest angle from the screen based on the rows and columms
    #added checks to make sure divide by 0 does not happen
    if (max_angle == 0.0):
        angle_score = 1.0
    else :
        angle_score = 1 - (angle / max_angle)
    angle_score = max(0.0, min(1.0, angle_score))  #extra 0-1 check

    #calculate distance to screem score 
    seat_distance = math.hypot(dx, dy) 
    max_distance = math.hypot(center_col, total_rows)
    if (max_distance  == 0.0):
        dist_score = 1.0
    else :
        dist_score = 1 - (seat_distance / max_distance)
    dist_score = max(0.0, min(1.0, dist_score))

    #speaker proximity score
    speaker_distances = [math.hypot(row - sr, col - sc) for sr, sc in speakers]  #caluclate distances using the distance formula
    avg_speaker_dist = sum(speaker_distances) / len(speaker_distances)
    max_speaker_dist = math.hypot(total_rows, center_col)
    if (avg_speaker_dist  == 0.0):
        speaker_score = 1.0
    else :
        speaker_score = 1 - (avg_speaker_dist / max_speaker_dist)
    speaker_score = max(0.0, min(1.0, speaker_score))

    #aisle proximity score
    min_aisle_dist = min(abs(col - a) for a in aisle_cols) 
    max_aisle_dist = total_cols / 2
    if (max_aisle_dist  == 0.0):
        aisle_score = 1.0
    else :
        aisle_score = 1 - (min_aisle_dist / max_aisle_dist)
    aisle_score = max(0.0, min(1.0, aisle_score))
    #add extra points to the seat if it is one of the legroom seats
    if (row in legroom_rows):
        legroom_score = 1.0
    else :
        legroom_score = 0.0

    weights = {  #weight all the scores to be totaled up for price multiplier 
        'center': 0.2,
        'angle': 0.2,
        'distance': 0.15,
        'speaker': 0.15,
        'legroom': 0.15,
        'aisle': 0.15
    }

    total_score = (  
        weights['center'] * col_score +
        weights['angle'] * angle_score +
        weights['distance'] * dist_score +
        weights['speaker'] * speaker_score +
        weights['legroom'] * legroom_score +
        weights['aisle'] * aisle_score
    )

    #price between base_price * 0.5 to base_price * 1.5
    price_multiplier = 0.5 + total_score
    final_price = round(base_price * price_multiplier, 2)  #multiply and round the answer two places for final price 

    return final_price
