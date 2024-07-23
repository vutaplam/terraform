def calculate_area(length, width):
  """Calculates the area of a rectangle."""
  area = length * width
  return area

def calculate_rectangle_perimeter(length, width):
  """Calculates the perimeter of a rectangle."""
  perimeter = 2 * (length + width)
  return perimeter

# Duplicate calculation logic
def calculate_square_area(side_length):
  """Calculates the area of a square."""
  area = side_length * side_length  # This duplicates the calculation from calculate_area
  return area
