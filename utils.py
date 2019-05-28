# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script

def countValues(x):
    """
    Count the sum of each item in the list.
    
    Parameter: 
    x : list or any readable in python
    
    Returns:
    Total sum for each item in the list. 
    
    """
    items = list(set(x))
    for value in items:
        print(value, x.count(value))
        
def createDir(x):
    """
    Creates a subdirectory
    
    Parameter:
    x : subfolder to be created
    
    Returns: 
    Prints a message if the subfolder exists. If the message is false, a new subfolder will be created. 
    
    """
   sub_dir = x.exists()
   if sub_dir:
       print("The subfolder {} exists.".format(x))
      
   else:
       x.mkdir(parents = True, exist_ok = True)
       print("The subfolder {} is created.".format(x))

    
def CountandCreate(x, output_dir):
    """
    Creation of a dataframe with the sum of each item i a text file
    
    Parameter: 
    x: dataframe to be created
    
    Returns:
    Saves the dataframe in a csv-file.
    
    """
    import pandas as pd
    items = list(set(x))
    countings = []
    for value in items: 
        countings.append(x.count(value))
    countings_df = pd.DataFrame({'model': items, 'countings': countings})
    
    output_name = output / "counts.csv"      
    countings_df.to_csv (output_name, header = True)

        

