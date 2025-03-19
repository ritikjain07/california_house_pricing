# California House Price Prediction

## Project Overview
This web application predicts house prices in California using machine learning algorithms. The system analyzes various factors such as location, house age, and neighborhood characteristics to provide accurate price estimates based on California census data.

## Live Demo
**[Try the application here](https://calhouseai-california-house-pricing.onrender.com/)**

## Technologies Used
- **Python**: Core programming language
- **Flask**: Web framework for building the application
- **Scikit-Learn**: Machine learning library for regression modeling
- **NumPy/Pandas**: Data manipulation and preprocessing
- **HTML/CSS**: Frontend design with responsive layouts
- **Render**: Cloud platform for deployment

## Key Features
1. **Interactive Web Interface**: User-friendly form that collects key housing metrics
2. **Real-time Predictions**: Instant price estimates upon form submission
3. **API Integration**: RESTful API endpoint for programmatic access
4. **Data Visualization**: Clear presentation of prediction results
5. **Responsive Design**: Optimized for both desktop and mobile devices

## Machine Learning Approach
- Implemented a regression model using California housing dataset
- Feature engineering to identify key price determinants
- Model training with cross-validation to ensure accuracy
- Feature scaling for improved prediction performance
- Serialization of trained model for production deployment

## How to Use
1. Visit the [application](https://calhouseai-california-house-pricing.onrender.com/)
2. Enter the required housing metrics:
   - Median Income (in $10,000s)
   - House Age (in years)
   - Average Rooms per household
   - Average Bedrooms per household
   - Population in the block
   - Average Occupancy
   - Latitude and Longitude coordinates
3. Click "Calculate House Price" to get your prediction

## Local Development
```bash
# Clone repository
git clone https://github.com/yourusername/california_house_pricing.git

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

