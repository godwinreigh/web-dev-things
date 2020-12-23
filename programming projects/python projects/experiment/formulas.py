#bouncy bounce formula
if jump_count >= -10:
    y -= (jump_count * abs(jump_count)) * 0.5
    jump_count -= 1
else:  # This will execute if our jump is finished
    jump_count = 10
    jump = False
    # Resetting our Variables