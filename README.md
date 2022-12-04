# MongoDB_Assessmnet
Edited files of MongoDB's Summer intern take home assessment, "ShoppingCart"

Time spent: approx 2hrs 30m

Work done:

  - Improved receipt printing:
    - Inclusion of spacing for readability
    - Total calculated and printed
    
  - Creating means to change layout of receipt printing quickly without need to change class IShoppingCart. Code is easily duplicatable to create additional layouts.
  
  - Improved testing:
    - Tests layout specified by user
    - Added evaluation of total price to all tests.
    
  - Additional testing added:
    - Tests if items are printed on the receipt in the order they have been scanned
    - Tests if value of item is correctly updated if an item type is scanned multiple times with other item types scanned between. Also tests if receipt prints in order of first iteration of an item type scanned.
