import streamlit as st
import pandas as pd
from PIL import Image

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
    df = pd.read_excel('./data/raw/registro_empresas.xlsx', index_col=None, sheet_name='empresas', 
                        converters={'Fecha de la resolución': str, 
                                    'Fecha Gaceta': str,
                                    'No. de Resolución': str})
    st.dataframe(df)



if __name__ == '__main__':
    main()