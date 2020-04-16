'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

#Average_speed = (distance / time)

Distance = 10

Time = 30.5

Speed = float (10 * 1.6) / float (30.5/60)

Speed = round(Speed, 2)

print ("Speed in Km per hour :", Speed)
