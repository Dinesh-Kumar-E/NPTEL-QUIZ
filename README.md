# 🎯 QuizBuzz

<div align="center">


**A modern, feature-rich web-based quiz application with retro aesthetics**

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![MathJax](https://img.shields.io/badge/MathJax-FF6B35?style=for-the-badge&logo=mathjax&logoColor=white)](https://www.mathjax.org/)

[🚀 Live Demo](https://dinesh-kumar-e.github.io/Quizbuzz/) • [📖 Documentation](docs.html) • [🔧 Data Builder](databuild.html) • [📊 Slide Builder](slidebuilder.html)

</div>

## ✨ Features

### 🎮 Core Quiz Features
- **Interactive Quiz Interface** - Modern retro-styled UI with smooth animations
- **Multi-Select Support** - Questions with single or multiple correct answers
- **LaTeX Math Support** - Render mathematical formulas using MathJax
- **Audio Integration** - Background music and sound effects
- **Real-time Progress** - Live timer and progress tracking
- **Smart Shuffling** - Randomize questions and answer options

### 📊 Data Management
- **JSON-Based** - Simple, structured quiz data format
- **Category Filtering** - Organize questions by categories and subcategories
- **Percentage Selection** - Choose what percentage of questions to include
- **Data Validation** - Built-in JSON validator with error reporting
- **Multiple Data Sources** - Support for Pastebin, direct URLs, and local JSON

### 🛠️ Additional Tools
- **Data Builder** - Combine multiple quiz JSON files
- **Slide Builder** - Generate PowerPoint presentations from quiz data
- **JSON Validator** - Validate and analyze quiz data structure
- **Results Analysis** - Detailed score breakdown and wrong answer review

### 🎨 User Experience
- **Responsive Design** - Works on desktop, tablet, and mobile devices
- **Customizable Settings** - Personalize quiz experience
- **Local Storage** - Remember user preferences
- **Accessibility** - Screen reader friendly with proper ARIA labels

## 🚀 Quick Start

### Option 1: Download and Run Locally
```bash
# Clone or download the repository
git clone https://github.com/yourusername/quizbuzz.git
cd quizbuzz

# Open in your browser
open index.html
# or
python -m http.server 8000  # For local server
```

### Option 2: Host on GitHub Pages
1. Fork this repository
2. Enable GitHub Pages in repository settings
3. Access via `https://yourusername.github.io/quizbuzz`

### Option 3: Deploy to Any Web Server
Simply upload all files to your web server directory.

## 📋 Usage

### Creating Your First Quiz

1. **Prepare Quiz Data** - Create a JSON file following our format:
```json
{
  "questions": [
    {
      "category": "Science",
      "subcategory": "Physics",
      "question": "What is the speed of light?",
      "options": [
        {"no": 1, "option": "300,000 km/s"},
        {"no": 2, "option": "150,000 km/s"},
        {"no": 3, "option": "450,000 km/s"}
      ],
      "correctoption": [1]
    }
  ]
}
```

2. **Host Your Data** - Upload to Pastebin or any web-accessible location
3. **Share Room ID** - Give participants the Pastebin ID or URL
4. **Start Quiz** - Participants enter Room ID and begin

### Taking a Quiz

1. **Enter Name** - Provide your name on the home screen
2. **Enter Room ID** - Input the quiz Room ID provided by instructor
3. **Configure Settings** - Choose categories, question percentage, and options
4. **Take Quiz** - Answer questions with real-time feedback
5. **Review Results** - See your score and review wrong answers

## 🔧 Advanced Features

### LaTeX Math Support
Render mathematical formulas in questions and answers:
```json
{
  "question": "What is the quadratic formula? $x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$",
  "options": [
    {"no": 1, "option": "$x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$"},
    {"no": 2, "option": "$x = \\frac{b \\pm \\sqrt{b^2-4ac}}{2a}$"}
  ]
}
```

### Multiple Correct Answers
Support questions with multiple right answers:
```json
{
  "question": "Which are prime numbers?",
  "options": [
    {"no": 1, "option": "2"},
    {"no": 2, "option": "3"},
    {"no": 3, "option": "4"},
    {"no": 4, "option": "5"}
  ],
  "correctoption": [1, 2, 4]
}
```

### Room ID System
- **Pastebin Integration**: Use Pastebin IDs for easy sharing
- **Direct URLs**: Support for any JSON-serving URL
- **URL Parameters**: Pre-fill Room ID with `?roomid=YOUR_ID`

## 🛠️ Tools Documentation

### 📊 Data Builder (`databuild.html`)
Combine multiple quiz JSON files into one:
- Add multiple JSON inputs
- Real-time validation and analytics
- Generate combined output
- Copy to clipboard functionality

### 📋 Slide Builder (`slidebuilder.html`)
Convert quiz data to PowerPoint presentations:
- Multiple theme options (Dark, Light, Colorful)
- Question and answer slides
- Category organization
- Live preview functionality
- Download as .pptx format

### ✅ JSON Validator (`validator.html`)
Validate and analyze quiz data:
- JSON syntax validation
- Quiz structure verification
- Statistics and breakdowns
- Math rendering error detection
- Category and subcategory analysis

## 🎨 Customization

### Themes and Styling
Modify CSS variables in any HTML file:
```css
:root {
  --primary: #8b58ff;    /* Primary color */
  --secondary: #ff5e5e;  /* Secondary color */
  --dark: #222034;       /* Background color */
  --light: #e6e6e6;      /* Text color */
  --success: #52de97;    /* Success color */
  --warning: #ffae22;    /* Warning color */
  --danger: #ff5555;     /* Error color */
}
```

### Audio Files
Replace audio files in the `asserts/` directory:
- `8bit-retro-bg-1-trim.mp3` - Background music
- `won1.mp3` - Success sound
- `lost1.mp3` - Failure sound

### Fonts and Icons
- **Fonts**: Press Start 2P (retro), VT323 (monospace)
- **Icons**: Font Awesome 6.0
- **Math**: MathJax 3.0

## 📁 Project Structure

```
QuizBuzz/
├── index.html          # Main quiz application
├── docs.html           # Documentation page
├── databuild.html      # Data builder tool
├── slidebuilder.html   # Slide builder tool
├── validator.html      # JSON validator tool
├── asserts/            # Audio and image assets
│   ├── 8bit-retro-bg-1-trim.mp3
│   ├── won1.mp3
│   ├── lost1.mp3
│   └── 1.webp ... 9.webp
└── README.md           # This file
```

## 🌐 Browser Support

| Browser | Version | Status |
|---------|---------|--------|
| Chrome  | 90+     | ✅ Full Support |
| Firefox | 88+     | ✅ Full Support |
| Safari  | 14+     | ✅ Full Support |
| Edge    | 90+     | ✅ Full Support |

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and test thoroughly
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Development Guidelines
- Follow existing code style and structure
- Test all features across different browsers
- Update documentation for new features
- Ensure accessibility standards are met

## 🐛 Bug Reports

Found a bug? Please open an issue with:
- Browser and version
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable

## 📖 API Reference

### JSON Quiz Format
```typescript
interface QuizData {
  questions: Question[];
}

interface Question {
  category: string;
  subcategory: string;
  question: string;
  options: Option[];
  correctoption: number[];
}

interface Option {
  no: number;
  option: string;
}
```

### URL Parameters
- `?roomid=PASTE_ID` - Pre-fill Room ID field
- `?theme=dark|light` - Set initial theme (if implemented)

## 🎯 Roadmap

- [ ] User authentication and saved progress
- [ ] Team/multiplayer quiz modes
- [ ] Question timer limits
- [ ] Advanced analytics dashboard
- [ ] Mobile app version
- [ ] Question bank management system
- [ ] Integration with learning management systems


<div align="center">

**Made with ❤️ for educators and learners worldwide**

[⭐ Star this repo](https://github.com/Dinesh-Kumar-E/Quizbuzz) • [🍴 Fork it](https://github.com/Dinesh-Kumar-E/Quizbuzz/fork)
</div>
