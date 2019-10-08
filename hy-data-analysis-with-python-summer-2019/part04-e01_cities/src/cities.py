#!/usr/bin/env python3

import pandas as pd

def cities():
    pop = pd.Series([643272, 279044, 231853, 223027, 201810], name = "Population")
    area = pd.Series([715.48, 528.03, 689.59, 240.35, 3817.52], name = "Total area")
    index = ["Helsinki", "Espoo" , "Tampere" , "Vantaa" , "Oulu"]    
    df = pd.DataFrame({pop.name : pop, area.name: area})
    df.index = index
    return df
    
def main():
    return
    
if __name__ == "__main__":
    main()
