class Alarm:
    def __init__(self, alarm_enabled = True, alarm_timer = 20, alarm_volume = 4, alarm_sound = "", alarm_times = None):
        self.alarm_enabled = alarm_enabled
        self.alarm_timer = alarm_timer
        self.alarm_volume = alarm_volume
        self.alarm_sound = alarm_sound
        self.alarm_times = alarm_times

    def modify_start_end_time(self, day, start_time, end_time):
        self.alarm_times[day] = (start_time, end_time)
