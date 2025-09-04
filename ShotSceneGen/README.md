# ShotSceneGen

AI-powered Python package to convert text stories into film scenes and shots using OpenAI GPT models.

## 🚀 Installation

Install directly from GitHub (no subdirectory required):

```bash
pip install git+https://github.com/yavuzkaanakyuz/ShotSceneGen.git
```

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- Internet connection

## 🔧 Usage

### Basic Usage

```python
from text_to_shots import TextToShotsProcessor

# Initialize with your OpenAI API key
processor = TextToShotsProcessor(api_key="your-openai-api-key")

# Process a story
story = """
Once upon a time, there was a young filmmaker who wanted to create 
the perfect movie. She spent days writing her script...
"""

result = processor.process_story(story)

# Access results
print("Detected Language:", result.detected_language)
print("Scenes:", result.scenes)
print("Shots:", result.shots)
```

### Using Environment Variables

```bash
export OPENAI_API_KEY=your-openai-api-key
```

```python
from text_to_shots import TextToShotsProcessor

# API key will be loaded from environment
processor = TextToShotsProcessor()
result = processor.process_story("Your story here...")
```

### With Custom Reference Documents

```python
processor = TextToShotsProcessor(
    api_key="your-key",
    references_folder="/path/to/your/references"
)
```

## 🎬 Features

- **Automatic Language Detection**: Supports Turkish and English
- **Auto Translation**: Automatically translates Turkish stories to English
- **Scene Generation**: Creates properly formatted film scenes
- **Shot Generation**: Generates detailed shot descriptions with visual prompts
- **Reference Support**: Uses reference documents to improve output quality
- **Multiple Formats**: Returns structured data for further processing

## 📊 Output Structure

The `StoryAnalysisResult` includes:

- `original_story`: Your input story
- `detected_language`: Auto-detected language
- `translated_story`: English translation (if needed)
- `scenes`: Generated scene breakdown
- `shots`: Detailed shot descriptions
- `references_used`: List of reference files used

## 🔧 Advanced Usage

```python
# Get available reference files
references = processor.get_available_references()
print("Available references:", references)

# Process without using references
result = processor.process_story(story, use_references=False)
```

## 🐛 Troubleshooting

### Common Issues

1. **Module not found**: Make sure you installed the package correctly
2. **API key error**: Set your OpenAI API key as environment variable
3. **Network issues**: Ensure stable internet connection

### Error Handling

```python
try:
    result = processor.process_story(story)
except ValueError as e:
    print(f"Input error: {e}")
except RuntimeError as e:
    print(f"API error: {e}")
```

## 📄 License

MIT License

## 🤝 Contributing

Issues and pull requests welcome at [GitHub repository](https://github.com/yavuzkaanakyuz/ShotSceneGen).

## 👨‍💻 Author

Yavuz Kaan Akyuz