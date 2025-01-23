def make_fs_df(firm_code) : 

    import requests
    import pandas as pd
    from io import StringIO

    # URL for the financial statement. I changed the structure of the URL, specifically moving the firm code part to the end of the URL.
    fs_url = 'https://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=D&gicode=A'+firm_code
    
    # Send HTTP request to fetch the page content
    fs_page = requests.get(fs_url)
    
    # Use StringIO to wrap the HTML content and pass it to pd.read_html
    fs_tables = pd.read_html(StringIO(fs_page.text))
    
    # Bring the first financial statement in the website and alter index the first column
    temp_df = fs_tables[0]
    temp_df = temp_df.set_index('IFRS(연결)')
    
    # Change index name 
#    temp_df = temp_df.rename_axis('IFRS(Consolidated)')
    
    # Drop 'same FY from previous year' and the ratio column
#    temp_df = temp_df.drop(columns=['전년동기', '전년동기(%)'])
    
    # Drop unnessesary rows except Sales, Operating Income and Net income
#    temp_df = temp_df.loc[['매출액', '영업이익', '당기순이익']]
    
    # Bring Statement of financial position from the web site and set index as 'IFRS(Consolidated)' 
    temp_df2 = fs_tables[2]
    temp_df2 = temp_df2.set_index('IFRS(연결)')
    
    # Chane index name from 'IFRS(연결)' to 'IFRS(Consolidated)'
    temp_df2 = temp_df2.rename_axis('IFRS(Consolidated)')
    
    # Drop unnessesary rows except Assets, Liabilities, and Owner's Equity
#    temp_df2 = temp_df2.loc[['자산', '부채', '자본']]
    
    # Bring the first financial statement in the website and alter index the first column
    temp_df3 = fs_tables[4]
    temp_df3 = temp_df3.set_index('IFRS(연결)')
    
    # Change index name 
    temp_df3 = temp_df3.rename_axis('IFRS(Consolidated)')
    
    # Drop unnessesary rows except Sales, Operating Income and Net income
#    temp_df3 = temp_df3.loc[['영업활동으로인한현금흐름']]
    
    # Consolidate all the tables above into one table
    fs_df = pd.concat([temp_df, temp_df2, temp_df3])

    # Replace index with new value
#    fs_df.index = ['Sales', 'Operating Income', 'Net Income', 'Assets', 'Liabilities', 'Owners Equity', 'Cashflow from Operating Activities']

    return fs_df