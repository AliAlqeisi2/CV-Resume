from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    cv_data = {
        'name': 'Ali Algeisi',
        'linkedin': 'https://www.linkedin.com/in/yourprofile',
        'experiences': [
            {
                'title': 'R&D Software Development Intern',
                'company': 'Brainlab’s Langer Medical',
                'duration': 'September 2024 - Februar 2025, Waldkirch, Deutschland',
                'details': [
                    'Reduzierung der Produktionszeit pro Gerät um 15 Minuten durch die Entwicklung eines automatisierten Windows-Installationssystems und eines Python-Programms, was einer Kosteneinsparung von etwa 7 USD pro Gerät entspricht.',
                    'Dokumentation gemäß IEC 62304-Medizinprodukte-Software-Lebenszyklusprozess, von der Stakeholder-Ebene bis zu den Testfällen.',
                    'Entwicklung einer unterstützenden Softwarelösung, die die Inbetriebnahme und kundenspezifische Konfiguration der Geräte durch das Produktionsteam erleichtert.',
                    'Beitrag zur Software- und Systemverifikationstests von Neuromonitoring-Geräten.'
                ]
            }
        ],
        'skills': [
            'Python', 'Powershell', 'Bash', 'Linux', 'Matlab', 'MDT', 'Docker', 'Kubernetes', 'Jenkins (CI/CD)', 'Terraform', 'Ansible', 'Azure', 'TensorFlow', 'Agile Methodik', 'Windows Server', 'Konfigurationsmanagement',
            'Arabisch (Muttersprache)', 'Englisch (Fließend)', 'Deutsch (C1)'
        ],
        'projects': [
            {
                'title': 'Containerisierte Flask-App mit CI/CD (Laufend)',
                'details': [
                    'Entwicklung einer Flask-Webanwendung, die mit Docker containerisiert wurde.',
                    'Erstellung einer CI/CD-Pipeline mit Jenkins für automatisierte Deployments.',
                    'Bereitstellung der Anwendung in einem Kubernetes-Cluster mithilfe von Deployments und NodePort-Service.'
                ]
            },
            {
                'title': 'Terraform-basierte AKS-Cluster-Deployment',
                'details': [
                    'Bereitstellung von AKS-Clustern in Azure mithilfe von Terraform.',
                    'Integration von Azure Key Vault für die sichere Verwaltung von secrets.',
                    'Automatisierung der AKS-Bereitstellung mit Terraform und Service Principals.'
                ]
            },
            {
                'title': 'Deep Learning zur Klassifizierung von Herztönen',
                'details': [
                    'Anwendung von Signalverarbeitung (Fourier-Transformation, Wavelets, Cepstrum) zur Extraktion von Merkmalen aus Herztonaufnahmen.',
                    'Erstellung eines TensorFlow-basierten CNN-Modells zur Klassifizierung von 5 Arten von Herzkrankheiten mit 97% Genauigkeit.'
                ]
            }
        ],
        'educations': [
            {
                'degree': 'Medizintechnik',
                'institution': 'Hochschule Rheinmain, Wiesbaden, Deutschland',
                'duration': 'März 2024 - März 2025',
                'details': '2 Auslandssemester als Erasmus-Stipendiat'
            },
            {
                'degree': 'Biomedizinische Technik (Schwerpunkt Elektrotechnik)',
                'institution': 'German Jordanian University, Madaba, Jordanien',
                'duration': 'September 2020 - März 2025',
                'details': 'Rang 5 im Studiengang Biomedizinische Technik'
            }
        ]
    }
    return render_template('index.html', **cv_data)

if __name__ == '__main__':
    app.run(debug=True)