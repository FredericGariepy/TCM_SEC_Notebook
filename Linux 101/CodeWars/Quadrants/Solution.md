## Task
Given a point in a Euclidean plane (x and y),

return the quadrant the point exists in: 1, 2, 3 or 4 (integer).

x and y are non-zero integers, therefore the given point never lies on the axes.

## Solution
Make a function to check `$1`, `$2` for their sign.

Assing quadrant based on sign combination using `if elif else` flow controll.

++ = 1 , +- = 2 , -+ = 3, -- = 4
