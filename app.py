import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


def main():
    # Open image with PIL
    favicon = Image.open(f'./assets/invntario.png')
    # Alternate names: setup_page, page, layout
    st.set_page_config( # Can be "centered" or "wide". In the future also "dashboard", etc.
                        layout="wide",
                        # Can be "auto", "expanded", "collapsed"
                        initial_sidebar_state="collapsed",
                        # String or None. Strings get appended with "• Streamlit"
                        page_title="Registro Nacional de Sucursales y Agentes de Sociedades Mercantiles Extranjeras en Cuba",
                        page_icon=favicon,  # String, anything supported by st.image, or None.
    )
    # data = pd.read_excel('./data/raw/registro_empresas.xlsx', index_col=None, sheet_name='empresas', 
    #                     converters={'Fecha de la resolución': str, 
    #                                 'Fecha Gaceta': str,
    #                                 'No. de Resolución': str})
    data = pd.read_csv('./data/processed/registro_empresas.csv', index_col=None, 
                    converters={'Fecha de la resolución': str, 
                                'Fecha Gaceta': str,
                                'No. de Resolución': str})

    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()

    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT', 
        update_mode='MODEL_CHANGED', 
        fit_columns_on_grid_load=False,
        theme='blue', #Add theme color to the table
        enable_enterprise_modules=True,
        height=800, 
        width='100%',
        reload_data=True
    )

    data = grid_response['data']
    selected = grid_response['selected_rows'] 
    df = pd.DataFrame(selected)

###
    data_objeto = pd.read_csv('./data/processed/objetos_empresas.csv', index_col=False, 
                        converters={'Fecha de la resolución': str, 
                                    'Fecha Gaceta': str,
                                    'No. de Resolución': str})

    gb = GridOptionsBuilder.from_dataframe(data_objeto)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()

    grid_response = AgGrid(
        data_objeto,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT', 
        update_mode='MODEL_CHANGED', 
        fit_columns_on_grid_load=False,
        theme='streamlit', #Add theme color to the table
        enable_enterprise_modules=True,
        height=800, 
        width='100%',
        reload_data=True
    )

    data_objeto = grid_response['data']
    selected = grid_response['selected_rows'] 
    df = pd.DataFrame(selected)



if __name__ == '__main__':
    main()