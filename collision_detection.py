def Collision_Detection(Rote_date):
    YesorNo = 'no'
    for body_date in Rote_date[1:]:
        if body_date == Rote_date[0]:
            YesorNo = 'yes'
            break
    return YesorNo