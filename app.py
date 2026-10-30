
from dash import Dash, html

app = Dash(__name__)
app.title = "Obuliraj | Cloud & DevOps Portfolio"

# COLORS
BG = "#050d1c"
PANEL = "#08172c"
TEXT = "#edf4ff"
MUTED = "#b7c8e5"
BLUE = "#08a5ff"
CYAN = "#20d9f5"
PURPLE = "#843cff"
ORANGE = "#ff982b"

# PERSONAL INFORMATION
NAME = "Obuliraj"
EMAIL = "obulirajs2016@gmail.com"
LINKEDIN = "https://linkedin.com/in/obuli-raj-a75b2a143"
GITHUB = "https://github.com/obuli007"

def card(title, content):
    return html.Div([
        html.H3(title, style={
            "color": TEXT,
            "marginTop": "0",
            "fontSize": "20px"
        }),
        content
    ], style={
        "background": "linear-gradient(145deg, #0b1b33, #071226)",
        "border": "1px solid #183354",
        "borderRadius": "15px",
        "padding": "22px",
        "minWidth": "0"
    })


def skill(name, emoji, color):
    return html.Div([
        html.Div(emoji, style={"fontSize": "34px"}),
        html.Div(name, style={
            "fontWeight": "bold",
            "marginTop": "9px"
        })
    ], style={
        "background": f"linear-gradient(145deg, {color}, #10203e)",
        "borderRadius": "12px",
        "padding": "17px 8px",
        "textAlign": "center",
        "border": "1px solid #ffffff20"
    })


def project(icon, title, description, tags, color):
    return html.Div([
        html.Div(icon, style={
            "fontSize": "32px",
            "background": "#10294b",
            "borderRadius": "12px",
            "width": "55px",
            "padding": "7px",
            "textAlign": "center"
        }),

        html.H4(title, style={"color": TEXT}),

        html.P(description, style={
            "color": MUTED,
            "fontSize": "13px",
            "lineHeight": "1.7"
        }),

        html.Div(" • ".join(tags), style={
            "color": color,
            "fontSize": "12px",
            "fontWeight": "bold"
        }),

        html.A("View Details →", href=GITHUB, target="_blank",
               style={
                   "display": "inline-block",
                   "marginTop": "18px",
                   "color": CYAN,
                   "textDecoration": "none"
               })

    ], style={
        "background": "#081a32",
        "border": "1px solid #1c385b",
        "borderRadius": "12px",
        "padding": "15px",
        "minWidth": "0"
    })


def sidebar_link(label, target, emoji):
    return html.A(f"{emoji}   {label}", href=f"#{target}", style={
        "display": "block",
        "padding": "13px 12px",
        "margin": "4px 0",
        "borderRadius": "9px",
        "color": "#dbeafe",
        "textDecoration": "none",
        "fontSize": "14px"
    })


app.layout = html.Div(style={
    "background": BG,
    "color": TEXT,
    "fontFamily": "Arial, sans-serif",
    "minHeight": "100vh",
    "margin": "0"
}, children=[

    # LEFT SIDEBAR
    html.Aside(style={
        "position": "fixed",
        "left": "0",
        "top": "0",
        "bottom": "0",
        "width": "205px",
        "padding": "23px 15px",
        "background": "#030b18",
        "borderRight": "1px solid #17304d",
        "boxSizing": "border-box",
        "overflowY": "auto",
        "zIndex": "10"
    }, children=[

        html.H3("☁️ Obuliraj", style={"color": CYAN}),

        html.P("BUILD • AUTOMATE • DEPLOY", style={
            "fontSize": "10px",
            "color": MUTED
        }),

        html.Hr(style={"borderColor": "#203753"}),

        sidebar_link("Home", "home", "⌂"),
        sidebar_link("About", "about", "♙"),
        sidebar_link("Skills", "skills", "⚙"),
        sidebar_link("Projects", "projects", "</>"),
        sidebar_link("Learning", "experience", "▣"),
        sidebar_link("Contact", "contact", "✉"),

        html.Hr(style={
            "borderColor": "#203753",
            "marginTop": "30px"
        }),

        html.P("CLOUD TECHNOLOGY", style={
            "color": CYAN,
            "fontSize": "12px"
        }),

        html.P("☁️ 🐳 🐧 ⚙️", style={"fontSize": "25px"})
    ]),

    # MAIN CONTENT
    html.Main(style={
        "marginLeft": "205px",
        "padding": "0 22px 20px",
        "maxWidth": "1600px"
    }, children=[

        # HERO SECTION
        html.Section(id="home", style={
            "margin": "0 -22px 22px",
            "padding": "52px 35px",
            "minHeight": "260px",
            "background": (
                "radial-gradient(circle at 85% 20%, #7926b9 0, transparent 30%),"
                "radial-gradient(circle at 65% 100%, #075da6 0, transparent 40%),"
                "linear-gradient(120deg, #071b44, #11165a, #19103d)"
            ),
            "borderRadius": "0 0 18px 18px",
            "display": "flex",
            "flexWrap": "wrap",
            "justifyContent": "space-between",
            "alignItems": "center",
            "gap": "25px"
        }, children=[

            html.Div(style={"flex": "1 1 300px"}, children=[

                html.P("CLOUD • AWS • DEVOPS", style={
                    "color": CYAN,
                    "letterSpacing": "3px",
                    "fontSize": "12px",
                    "fontWeight": "bold"
                }),

                html.H1([
                    "Hello, I'm",
                    html.Br(),
                    html.Span(NAME, style={
                        "background": "linear-gradient(90deg, #12b8ff, #a855f7, #ff9b37)",
                        "WebkitBackgroundClip": "text",
                        "WebkitTextFillColor": "transparent"
                    })
                ], style={
                    "fontSize": "clamp(36px, 5vw, 57px)",
                    "lineHeight": "1.12",
                    "margin": "15px 0"
                }),

                html.H2("Aspiring Cloud & DevOps Engineer", style={
                    "fontSize": "21px",
                    "marginBottom": "15px"
                }),

                html.P(
                    "I am passionate about cloud computing, "
                    "automation and building reliable infrastructure "
                    "using AWS and modern DevOps technologies.",
                    style={
                        "color": MUTED,
                        "maxWidth": "480px"
                    }
                ),

                html.Div([

                    html.A("View My Projects →", href="#projects",
                           style={
                               "display": "inline-block",
                               "padding": "12px 20px",
                               "borderRadius": "25px",
                               "margin": "10px 8px 0 0",
                               "background": "linear-gradient(90deg, #079fff, #793cff)",
                               "color": "white",
                               "textDecoration": "none",
                               "fontWeight": "bold"
                           }),

                    html.A("Contact Me ↗", href="#contact",
                           style={
                               "display": "inline-block",
                               "padding": "11px 20px",
                               "border": "1px solid #48baff",
                               "borderRadius": "25px",
                               "marginTop": "10px",
                               "color": "white",
                               "textDecoration": "none"
                           })
                ])
            ]),

            html.Div(style={
                "flex": "1 1 240px",
                "textAlign": "center",
                "padding": "20px",
                "background": "#ffffff08",
                "border": "1px solid #ffffff20",
                "borderRadius": "20px"
            }, children=[

                html.Div("☁️", style={
                    "fontSize": "100px",
                    "filter": "drop-shadow(0 0 25px #079fff)"
                }),

                html.H2("AWS CLOUD", style={
                    "color": "#ffb04d",
                    "letterSpacing": "3px"
                }),

                html.P("🐳 Docker • ☸ Kubernetes", style={
                    "color": CYAN
                }),

                html.P("🐧 Linux • Terraform • Git", style={
                    "color": MUTED
                })
            ])
        ]),

        # ABOUT AND SKILLS
        html.Div(style={
            "display": "grid",
            "gridTemplateColumns": "repeat(auto-fit, minmax(min(100%, 300px), 1fr))",
            "gap": "20px",
            "marginBottom": "22px"
        }, children=[

            card("♙ About Me", html.Div([

                html.P(
                    "I completed my B.E. in Computer Science in 2020. "
                    "After graduation, I worked in my family textile "
                    "business. I am now transitioning into the IT "
                    "industry and building my technical skills.",
                    style={
                        "color": MUTED,
                        "lineHeight": "1.8"
                    }
                ),

                html.P("📍 Chennai, Tamil Nadu, India", style={
                    "color": TEXT
                }),

                html.P("✉️ " + EMAIL, style={"color": TEXT}),

                html.P("🎓 B.E. Computer Science | 2020", style={
                    "color": TEXT
                }),

                html.P("📚 AWS + DevOps Training | FITA, Chennai", style={
                    "color": TEXT
                }),

                html.Div("Dream • Learn • Build", style={
                    "textAlign": "right",
                    "color": CYAN,
                    "fontStyle": "italic",
                    "fontSize": "18px"
                })
            ])),

            card("⚡ My Technical Skills", html.Div([

                html.Div([

                    skill("AWS", "☁️", "#75420b"),
                    skill("Docker", "🐳", "#075b9e"),
                    skill("Kubernetes", "☸️", "#124bc0"),
                    skill("Terraform", "◆", "#5930a7"),
                    skill("Linux", "🐧", "#8c5a0b"),
                    skill("Jenkins", "⚙️", "#a41f45"),
                    skill("Git & GitHub", "⑂", "#273d59"),
                    skill("Python", "🐍", "#287c31")

                ], style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(4, minmax(0, 1fr))",
                    "gap": "10px"
                })
            ]))
        ]),

        # PROJECTS AND LEARNING
        html.Div(style={
            "display": "grid",
            "gridTemplateColumns": "minmax(0, 1.6fr) minmax(240px, 1fr)",
            "gap": "20px",
            "marginBottom": "22px"
        }, children=[

            card("⌘ My Projects", html.Div([

                html.Div([

                    project(
                        "☁️",
                        "AWS Cloud Practice",
                        "Hands-on practice with EC2, S3, IAM, VPC and AWS services.",
                        ["AWS", "EC2", "S3"],
                        ORANGE
                    ),

                    project(
                        "🐳",
                        "Docker Portfolio",
                        "Built a personal portfolio using Python, Dash and Docker.",
                        ["Python", "Docker", "Dash"],
                        CYAN
                    ),

                    project(
                        "⚙️",
                        "AWS Lambda Automation",
                        "Practiced EC2 instance automation using Python and Boto3.",
                        ["Lambda", "Python", "Boto3"],
                        "#c084fc"
                    )

                ], style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(auto-fit, minmax(145px, 1fr))",
                    "gap": "12px"
                })
            ])),

            card("▣ Learning & Development", html.Div([

                html.Div([
                    html.Span("●", style={
                        "color": CYAN,
                        "fontSize": "23px"
                    }),

                    html.Div([
                        html.Strong("AWS Cloud", style={"color": TEXT}),

                        html.P(
                            "EC2, S3, IAM, VPC and Lambda practice",
                            style={
                                "color": MUTED,
                                "fontSize": "13px"
                            }
                        )
                    ])
                ], style={
                    "display": "flex",
                    "gap": "13px",
                    "marginBottom": "17px"
                }),

                html.Div([
                    html.Span("●", style={
                        "color": PURPLE,
                        "fontSize": "23px"
                    }),

                    html.Div([
                        html.Strong("DevOps Tools", style={"color": TEXT}),

                        html.P(
                            "Docker, Git and CI/CD fundamentals",
                            style={
                                "color": MUTED,
                                "fontSize": "13px"
                            }
                        )
                    ])
                ], style={
                    "display": "flex",
                    "gap": "13px",
                    "marginBottom": "17px"
                }),

                html.Div([
                    html.Span("●", style={
                        "color": ORANGE,
                        "fontSize": "23px"
                    }),

                    html.Div([
                        html.Strong("Linux & Python", style={"color": TEXT}),

                        html.P(
                            "Linux commands, Python scripting and Dash",
                            style={
                                "color": MUTED,
                                "fontSize": "13px"
                            }
                        )
                    ])
                ], style={
                    "display": "flex",
                    "gap": "13px"
                }),

                html.Div([
                    html.Span("●", style={
                        "color": "#22c55e",
                        "fontSize": "23px"
                    }),

                    html.Div([
                        html.Strong("Current Training", style={"color": TEXT}),

                        html.P(
                            "AWS + DevOps at FITA, Chennai",
                            style={
                                "color": MUTED,
                                "fontSize": "13px"
                            }
                        )
                    ])
                ], style={
                    "display": "flex",
                    "gap": "13px"
                })
            ]))
        ]),

        # CONTACT SECTION
        html.Section(id="contact", style={
            "background": "linear-gradient(110deg, #073b9b, #5621a6, #a12b81)",
            "borderRadius": "15px",
            "padding": "25px",
            "display": "flex",
            "flexWrap": "wrap",
            "alignItems": "center",
            "justifyContent": "space-between",
            "gap": "15px",
            "marginBottom": "22px"
        }, children=[

            html.Div([
                html.H2("✈️ Let's Connect!", style={
                    "marginTop": "0"
                }),

                html.P(
                    "Open to learning, collaboration and new opportunities."
                )
            ]),

            html.Div([

                html.P([
                    "✉️ ",
                    html.A(EMAIL, href=f"mailto:{EMAIL}",
                           style={"color": "white"})
                ]),

                html.P([
                    "in  ",
                    html.A("LinkedIn Profile", href=LINKEDIN,
                           target="_blank",
                           style={"color": "white"})
                ]),

                html.P([
                    "⌘  ",
                    html.A("GitHub Profile", href=GITHUB,
                           target="_blank",
                           style={"color": "white"})
                ])

            ]),

            html.A(
                "Send Message →",
                href=f"mailto:{EMAIL}",
                style={
                    "background": "#079fff",
                    "color": "white",
                    "padding": "13px 20px",
                    "borderRadius": "25px",
                    "textDecoration": "none",
                    "fontWeight": "bold"
                }
            )
        ]),

        # FOOTER
        html.Footer(style={
            "borderTop": "1px solid #1c385b",
            "padding": "20px 5px",
            "display": "flex",
            "justifyContent": "space-between",
            "flexWrap": "wrap",
            "gap": "10px",
            "color": MUTED,
            "fontSize": "12px"
        }, children=[

            html.Span("☁️ Obuliraj | DevOps Portfolio"),

            html.Span(
                "© 2026 Obuliraj | Python • Dash • Docker • AWS"
            ),

            html.Span("AWS • 🐳 • ☸ • 🐍 • Git")
        ])
    ])
])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=False)
