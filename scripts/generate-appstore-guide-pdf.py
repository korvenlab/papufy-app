"""Gera PDF com passo a passo para enviar o Papufy à App Store no Mac."""
from __future__ import annotations

import os

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUT = r"D:\Projetos\papufy-app\store\Papufy-App-Store-passo-a-passo-Mac.pdf"

arial = r"C:\Windows\Fonts\arial.ttf"
arialbd = r"C:\Windows\Fonts\arialbd.ttf"
if os.path.exists(arial):
    pdfmetrics.registerFont(TTFont("Arial", arial))
if os.path.exists(arialbd):
    pdfmetrics.registerFont(TTFont("Arial-Bold", arialbd))

FN = "Arial" if os.path.exists(arial) else "Helvetica"
FB = "Arial-Bold" if os.path.exists(arialbd) else "Helvetica-Bold"

SKY = HexColor("#0284c7")
SKY_DARK = HexColor("#0369a1")
SLATE = HexColor("#0f172a")
MUTED = HexColor("#475569")
LIGHT = HexColor("#f0f9ff")
BORDER = HexColor("#bae6fd")
WARN_BG = HexColor("#fff7ed")
WARN = HexColor("#c2410c")
OK = HexColor("#15803d")
OK_BG = HexColor("#f0fdf4")


def main() -> None:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)

    doc = SimpleDocTemplate(
        OUT,
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=1.6 * cm,
        bottomMargin=1.8 * cm,
        title="Papufy — Enviar o app para a App Store (Mac)",
        author="Papufy",
    )

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            fontName=FB,
            fontSize=20,
            textColor=SKY_DARK,
            leading=26,
            spaceAfter=6,
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSub",
            fontName=FN,
            fontSize=11,
            textColor=MUTED,
            leading=15,
            spaceAfter=4,
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H1",
            fontName=FB,
            fontSize=13,
            textColor=SKY_DARK,
            leading=17,
            spaceBefore=12,
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2",
            fontName=FB,
            fontSize=11,
            textColor=SLATE,
            leading=14,
            spaceBefore=8,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            fontName=FN,
            fontSize=10,
            textColor=SLATE,
            leading=14,
            spaceAfter=4,
            alignment=TA_JUSTIFY,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BulletItem",
            fontName=FN,
            fontSize=10,
            textColor=SLATE,
            leading=14,
            leftIndent=10,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="StepTitle",
            fontName=FB,
            fontSize=10.5,
            textColor=white,
            leading=14,
        )
    )
    styles.add(
        ParagraphStyle(
            name="StepBody",
            fontName=FN,
            fontSize=10,
            textColor=SLATE,
            leading=13.5,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeBlock",
            fontName="Courier",
            fontSize=8.2,
            textColor=SLATE,
            leading=11,
            leftIndent=4,
            spaceBefore=1,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Note",
            fontName=FN,
            fontSize=9,
            textColor=WARN,
            leading=12,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="OkNote",
            fontName=FN,
            fontSize=9,
            textColor=OK,
            leading=12,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Footer",
            fontName=FN,
            fontSize=8,
            textColor=MUTED,
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Cell",
            fontName=FN,
            fontSize=9,
            textColor=SLATE,
            leading=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CellB",
            fontName=FB,
            fontSize=9,
            textColor=SLATE,
            leading=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CellW",
            fontName=FB,
            fontSize=9,
            textColor=white,
            leading=12,
        )
    )

    story: list = []

    def info_box(text: str, kind: str = "warn"):
        bg = WARN_BG if kind == "warn" else OK_BG
        style = styles["Note"] if kind == "warn" else styles["OkNote"]
        border = WARN if kind == "warn" else OK
        t = Table([[Paragraph(text, style)]], colWidths=[17 * cm])
        t.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), bg),
                    ("BOX", (0, 0), (-1, -1), 0.6, border),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ]
            )
        )
        return [t, Spacer(1, 8)]

    def step_box(num: int, title: str, body_paras: list):
        header = Table(
            [[Paragraph(f"PASSO {num} — {title}", styles["StepTitle"])]],
            colWidths=[17 * cm],
        )
        header.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), SKY),
                    ("LEFTPADDING", (0, 0), (-1, -1), 10),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ]
            )
        )
        parts: list = [header, Spacer(1, 4)]
        for item in body_paras:
            if isinstance(item, list):
                parts.extend(item)
            else:
                parts.append(item)
        parts.append(Spacer(1, 9))
        return parts

    # Capa
    story.append(Spacer(1, 1.8 * cm))
    story.append(Paragraph("PAPUFY", styles["CoverTitle"]))
    story.append(
        Paragraph("Enviar o app para a Apple App Store", styles["CoverTitle"])
    )
    story.append(Spacer(1, 0.2 * cm))
    story.append(
        Paragraph(
            "Passo a passo no MacBook (Xcode + App Store Connect)",
            styles["CoverSub"],
        )
    )
    story.append(Paragraph("Documento interno — novembro 2026", styles["CoverSub"]))
    story.append(Spacer(1, 0.6 * cm))

    meta = [
        [Paragraph("<b>App</b>", styles["CellB"]), Paragraph("Papufy", styles["Cell"])],
        [
            Paragraph("<b>Bundle ID</b>", styles["CellB"]),
            Paragraph("com.papufy.app", styles["Cell"]),
        ],
        [
            Paragraph("<b>Projeto</b>", styles["CellB"]),
            Paragraph("papufy-app / pasta ios", styles["Cell"]),
        ],
        [
            Paragraph("<b>Site no app</b>", styles["CellB"]),
            Paragraph("https://papufy.com", styles["Cell"]),
        ],
        [
            Paragraph("<b>Privacidade</b>", styles["CellB"]),
            Paragraph("https://papufy.com/privacidade", styles["Cell"]),
        ],
        [
            Paragraph("<b>Termos</b>", styles["CellB"]),
            Paragraph("https://papufy.com/termos", styles["Cell"]),
        ],
        [
            Paragraph("<b>Suporte</b>", styles["CellB"]),
            Paragraph("contato@papufy.com", styles["Cell"]),
        ],
        [
            Paragraph("<b>Excluir conta</b>", styles["CellB"]),
            Paragraph("https://papufy.com/excluir-conta", styles["Cell"]),
        ],
    ]
    mt = Table(meta, colWidths=[4 * cm, 13 * cm])
    mt.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
                ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
                ("INNERGRID", (0, 0), (-1, -1), 0.3, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(mt)
    story.append(Spacer(1, 0.5 * cm))
    story.extend(
        info_box(
            "<b>Importante:</b> o arquivo .aab da Google Play NÃO serve para a Apple. "
            "No Mac você gera um build iOS a partir da pasta <b>ios</b> do mesmo repositório."
        )
    )
    story.append(
        Paragraph(
            "Este guia assume que o MacBook tem internet e que você consegue abrir "
            "o Terminal e o Xcode.",
            styles["Body"],
        )
    )

    story.append(PageBreak())

    # Antes
    story.append(Paragraph("1. Antes de começar", styles["H1"]))
    story.append(Paragraph("Você precisa destes itens prontos:", styles["Body"]))
    for b in [
        "Conta <b>Apple Developer Program</b> ativa (US$ 99/ano) em developer.apple.com.",
        "MacBook com <b>macOS recente</b> e <b>Xcode</b> instalado pela App Store.",
        "Código do app: repositório <b>papufy-app</b> (GitHub ou cópia da pasta).",
        "Prints: pasta <b>store/screenshots</b> (copie do Windows para o Mac).",
        "Conta de teste para revisão: <b>play.review@papufy.com</b> (mesma da Play).",
    ]:
        story.append(Paragraph(f"• {b}", styles["BulletItem"]))
    story.append(Spacer(1, 0.15 * cm))
    story.extend(
        info_box(
            "Se o Xcode ainda não estiver instalado: App Store no Mac → busque "
            "“Xcode” → Instalar. Na primeira abertura, aceite a licença."
        )
    )

    story.append(Paragraph("Pastas importantes no projeto", styles["H2"]))
    code_rows = [
        [
            Paragraph("Caminho", styles["CellW"]),
            Paragraph("Para quê", styles["CellW"]),
        ],
        [
            Paragraph("papufy-app/", styles["Cell"]),
            Paragraph("Raiz do app Capacitor", styles["Cell"]),
        ],
        [
            Paragraph("papufy-app/ios/App/App.xcworkspace", styles["Cell"]),
            Paragraph("Abrir no Xcode (sempre o .xcworkspace)", styles["Cell"]),
        ],
        [
            Paragraph("store/screenshots/app-store-iphone-6.9/", styles["Cell"]),
            Paragraph("Prints iPhone", styles["Cell"]),
        ],
        [
            Paragraph("store/screenshots/app-store-ipad-13/", styles["Cell"]),
            Paragraph("Prints iPad", styles["Cell"]),
        ],
        [
            Paragraph("store/icon-1024.png", styles["Cell"]),
            Paragraph("Ícone 1024×1024", styles["Cell"]),
        ],
    ]
    ct = Table(code_rows, colWidths=[9.5 * cm, 7.5 * cm])
    ct.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), SKY),
                ("BOX", (0, 0), (-1, -1), 0.6, BORDER),
                ("INNERGRID", (0, 0), (-1, -1), 0.3, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(ct)

    story.append(PageBreak())
    story.append(Paragraph("2. Passo a passo no Mac", styles["H1"]))

    story.extend(
        step_box(
            1,
            "Levar o projeto para o Mac",
            [
                Paragraph("Escolha um destes jeitos:", styles["StepBody"]),
                Paragraph(
                    "• <b>Opção A (melhor):</b> no Mac, clone o repositório Git:",
                    styles["StepBody"],
                ),
                Paragraph(
                    "git clone https://github.com/korvenlab/papufy-app.git",
                    styles["CodeBlock"],
                ),
                Paragraph("cd papufy-app", styles["CodeBlock"]),
                Paragraph(
                    "• <b>Opção B:</b> copie a pasta D:\\Projetos\\papufy-app do "
                    "Windows para o Mac (pendrive, AirDrop, OneDrive). Se copiar "
                    "sem node_modules, rode npm install no Mac.",
                    styles["StepBody"],
                ),
                Paragraph("Dentro da pasta do projeto, rode:", styles["StepBody"]),
                Paragraph("npm install", styles["CodeBlock"]),
                Paragraph("npx cap sync ios", styles["CodeBlock"]),
            ],
        )
    )

    story.extend(
        step_box(
            2,
            "Instalar CocoaPods (dependências iOS)",
            [
                Paragraph("No Terminal do Mac:", styles["StepBody"]),
                Paragraph("sudo gem install cocoapods", styles["CodeBlock"]),
                Paragraph("cd ios/App", styles["CodeBlock"]),
                Paragraph("pod install", styles["CodeBlock"]),
                Paragraph(
                    "Se falhar por versão do Ruby, use o Homebrew:",
                    styles["StepBody"],
                ),
                Paragraph("brew install cocoapods", styles["CodeBlock"]),
                Paragraph("pod install", styles["CodeBlock"]),
                info_box(
                    "Sempre abra o arquivo <b>App.xcworkspace</b>, nunca o "
                    ".xcodeproj sozinho. O CocoaPods exige o workspace.",
                    "ok",
                ),
            ],
        )
    )

    story.extend(
        step_box(
            3,
            "Abrir o projeto no Xcode",
            [
                Paragraph("No Terminal:", styles["StepBody"]),
                Paragraph("open ios/App/App.xcworkspace", styles["CodeBlock"]),
                Paragraph(
                    "Ou: Finder → papufy-app → ios → App → clique duas vezes em "
                    "<b>App.xcworkspace</b>.",
                    styles["StepBody"],
                ),
                Paragraph("No Xcode, no topo:", styles["StepBody"]),
                Paragraph("• Scheme: <b>App</b>", styles["StepBody"]),
                Paragraph(
                    "• Destino: <b>Any iOS Device (arm64)</b> "
                    "(não use simulador para enviar à loja)",
                    styles["StepBody"],
                ),
            ],
        )
    )

    story.append(PageBreak())

    story.extend(
        step_box(
            4,
            "Entrar com a conta Apple no Xcode",
            [
                Paragraph(
                    "Xcode → Settings → <b>Accounts</b> → + → Apple ID.",
                    styles["StepBody"],
                ),
                Paragraph(
                    "Faça login com a mesma conta do Apple Developer Program.",
                    styles["StepBody"],
                ),
                Paragraph(
                    "Depois, no painel esquerdo: target <b>App</b> → aba "
                    "<b>Signing &amp; Capabilities</b>:",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• Marque <b>Automatically manage signing</b>",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• Team: escolha sua equipe / conta Developer",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• Bundle Identifier: confirme <b>com.papufy.app</b>",
                    styles["StepBody"],
                ),
                Paragraph(
                    "Se o Bundle ID ainda não existir no Developer, o Xcode tenta "
                    "criar. Se der erro de “already exists”, use o ID já "
                    "registrado em developer.apple.com → Identifiers.",
                    styles["StepBody"],
                ),
            ],
        )
    )

    story.extend(
        step_box(
            5,
            "Criar o app no App Store Connect (navegador)",
            [
                Paragraph(
                    "Abra appstoreconnect.apple.com → Apps → + → Novo app.",
                    styles["StepBody"],
                ),
                Paragraph("Preencha:", styles["StepBody"]),
                Paragraph("• Plataformas: <b>iOS</b>", styles["StepBody"]),
                Paragraph("• Nome: <b>Papufy</b>", styles["StepBody"]),
                Paragraph(
                    "• Idioma principal: <b>Português (Brasil)</b>",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• Bundle ID: <b>com.papufy.app</b>", styles["StepBody"]
                ),
                Paragraph(
                    "• SKU: por exemplo <b>papufy-ios-001</b> (só interno)",
                    styles["StepBody"],
                ),
                Paragraph("• Acesso do usuário: Acesso completo", styles["StepBody"]),
            ],
        )
    )

    story.extend(
        step_box(
            6,
            "Gerar o Archive e enviar o build",
            [
                Paragraph(
                    "No Xcode, com destino <b>Any iOS Device</b>:",
                    styles["StepBody"],
                ),
                Paragraph(
                    "1. Menu <b>Product → Archive</b> (pode demorar alguns minutos).",
                    styles["StepBody"],
                ),
                Paragraph(
                    "2. Quando terminar, abre o <b>Organizer</b>.",
                    styles["StepBody"],
                ),
                Paragraph(
                    "3. Selecione o archive mais recente → <b>Distribute App</b>.",
                    styles["StepBody"],
                ),
                Paragraph(
                    "4. Escolha <b>App Store Connect</b> → Next.",
                    styles["StepBody"],
                ),
                Paragraph("5. Escolha <b>Upload</b> → Next.", styles["StepBody"]),
                Paragraph(
                    "6. Deixe as opções padrão → Upload.",
                    styles["StepBody"],
                ),
                Paragraph(
                    "7. Aguarde “Upload Successful”.",
                    styles["StepBody"],
                ),
                info_box(
                    "O build demora de 5 a 30 minutos para aparecer no "
                    "App Store Connect. Não envie de novo enquanto estiver "
                    "“Processing”."
                ),
            ],
        )
    )

    story.append(PageBreak())
    story.append(Paragraph("3. Ficha da loja no App Store Connect", styles["H1"]))

    story.extend(
        step_box(
            7,
            "Preencher a página do produto (pt-BR)",
            [
                Paragraph(
                    "Em App Store → versão 1.0 (ou a que estiver aberta):",
                    styles["StepBody"],
                ),
                Paragraph("• <b>Nome:</b> Papufy", styles["StepBody"]),
                Paragraph(
                    "• <b>Subtítulo</b> (até 30 caracteres): Serviços perto de você",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• <b>Categoria principal:</b> Estilo de vida (Lifestyle)",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• <b>Categoria secundária:</b> Negócios (Business), se pedir",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• Descrição: use o mesmo texto da Google Play "
                    "(marketplace de serviços locais).",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• <b>URL de suporte / marketing:</b> https://papufy.com",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• <b>Política de privacidade:</b> https://papufy.com/privacidade",
                    styles["StepBody"],
                ),
            ],
        )
    )

    story.extend(
        step_box(
            8,
            "Enviar os prints (screenshots)",
            [
                Paragraph(
                    "Copie do Windows para o Mac estas pastas:",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• store/screenshots/app-store-iphone-6.9/ → 01 a 05",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• store/screenshots/app-store-ipad-13/ → 01 a 04",
                    styles["StepBody"],
                ),
                Paragraph(
                    "No App Store Connect, arraste os PNGs para o tamanho "
                    "correspondente (iPhone 6.9\" e iPad 13\").",
                    styles["StepBody"],
                ),
                Paragraph(
                    "Ícone: use store/icon-1024.png (1024×1024, sem transparência).",
                    styles["StepBody"],
                ),
            ],
        )
    )

    story.extend(
        step_box(
            9,
            "Privacidade, idade e criptografia",
            [
                Paragraph(
                    "• Questionário de privacidade alinhado à política: conta, "
                    "localização opcional, fotos, mensagens, pagamento via provedor.",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• Classificação etária: app 18+ (pagamentos / CPF).",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• Criptografia: o Info.plist já tem "
                    "ITSAppUsesNonExemptEncryption = false. Marque criptografia "
                    "isenta (HTTPS padrão).",
                    styles["StepBody"],
                ),
                Paragraph(
                    "• Exclusão de conta: https://papufy.com/excluir-conta",
                    styles["StepBody"],
                ),
            ],
        )
    )

    story.extend(
        step_box(
            10,
            "Notas para a equipe de revisão (Review Notes)",
            [
                Paragraph(
                    "Cole um texto parecido com este (inglês ajuda na revisão):",
                    styles["StepBody"],
                ),
                Paragraph(
                    "Papufy is a local services marketplace (own product). "
                    "The app loads https://papufy.com in a WebView — it is not "
                    "a generic browser. Users can create listings, chat, and "
                    "pay via Pagar.me (Pix/card) without leaving the app.",
                    styles["CodeBlock"],
                ),
                Paragraph(
                    "Test account: play.review@papufy.com",
                    styles["CodeBlock"],
                ),
                Paragraph(
                    "Password: [senha da conta de revisão]",
                    styles["CodeBlock"],
                ),
                Paragraph(
                    "No paid subscription. Location can be denied. "
                    "Camera/photos only for profile, listings and chat.",
                    styles["CodeBlock"],
                ),
                Paragraph(
                    "Account deletion: https://papufy.com/excluir-conta",
                    styles["CodeBlock"],
                ),
            ],
        )
    )

    story.append(PageBreak())

    story.extend(
        step_box(
            11,
            "Selecionar o build e enviar para revisão",
            [
                Paragraph(
                    "1. Na versão do app, em Build, clique em + e escolha o "
                    "build que terminou de processar.",
                    styles["StepBody"],
                ),
                Paragraph(
                    "2. Confira ícone, prints, descrição e privacidade.",
                    styles["StepBody"],
                ),
                Paragraph(
                    "3. Clique em <b>Adicionar para revisão</b> / "
                    "<b>Enviar para revisão</b>.",
                    styles["StepBody"],
                ),
                Paragraph(
                    "4. Responda as perguntas finais (export compliance, etc.).",
                    styles["StepBody"],
                ),
                Paragraph(
                    "5. Envie. Status: “Em análise”. Pode levar de 24h a alguns dias.",
                    styles["StepBody"],
                ),
            ],
        )
    )

    story.append(Paragraph("4. TestFlight (teste antes da loja)", styles["H1"]))
    story.append(
        Paragraph(
            "Depois que o build processar, ele aparece no <b>TestFlight</b>. Você pode:",
            styles["Body"],
        )
    )
    for b in [
        "Adicionar testadores internos (sua conta Apple).",
        "Instalar o app TestFlight no iPhone e testar abertura, login, chat e pagamento.",
        "Só depois enviar para a revisão pública da App Store.",
    ]:
        story.append(Paragraph(f"• {b}", styles["BulletItem"]))

    story.append(Paragraph("5. Checklist rápido no dia", styles["H1"]))
    for i, c in enumerate(
        [
            "Apple Developer ativo",
            "Xcode instalado e logado",
            "npm install + cap sync ios + pod install",
            "Abrir App.xcworkspace",
            "Signing com Team + Bundle ID com.papufy.app",
            "Product → Archive → Upload",
            "App Store Connect: ficha + prints + privacidade",
            "Associar build + notas de revisão + enviar",
        ],
        1,
    ):
        story.append(Paragraph(f"☐  {i}. {c}", styles["BulletItem"]))

    story.append(Spacer(1, 0.35 * cm))
    story.append(Paragraph("6. Problemas comuns", styles["H1"]))
    problems = [
        (
            "“No signing certificate”",
            "Xcode → Settings → Accounts → Download Manual Profiles, ou remova e "
            "marque de novo Automatically manage signing.",
        ),
        (
            "“Unable to install CocoaPods”",
            "Instale via Homebrew (brew install cocoapods) e rode pod install de novo.",
        ),
        (
            "Build não aparece no Connect",
            "Aguarde até 30 min. Veja o e-mail da Apple se o processamento falhou.",
        ),
        (
            "Rejeição “WebView / browser”",
            "Nas Review Notes deixe claro que papufy.com é produto próprio, "
            "não um navegador genérico.",
        ),
        (
            "Push notifications",
            "O entitlements já tem aps-environment production. Chaves APNs no "
            "backend ainda podem ser configuradas depois; o app abre sem isso.",
        ),
    ]
    for title, body in problems:
        story.append(Paragraph(f"<b>{title}</b>", styles["H2"]))
        story.append(Paragraph(body, styles["Body"]))

    story.append(Spacer(1, 0.4 * cm))
    story.append(HRFlowable(width="100%", thickness=0.6, color=BORDER))
    story.append(Spacer(1, 0.25 * cm))
    story.append(
        Paragraph(
            "Papufy · Guia App Store (Mac) · Bundle ID com.papufy.app · "
            "Não inclui o .aab da Google Play",
            styles["Footer"],
        )
    )
    story.append(
        Paragraph(
            "Arquivo gerado para uso no MacBook. Se travar, volte ao passo em que parou.",
            styles["Footer"],
        )
    )

    def add_page_number(canvas, _doc):
        canvas.saveState()
        page = canvas.getPageNumber()
        canvas.setFont(FN, 8)
        canvas.setFillColor(MUTED)
        canvas.drawCentredString(
            A4[0] / 2, 1.1 * cm, f"Papufy — App Store no Mac  ·  página {page}"
        )
        canvas.restoreState()

    flat: list = []
    for item in story:
        if isinstance(item, list):
            flat.extend(item)
        else:
            flat.append(item)
    bad = [i for i, x in enumerate(flat) if isinstance(x, list)]
    if bad:
        raise TypeError(f"list still nested at indices {bad[:5]}")

    doc.build(flat, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print("OK", OUT, os.path.getsize(OUT))


if __name__ == "__main__":
    main()
