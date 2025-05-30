import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
import io
import base64

# Configuração da página
st.set_page_config(
    page_title="Kairós - Protótipo Visual",
    page_icon="⏱️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado
st.markdown("""
<style>
    /* Cores principais */
    :root {
        --primary: #0066ff;
        --secondary: #001133;
        --accent: #00ccff;
        --background: #ffffff;
        --text: #001133;
    }
    
    /* Estilo geral */
    .main {
        background-color: var(--background);
        color: var(--text);
    }
    
    /* Cabeçalhos */
    h1, h2, h3 {
        color: var(--primary);
        font-family: 'Arial', sans-serif;
        font-weight: bold;
    }
    
    /* Texto */
    p, li {
        font-size: 18px;
        line-height: 1.6;
        color: var(--text);
    }
    
    /* Botões */
    .stButton>button {
        background-color: var(--primary);
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        font-weight: bold;
        border: none;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background-color: var(--accent);
        transform: scale(1.05);
    }
    
    /* Cards */
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        border-left: 5px solid var(--primary);
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: var(--secondary);
    }
    
    .sidebar .sidebar-content {
        background-color: var(--secondary);
    }
</style>
""", unsafe_allow_html=True)

# Função para criar avatar animado
def create_avatar():
    # Simulação de avatar animado
    cols = st.columns([1, 3, 1])
    with cols[1]:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        with st.container():
            placeholder = st.empty()
            for i in range(5):
                if i % 2 == 0:
                    placeholder.markdown("""
                    <div style="background-color: #001133; border-radius: 50%; width: 150px; height: 150px; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
                        <div style="color: #00ccff; font-size: 24px; font-weight: bold;">VoxMind™</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    placeholder.markdown("""
                    <div style="background-color: #0066ff; border-radius: 50%; width: 150px; height: 150px; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
                        <div style="color: white; font-size: 24px; font-weight: bold;">VoxMind™</div>
                    </div>
                    """, unsafe_allow_html=True)
                time.sleep(0.5)
            
            placeholder.markdown("""
            <div style="background-color: #001133; border-radius: 50%; width: 150px; height: 150px; margin: 0 auto; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
                <div style="color: #00ccff; font-size: 24px; font-weight: bold;">VoxMind™</div>
                <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 30%; background: linear-gradient(to top, #00ccff, transparent);"></div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Função para criar QR Code
def create_qr_code():
    # Simulação de QR Code
    qr_data = np.random.randint(0, 2, (25, 25))
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(qr_data, cmap='Blues')
    ax.axis('off')
    
    # Adicionar logo no centro
    logo_size = 7
    logo_pos = (25 - logo_size) // 2
    logo = np.ones((logo_size, logo_size)) * 0.5
    qr_data[logo_pos:logo_pos+logo_size, logo_pos:logo_pos+logo_size] = logo
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    return buf

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='color: white; text-align: center;'>Kairós</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: white; text-align: center;'>Assistente Pessoal de IA</p>", unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    menu = st.radio(
        "Navegação",
        ["Dashboard", "Agentes", "Automações", "Monetização", "Configurações"]
    )
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Perfil do usuário
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<div style='background-color: #0066ff; width: 60px; height: 60px; border-radius: 50%; margin: 0 auto; display: flex; align-items: center; justify-content: center;'><span style='color: white; font-size: 24px;'>JP</span></div>", unsafe_allow_html=True)
    st.markdown("<p style='color: white; margin-top: 10px;'>João Paulo</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Status do sistema
    st.markdown("<div style='margin-top: 20px; background-color: #002255; padding: 10px; border-radius: 5px;'>", unsafe_allow_html=True)
    st.markdown("<p style='color: white; margin: 0;'>Status: <span style='color: #00ff00;'>Online</span></p>", unsafe_allow_html=True)
    st.markdown("<p style='color: white; margin: 0;'>Agentes ativos: 3/3</p>", unsafe_allow_html=True)
    st.markdown("<p style='color: white; margin: 0;'>Automações: 5 ativas</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Conteúdo principal
if menu == "Dashboard":
    st.markdown("<h1 style='text-align: center;'>Dashboard Kairós</h1>", unsafe_allow_html=True)
    
    # Avatar animado
    create_avatar()
    
    st.markdown("<p style='text-align: center; font-size: 20px;'>Olá, João Paulo! Como posso ajudar você hoje?</p>", unsafe_allow_html=True)
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.metric("Tarefas Pendentes", "5", "-2")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.metric("Projetos Ativos", "3", "+1")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.metric("Receita (Maio)", "R$ 3.250", "+15%")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col4:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.metric("Bem-estar", "85%", "+5%")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Widgets
    st.markdown("<h2>Widgets</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h3>Agenda de Hoje</h3>", unsafe_allow_html=True)
        st.markdown("""
        - 09:00 - Reunião com cliente (Projeto Alpha)
        - 11:30 - Revisão de conteúdo para blog
        - 14:00 - Desenvolvimento de landing page
        - 16:30 - Análise de métricas de campanha
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h3>Análise Emocional</h3>", unsafe_allow_html=True)
        
        # Gráfico de radar para análise emocional
        categories = ['Foco', 'Energia', 'Motivação', 'Criatividade', 'Equilíbrio']
        values = [0.8, 0.6, 0.9, 0.7, 0.75]
        
        fig = plt.figure(figsize=(4, 4))
        ax = fig.add_subplot(111, polar=True)
        
        angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
        values = values + [values[0]]
        angles = angles + [angles[0]]
        categories = categories + [categories[0]]
        
        ax.plot(angles, values, 'o-', linewidth=2, color='#0066ff')
        ax.fill(angles, values, alpha=0.25, color='#0066ff')
        ax.set_thetagrids(np.degrees(angles[:-1]), categories[:-1])
        ax.set_ylim(0, 1)
        ax.grid(True)
        ax.set_facecolor('white')
        
        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Atividade recente
    st.markdown("<h2>Atividade Recente</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    activity_data = {
        'Horário': ['08:15', '08:00', 'Ontem 22:30', 'Ontem 18:45', 'Ontem 15:20'],
        'Atividade': [
            'Automação "Email Marketing" executada com sucesso',
            'Agente Carreira: 3 novas oportunidades identificadas',
            'Relatório semanal de monetização gerado',
            'Novo fluxo de automação criado: "Geração de Conteúdo"',
            'Integração com Notion atualizada'
        ],
        'Status': ['Concluído', 'Novo', 'Concluído', 'Novo', 'Atualizado']
    }
    
    df = pd.DataFrame(activity_data)
    
    # Estilizar o dataframe
    def highlight_status(val):
        if val == 'Concluído':
            return 'background-color: #e6ffe6; color: #006600'
        elif val == 'Novo':
            return 'background-color: #e6f2ff; color: #0066cc'
        else:
            return 'background-color: #fff5e6; color: #cc7700'
    
    styled_df = df.style.applymap(highlight_status, subset=['Status'])
    
    st.table(styled_df)
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Agentes":
    st.markdown("<h1 style='text-align: center;'>Agentes Especializados</h1>", unsafe_allow_html=True)
    
    # Tabs para os diferentes agentes
    tab1, tab2, tab3 = st.tabs(["Agente Mente", "Agente Corpo", "Agente Carreira"])
    
    with tab1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Agente Mente</h2>", unsafe_allow_html=True)
        st.markdown("<p>Especializado em produtividade, organização e bem-estar mental.</p>", unsafe_allow_html=True)
        
        # Status do agente
        st.markdown("<h3>Status</h3>", unsafe_allow_html=True)
        st.progress(0.9)
        st.markdown("<p>Desempenho: 90% - Excelente</p>", unsafe_allow_html=True)
        
        # Funcionalidades
        st.markdown("<h3>Funcionalidades</h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            - Gestão de tarefas e projetos
            - Técnicas de foco e concentração
            - Organização de informações
            - Lembretes contextuais
            """)
        
        with col2:
            st.markdown("""
            - Meditação guiada
            - Análise de produtividade
            - Integração com Notion
            - Resumo de conteúdos
            """)
        
        # Configurações
        st.markdown("<h3>Configurações</h3>", unsafe_allow_html=True)
        st.slider("Nível de Proatividade", 0, 100, 75)
        st.slider("Frequência de Lembretes", 0, 100, 60)
        st.multiselect("Integrações Ativas", ["Notion", "Google Calendar", "Todoist", "Evernote"], ["Notion", "Google Calendar"])
        
        st.button("Salvar Configurações do Agente Mente")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Agente Corpo</h2>", unsafe_allow_html=True)
        st.markdown("<p>Especializado em saúde física, exercícios e hábitos saudáveis.</p>", unsafe_allow_html=True)
        
        # Status do agente
        st.markdown("<h3>Status</h3>", unsafe_allow_html=True)
        st.progress(0.85)
        st.markdown("<p>Desempenho: 85% - Muito Bom</p>", unsafe_allow_html=True)
        
        # Funcionalidades
        st.markdown("<h3>Funcionalidades</h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            - Acompanhamento de atividades físicas
            - Monitoramento de hidratação
            - Lembretes para pausas e movimento
            - Análise de padrões de sono
            """)
        
        with col2:
            st.markdown("""
            - Recomendações nutricionais
            - Integração com dispositivos wearables
            - Exercícios rápidos para pausas
            - Monitoramento de indicadores de saúde
            """)
        
        # Configurações
        st.markdown("<h3>Configurações</h3>", unsafe_allow_html=True)
        st.slider("Frequência de Lembretes de Movimento", 0, 100, 80)
        st.slider("Intensidade de Exercícios", 0, 100, 65)
        st.multiselect("Integrações Ativas", ["Google Fit", "Apple Health", "Fitbit", "Strava"], ["Google Fit"])
        
        st.button("Salvar Configurações do Agente Corpo")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Agente Carreira</h2>", unsafe_allow_html=True)
        st.markdown("<p>Especializado em desenvolvimento profissional, networking e monetização.</p>", unsafe_allow_html=True)
        
        # Status do agente
        st.markdown("<h3>Status</h3>", unsafe_allow_html=True)
        st.progress(0.95)
        st.markdown("<p>Desempenho: 95% - Excepcional</p>", unsafe_allow_html=True)
        
        # Funcionalidades
        st.markdown("<h3>Funcionalidades</h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            - Gestão de projetos profissionais
            - Identificação de oportunidades
            - Automação de processos de negócio
            - Análise de mercado e tendências
            """)
        
        with col2:
            st.markdown("""
            - Fluxos de monetização digital
            - Integração com plataformas de e-commerce
            - Automação de marketing digital
            - Relatórios de desempenho financeiro
            """)
        
        # Configurações
        st.markdown("<h3>Configurações</h3>", unsafe_allow_html=True)
        st.slider("Agressividade de Monetização", 0, 100, 70)
        st.slider("Frequência de Relatórios", 0, 100, 85)
        st.multiselect("Integrações Ativas", ["LinkedIn", "Shopify", "Google Analytics", "Meta Ads"], ["LinkedIn", "Google Analytics"])
        
        st.button("Salvar Configurações do Agente Carreira")
        st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Automações":
    st.markdown("<h1 style='text-align: center;'>Automações Configuráveis</h1>", unsafe_allow_html=True)
    
    # Biblioteca de automações
    st.markdown("<h2>Biblioteca de Automações</h2>", unsafe_allow_html=True)
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.selectbox("Categoria", ["Todas", "Produtividade", "Marketing", "E-commerce", "Conteúdo", "Finanças"])
    
    with col2:
        st.selectbox("Nicho", ["Todos", "Agência Digital", "Educação", "Saúde", "Varejo", "Tecnologia"])
    
    with col3:
        st.selectbox("Status", ["Todos", "Ativo", "Inativo", "Em Teste"])
    
    # Lista de automações
    automations = [
        {
            "nome": "Geração de Conteúdo Automatizado",
            "categoria": "Conteúdo",
            "descricao": "Cria artigos, posts e vídeos com base em palavras-chave e tendências.",
            "status": "Ativo"
        },
        {
            "nome": "Funil de Email Marketing",
            "categoria": "Marketing",
            "descricao": "Sequência automatizada de emails para nutrição de leads.",
            "status": "Ativo"
        },
        {
            "nome": "Gestão de E-commerce",
            "categoria": "E-commerce",
            "descricao": "Automação de catálogo, precificação e atendimento para lojas virtuais.",
            "status": "Inativo"
        },
        {
            "nome": "Análise de Concorrência",
            "categoria": "Marketing",
            "descricao": "Monitoramento automático de concorrentes e geração de insights.",
            "status": "Ativo"
        },
        {
            "nome": "Relatórios Financeiros",
            "categoria": "Finanças",
            "descricao": "Geração automática de relatórios de receitas, despesas e projeções.",
            "status": "Ativo"
        }
    ]
    
    for i, automation in enumerate(automations):
        st.markdown(f"""
        <div class='card'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div>
                    <h3>{automation['nome']}</h3>
                    <p><strong>Categoria:</strong> {automation['categoria']}</p>
                    <p>{automation['descricao']}</p>
                </div>
                <div>
                    <span style='background-color: {"#e6ffe6" if automation["status"] == "Ativo" else "#ffe6e6"}; 
                                color: {"#006600" if automation["status"] == "Ativo" else "#cc0000"}; 
                                padding: 5px 10px; 
                                border-radius: 15px;'>
                        {automation['status']}
                    </span>
                </div>
            </div>
            <div style='display: flex; gap: 10px; margin-top: 10px;'>
                <button style='background-color: #0066ff; color: white; border: none; padding: 5px 15px; border-radius: 5px; cursor: pointer;'>Editar</button>
                <button style='background-color: {"#cc0000" if automation["status"] == "Ativo" else "#0066ff"}; color: white; border: none; padding: 5px 15px; border-radius: 5px; cursor: pointer;'}>
                    {"Desativar" if automation["status"] == "Ativo" else "Ativar"}
                </button>
                <button style='background-color: #333333; color: white; border: none; padding: 5px 15px; border-radius: 5px; cursor: pointer;'>Duplicar</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Criar nova automação
    st.markdown("<h2>Criar Nova Automação</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.text_input("Nome da Automação", "Nova Automação")
    st.selectbox("Categoria da Automação", ["Produtividade", "Marketing", "E-commerce", "Conteúdo", "Finanças"])
    st.selectbox("Nicho", ["Agência Digital", "Educação", "Saúde", "Varejo", "Tecnologia", "Outro"])
    st.text_area("Descrição", "Descreva o objetivo desta automação...")
    
    st.markdown("<h3>Editor de Fluxo</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style="border: 1px dashed #0066ff; border-radius: 5px; padding: 20px; text-align: center; margin-bottom: 20px;">
        <p style="color: #0066ff;">Arraste e solte componentes para criar seu fluxo de automação</p>
        <div style="display: flex; justify-content: center; gap: 10px; margin-top: 10px;">
            <button style="background-color: #0066ff; color: white; border: none; padding: 5px 15px; border-radius: 5px; cursor: pointer;">Gatilho</button>
            <button style="background-color: #0066ff; color: white; border: none; padding: 5px 15px; border-radius: 5px; cursor: pointer;">Condição</button>
            <button style="background-color: #0066ff; color: white; border: none; padding: 5px 15px; border-radius: 5px; cursor: pointer;">Ação</button>
            <button style="background-color: #0066ff; color: white; border: none; padding: 5px 15px; border-radius: 5px; cursor: pointer;">Integração</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.button("Cancelar")
    
    with col2:
        st.button("Criar Automação")
    
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Monetização":
    st.markdown("<h1 style='text-align: center;'>Fluxos de Monetização Digital</h1>", unsafe_allow_html=True)
    
    # Métricas de monetização
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.metric("Receita Mensal", "R$ 3.250", "+15%")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.metric("Conversões", "32", "+8")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.metric("Taxa de Conversão", "3.8%", "+0.5%")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col4:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.metric("Custo de Aquisição", "R$ 18,50", "-12%")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Estratégias de monetização
    st.markdown("<h2>Estratégias de Monetização</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Web Design Automatizado", 
        "Negócios Digitais", 
        "Agência de Serviços", 
        "Conteúdo Automatizado",
        "E-commerce"
    ])
    
    with tab1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h3>Web Design Automatizado</h3>", unsafe_allow_html=True)
        st.markdown("<p>Crie sites, landing pages e aplicativos completos sem conhecimento técnico.</p>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h4>Fluxo de Trabalho</h4>", unsafe_allow_html=True)
            st.markdown("""
            1. **Configuração de Projeto**: Definição de objetivos e requisitos
            2. **Geração de Design**: Criação automatizada de layouts
            3. **Produção de Conteúdo**: Textos e mídias personalizados
            4. **Publicação**: Integração com hospedagem e domínios
            5. **Otimização**: Ajustes baseados em métricas de desempenho
            """)
        
        with col2:
            st.markdown("<h4>Ferramentas Integradas</h4>", unsafe_allow_html=True)
            st.markdown("""
            - **Bolt.new**: Criação de aplicativos com prompts
            - **Gamma**: Geração de layouts profissionais
            - **Midjourney/DALL-E**: Elementos visuais personalizados
            - **ChatGPT**: Conteúdo textual otimizado para SEO
            - **Hostgator**: Publicação e hospedagem automática
            """)
        
        st.markdown("<h4>Resultados Esperados</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Criação de sites profissionais em horas, não semanas
        - Redução de custos de desenvolvimento em até 90%
        - Capacidade de atender múltiplos clientes simultaneamente
        - Escalabilidade sem necessidade de equipe técnica
        """)
        
        st.button("Ativar Fluxo de Web Design")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h3>Negócios Digitais Automatizados</h3>", unsafe_allow_html=True)
        st.markdown("<p>Desenvolva negócios digitais completos em horas, incluindo produto, marketing e vendas.</p>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h4>Fluxo de Trabalho</h4>", unsafe_allow_html=True)
            st.markdown("""
            1. **Validação de Ideias**: Análise de mercado automatizada
            2. **Criação de Produto**: Geração de infoprodutos digitais
            3. **Desenvolvimento de Funil**: Automação de jornada de vendas
            4. **Configuração de Marketing**: Campanhas e conteúdo
            5. **Atendimento ao Cliente**: Suporte automatizado
            """)
        
        with col2:
            st.markdown("<h4>Ferramentas Integradas</h4>", unsafe_allow_html=True)
            st.markdown("""
            - **ChatGPT**: Pesquisa de mercado e criação de conteúdo
            - **Synthesia**: Produção de vídeo-aulas profissionais
            - **Mailerlite**: Automação de email marketing
            - **Hotmart/Kiwify**: Plataformas de venda de infoprodutos
            - **Umbler Talk**: Atendimento automatizado ao cliente
            """)
        
        st.markdown("<h4>Resultados Esperados</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Lançamento de produtos digitais em dias, não meses
        - Automação de 90% do processo de vendas e marketing
        - Escalabilidade sem aumento proporcional de custos
        - Análise contínua e otimização baseada em dados
        """)
        
        st.button("Ativar Fluxo de Negócios Digitais")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Gráfico de desempenho
    st.markdown("<h2>Desempenho de Monetização</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # Dados simulados para o gráfico
    dates = pd.date_range(start='2025-04-01', end='2025-05-24', freq='D')
    revenue = np.cumsum(np.random.normal(100, 30, size=len(dates)))
    revenue = np.maximum(revenue, 0)  # Garantir valores não negativos
    
    df = pd.DataFrame({
        'Data': dates,
        'Receita': revenue
    })
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['Data'], df['Receita'], color='#0066ff', linewidth=2)
    ax.fill_between(df['Data'], df['Receita'], color='#0066ff', alpha=0.2)
    ax.set_xlabel('Data')
    ax.set_ylabel('Receita Acumulada (R$)')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_title('Receita Acumulada - Últimos 60 dias')
    
    # Formatação do eixo y para mostrar valores em reais
    from matplotlib.ticker import FuncFormatter
    def currency_formatter(x, pos):
        return f'R$ {x:.2f}'
    
    ax.yaxis.set_major_formatter(FuncFormatter(currency_formatter))
    
    # Rotacionar datas no eixo x para melhor visualização
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    st.pyplot(fig)
    
    # Seletor de período
    st.selectbox("Período", ["Últimos 30 dias", "Últimos 60 dias", "Últimos 90 dias", "Este ano", "Personalizado"])
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Oportunidades de monetização
    st.markdown("<h2>Oportunidades Identificadas</h2>", unsafe_allow_html=True)
    
    opportunities = [
        {
            "titulo": "Criação de Canal Dark no YouTube",
            "potencial": "Alto",
            "complexidade": "Média",
            "retorno": "R$ 1.000 - R$ 3.000/mês"
        },
        {
            "titulo": "Agência de Web Design Automatizado",
            "potencial": "Muito Alto",
            "complexidade": "Baixa",
            "retorno": "R$ 3.000 - R$ 10.000/mês"
        },
        {
            "titulo": "Dropshipping Nicho de Tecnologia",
            "potencial": "Médio",
            "complexidade": "Média",
            "retorno": "R$ 2.000 - R$ 5.000/mês"
        }
    ]
    
    for opportunity in opportunities:
        st.markdown(f"""
        <div class='card'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div>
                    <h3>{opportunity['titulo']}</h3>
                    <p><strong>Potencial de Mercado:</strong> <span style='color: {"#006600" if opportunity["potencial"] in ["Alto", "Muito Alto"] else "#cc7700"};'>{opportunity['potencial']}</span></p>
                    <p><strong>Complexidade de Implementação:</strong> <span style='color: {"#006600" if opportunity["complexidade"] == "Baixa" else "#cc7700" if opportunity["complexidade"] == "Média" else "#cc0000"};'>{opportunity['complexidade']}</span></p>
                    <p><strong>Retorno Estimado:</strong> {opportunity['retorno']}</p>
                </div>
                <div>
                    <button style='background-color: #0066ff; color: white; border: none; padding: 8px 20px; border-radius: 5px; cursor: pointer;'>Implementar</button>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif menu == "Configurações":
    st.markdown("<h1 style='text-align: center;'>Configurações do Sistema</h1>", unsafe_allow_html=True)
    
    # Tabs para diferentes configurações
    tab1, tab2, tab3, tab4 = st.tabs(["Perfil", "Integrações", "Acessibilidade", "Sistema"])
    
    with tab1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Perfil do Usuário</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown("<div style='background-color: #0066ff; width: 150px; height: 150px; border-radius: 50%; display: flex; align-items: center; justify-content: center;'><span style='color: white; font-size: 48px;'>JP</span></div>", unsafe_allow_html=True)
            st.button("Alterar Avatar")
        
        with col2:
            st.text_input("Nome", "João Paulo")
            st.text_input("Email", "joao.paulo@exemplo.com")
            st.text_input("Telefone", "+55 (11) 98765-4321")
            st.selectbox("Fuso Horário", ["America/Sao_Paulo (UTC-3)", "America/New_York (UTC-4)", "Europe/London (UTC+1)"])
        
        st.markdown("<h3>Preferências</h3>", unsafe_allow_html=True)
        st.selectbox("Idioma", ["Português (Brasil)", "English (US)", "Español"])
        st.selectbox("Tema", ["Claro", "Escuro", "Sistema"])
        st.slider("Volume de Notificações", 0, 100, 70)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.checkbox("Ativar notificações por email")
            st.checkbox("Ativar notificações por push")
        
        with col2:
            st.checkbox("Ativar sons de sistema")
            st.checkbox("Ativar modo de economia de dados")
        
        st.button("Salvar Alterações de Perfil")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Integrações</h2>", unsafe_allow_html=True)
        
        # Notion
        st.markdown("<h3>Notion</h3>", unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("<p>Sincronize tarefas, projetos e bases de conhecimento com o Notion.</p>", unsafe_allow_html=True)
            st.text_input("Token de API Notion", "••••••••••••••••••••••••••••••")
            st.multiselect("Workspaces Sincronizados", ["Pessoal", "Trabalho", "Projetos", "Estudos"], ["Pessoal", "Projetos"])
        
        with col2:
            st.markdown("<div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px; text-align: center;'>", unsafe_allow_html=True)
            st.markdown("<p style='margin: 0;'>Status: <span style='color: #006600;'>Conectado</span></p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.button("Desconectar Notion")
        
        # Android Auto
        st.markdown("<h3>Android Auto</h3>", unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("<p>Acesse o Kairós de forma segura durante deslocamentos via Android Auto.</p>", unsafe_allow_html=True)
            st.selectbox("Dispositivo Conectado", ["Samsung Galaxy S22", "Adicionar novo dispositivo"])
            st.multiselect("Funcionalidades Ativas", ["Comandos de Voz", "Resumos Auditivos", "Notificações", "Agendamento por Voz"], ["Comandos de Voz", "Resumos Auditivos"])
        
        with col2:
            st.markdown("<div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px; text-align: center;'>", unsafe_allow_html=True)
            st.markdown("<p style='margin: 0;'>Status: <span style='color: #006600;'>Conectado</span></p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.button("Desconectar Android Auto")
        
        # Outras integrações
        st.markdown("<h3>Outras Integrações</h3>", unsafe_allow_html=True)
        
        integrations = [
            {"nome": "Google Calendar", "status": "Conectado", "icon": "📅"},
            {"nome": "Gmail", "status": "Desconectado", "icon": "✉️"},
            {"nome": "Shopify", "status": "Conectado", "icon": "🛒"},
            {"nome": "LinkedIn", "status": "Desconectado", "icon": "👔"},
            {"nome": "Meta Ads", "status": "Conectado", "icon": "📣"}
        ]
        
        for integration in integrations:
            st.markdown(f"""
            <div style='display: flex; justify-content: space-between; align-items: center; padding: 10px; border-bottom: 1px solid #eee;'>
                <div style='display: flex; align-items: center;'>
                    <span style='font-size: 24px; margin-right: 10px;'>{integration['icon']}</span>
                    <span>{integration['nome']}</span>
                </div>
                <div>
                    <span style='color: {"#006600" if integration["status"] == "Conectado" else "#cc0000"};'>{integration['status']}</span>
                    <button style='background-color: {"#cc0000" if integration["status"] == "Conectado" else "#0066ff"}; color: white; border: none; padding: 5px 10px; border-radius: 5px; margin-left: 10px; cursor: pointer;'>
                        {"Desconectar" if integration["status"] == "Conectado" else "Conectar"}
                    </button>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.button("Adicionar Nova Integração")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Acessibilidade</h2>", unsafe_allow_html=True)
        
        st.markdown("<h3>Configurações Visuais</h3>", unsafe_allow_html=True)
        st.slider("Tamanho da Fonte", 80, 150, 100, format="%d%%")
        st.slider("Contraste", 80, 150, 100, format="%d%%")
        st.checkbox("Modo de Alto Contraste")
        st.checkbox("Reduzir Animações")
        
        st.markdown("<h3>Leitores de Tela</h3>", unsafe_allow_html=True)
        st.checkbox("Otimizar para leitores de tela")
        st.selectbox("Velocidade de Narração", ["Muito Lenta", "Lenta", "Normal", "Rápida", "Muito Rápida"])
        
        st.markdown("<h3>Suporte a Libras</h3>", unsafe_allow_html=True)
        st.checkbox("Ativar tradutor de Libras")
        st.selectbox("Tamanho do Intérprete", ["Pequeno", "Médio", "Grande"])
        st.selectbox("Posição do Intérprete", ["Inferior Direito", "Inferior Esquerdo", "Superior Direito", "Superior Esquerdo"])
        
        st.markdown("<h3>Entrada Alternativa</h3>", unsafe_allow_html=True)
        st.checkbox("Ativar controle por voz avançado")
        st.checkbox("Ativar navegação por teclado aprimorada")
        st.checkbox("Ativar controle por gestos (webcam)")
        
        st.button("Salvar Configurações de Acessibilidade")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab4:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Configurações do Sistema</h2>", unsafe_allow_html=True)
        
        st.markdown("<h3>Desempenho</h3>", unsafe_allow_html=True)
        st.slider("Nível de Processamento", 0, 100, 80, format="%d%%")
        st.slider("Armazenamento Local", 0, 100, 50, format="%d%%")
        st.checkbox("Processar tarefas em segundo plano")
        st.checkbox("Otimizar para dispositivos de baixo desempenho")
        
        st.markdown("<h3>Privacidade e Dados</h3>", unsafe_allow_html=True)
        st.checkbox("Armazenar dados sensíveis apenas localmente")
        st.checkbox("Criptografar todos os dados")
        st.checkbox("Enviar dados anônimos de uso para melhorias")
        
        st.markdown("<h3>Backup e Sincronização</h3>", unsafe_allow_html=True)
        st.selectbox("Frequência de Backup", ["Diária", "Semanal", "Mensal", "Manual"])
        st.selectbox("Destino de Backup", ["Nuvem (Criptografado)", "Local", "Ambos"])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.button("Fazer Backup Agora")
        
        with col2:
            st.button("Restaurar Backup")
        
        st.markdown("<h3>Manutenção</h3>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.button("Limpar Cache")
        
        with col2:
            st.button("Verificar Atualizações")
        
        with col3:
            st.button("Reiniciar Sistema")
        
        st.markdown("<div style='background-color: #ffe6e6; padding: 10px; border-radius: 5px; margin-top: 20px;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #cc0000; margin-top: 0;'>Zona de Perigo</h3>", unsafe_allow_html=True)
        st.markdown("<p>Estas ações são irreversíveis e podem resultar em perda de dados.</p>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.button("Redefinir para Padrões de Fábrica")
        
        with col2:
            st.button("Excluir Conta e Dados")
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Seção de conexão via QR Code
st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='color: white; text-align: center;'>Conectar Dispositivo</h3>", unsafe_allow_html=True)

qr_buf = create_qr_code()
qr_img = Image.open(qr_buf)

st.sidebar.image(qr_img, width=150, caption="Escaneie para conectar")
st.sidebar.markdown("<p style='color: white; text-align: center; font-size: 12px;'>Ou use o código: <strong>KAIROS-JP-2505</strong></p>", unsafe_allow_html=True)

# Rodapé
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-size: 12px;'>Kairós v1.0.0 | © 2025 Todos os direitos reservados</p>", unsafe_allow_html=True)
