from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Character data - could be moved to a database in a real application
    characters = [
        {
            'id': 'street-chef',
            'name': 'The Street Chef in Bangkok',
            'activities': [
                'Wake up at 4am to shop the wet market',
                'Cook with locals in a hidden alley',
                'Take a nap in a hammock above your stall',
                'Midnight boat ride with other chefs'
            ],
            'image': 'street-chef.jpg',
            'location': 'Bangkok',
            'color': 'bg-orange-500'
        },
        {
            'id': 'boho-barista',
            'name': 'The Boho Barista of Brașov',
            'activities': [
                'Morning meditation in the mountain mist',
                'Craft coffee brewing with local beans',
                'Afternoon poetry readings with locals',
                'Evening acoustic music in hidden cafes'
            ],
            'image': 'boho-barista.jpg',
            'location': 'Brașov',
            'color': 'bg-purple-500'
        },
        {
            'id': 'minimal-dj',
            'name': 'The Minimal DJ in Bucharest',
            'activities': [
                'Afternoon vinyl shopping in hidden record stores',
                'Sunset sound check at underground clubs',
                'Midnight DJ set at exclusive warehouse parties',
                'Sunrise afterparty on Bucharest rooftops'
            ],
            'image': 'minimal-dj.jpg',
            'location': 'Bucharest',
            'color': 'bg-gray-800'
        }
    ]
    
    return render_template('index.html', characters=characters)

@app.route('/character/<character_id>')
def character_detail(character_id):
    # In a real application, you'd fetch this from a database
    characters = {
        'street-chef': {
            'id': 'street-chef',
            'name': 'The Street Chef in Bangkok',
            'activities': [
                'Wake up at 4am to shop the wet market',
                'Cook with locals in a hidden alley',
                'Take a nap in a hammock above your stall',
                'Midnight boat ride with other chefs'
            ],
            'image': 'street-chef.jpg',
            'location': 'Bangkok',
            'description': 'Live the authentic life of a Bangkok street chef, from early morning market visits to late night culinary adventures.',
            'color': 'bg-orange-500'
        },
        'boho-barista': {
            'id': 'boho-barista',
            'name': 'The Boho Barista of Brașov',
            'activities': [
                'Morning meditation in the mountain mist',
                'Craft coffee brewing with local beans',
                'Afternoon poetry readings with locals',
                'Evening acoustic music in hidden cafes'
            ],
            'image': 'boho-barista.jpg',
            'location': 'Brașov',
            'description': 'Immerse yourself in the bohemian lifestyle of Transylvania, where mountain vistas meet artistic expression in one of Europe\'s most charming hidden gems.',
            'color': 'bg-purple-500'
        },
        'minimal-dj': {
            'id': 'minimal-dj',
            'name': 'The Minimal DJ in Bucharest',
            'activities': [
                'Afternoon vinyl shopping in hidden record stores',
                'Sunset sound check at underground clubs',
                'Midnight DJ set at exclusive warehouse parties',
                'Sunrise afterparty on Bucharest rooftops'
            ],
            'image': 'minimal-dj.jpg',
            'location': 'Bucharest',
            'description': 'Experience the legendary minimal techno scene of Romania\'s capital, from vinyl hunting to playing sunrise sets at the city\'s most exclusive underground parties.',
            'color': 'bg-gray-800'
        }
    }
    
    character = characters.get(character_id)
    if character:
        return render_template('character_detail.html', character=character)
    else:
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True) 