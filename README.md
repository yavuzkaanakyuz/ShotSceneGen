# ShotSceneGen 🎬

**AI-powered Python package that converts text stories into professional film scenes and camera shots using OpenAI GPT models.**

Transform your written stories into detailed filmmaking blueprints with automatic scene breakdowns, shot descriptions, and visual prompts perfect for directors, cinematographers, and content creators.

## ✨ Key Features

- **🌍 Multi-language Support**: Automatically detects Turkish/English and translates when needed
- **🎭 Smart Scene Generation**: Intelligently breaks stories into properly formatted film scenes
- **📹 Detailed Shot Breakdown**: Creates comprehensive shot lists with visual prompts
- **📚 Reference-Enhanced**: Uses reference documents to improve output quality
- **⚡ Easy Integration**: Simple Python API with minimal setup required

## 🚀 Quick Start

### Installation

```bash
pip install git+https://github.com/yavuzkaanakyuz/ShotSceneGen.git
```

### Basic Usage (30 seconds to get started!)

```python
from text_to_shots import TextToShotsProcessor

# 1. Initialize with your OpenAI API key
processor = TextToShotsProcessor(api_key="your-openai-api-key")

# 2. Process any story
story = """
Sarah walked into the old library. The afternoon sun streamed through 
dusty windows as she searched for the mysterious book. Behind her, 
footsteps echoed in the silence.
"""

# 3. Get professional film breakdown
result = processor.process_story(story)

# 4. Access your results
print("🎬 SCENES:")
print(result.scenes)
print("\n📹 SHOTS:")
print(result.shots)
```

**That's it!** You now have professional scene and shot breakdowns ready for production.

## 📋 Setup Requirements

- **Python**: 3.8 or higher
- **OpenAI API Key**: Get one from [OpenAI Platform](https://platform.openai.com/)
- **Internet connection**: For API calls

### Environment Setup (Recommended)

```bash
# Set your API key as environment variable
export OPENAI_API_KEY=your-openai-api-key
```

```python
# No need to pass API key in code
processor = TextToShotsProcessor()
result = processor.process_story("Your story here...")
```

## 🎯 What You Get

### Input Story:
```
Once upon a time, there was a young filmmaker who dreamed of creating 
the perfect movie. She spent days writing her script in a small café.
```

### Generated Scenes:
```
SCENE 1 / SMALL CAFÉ / DAY / INTERIOR / YOUNG FILMMAKER
The young filmmaker sits at a corner table, surrounded by crumpled papers 
and empty coffee cups, intensely writing her script.

YOUNG FILMMAKER (muttering to herself)
This has to be perfect... just perfect.
```

### Generated Shots:
```
SCENE 1 / SMALL CAFÉ / DAY / INTERIOR / YOUNG FILMMAKER
🎥 Objective: Establish the creative workspace and filmmaker's dedication

1. Wide Shot – Café overview with filmmaker at corner table
Prompt: "Cozy café interior, warm lighting, young woman at corner table 
surrounded by papers, creative chaos, golden hour lighting..."

2. Medium Shot – Filmmaker writing intensely  
Prompt: "Determined young woman hunched over notebook, pen in hand, 
coffee steam rising, focused expression..."

3. Close-Up – Hand writing on paper
Prompt: "Extreme close-up of hand holding pen, words flowing across 
paper, ink glistening under café lighting..."
```

## 🔧 Advanced Features

### Custom Reference Documents

```python
# Use your own reference materials to improve output quality
processor = TextToShotsProcessor(
    api_key="your-key",
    references_folder="/path/to/your/film-references"
)
```

### Language Detection & Translation

```python
# Automatically handles Turkish stories
turkish_story = "Bir zamanlar genç bir yönetmen vardı..."
result = processor.process_story(turkish_story)

print("Detected Language:", result.detected_language)  # "turkish"
print("Original:", result.original_story)              # Turkish text
print("Translated:", result.translated_story)          # English translation
```

### Check Available References

```python
# See what reference files are loaded
references = processor.get_available_references()
print("Available references:", references)
```

### Control Reference Usage

```python
# Process without using reference documents
result = processor.process_story(story, use_references=False)
```

## 📊 Complete Output Structure

The `StoryAnalysisResult` object contains:

```python
result.original_story      # Your input text
result.detected_language   # "english" or "turkish" 
result.translated_story    # English translation (if needed)
result.scenes             # Professional scene breakdown
result.shots              # Detailed shot descriptions with prompts
result.references_used    # List of reference files utilized
```

## 💡 Use Cases

- **🎬 Film Directors**: Convert scripts into shot lists
- **📺 Content Creators**: Plan video productions  
- **🎓 Film Students**: Learn professional scene structure
- **✍️ Writers**: Visualize story adaptations
- **🎨 Storyboard Artists**: Get detailed visual prompts

## 🛠️ Error Handling

```python
try:
    result = processor.process_story(story)
    print("✅ Success! Scenes generated.")
except ValueError as e:
    print(f"❌ Input error: {e}")
except RuntimeError as e:
    print(f"❌ API error: {e}")
```

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `Module not found` | Reinstall: `pip install git+https://github.com/yavuzkaanakyuz/ShotSceneGen.git` |
| `API key error` | Set `OPENAI_API_KEY` environment variable |
| `Empty output` | Check story length (minimum ~50 characters) |
| `Network issues` | Verify internet connection and OpenAI API status |

## 🔍 Example Workflows

### For Short Films
```python
short_film = "A detective enters a dark alley. Rain falls heavily..."
result = processor.process_story(short_film)
# Perfect for 2-5 minute productions
```

### For Commercial Scripts  
```python
commercial = "A family gathers around breakfast table. The coffee aroma fills the kitchen..."
result = processor.process_story(commercial)
# Great for advertising storyboards
```

### For Documentary Segments
```python
documentary = "The old fisherman mends his nets by the harbor as seagulls circle overhead..."
result = processor.process_story(documentary)
# Ideal for documentary shot planning
```

## 📄 License

MIT License - Feel free to use in personal and commercial projects.

## 🤝 Contributing

Found a bug? Have a feature idea? 

1. Check [existing issues](https://github.com/yavuzkaanakyuz/ShotSceneGen/issues)
2. Open a new issue with details
3. Pull requests welcome!

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yavuzkaanakyuz/ShotSceneGen/issues)
- **Documentation**: This README + inline code comments
- **Updates**: Watch the repository for new releases

## 👨‍💻 Author

**Yavuz Kaan Akyuz**  
*Film Technology Enthusiast*

---

**⭐ If this project helps your creative workflow, please give it a star!**

*Transform your stories into cinema-ready blueprints in seconds.*
