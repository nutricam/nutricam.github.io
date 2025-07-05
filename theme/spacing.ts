/**
 * NutriCam Spacing System
 * 
 * Defines spacing values for margin, padding, and layout
 * Uses an 8-point grid system (multiples of 4 or 8) for consistency
 */

// Base spacing values on an 8-point grid
const spacing = {
  // Core spacing values
  '0': 0,
  '0.5': 2,
  '1': 4,
  '2': 8,
  '3': 12,
  '4': 16,
  '5': 20,
  '6': 24,
  '7': 28,
  '8': 32,
  '9': 36,
  '10': 40,
  '12': 48,
  '16': 64,
  '20': 80,
  '24': 96,
  '32': 128,
  '40': 160,
  '48': 192,
  '56': 224,
  '64': 256,
};

// Semantic spacing for specific use cases
const layout = {
  // Screen edges
  screenPadding: spacing['4'],
  screenMargin: spacing['4'],
  
  // Card/container spacing
  containerPadding: spacing['4'],
  cardPadding: spacing['4'],
  cardMargin: spacing['3'],
  
  // Content spacing
  contentSpacing: spacing['4'],
  itemSpacing: spacing['3'],
  textSpacing: spacing['2'],
  
  // Form elements
  inputPadding: spacing['3'],
  inputMargin: spacing['2'],
  inputGap: spacing['4'],
  
  // Button spacing
  buttonPadding: {
    small: { horizontal: spacing['3'], vertical: spacing['2'] },
    medium: { horizontal: spacing['4'], vertical: spacing['3'] },
    large: { horizontal: spacing['6'], vertical: spacing['4'] },
  },
  buttonGap: spacing['2'],
  
  // Component gaps
  gapSmall: spacing['2'],
  gapMedium: spacing['4'],
  gapLarge: spacing['6'],
  
  // Nutrition-specific spacing
  nutritionGroupSpacing: spacing['6'],
  nutritionItemSpacing: spacing['3'],
};

// Utility border radiuses
const borderRadius = {
  none: 0,
  xs: 2,
  sm: 4,
  md: 8,
  lg: 12,
  xl: 16,
  '2xl': 24,
  full: 9999,
};

// Shadows for different elevations
const shadow = {
  none: {
    shadowColor: 'transparent',
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0,
    shadowRadius: 0,
    elevation: 0,
  },
  xs: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 2,
    elevation: 1,
  },
  sm: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.15,
    shadowRadius: 3,
    elevation: 2,
  },
  md: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.15,
    shadowRadius: 5,
    elevation: 3,
  },
  lg: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.15,
    shadowRadius: 8,
    elevation: 4,
  },
  xl: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.15,
    shadowRadius: 12,
    elevation: 5,
  },
};

// Helper function for creating margins
const createMargin = (value: keyof typeof spacing) => ({
  margin: spacing[value],
  marginHorizontal: spacing[value],
  marginVertical: spacing[value],
  marginTop: spacing[value],
  marginRight: spacing[value],
  marginBottom: spacing[value],
  marginLeft: spacing[value],
});

// Helper function for creating padding
const createPadding = (value: keyof typeof spacing) => ({
  padding: spacing[value],
  paddingHorizontal: spacing[value],
  paddingVertical: spacing[value],
  paddingTop: spacing[value],
  paddingRight: spacing[value],
  paddingBottom: spacing[value],
  paddingLeft: spacing[value],
});

export default {
  spacing,
  layout,
  borderRadius,
  shadow,
  createMargin,
  createPadding,
}; 