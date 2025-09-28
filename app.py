from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

@app.route('/')
def home():
    # Same projects data as in projects route
    projects_data = [
        {
            'title': 'AI Agent z RAG dla Slack',
            'description': 'Inteligentny agent AI zintegrowany ze Slackiem, wykorzystujący RAG do odpowiadania na pytania biznesowe na podstawie dokumentacji firmowej',
            'technologies': ['Python', 'LangChain', 'ChromaDB', 'Slack API', 'OpenAI'],
            'image': 'project1.jpg',
            'github': 'https://github.com/yourusername/slack-ai-agent',
            'demo': '#'
        },
        {
            'title': 'System Generowania Obrazów AI',
            'description': 'API do automatycznego generowania obrazów z wykorzystaniem modeli DALL-E i Stable Diffusion dla potrzeb marketingowych',
            'technologies': ['Python', 'Flask', 'DALL-E', 'Stable Diffusion', 'Docker'],
            'image': 'project2.jpg',
            'github': 'https://github.com/yourusername/ai-image-generator',
            'demo': '#'
        },
        {
            'title': 'Dashboard Analityczny',
            'description': 'Interaktywny dashboard do analizy danych biznesowych z automatycznymi raportami i predykcjami ML',
            'technologies': ['Python', 'Streamlit', 'Pandas', 'Scikit-learn', 'Plotly'],
            'image': 'project3.jpg',
            'github': 'https://github.com/yourusername/analytics-dashboard',
            'demo': '#'
        },
        {
            'title': 'Multi-LLM API Gateway',
            'description': 'Zunifikowane API do komunikacji z różnymi modelami LLM (OpenAI, Anthropic, Cohere) z load balancingiem',
            'technologies': ['Python', 'FastAPI', 'Docker', 'Redis', 'PostgreSQL'],
            'image': 'project4.jpg',
            'github': 'https://github.com/yourusername/llm-gateway',
            'demo': '#'
        }
    ]
    return render_template('index.html', projects=projects_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects_data = [
        {
            'title': 'AI Agent z RAG dla Slack',
            'description': 'Inteligentny agent AI zintegrowany ze Slackiem, wykorzystujący RAG do odpowiadania na pytania biznesowe na podstawie dokumentacji firmowej',
            'technologies': ['Python', 'LangChain', 'ChromaDB', 'Slack API', 'OpenAI'],
            'image': 'project1.jpg',
            'github': 'https://github.com/yourusername/slack-ai-agent',
            'demo': '#'
        },
        {
            'title': 'System Generowania Obrazów AI',
            'description': 'API do automatycznego generowania obrazów z wykorzystaniem modeli DALL-E i Stable Diffusion dla potrzeb marketingowych',
            'technologies': ['Python', 'Flask', 'DALL-E', 'Stable Diffusion', 'Docker'],
            'image': 'project2.jpg',
            'github': 'https://github.com/yourusername/ai-image-generator',
            'demo': '#'
        },
        {
            'title': 'Dashboard Analityczny',
            'description': 'Interaktywny dashboard do analizy danych biznesowych z automatycznymi raportami i predykcjami ML',
            'technologies': ['Python', 'Streamlit', 'Pandas', 'Scikit-learn', 'Plotly'],
            'image': 'project3.jpg',
            'github': 'https://github.com/yourusername/analytics-dashboard',
            'demo': '#'
        },
        {
            'title': 'Multi-LLM API Gateway',
            'description': 'Zunifikowane API do komunikacji z różnymi modelami LLM (OpenAI, Anthropic, Cohere) z load balancingiem',
            'technologies': ['Python', 'FastAPI', 'Docker', 'Redis', 'PostgreSQL'],
            'image': 'project4.jpg',
            'github': 'https://github.com/yourusername/llm-gateway',
            'demo': '#'
        }
    ]
    return render_template('projects.html', projects=projects_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/api/skills')
def api_skills():
    skills_data = {
        'current_company': {
            'technologies': [
                {'name': 'Python', 'category': 'Data Science'},
                {'name': 'Flask', 'category': 'Framework'},
                {'name': 'Pandas', 'level': 85, 'category': 'Data Science'},
                {'name': 'Scikit-learn', 'category': 'Machine Learning'},
                {'name': 'LangChain', 'category': 'AI/LLM'},
                {'name': 'OpenAI API', 'category': 'AI/LLM'},
                {'name': 'Docker', 'category': 'DevOps'},
                {'name': 'Git', 'category': 'Tools'},
                {'name': 'RAG Systems', 'category': 'AI/LLM'},
                {'name': 'Slack API', 'category': 'Integrations'},
                {'name': 'JavaScript', 'category': 'Frontend'},
                {'name': 'ChromaDB', 'category': 'Vector DB'}
            ]
        }
    }
    return jsonify(skills_data)

if __name__ == '__main__':
    app.run(debug=True) 