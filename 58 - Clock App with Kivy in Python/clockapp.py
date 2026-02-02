from time import strftime
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from datetime import datetime


class ClockApp(App):
    sw_started = False
    sw_seconds = 0
    laps = []

    alarm_time = None
    alarm_active = False

    def build(self):
        return Builder.load_file("clock.kv")

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0.1)

    def update_time(self, dt):
        if self.sw_started:
            self.sw_seconds += dt

        minutes, seconds = divmod(self.sw_seconds, 60)
        millis = int((seconds - int(seconds)) * 100)

        self.root.ids.stopwatch.text = (
            f"{int(minutes):02d}:{int(seconds):02d}."
            f"[size=32]{millis:02d}[/size]"
        )

        current_time = strftime("%H:%M:%S")
        self.root.ids.time.text = f"[b]{current_time}[/b]"

        if self.alarm_active and self.alarm_time == current_time:
            self.trigger_alarm()

    def start_stop(self):
        self.sw_started = not self.sw_started
        self.root.ids.start_stop.text = "Stop" if self.sw_started else "Start"

    def reset(self):
        self.sw_started = False
        self.sw_seconds = 0
        self.laps.clear()
        self.root.ids.lap_box.clear_widgets()
        self.root.ids.start_stop.text = "Start"

    def add_lap(self):
        lap_time = self.root.ids.stopwatch.text
        self.laps.append(lap_time)

        self.root.ids.lap_box.add_widget(
            Builder.load_string(
                f'''
Label:
    text: "Lap {len(self.laps)} : {lap_time}"
    size_hint_y: None
    height: "25dp"
    color: 1,1,1,1
'''
            )
        )

    def set_alarm(self):
        self.alarm_time = self.root.ids.alarm_input.text
        self.alarm_active = True
        self.root.ids.alarm_status.text = f"Alarm set for {self.alarm_time}"

    def trigger_alarm(self):
        self.alarm_active = False
        self.root.ids.alarm_status.text = "⏰ ALARM RINGING!"


if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex("#101216")

    LabelBase.register(
        name="Roboto",
        fn_regular="Roboto-Thin.ttf",
        fn_bold="Roboto-Medium.ttf"
    )

    ClockApp().run()
