

class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""
    GLUCOSE_PER_CARB = 0.5      # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3  # fixed decrease per minute of exercise
    GLUCOSE_THRESH = 50  # fixed glucose threshold

    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
        self._glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance
        self._total_insulin_delivered = 0

    #create a property method that return the glucose level
    @property
    def glusose_level(self):
      return self._glucose_level

    #create a property method that return the glucose level
    @property
    def total_insulin_delivered(self):
      return self._total_insulin_delivered

    def meal(self, carbs: float):
        """Simulate a meal event (input feature: carbs)."""
        if carbs > 0:
            self._glucose_level += carbs * ArtificialPancreasSystem.GLUCOSE_PER_CARB
            print(f"Glucose level after meal: {self._glucose_level}")
            return self._glucose_level
        else:
            print("Enter a valid value for carbs!!! Carb cannot be negative!!!")

    def exercise(self, duration: float):
        """Simulate physical activity (input feature: duration)."""
        if not isinstance(duration, int):
          raise ValueError("Duration should be a number")
        else:
            if duration > 0:
                new_glucose_level = self._glucose_level - (duration * ArtificialPancreasSystem.GLUCOSE_BURN_PER_MIN)
                if new_glucose_level < ArtificialPancreasSystem.GLUCOSE_THRESH:
                    self._glucose_level = ArtificialPancreasSystem.GLUCOSE_THRESH
                    print(f"Glucose level after exercise: {self._glucose_level}")
                    return self._glucose_level
                else:
                    self._glucose_level = new_glucose_level
                    print(f"Glucose level after exercise: {self._glucose_level}")
                    return self._glucose_level
            else:
                raise ValueError("Duration should be a positive number")
                print("Enter a valid value for duration!!! uration of an exercise cannot be negative!!!")

    def predict_action(self):
        """
        Predict and apply an appropriate system action.
        Acts like a decision function in a model.

        """
        high_glucose_val = self.target_glucose + self.tolerance
        low_glucose_val = self.target_glucose - self.tolerance

        if self._glucose_level > high_glucose_val:
            # High glucose level, deliver insulin
            print('Glucose too high. I want to deliver insulin')
            insulin_dose = self._glucose_level - self.target_glucose
            self._glucose_level -= insulin_dose
            self._total_insulin_delivered += insulin_dose
            return "deliver_insulin",  self._glucose_level

        elif (self._glucose_level >= low_glucose_val) & (self._glucose_level <= high_glucose_val):
            return "maintain",self.glusose_level
           

        
        elif self._glucose_level < low_glucose_val:
            # Warning!!!Low glucose level
             return "warn_low_glucose", self._glucose_level

        else:
          pass

'''
if __name__ == "__main__":
    controller=ArtificialPancreasSystem(100, 1.0, 100, 10)
    controller.meal(40)
    controller.exercise(20)
    action,level=controller.predict_action()
    print(action,level)

'''



