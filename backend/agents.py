class LifestyleAgent:
    def generate_plan(self, user_data):
        return {
            "status": "success",
            "message": "Plan generated",
            "data": {
                "diet": "Balanced 2200 calories",
                "fitness": "Workout 4x/week",
                "sleep": "7-8 hours",
            }
        }

