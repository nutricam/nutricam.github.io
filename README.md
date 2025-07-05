# NutriCam

A React Native Expo app that uses Google Gemini 2.5 Flash AI to analyze food in photos. Simply take a picture of your meal and get detailed information about the food, quantity, and nutritional content.

## Features

- Take photos using the device camera
- Analyze food with Google Gemini AI
- Get detailed information about:
  - Food identification
  - Quantity estimation
  - Caloric content
  - Macronutrients (proteins, carbs, fats)
  - Micronutrients (vitamins and minerals)

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   npm install
   ```
3. Get a Google Gemini API key:
   - Go to [Google AI Studio](https://makersuite.google.com/)
   - Create an account if you don't have one
   - Navigate to the API Keys section
   - Create a new API key
   
4. Add your API key:
   - Open `services/geminiService.ts`
   - Replace `YOUR_GEMINI_API_KEY` with your actual API key

5. Start the development server:
   ```
   npm start
   ```

## Troubleshooting

### Dashboard Loading Issues

If you see "Loading your data..." indefinitely on the Dashboard:

1. Verify your Supabase API key is correctly set
2. Check the console logs for authentication errors
3. Ensure your user account has a profile in the `profiles` table

## Development

### Database Migrations

Migrations are stored in `supabase/migrations/`. To apply migrations:

```bash
supabase db push
```

### Testing

Run tests with:

```bash
npm test
```

## Nutrient Parsing

The NutriCam app uses AI (Gemini) to analyze food images and extract nutritional information. The extracted text is then parsed to identify individual nutrients and their amounts.

### Nutrient Parser

The nutrient parser (`app/utils/nutrientParser.ts`) is responsible for:

1. Extracting nutrient information from Gemini's analysis text
2. Mapping nutrient names to compound IDs in the database
3. Converting units to the standardized form for each nutrient
4. Saving the structured data to the `nutrient_data` field in the database

### Batch Update Scripts

If you need to update the nutrient data for existing meals (e.g., after improving the parser), use the scripts in the `scripts/` directory:

```bash
# Update a single meal
node scripts/update-meal-nutrients.js <meal-id>

# Update all meals (dry run)
node scripts/batch-update-meal-nutrients.js

# Update all meals (live)
node scripts/batch-update-meal-nutrients.js --live
```

See `scripts/README.md` for more details on these utility scripts.

## License

MIT 