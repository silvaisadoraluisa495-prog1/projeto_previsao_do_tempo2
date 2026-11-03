import streamlit as st
from dados_api import previsao_temperatura

# Cidades
cidades = {
    'Berlim' : [-52.52096982608005, -13.408264583170581],
    'Jandira' : [-23.530269939378805, -46.897964228102495],
    'Cairo' : [-30.047149626016378, -31.237034064352645],
    'Santana' : [-23.500937572312477, -46.6209665536953],
    'Dayrout' : [-27.57466715756984, -30.58005043890711],
    'Comercinho' : [-16.296207479191803, -41.794010136709545],
    'Pescara' : [-42.414938781246995, -15.119600081976511],
    'Tianguá' : [-3.7267115487030797, -40.99516293486748]
}

#------------------------- SIDEBAR
st.sidebar.title('Previsão do tempo')
st.sidebar.subheader('Confira sua previsão para nao ficar na mão e nao deixe o raposo roubar sua diversão')
st.sidebar.image('logo.png')

cidade = st.sidebar.selectbox('Escolha a cidade:', cidades.keys())
latitude , longitude = cidades[cidade]

# --------------- BODY
st.title(f'Previsão do tempo em {cidade} para os próximos 7 dias')

st.markdown('---')

# Previsão de temperatura
dados, temperatura_media = previsao_temperatura(latitude, longitude)

for i,d in temperatura_media.iterrows():

    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric('Data',f'{int(d['dia'])}/{int(d['mes'])}')

        with col2:
            st.metric('Temperatura média', f'{d['temperatura_media']:.2f}°')

        with col3:
            if d['temperatura_media'] < 10:
                temp = 'cold.png'

            elif d['temperatura_media'] <18:
                temp = 'cool.png'


            elif d['temperatura_media'] <25:
                temp = 'comfort.png'


            else:
                temp = 'warm.png'

            st.image(temp, width=400)