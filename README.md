# TECHNYU-OA
Showing all available locations 
and
Example of 4 other locations
zach@MacBook-Pro scripts % python3 plan.py --list

25 available locations:

  [landmark]
    Brooklyn Bridge
    Charging Bull
    Empire State Building
    Grand Central Terminal
    Rockefeller Center
    Staten Island Ferry
    Times Square
    Wall Street
  [market]
    Chelsea Market
    Industry City
  [memorial]
    9/11 Memorial
  [museum]
    American Museum of Natural History
    Brooklyn Museum
    Guggenheim Museum
    Metropolitan Museum of Art
    MoMA
    Whitney Museum
  [neighborhood]
    DUMBO
  [park]
    Battery Park
    Brooklyn Bridge Park
    Bryant Park
    Central Park
    Coney Island
    High Line
    Prospect Park
zach@MacBook-Pro scripts % python3 plan.py "Empire State Building" "DUMBO" "Prospect Park" "MoMA"

Planning: Empire State Building, DUMBO, Prospect Park, MoMA

Route  (4 stops · 6.0 h)
--------------------------------------------------
    9:00 AM  Empire State Building
   10:40 AM  MoMA  ← subway (10 min)
   12:59 PM  DUMBO  ← rideshare (19 min)
    1:59 PM  Prospect Park  ← rideshare (15 min)

Your 4-stop NYC day plan:

  1. Empire State Building  |  9:00 AM – 10:30 AM
  2. MoMA  |  10:40 AM – 12:40 PM  ← subway (10 min)
  3. DUMBO  |  12:59 PM – 1:44 PM  ← rideshare (19 min)
  4. Prospect Park  |  1:59 PM – 2:59 PM  ← rideshare (15 min)