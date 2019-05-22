


from pyparrot.Minidrone import Mambo

mamboAddr = "e0:14:c1:6c:3d:cf"



mambo = Mambo(mamboAddr, use_wifi=False)


print("trying to connect")
success = mambo.connect(num_retries=5)
print("connected: %s" % success)


if (success):
    # get the state information
    print("sleeping")
    mambo.smart_sleep(5)


    print("taking off!")
    mambo.safe_takeoff(5)
    
    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-10, duration=2)
    mambo.smart_sleep(0)

    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=4)
    mambo.smart_sleep(0)
    
    print("Showing turning (in place) using turn_degrees")
    mambo.turn_degrees(-45)
    mambo.smart_sleep(0)
    
    print("Showing turning (in place) using turn_degrees")
    mambo.turn_degrees(-45)
    mambo.smart_sleep(0)
    
    print("Showing turning (in place) using turn_degrees")
    mambo.turn_degrees(-45)
    mambo.smart_sleep(0)
    
    print("Showing turning (in place) using turn_degrees")
    mambo.turn_degrees(-45)
    mambo.smart_sleep(2)
    
    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=10, pitch=0, yaw=0, vertical_movement=0, duration=1)
    mambo.smart_sleep(3)
    
    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=-20, pitch=0, yaw=0, vertical_movement=0, duration=0.3)
    mambo.smart_sleep(3)
    
    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=3)
    mambo.smart_sleep(3)
    
    print("flip front")
    print("flying state is %s" % mambo.sensors.flying_state)
    success = mambo.flip(direction="front")
    print("mambo flip result %s" % success)
    mambo.smart_sleep(5)
    
    print("landing")
    mambo.safe_land(5)
    mambo.smart_sleep(5)

    print("disconnect")
    mambo.disconnect()    
    
    
    
    