# NutriCam Premium Theme System

This theme system provides a luxurious, sophisticated look and feel across the NutriCam application. Designed specifically for the premium wellness market targeting ages 18-35, it combines elegance with bold, energetic aesthetics while maintaining perfect gender neutrality.

## 🎨 Design Philosophy & Principles

### Premium Luxury Aesthetic
The app should evoke a sense of being:
- **Premium and sophisticated** - appealing to luxury market expectations
- **Bold yet elegant** - energetic colors balanced with refined taste
- **Gender-neutral** - sophisticated jewel tones that appeal universally
- **Modern and tech-forward** - perfect for the 18-35 demographic
- **Confident and empowering** - inspiring users on their wellness journey

This creates an ideal experience for a **premium wellness product** rooted in **luxury, personalization, and sophisticated simplicity**.

### Target Demographic: 18-35 Luxury Segment
- **Young professionals** seeking premium wellness solutions
- **Tech-savvy** users who appreciate modern, sophisticated design
- **Quality-conscious** individuals willing to invest in premium experiences
- **Aesthetically aware** users who value beautiful, thoughtful design

### General Design Guidelines

#### Color Usage
- **Primary Emerald Green (#10B981):** Use for primary actions, wellness indicators, and success states
- **Royal Purple (#7C3AED):** Use for premium features, secondary actions, and luxury touches
- **Vibrant Coral (#FF6B6B):** Use for energetic accents, call-to-actions, and motivational elements
- **Champagne Gold (#D4AF37):** Use sparingly for premium badges, achievements, and luxury highlights

#### Typography
- **Line Height:** Employ larger line heights (approximately 140–160% of the font size) to create an airy, premium feel and enhance readability
- **All Caps:** Use strategically for buttons and micro-labels to add sophistication
- **Font Families:** Stick to the premium font families (DM Sans, Inter, and Manrope) for consistency and luxury appeal

#### White Space & Layout
- Utilize white space **generously** to create premium, breathable layouts
- Embrace **asymmetrical layouts** where appropriate for modern sophistication
- Use **high contrast** between elements for clarity and premium feel
- Implement **subtle shadows and elevation** to add depth and luxury

#### Tone of Voice
- **Sophisticated yet approachable** - never condescending
- **Empowering and motivational** - inspiring users toward their goals
- **Precise and intelligent** - backed by science and expertise
- **Personalized** - feels tailored to each individual user

## Table of Contents
- [Directory Structure](#directory-structure)
- [Theme Usage](#theme-usage)
- [Premium Colors](#premium-colors)
- [Typography](#typography)
- [Spacing](#spacing)
- [UI Components](#ui-components)
- [Luxury Features](#luxury-features)

## Directory Structure

```
app/theme/
├── colors.ts         # Premium color palette and theme definitions
├── typography.ts     # Sophisticated typography system
├── spacing.ts        # Spacing, sizing and layout system
├── ThemeContext.tsx  # Theme context provider
├── index.ts          # Exports
└── README.md         # Documentation
```

## Theme Usage

### Wrapping Your App

The theme is already wrapped around the application in `App.tsx`:

```tsx
// App.tsx
import { ThemeProvider } from "./app/theme";

export default function App() {
  return (
    <GestureHandlerRootView style={{ flex: 1 }}>
      <SafeAreaProvider>
        <ThemeProvider>
          <AuthProvider>
            {/* App content */}
          </AuthProvider>
        </ThemeProvider>
      </SafeAreaProvider>
    </GestureHandlerRootView>
  );
}
```

### Using Theme in Components

```tsx
import { useTheme } from "../app/theme";

const MyComponent = () => {
  const { theme } = useTheme();
  
  return (
    <View style={{ 
      backgroundColor: theme.colors.background.primary,
      padding: theme.spacing.layout.contentSpacing,
    }}>
      {/* Component content */}
    </View>
  );
};
```

### Toggling Theme

```tsx
import { useTheme } from "../app/theme";

const ThemeToggle = () => {
  const { theme, toggleTheme } = useTheme();
  
  return (
    <Button 
      onPress={toggleTheme}
      label={`Switch to ${theme.mode === 'light' ? 'dark' : 'light'} mode`}
    />
  );
};
```

## Premium Colors

The premium color system features sophisticated jewel tones and luxury accents designed for the high-end wellness market.

### Primary Color Palette

#### Light Mode
- **Background:** Crisp white (#FFFFFF) with off-white (#F9FAFB) accents
- **Primary:** Emerald green (#10B981) - premium wellness indicator
- **Secondary:** Royal purple (#7C3AED) - luxury and sophistication
- **Accent:** Vibrant coral (#FF6B6B) - energy and motivation
- **Text:** Charcoal black (#111827) for maximum contrast and readability

#### Dark Mode
- **Background:** Charcoal black (#111827) with soft black (#1F2937) layers
- **Primary:** Bright emerald (#34D399) - enhanced visibility
- **Secondary:** Bright purple (#A855F7) - maintained luxury feel
- **Accent:** Soft coral (#FF8A80) - energetic but eye-friendly
- **Text:** Crisp white (#FFFFFF) for clarity

### Luxury Accent Colors

```tsx
// Luxury accent usage
const { theme } = useTheme();

// Premium gold for achievements
const achievementColor = theme.colors.luxury.gold;

// Rose gold for special features
const premiumFeatureColor = theme.colors.luxury.rosegold;

// Platinum for subtle luxury touches
const subtleAccentColor = theme.colors.luxury.platinum;
```

### Nutrition Color System

The nutrition colors are bold and energetic while maintaining sophistication:

```tsx
// Enhanced nutrition colors
const nutritionColors = {
  protein: theme.colors.nutrition.protein,    // Rich royal purple
  carbs: theme.colors.nutrition.carbs,        // Bold orange
  fat: theme.colors.nutrition.fat,            // Energy orange
  fiber: theme.colors.nutrition.fiber,        // Emerald green
  vitamin: theme.colors.nutrition.vitamin,    // Rich indigo
  mineral: theme.colors.nutrition.mineral,    // Vibrant coral
  calories: theme.colors.nutrition.calories,  // Premium gold
};
```

### Usage Examples

```tsx
import { useTheme } from "../app/theme";

const { theme } = useTheme();

// Primary action button
const primaryButtonStyle = {
  backgroundColor: theme.colors.primary.main,
  color: theme.colors.primary.contrast,
};

// Premium feature highlight
const premiumHighlight = {
  backgroundColor: theme.colors.secondary.main,
  borderColor: theme.colors.luxury.gold,
};

// Energetic call-to-action
const energeticCTA = {
  backgroundColor: theme.colors.accent.main,
  color: theme.colors.accent.contrast,
};
```

## Typography

The typography system emphasizes sophistication and premium feel:

### Font Usage for Premium Aesthetic

- **App Title / Headline:** DM Sans / Bold, 28–36pt, tight letter spacing for impact
- **Premium Subheadings:** Inter / Medium, 18–24pt, subtle letter spacing for elegance
- **Body Text:** Inter / Regular, 16–18pt, 1.6 line height for luxury readability
- **Button Text:** Manrope / Medium, 14–18pt, slightly spaced for sophistication
- **Luxury Microcopy:** Inter / Light, 13–14pt, elegant and subtle

### Enhanced Typography Usage

```tsx
import { Text } from "../components/ui";

// Premium headline
<Text variant="appTitleLarge" style={{ letterSpacing: -0.5 }}>
  Premium Nutrition Insights
</Text>

// Sophisticated subheading
<Text variant="subheadingLarge" style={{ letterSpacing: 0.5 }}>
  Personalized for You
</Text>

// Luxury button text
<Text variant="buttonLarge" style={{ letterSpacing: 1 }}>
  GET PREMIUM ACCESS
</Text>
```

## Spacing

Enhanced spacing system for premium layouts:

### Premium Spacing Guidelines

- Use **generous white space** to create breathing room
- Implement **consistent 8pt grid** with larger intervals for luxury feel
- Apply **asymmetrical spacing** where appropriate for modern sophistication
- Use **elevated spacing** (24px, 32px, 48px) more frequently than compact spacing

```tsx
import { useTheme } from "../app/theme";

const { theme } = useTheme();

// Premium layout spacing
const premiumContainer = {
  padding: theme.spacing.spacing['8'], // 32px for generous feel
  margin: theme.spacing.spacing['6'],  // 24px for elegant separation
};

// Luxury card spacing
const luxuryCard = {
  padding: theme.spacing.spacing['10'], // 40px for premium interior
  borderRadius: theme.spacing.borderRadius.xl, // Larger radius for sophistication
  ...theme.spacing.shadow.lg, // Elevated shadow for depth
};
```

## UI Components

Premium UI components that embody the luxury aesthetic:

### Enhanced Button Variants

```tsx
import { Button } from "../components/ui";

// Premium primary button
<Button
  variant="primary"
  size="large"
  label="Unlock Premium Features"
  style={{ letterSpacing: 1 }}
  fullWidth
/>

// Luxury secondary button  
<Button
  variant="secondary"
  size="medium"
  label="Explore Insights"
  leftIcon={<PremiumIcon />}
/>

// Energetic accent button
<Button
  variant="accent"
  size="medium" 
  label="Start Your Journey"
  rightIcon={<ArrowForward />}
/>
```

### Premium Container Layouts

```tsx
import { Container } from "../components/ui";

// Luxury content container
<Container
  padding="xl"
  margin="lg"
  backgroundColor={theme.colors.surface}
  style={{
    borderRadius: theme.spacing.borderRadius.xl,
    ...theme.spacing.shadow.lg,
  }}
>
  {/* Premium content */}
</Container>
```

## Luxury Features

### Premium Indicators

Use luxury accent colors to indicate premium features:

```tsx
// Premium badge
<View style={{
  backgroundColor: theme.colors.luxury.gold,
  paddingHorizontal: 12,
  paddingVertical: 4,
  borderRadius: 20,
}}>
  <Text style={{ color: theme.colors.black, fontWeight: 'bold' }}>
    PREMIUM
  </Text>
</View>

// Luxury border accent
<View style={{
  borderWidth: 2,
  borderColor: theme.colors.luxury.rosegold,
  borderRadius: theme.spacing.borderRadius.lg,
}}>
  {/* Premium feature content */}
</View>
```

### Achievement System

Use the enhanced color system for achievement indicators:

```tsx
// Achievement levels using luxury colors
const achievementColors = {
  bronze: theme.colors.nutrition.carbs,    // Bold orange
  silver: theme.colors.luxury.platinum,   // Platinum
  gold: theme.colors.luxury.gold,         // Champagne gold
  premium: theme.colors.secondary.main,   // Royal purple
};
```

## Icons

Maintain sophistication with carefully chosen icons:

- **Primary Icon Library:** `Ionicons` (from `@expo/vector-icons`)
- **Preferred Style:** `outline` for elegance, `filled` for premium features
- **Size Guidelines:** Use larger icon sizes (24px-32px) for premium feel
- **Color Strategy:** Use theme colors strategically - primary for actions, luxury accents for premium features

### Premium Icon Usage

```tsx
import { Ionicons } from '@expo/vector-icons';
import { useTheme } from "../app/theme";

const PremiumIcon = () => {
  const { theme } = useTheme();

  return (
    <View style={{ flexDirection: 'row', alignItems: 'center' }}>
      <Ionicons 
        name="diamond-outline" 
        size={28} 
        color={theme.colors.luxury.gold} 
      />
      <Ionicons 
        name="fitness-outline" 
        size={24} 
        color={theme.colors.primary.main} 
      />
      <Ionicons 
        name="trending-up-outline" 
        size={24} 
        color={theme.colors.accent.main} 
      />
    </View>
  );
};
```

## Contributing

When extending the premium theme system:

1. Maintain **luxury aesthetic** - always consider the premium market positioning
2. Ensure **gender neutrality** - test colors and designs with diverse users
3. Consider **18-35 demographic** - modern, tech-savvy, quality-conscious
4. Preserve **sophisticated boldness** - energetic yet elegant
5. Test in **both light and dark modes** - ensure premium feel across themes
6. Use **generous spacing** and **high contrast** for premium experience
7. Export new components from `components/ui/index.ts` 