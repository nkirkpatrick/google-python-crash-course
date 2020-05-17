def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number==1:
    return True
  if number < base:
    return False
  number/=base

  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False