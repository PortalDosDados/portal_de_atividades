import streamlit as st
from pathlib import Path
from datetime import datetime

# ==========================================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================================================
# Aqui definimos como a aba do navegador vai aparecer para o usuário
st.set_page_config(
    page_title="Oxicorte - Avaliação de Aprendizado",
    page_icon="🔥",
    layout="wide",
)


# Função para carregar o CSS (mantida exatamente como no seu modelo original)
def load_css(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Erro: CSS não encontrado em '{file_path}'")


# Ajuste o caminho do CSS conforme a estrutura de pastas do seu projeto
load_css(Path(__file__).resolve().parents[1] / "style.css")

# ==========================================================================
# 2. ESTADO DA SESSÃO (SESSION STATE)
# ==========================================================================
# O Streamlit recarrega o código a cada clique. Usamos o session_state para
# "lembrar" as informações do usuário entre uma tela e outra.
if "etapa_oxicorte" not in st.session_state:
    st.session_state.etapa_oxicorte = "inicio"
if "nome_aluno" not in st.session_state:
    st.session_state.nome_aluno = ""
if "questao_atual" not in st.session_state:
    st.session_state.questao_atual = 0
if "respostas" not in st.session_state:
    st.session_state.respostas = []

# ==========================================================================
# 3. BANCO DE DADOS DO EXERCÍCIO (20 Questões de Oxicorte)
# ==========================================================================
# Uma lista de dicionários contendo o id, pergunta, as 4 opções,
# o índice da resposta correta (0, 1, 2 ou 3) e a justificativa.
questoes = [
    {
        "id": 1,
        "pergunta": "Qual é o princípio fundamental de operação do processo de oxicorte e a qual temperatura ele ocorre?",
        "opcoes": [
            "Fusão mecânica do aço utilizando arco elétrico a 5000°C.",
            "Combustão (oxidação viva) localizada e contínua do ferro, a aproximadamente 1350°C.",
            "Derretimento do material por atrito mecânico a 800°C.",
            "Reação química a frio utilizando gases nobres.",
        ],
        "resposta_correta": 1,
        "justificativa": "O processo baseia-se na combustão (oxidação viva) localizada e contínua do ferro, ocorrendo a uma temperatura de aproximadamente 1350°C.",
    },
    {
        "id": 2,
        "pergunta": "O oxicorte é considerado um processo altamente econômico para quais condições de material?",
        "opcoes": [
            "Corte de chapas finas de alumínio e cobre.",
            "Apenas para o corte de plásticos e polímeros.",
            "Corte de materiais com alto teor de cromo.",
            "Especialmente para o corte de grandes espessuras de metal.",
        ],
        "resposta_correta": 3,
        "justificativa": "Ele é o processo mais econômico especialmente para o corte de grandes espessuras de metal.",
    },
    {
        "id": 3,
        "pergunta": "Quais são as três principais vantagens do processo de oxicorte listadas no material?",
        "opcoes": [
            "Alta velocidade em chapas finas, ausência de escória e uso de energia elétrica.",
            "Baixo investimento inicial, facilidade operacional e ser ideal para diversas espessuras de chapas.",
            "Corte perfeito de alumínio, baixo ruído e equipamento leve.",
            "Não necessita de EPIs, não gera fumaça e usa apenas um tipo de gás.",
        ],
        "resposta_correta": 1,
        "justificativa": "As vantagens são: Baixo investimento inicial, facilidade operacional e ser ideal para diversas espessuras de chapas.",
    },
    {
        "id": 4,
        "pergunta": "Cite os três principais fatores que afetam diretamente a qualidade do corte no processo de oxicorte.",
        "opcoes": [
            "A pureza do oxigênio, a distância correta entre o bico e a peça, e a estabilidade da velocidade de corte.",
            "A marca do maçarico, a temperatura ambiente e a cor da mangueira.",
            "A pressão do argônio, o tamanho do cilindro e o tipo de EPI utilizado.",
            "O comprimento da chapa, a largura do bico e o sentido do corte.",
        ],
        "resposta_correta": 0,
        "justificativa": "A pureza do oxigênio (O2), a distância correta entre o bico e a peça, e a estabilidade da velocidade de corte afetam diretamente a qualidade.",
    },
    {
        "id": 5,
        "pergunta": "Qual é o impacto percentual na eficiência do corte se houver variação na pureza do oxigênio utilizado?",
        "opcoes": [
            "Impacto nulo, a pureza não interfere no corte.",
            "Impacto de até 5% na velocidade apenas.",
            "A pureza do oxigênio gera um impacto de até 15% nos fatores de qualidade do processo.",
            "Impacto de 50%, inviabilizando totalmente o corte.",
        ],
        "resposta_correta": 2,
        "justificativa": "A pureza do oxigênio gera um impacto de até 15% nos fatores de qualidade do processo.",
    },
    {
        "id": 6,
        "pergunta": "Por que o oxicorte é restrito basicamente aos aços carbono? Explique a condição ideal de fusão.",
        "opcoes": [
            "Porque o aço carbono é o único metal que conduz eletricidade o suficiente para a chama.",
            "Porque a condição ideal é que o óxido fundido tenha temperatura de fusão inferior à do metal base (~1370°C óxido vs ~1538°C metal).",
            "Porque o aço carbono é o metal mais barato do mercado, viabilizando o gás.",
            "Porque o óxido do aço carbono é mais duro que o próprio aço, facilitando a quebra.",
        ],
        "resposta_correta": 1,
        "justificativa": "A condição ideal é que o óxido funda antes do metal base. No aço carbono, o metal funde a ~1538°C e o óxido (FeO) a ~1370°C, permitindo que o jato de O2 remova a escória.",
    },
    {
        "id": 7,
        "pergunta": "Explique fisicamente por que o oxicorte não consegue cortar o alumínio.",
        "opcoes": [
            "O alumínio não derrete com o calor.",
            "A chama do oxicorte é muito fria para o alumínio.",
            "O óxido de alumínio (Al2O3) tem um ponto de fusão muito superior (~2050°C), criando uma barreira refratária que bloqueia o corte.",
            "O alumínio reage de forma explosiva com o oxigênio em qualquer temperatura.",
        ],
        "resposta_correta": 2,
        "justificativa": "O óxido (Al2O3) tem ponto de fusão de ~2050°C (muito superior aos ~660°C do metal base), criando uma barreira sólida.",
    },
    {
        "id": 8,
        "pergunta": "De que forma a presença do cromo (acima de 10,5%) impede o oxicorte no aço inoxidável?",
        "opcoes": [
            "O cromo absorve todo o calor da chama, esfriando a chapa.",
            "O cromo gera uma película de óxido (Cr2O3) altamente estável e viscosa com ponto de fusão elevado (~2435°C), atuando como barreira.",
            "O cromo apaga a chama do acetileno assim que há o contato.",
            "O cromo torna o aço inoxidável magnético, desviando o jato de oxigênio.",
        ],
        "resposta_correta": 1,
        "justificativa": "O cromo reage com o oxigênio gerando uma película de óxido de cromo (Cr2O3) com ponto de fusão elevado (~2435°C), que funciona como uma barreira física.",
    },
    {
        "id": 9,
        "pergunta": "Quais processos térmicos são recomendados para o corte de aço inox e por que eles funcionam onde o oxicorte falha?",
        "opcoes": [
            "Corte com serra fita manual, por não gerar calor.",
            "Plasma ou Laser, pois fornecem alta energia para fundir o metal mecanicamente, sem depender da oxidação.",
            "Corte a jato de água abrasivo com adição de oxigênio líquido.",
            "Goivagem com eletrodo revestido de carvão ativo.",
        ],
        "resposta_correta": 1,
        "justificativa": "São recomendados Plasma ou Laser, pois eles fornecem alta energia para fundir o metal mecanicamente, sem depender da reação química de oxidação.",
    },
    {
        "id": 10,
        "pergunta": "Qual é a função principal dos reguladores de pressão fixados nos cilindros de gás?",
        "opcoes": [
            "Medir a pureza do gás dentro do cilindro.",
            "Reduzir a alta pressão interna do cilindro para uma pressão de trabalho constante e segura.",
            "Evitar que o cilindro tombe durante o uso.",
            "Misturar o oxigênio e o acetileno antes de irem para a mangueira.",
        ],
        "resposta_correta": 1,
        "justificativa": "Eles reduzem a alta pressão interna para uma pressão de trabalho constante e segura, garantindo a estabilidade da chama.",
    },
    {
        "id": 11,
        "pergunta": "Como diferenciar visualmente os reguladores e manômetros destinados ao Oxigênio daqueles destinados ao Acetileno?",
        "opcoes": [
            "O oxigênio possui corpo em latão; o acetileno é identificado pela cor vermelha ou por conexões específicas para gás combustível.",
            "Ambos são idênticos e podem ser trocados sem problemas de segurança.",
            "O oxigênio sempre usa mostradores digitais, enquanto o acetileno usa analógicos.",
            "O regulador de oxigênio é verde escuro e o de acetileno é azul claro.",
        ],
        "resposta_correta": 0,
        "justificativa": "O oxigênio geralmente possui corpo em latão, enquanto o acetileno é identificado pela cor vermelha nos manômetros ou por conexões específicas para gás combustível.",
    },
    {
        "id": 12,
        "pergunta": "Quais são as cores padronizadas das mangueiras gêmeas de solda/corte e o que cada cor transporta?",
        "opcoes": [
            "Azul para água de resfriamento e amarela para oxigênio.",
            "Preta para oxigênio e branca para acetileno.",
            "Verde transporta Oxigênio (comburente) e Vermelha transporta Acetileno (combustível).",
            "Ambas são pretas, diferenciadas apenas pelo diâmetro.",
        ],
        "resposta_correta": 2,
        "justificativa": "A mangueira Verde transporta o Oxigênio (gás comburente) e a mangueira Vermelha transporta o Acetileno ou outros gases combustíveis.",
    },
    {
        "id": 13,
        "pergunta": "Quais são os limites de temperatura de trabalho e a pressão máxima suportada pelas mangueiras flexíveis de PVC descritas?",
        "opcoes": [
            "Pressão máxima de 100 psi e temperatura de 0°C a 20°C.",
            "Pressão máxima de 500 psi e temperatura de -20°C a 100°C.",
            "Pressão máxima de 300 psi e faixa de temperatura segura de -5°C até +55°C.",
            "Pressão máxima de 150 psi e temperatura fixa de 25°C.",
        ],
        "resposta_correta": 2,
        "justificativa": "A pressão máxima é de 300 psi e a faixa de temperatura de trabalho segura vai de -5°C até +55°C.",
    },
    {
        "id": 14,
        "pergunta": "Explique a diferença de aplicação e funcionamento entre um Maçarico Injetor e um Maçarico Misturador.",
        "opcoes": [
            "O injetor mistura os gases na ponta do bico; o misturador mistura os gases no cilindro.",
            "O Injetor usa o Efeito Venturi do O2 para succionar gás combustível em baixa pressão; o Misturador atua com pressões médias/altas e iguais em ambos os gases.",
            "Não há diferença, são apenas nomes comerciais para a mesma ferramenta.",
            "O injetor é usado exclusivamente para cortes retos e o misturador para cortes circulares.",
        ],
        "resposta_correta": 1,
        "justificativa": "O Injetor é usado para baixa pressão (Efeito Venturi). O Misturador é utilizado com pressões médias/altas e iguais em ambos os gases.",
    },
    {
        "id": 15,
        "pergunta": "Como funciona um Gerador de Acetileno (carbureteira) e em quais situações ele substitui os cilindros pressurizados?",
        "opcoes": [
            "Gera acetileno a partir do ar ambiente; substitui cilindros em indústrias petroquímicas.",
            "Gera acetileno por compressão de gás natural; usado apenas em robôs de solda.",
            "Gera acetileno através da reação química entre carboneto de cálcio e água; ideal para oficinas e obras sem facilidade de abastecimento de cilindros.",
            "Gera acetileno aquecendo carvão vegetal; usado em cortes subaquáticos.",
        ],
        "resposta_correta": 2,
        "justificativa": "Ele gera acetileno em baixas pressões através da reação química entre o carboneto de cálcio e a água. Ideal para locais de difícil abastecimento logístico.",
    },
    {
        "id": 16,
        "pergunta": "Diferencie as funções dos acessórios 'Cintel', 'Carrinho de Corte' e 'Tartaruga'.",
        "opcoes": [
            "Cintel: cortes circulares; Carrinho: deslocamento retilíneo; Tartaruga: mecanizado para cortes automáticos longos.",
            "Cintel: mecanizado longo; Carrinho: cortes circulares; Tartaruga: limpa o bico.",
            "São todos equipamentos robóticos para controle numérico computadorizado (CNC).",
            "Cintel: acende a chama; Carrinho: transporta o cilindro; Tartaruga: apoia a mangueira.",
        ],
        "resposta_correta": 0,
        "justificativa": "Cintel é um compasso para cortes circulares; o Carrinho auxilia no deslocamento manual retilíneo; e a Tartaruga é um equipamento mecanizado para grandes extensões.",
    },
    {
        "id": 17,
        "pergunta": "Quais são as ferramentas essenciais usadas para a ignição da chama e para a desobstrução dos orifícios do bico do maçarico?",
        "opcoes": [
            "Fósforos de madeira e lixa de ferro.",
            "Acendedor de Copinho (gerador de faísca seguro) e o Limpador de Bicos ou Agulheiro.",
            "Isqueiro comum a gás e agulha de costura.",
            "Arco elétrico e escova de aço rotativa.",
        ],
        "resposta_correta": 1,
        "justificativa": "Utiliza-se o Acendedor de Copinho (gerador de faísca seguro) para ignição e o Limpador de Bicos (conjunto de agulhas calibradas) para desobstrução.",
    },
    {
        "id": 18,
        "pergunta": "Descreva as características da Chama Neutra, Chama Oxidante e Chama Carburante.",
        "opcoes": [
            "Neutra: não tem cor; Oxidante: solta fumaça; Carburante: usada apenas para aquecimento de chumbo.",
            "Neutra (1:1); Oxidante (excesso de O2, cone curto); Carburante (excesso acetileno, 'franja/véu').",
            "Todas possuem a mesma proporção, diferem apenas na pressão de saída ajustada no manômetro.",
            "Neutra: queima sem barulho; Oxidante: excesso de acetileno; Carburante: excesso de oxigênio.",
        ],
        "resposta_correta": 1,
        "justificativa": "Neutra (proporção 1:1), Oxidante (excesso de O2, para chapas grossas) e Carburante (excesso de acetileno, reduz oxidação superficial).",
    },
    {
        "id": 19,
        "pergunta": "Qual a importância das garras e correntes de fixação no armazenamento de cilindros e o que pode ocorrer em caso de queda livre?",
        "opcoes": [
            "Elas evitam arranhões na pintura do cilindro.",
            "Elas impedem que o gás evapore devido a trepidações.",
            "Evitam a queda acidental. Caso caiam, a válvula pode se romper, transformando o cilindro em um projétil perigoso devido à liberação violenta da pressão.",
            "Apenas para cumprir exigências estéticas na oficina, sem impacto na segurança.",
        ],
        "resposta_correta": 2,
        "justificativa": "Elas evitam a queda. O impacto pode romper a válvula de segurança, transformando o cilindro pressurizado em um projétil devido à alta pressão interna.",
    },
    {
        "id": 20,
        "pergunta": "Quais são os Equipamentos de Proteção Individual (EPIs) mínimos obrigatórios para a execução do oxicorte e o grau de proteção ocular exigido?",
        "opcoes": [
            "Protetor solar, óculos transparentes comuns e tênis esportivo.",
            "Óculos grau 3 a 8, avental de raspa, luvas de couro longas, perneiras, máscara PFF2 e botinas de segurança.",
            "Máscara de solda automática grau 13, luvas de procedimento cirúrgico e bota de borracha.",
            "Capacete de obra, protetor auricular tipo plug e jaleco de algodão.",
        ],
        "resposta_correta": 1,
        "justificativa": "Obrigatórios: Óculos com lentes grau 3 a 8, avental de raspa, luvas de couro de cano longo, perneiras, máscara PFF2 (contra fumos) e botinas com biqueira.",
    },
]

# ==========================================================================
# 4. TELA INICIAL - IDENTIFICAÇÃO
# ==========================================================================
if st.session_state.etapa_oxicorte == "inicio":
    st.markdown(
        """
        <div style='text-align: center; padding: 30px 0;'>
            <h1 style='color: #005088;'>Avaliação de Conhecimentos: Oxicorte</h1>
            <p style='color: #666; font-size: 16px;'>Avaliação técnica baseada no material de aula sobre o processo de oxicorte.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    nome = st.text_input(
        "Digite seu nome completo:", placeholder="Seu nome aqui...", key="input_nome"
    )

    col1, col2 = st.columns(2)
    with col1:
        # Quando o aluno clica em Iniciar, verificamos se ele preencheu o nome
        if st.button("Iniciar Avaliação", type="primary", use_container_width=True):
            if nome.strip():
                st.session_state.nome_aluno = nome
                st.session_state.etapa_oxicorte = "quiz"
                # Cria uma lista vazia com o mesmo tamanho da quantidade de questões
                st.session_state.respostas = [None] * len(questoes)
                st.rerun()  # Atualiza a tela imediatamente
            else:
                st.warning("Por favor, digite seu nome para continuar.")

    with col2:
        # Botão de voltar (Se você usa navegação multipáginas)
        if st.button("← Voltar", use_container_width=True):
            st.switch_page("Dione_Nascimento")

# ==========================================================================
# 5. TELA DO QUIZ (APRESENTAÇÃO DAS PERGUNTAS)
# ==========================================================================
elif st.session_state.etapa_oxicorte == "quiz":
    idx = st.session_state.questao_atual
    q = questoes[idx]

    # Barra de progresso visual para o aluno saber onde está
    st.progress((idx + 1) / len(questoes))
    st.markdown(
        f"<p style='text-align: center; color: #666;'>Questão {idx + 1} de {len(questoes)}</p>",
        unsafe_allow_html=True,
    )

    st.divider()

    # Apresenta a Pergunta atual na tela
    st.markdown(f"### {q['pergunta']}")

    # O widget radio gera as "bolinhas" de múltipla escolha.
    # O format_func puxa os textos que criamos nas opções.
    resposta = st.radio(
        "Selecione uma alternativa:",
        options=range(len(q["opcoes"])),
        format_func=lambda x: q["opcoes"][x],
        label_visibility="collapsed",
        key=f"radio_q{idx}",
    )

    st.divider()

    # Botões de navegação
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        # Se não for a primeira questão, permite voltar
        if idx > 0:
            if st.button("← Anterior", use_container_width=True):
                st.session_state.questao_atual -= 1
                st.rerun()

    with col2:
        # Botão para salvar a resposta e avançar
        if st.button("Confirmar", type="primary", use_container_width=True):
            st.session_state.respostas[idx] = resposta

            # Se ainda houver questões, avança para a próxima
            if idx < len(questoes) - 1:
                st.session_state.questao_atual += 1
                st.rerun()
            # Se for a última questão, vai para a tela de resultados
            else:
                st.session_state.etapa_oxicorte = "resultado"
                st.rerun()

    with col3:
        if st.button("← Cancelar e Voltar à Home", use_container_width=True):
            st.switch_page("Dione_Nascimento")

# ==========================================================================
# 6. TELA DE RESULTADOS E FEEDBACK
# ==========================================================================
elif st.session_state.etapa_oxicorte == "resultado":

    # Esta linha de código avançada (compreensão de lista) soma 1
    # toda vez que a resposta gravada bater com a resposta correta no BD.
    acertos = sum(
        1
        for i, q in enumerate(questoes)
        if st.session_state.respostas[i] == q["resposta_correta"]
    )

    total = len(questoes)
    percentual = (acertos / total) * 100
    data = datetime.now().strftime("%d/%m/%Y às %H:%M")

    # Cabeçalho de resultado personalizado
    st.markdown(
        f"""
        <div style='text-align: center; padding: 20px; background-color: #f0f8ff; border-radius: 8px; margin-bottom: 20px;'>
            <h2 style='color: #005088; margin: 0;'>Avaliação Concluída!</h2>
            <p style='color: #666; margin: 10px 0 0 0;'>{st.session_state.nome_aluno} | {data}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Mensagens condicionais baseadas na nota (percentual)
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

    # Revisão das questões (Gera o gabarito comentado)
    st.markdown("### Revisão das Questões")

    for i, q in enumerate(questoes):
        resposta_aluno = st.session_state.respostas[i]
        acertou = resposta_aluno == q["resposta_correta"]

        # Define as cores: Verde se acertou, Vermelho se errou
        cor = "#10b981" if acertou else "#ef4444"
        status = "✓ Correto" if acertou else "✗ Incorreto"

        st.markdown(
            f"""
            <div style='border-left: 5px solid {cor}; padding: 12px; background-color: #f9f9f9; margin-bottom: 15px; border-radius: 4px;'>
                <strong>Questão {i + 1}</strong> - {status}<br>
                <em>Sua resposta:</em> {q["opcoes"][resposta_aluno]}<br>
                <em>Resposta correta:</em> {q["opcoes"][q["resposta_correta"]]}<br><br>
                <strong>Justificativa do Professor:</strong> {q["justificativa"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    # Botões finais para reiniciar ou voltar à Home
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Fazer Novamente", use_container_width=True):
            st.session_state.etapa_oxicorte = "inicio"
            st.session_state.questao_atual = 0
            st.session_state.respostas = []
            st.session_state.nome_aluno = ""
            st.rerun()

    with col2:
        if st.button("← Voltar à Home", type="primary", use_container_width=True):
            st.switch_page("pages")  # Ajuste conforme as páginas do seu app
