import streamlit as st

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="Portal dos Dados - Portal de Exercícios",
    page_icon="assets/portal.png",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------------------------------
# Funções Utilitárias
# --------------------------------------------------------------------------
def load_css(file_path: str):
    """
    Lê um arquivo CSS local e injeta os estilos na aplicação Streamlit.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(
            f"Erro Crítico: O arquivo de estilos '{file_path}' não foi encontrado."
        )


# Carregamento dos estilos globais
load_css("style.css")

# --------------------------------------------------------------------------
# Seção: Hero / Apresentação
# --------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero-card">
        <div class="hero-content">
            <p class="eyebrow">Portal de exercícios acadêmicos</p>
            <h1>Portal dos Dados</h1>
            <p class="hero-subtitle">
                Uma experiência moderna para estudar, praticar e consolidar conceitos
                com foco em dados, manutenção e confiabilidade.
            </p>
            <div class="hero-actions">
                <a href="#canais" class="btn-primary">Explorar materiais</a>
                <span class="hero-pill">Prática • Conceitos • Aplicação</span>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='section-title'>Por que este portal faz sentido?</div>",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown(
        """
        <div class="info-card">
            <h3>Pratique com propósito</h3>
            <p>Exercícios orientados para transformar teoria em habilidade aplicada e útil no dia a dia profissional.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="info-card">
            <h3>Aprendizado progressivo</h3>
            <p>Uma estrutura clara para revisar conceitos, testar compreensão e construir conhecimento com mais segurança.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="info-card">
            <h3>Recursos complementares</h3>
            <p>Materiais externos e conteúdos institucionais para aprofundar ainda mais seus estudos.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-title'>Como navegar pelo ambiente</div>",
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="list-card">
        <ul>
            <li>Escolha o conteúdo desejado e avance com foco em cada etapa do aprendizado.</li>
            <li>Use os recursos complementares para reforçar conceitos e ampliar sua visão prática.</li>
            <li>Construa uma rotina de estudo consistente e acompanhe seu progresso com mais clareza.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown(
    "<div id='canais' class='section-title'>Canais do Portal dos Dados</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='social-section'>Acesse materiais técnicos complementares sobre manutenção, confiabilidade e dados.</div>",
    unsafe_allow_html=True,
)

col_btn1, col_btn2 = st.columns(2, gap="small")

with col_btn1:
    st.markdown(
        """
        <a href='https://www.youtube.com/@Portal_dos_Dados' target='_blank' style='text-decoration: none;'>
            <button class='social-btn btn-youtube'>
                <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'>
                    <path d='M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z'/>
                </svg>
                <span>YouTube</span>
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )

with col_btn2:
    st.markdown(
        """
        <a href='https://github.com/PortalDosDados' target='_blank' style='text-decoration: none;'>
            <button class='social-btn btn-github'>
                <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'>
                    <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                </svg>
                <span>GitHub</span>
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )
