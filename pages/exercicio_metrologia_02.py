import streamlit as st
from pathlib import Path
from datetime import datetime

# --------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------------------------------------

st.set_page_config(
    page_title="Metrologia - Exercício 02",
    page_icon="assets/portal.png",
    layout="wide",
)


# Carregamento do CSS
def load_css(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Erro: CSS não encontrado em '{file_path}'")


load_css(Path(__file__).resolve().parents[1] / "style.css")

# --------------------------------------------------------------------------
# ESTADO DA SESSÃO
# --------------------------------------------------------------------------

if "etapa_metrologia_02" not in st.session_state:
    st.session_state.etapa_metrologia_02 = "inicio"
if "nome_aluno_02" not in st.session_state:
    st.session_state.nome_aluno_02 = ""
if "questao_atual_02" not in st.session_state:
    st.session_state.questao_atual_02 = 0
if "respostas_02" not in st.session_state:
    st.session_state.respostas_02 = []

# --------------------------------------------------------------------------
# BANCO DE DADOS DO EXERCÍCIO
# --------------------------------------------------------------------------

questoes = [
    {
        "id": 1,
        "pergunta": "O que é tolerância dimensional?",
        "opcoes": [
            "A medida exata da peça",
            "A variação permitida nas dimensões de uma peça",
            "O erro de medição do instrumento",
            "A capacidade de suportar carga",
        ],
        "resposta_correta": 1,
        "justificativa": "Tolerância é o intervalo permitido de variação nas dimensões, definido por limites máximo e mínimo.",
    },
    {
        "id": 2,
        "pergunta": "Qual é a função do paquímetro?",
        "opcoes": [
            "Medir ângulos de peças",
            "Medir comprimentos, profundidades e diâmetros",
            "Medir rugosidade de superfícies",
            "Verificar temperatura",
        ],
        "resposta_correta": 1,
        "justificativa": "O paquímetro é um instrumento versátil que permite medir comprimentos externos, internos, profundidades e diâmetros.",
    },
    {
        "id": 3,
        "pergunta": "Qual é a resolução típica de um paquímetro analógico?",
        "opcoes": ["0,1 mm", "0,01 mm (1/20 de mm)", "0,5 mm", "1 mm"],
        "resposta_correta": 1,
        "justificativa": "A maioria dos paquímetros analógicos tem resolução de 0,05 mm ou 0,01 mm dependendo do nônio.",
    },
    {
        "id": 4,
        "pergunta": "O que é calibração de um instrumento?",
        "opcoes": [
            "Consertar o instrumento quando está quebrado",
            "Estabelecer a relação entre o instrumento e um padrão de referência",
            "Limpar o instrumento",
            "Guardar o instrumento adequadamente",
        ],
        "resposta_correta": 1,
        "justificativa": "Calibração é o processo de comparação com um padrão confiável para verificar e ajustar a precisão.",
    },
]

# --------------------------------------------------------------------------
# TELA INICIAL - IDENTIFICAÇÃO
# --------------------------------------------------------------------------

if st.session_state.etapa_metrologia_02 == "inicio":
    st.markdown(
        """
        <div style='text-align: center; padding: 30px 0;'>
            <h1 style='color: #005088;'>Metrologia - Exercício 02</h1>
            <p style='color: #666; font-size: 16px;'>Conceitos sobre tolerâncias dimensionais e desgastes em equipamentos.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    nome = st.text_input(
        "Digite seu nome completo:", placeholder="Seu nome aqui...", key="input_nome_02"
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Iniciar Exercício", type="primary", use_container_width=True):
            if nome.strip():
                st.session_state.nome_aluno_02 = nome
                st.session_state.etapa_metrologia_02 = "quiz"
                st.session_state.respostas_02 = [None] * len(questoes)
                st.rerun()
            else:
                st.warning("Por favor, digite seu nome para continuar.")

    with col2:
        if st.button("← Voltar", use_container_width=True):
            st.switch_page("Dione_Nascimento")

# --------------------------------------------------------------------------
# TELA DO QUIZ
# --------------------------------------------------------------------------

elif st.session_state.etapa_metrologia_02 == "quiz":
    idx = st.session_state.questao_atual_02
    q = questoes[idx]

    # Barra de progresso
    st.progress((idx + 1) / len(questoes))
    st.markdown(
        f"<p style='text-align: center; color: #666;'>Questão {idx + 1} de {len(questoes)}</p>",
        unsafe_allow_html=True,
    )

    st.divider()

    # Pergunta
    st.markdown(f"### {q['pergunta']}")

    # Opções
    resposta = st.radio(
        "Selecione uma alternativa:",
        options=range(len(q["opcoes"])),
        format_func=lambda x: q["opcoes"][x],
        label_visibility="collapsed",
        key=f"radio_q{idx}_02",
    )

    st.divider()

    # Botões de navegação
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if idx > 0:
            if st.button("← Anterior", use_container_width=True):
                st.session_state.questao_atual_02 -= 1
                st.rerun()

    with col2:
        if st.button("Confirmar", type="primary", use_container_width=True):
            st.session_state.respostas_02[idx] = resposta

            if idx < len(questoes) - 1:
                st.session_state.questao_atual_02 += 1
                st.rerun()
            else:
                st.session_state.etapa_metrologia_02 = "resultado"
                st.rerun()

    with col3:
        if st.button("← Voltar à Home", use_container_width=True):
            st.switch_page("Dione_Nascimento")

# --------------------------------------------------------------------------
# TELA DE RESULTADOS
# --------------------------------------------------------------------------

elif st.session_state.etapa_metrologia_02 == "resultado":
    acertos = sum(
        1
        for i, q in enumerate(questoes)
        if st.session_state.respostas_02[i] == q["resposta_correta"]
    )

    total = len(questoes)
    percentual = (acertos / total) * 100
    data = datetime.now().strftime("%d/%m/%Y às %H:%M")

    st.markdown(
        f"""
        <div style='text-align: center; padding: 20px; background-color: #f0f8ff; border-radius: 8px; margin-bottom: 20px;'>
            <h2 style='color: #005088; margin: 0;'>Exercício Concluído!</h2>
            <p style='color: #666; margin: 10px 0 0 0;'>{st.session_state.nome_aluno_02} | {data}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Resultado
    if percentual >= 80:
        st.success(
            f"✅ Excelente! Você acertou **{acertos} de {total}** ({percentual:.1f}%)"
        )
    elif percentual >= 60:
        st.info(
            f"👍 Bom trabalho! Você acertou **{acertos} de {total}** ({percentual:.1f}%)"
        )
    else:
        st.warning(
            f"📚 Revise os conceitos. Você acertou **{acertos} de {total}** ({percentual:.1f}%)"
        )

    st.divider()

    # Revisão das questões
    st.markdown("### Revisão das Questões")

    for i, q in enumerate(questoes):
        resposta_aluno = st.session_state.respostas_02[i]
        acertou = resposta_aluno == q["resposta_correta"]

        cor = "#10b981" if acertou else "#ef4444"
        status = "✓ Correto" if acertou else "✗ Incorreto"

        st.markdown(
            f"""
            <div style='border-left: 5px solid {cor}; padding: 12px; background-color: #f9f9f9; margin-bottom: 15px; border-radius: 4px;'>
                <strong>Questão {i + 1}</strong> - {status}<br>
                <em>Sua resposta:</em> {q["opcoes"][resposta_aluno]}<br>
                <em>Resposta correta:</em> {q["opcoes"][q["resposta_correta"]]}<br>
                <strong>Justificativa:</strong> {q["justificativa"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Fazer Novamente", use_container_width=True):
            st.session_state.etapa_metrologia_02 = "inicio"
            st.session_state.questao_atual_02 = 0
            st.session_state.respostas_02 = []
            st.session_state.nome_aluno_02 = ""
            st.rerun()

    with col2:
        if st.button("← Voltar à Home", type="primary", use_container_width=True):
            st.switch_page("pages")
