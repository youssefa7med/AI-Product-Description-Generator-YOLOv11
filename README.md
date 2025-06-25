# Goods Detector YOLOv11 🛍️

![Goods Detector YOLOv11](https://miro.medium.com/v2/resize:fit:1358/0*YTLUwphSdWs08-dK.gif)

This project is an AI-powered product detection and description generator that combines YOLOv11 object detection with automated product description generation and text-to-speech capabilities. The system can identify products from images and generate professional product descriptions with audio narration in multiple languages. 🚀

## Overview

The Goods Detector YOLOv11 project aims to revolutionize e-commerce product management by automatically detecting product categories from images and generating comprehensive product descriptions. The application leverages a custom-trained YOLOv11 model for accurate product detection and integrates with advanced AI services for description generation and text-to-speech conversion.

### Key Features ✨

- **Advanced Product Detection 🔍**:
  - Custom YOLOv11 model trained on 100 epochs with over 15,000 product images
  - Accurate classification across 8 different product categories
  - High-precision object detection optimized for e-commerce products

- **Intelligent Description Generation 📝**:
  - AI-powered product description creation using DeepSeek API
  - Multi-language support for global e-commerce applications
  - Professional, SEO-optimized product descriptions

- **Text-to-Speech Integration 🔊**:
  - Open-source TTS model from OpenAI
  - Multi-language audio generation capabilities
  - Various voice options for different use cases

- **Flexible Input Methods 📤**:
  - Direct image upload functionality
  - URL-based image processing
  - Real-time processing and analysis

## Live Application 🌐

Experience the Goods Detector YOLOv11 tool directly through our live application: [Goods Detector YOLOv11](https://huggingface.co/spaces/YoussefA7med/Goods_Detector_YOLOv11)

## Model Details 🤖

### YOLOv11 Custom Training ⚡
- **Training Duration**: 100 epochs for optimal accuracy
- **Dataset Size**: Over 15,000 carefully curated product images
- **Categories**: 8 distinct product categories
- **Model Performance**: Optimized for real-world e-commerce scenarios

### Supported Product Categories 📦
The model can accurately detect and classify products across 8 major categories, making it suitable for various e-commerce applications.

## Analysis

### Product Detection Pipeline

- **Image Processing**:
  - PIL-based image handling and preprocessing
  - Support for various image formats and sizes
  - Automatic image optimization for detection

- **YOLOv11 Inference**:
  - Real-time object detection and classification
  - Confidence scoring for accurate predictions
  - Bounding box detection for precise localization

### Description Generation

- **AI-Powered Content Creation**:
  - DeepSeek API integration for natural language generation
  - Context-aware product descriptions
  - Customizable description length and style

- **Multi-Language Support**:
  - Support for 50+ languages
  - Culturally appropriate content generation
  - RTL language support including Arabic

### Text-to-Speech Features

- **OpenAI TTS Integration**:
  - High-quality voice synthesis
  - Multiple voice options (nova, alloy, echo, fable, onyx, shimmer)
  - Emotion and tone customization

## Technologies Used

- **Python**: Core programming language for AI model integration
- **YOLOv11 (Ultralytics)**: State-of-the-art object detection model
- **PIL (Pillow)**: Image processing and manipulation
- **Gradio**: Interactive web interface for user-friendly experience
- **DeepSeek API**: Advanced language model for description generation
- **OpenAI TTS**: Text-to-speech conversion with multiple voice options
- **Requests**: HTTP client for API integrations
- **Logging**: Comprehensive logging system for debugging and monitoring

## Getting Started 🚀

### Prerequisites

Ensure you have Python 3.8+ installed, along with the required dependencies.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/goods-detector-yolov11.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd goods-detector-yolov11
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   ```bash
   # Create a .env file with the following variables:
   DEEPSEEK_API_KEY=your_deepseek_api_key
   TTS_PASSWORD=your_tts_password
   HF_TOKEN=your_huggingface_token
   ```

### Model Setup

1. **Download the Trained Model**:
   - Place the `best.pt` file (trained YOLOv11 model) in the project directory
   - Ensure the model file is accessible by the application

2. **Verify Model Loading**:
   ```bash
   python -c "from ultralytics import YOLO; model = YOLO('best.pt'); print('Model loaded successfully')"
   ```

### Running the Application

1. **Start the Gradio Interface**:
   ```bash
   python app.py
   ```

2. **Access the Application**:
   - Open your web browser and navigate to the displayed local URL
   - Upload an image or provide an image URL to test the system

## Usage 💡

### Product Detection and Description Generation

1. **Upload Method**:
   - Upload a product image using the file picker
   - Optionally provide a product name for more accurate descriptions
   - Select your preferred language for the description
   - Click "Generate Description" to process

2. **URL Method**:
   - Enter a direct URL to a product image
   - Follow the same steps as the upload method
   - The system will automatically download and process the image

3. **Results**:
   - View the detected product category
   - Read the generated product description
   - Listen to the audio narration of the description

### Debug Tools

The application includes built-in debugging tools to help troubleshoot API connections and system performance:

- **TTS API Testing**: Verify text-to-speech functionality
- **API Status Monitoring**: Check the status of all integrated services
- **Logging System**: Comprehensive logging for error tracking

## API Integration

### DeepSeek API
- Used for generating natural language product descriptions
- Supports multiple languages and customizable writing styles
- Provides high-quality, contextually relevant content

### Text-to-Speech API
- OpenAI-based TTS model for audio generation
- Multiple voice options and emotional tones
- Support for various languages including Arabic

### Hugging Face Integration
- Secure API access using HF tokens
- Integration with private TTS models
- Scalable cloud-based processing

## Performance Optimization

- **Efficient Image Processing**: Optimized PIL operations for fast image handling
- **Smart Caching**: Temporary file management for efficient processing
- **Error Handling**: Comprehensive error handling and recovery mechanisms
- **Logging System**: Detailed logging for performance monitoring and debugging

## Contributing 🤝

Contributions are welcome! If you have suggestions for improvements, additional features, or bug fixes, please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution

- **Model Improvements**: Enhance YOLOv11 training with additional categories
- **Language Support**: Add support for more languages and regional dialects
- **UI/UX Enhancements**: Improve the Gradio interface design
- **Performance Optimization**: Optimize processing speed and resource usage
- **Documentation**: Enhance documentation and add tutorials

## License

This project is licensed under the MIT License. For more information, please refer to the [LICENSE](LICENSE) file.

## Acknowledgments 🙏

- **Ultralytics**: For the excellent YOLOv11 implementation
- **OpenAI**: For the open-source TTS model
- **DeepSeek**: For providing advanced language model capabilities
- **Hugging Face**: For the platform and hosting services
- **Open Source Community**: For the tools and libraries that made this project possible

## Support

For support, questions, or feature requests:
- Open an issue on GitHub
- Visit our live application for demonstrations
- Check the debug tools for troubleshooting

---

*Built with ❤️ for the e-commerce and AI community*
