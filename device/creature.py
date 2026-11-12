
class LilGuyCreature:
    def __init__(self):
        self.mood = "neutral"

    def handle_event(self, event):
        previous_mood = self.mood

        if event == "motion_detected":
            self.mood = "awake"

        elif event == "motion_stopped":
            self.mood = "neutral"

        elif event == "short_touch":
            self.mood = "annoyed"

        elif event == "long_touch":
            self.mood = "happy"

        elif event == "light_detected":
            self.mood = "awake"

        elif event == "darkness_detected":
            self.mood = "sleepy"

        else:
            print(f"Unknown event: {event}")
            return

        if self.mood != previous_mood:
            print(f"Lil_Guy mood changed: {previous_mood} -> {self.mood}")

    def get_mood(self):
        return self.mood
