import pytest

import main.artificial_pancreas as art_pan_syst

@pytest.fixture
def art_pan_sys():
   
   return [art_pan_syst.ArtificialPancreasSystem(glucose_level, 1.0, 100, 10) for glucose_level in [100, 80, 130, 95, 50]]

   """return [ 
    
  art_pan_syst.ArtificialPancreasSystem(100, 1.0, 100, 10),
  art_pan_syst.ArtificialPancreasSystem(80, 1.0, 100, 10),
  art_pan_syst.ArtificialPancreasSystem(130, 1.0, 100, 10),
  art_pan_syst.ArtificialPancreasSystem(95, 1.0, 100, 10),
   art_pan_syst.ArtificialPancreasSystem(50, 1.0, 100, 10)
  ]"""


def test_glucose_increase_after_meal(art_pan_sys):
  assert art_pan_sys[0].meal(40)  == 120 , "Should be 120"

def test_glucose_decrease_after_exercise(art_pan_sys):
  assert art_pan_sys[0].exercise(20) == 94 , "Should be 94"
 
@pytest.mark.parametrize("art_sys_index,  expected_action", [
  (2, "deliver_insulin"), 
  (1, "warn_low_glucose"),
  (3, "maintain")
])
def test_correct_action(art_pan_sys, art_sys_index, expected_action):
  art_pan_syst_obj = art_pan_sys[art_sys_index]
  assert art_pan_syst_obj.predict_action()[0] == expected_action , f'Should be {expected_action}'
  

def test_glucose_never_drps_below_min(art_pan_sys):
  assert art_pan_sys[4].exercise(20) == 50 , 'Should be 50'
  #assert art_pan_sys[1].exercise(80) == 56 , 'Should be 56'


def test_total_isulin(art_pan_sys):
  art_pan_syst_obj = art_pan_sys[2]
  art_pan_syst_obj.predict_action()

  assert art_pan_syst_obj.total_insulin_delivered == 30 , 'Should be 20'

def test_multiple_sequential_event(art_pan_sys):
  art_sys_obj = art_pan_sys[3]
  art_sys_obj.meal(20)
  art_sys_obj.exercise(10)
  assert art_sys_obj.predict_action()[0] == "maintain" , 'Should be maintain'

def test_invalid_input_meal(art_pan_sys):
  with pytest.raises(TypeError):
    art_pan_sys[0].meal('hello')


def test_invalid_input_exercise(art_pan_sys):
  with pytest.raises(ValueError):
    art_pan_sys[1].exercise(-15)
    #art_pan_sys[1].exercise(-30)

