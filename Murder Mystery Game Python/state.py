current_room = "foyer"



floor = "downstairs"

first_time_foyer = True

visited = []



# DIALOG STAGE CONTROL

pearl_stage = 1
pearl_current = 0

mitsy_stage = 1
mitsy_current = 0

tallulah_stage = 1
tallulah_current = 0

bernard_stage = 1
bernard_current = 0

total_current = mitsy_current + tallulah_current + bernard_current



#Unlcok States

items = []

study_open_attempted = False

bathroom_weapon_found = False
#changing to study door locked false for mitsy dialog 3 unlock
study_locked = True

key_found = False

safe_code_found = False

family_letter_found = False

bathroom_hint = False

brick_hint = False

library_hint = False

documents_found = False

mit_fail_safe = False

const_not_ready = False



