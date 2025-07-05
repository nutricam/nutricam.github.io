/**
 * NutriCam Premium Color System
 * Designed for luxury wellness app targeting ages 18-35
 * Premium, elegant, bold and energetic aesthetic
 * Gender-neutral with sophisticated jewel tones
 * Supports both light and dark modes
 */

// Base palette - sophisticated luxury colors
const palette = {
  // Primary colors - deep emerald greens for premium wellness
  emeraldGreen: '#10B981',
  forestEmerald: '#059669',
  deepEmerald: '#047857',

  // Secondary colors - rich purples for luxury
  royalPurple: '#7C3AED',
  deepPurple: '#5B21B6',
  richIndigo: '#4338CA',

  // Accent colors - vibrant energy
  vibrantCoral: '#FF6B6B',
  energyOrange: '#FF8E53',
  boldOrange: '#F97316',

  // Premium neutrals
  charcoalBlack: '#111827',
  softBlack: '#1F2937',
  premiumGray: '#374151',
  sophisticatedGray: '#6B7280',
  lightGray: '#9CA3AF',
  elegantGray: '#D1D5DB',
  crispWhite: '#FFFFFF',
  offWhite: '#F9FAFB',

  // Luxury accents
  champagneGold: '#D4AF37',
  rosegold: '#E8B4A0',
  platinum: '#E5E7EB',

  // Pure colors
  white: '#FFFFFF',
  black: '#000000',
  
  // Semantic colors - bold and modern
  success: '#10B981', // Premium emerald
  warning: '#F59E0B', // Rich amber
  error: '#EF4444',   // Bold red
  info: '#3B82F6',    // Premium blue

  // Enhanced grays for better contrast
  gray: {
    50: '#F9FAFB',
    100: '#F3F4F6',
    200: '#E5E7EB',
    300: '#D1D5DB',
    400: '#9CA3AF',
    500: '#6B7280',
    600: '#4B5563',
    700: '#374151',
    800: '#1F2937',
    900: '#111827',
    950: '#030712',
  },
}

// Light theme definitions - elegant and premium
export const lightTheme = {
  // Core interface colors
  background: {
    primary: palette.crispWhite,
    secondary: palette.offWhite,
    tertiary: palette.gray[50],
  },
  text: {
    primary: palette.charcoalBlack,
    secondary: palette.premiumGray,
    tertiary: palette.sophisticatedGray,
    inverse: palette.crispWhite,
  },
  
  // Theme colors - sophisticated and bold
  primary: {
    main: palette.emeraldGreen,
    light: '#34D399', // Lighter emerald
    dark: palette.deepEmerald,
    contrast: palette.crispWhite,
  },
  secondary: {
    main: palette.royalPurple,
    light: '#A855F7', // Lighter purple
    dark: palette.deepPurple,
    contrast: palette.crispWhite,
  },
  accent: {
    main: palette.vibrantCoral,
    light: '#FF8A80', // Lighter coral
    dark: '#E53E3E', // Deeper coral
    contrast: palette.crispWhite,
  },
  
  // UI element colors
  surface: palette.crispWhite,
  divider: palette.elegantGray,
  outline: palette.lightGray,
  
  // Semantic colors
  success: palette.success,
  warning: palette.warning,
  error: palette.error,
  info: palette.info,
  
  // Premium luxury accents
  luxury: {
    gold: palette.champagneGold,
    rosegold: palette.rosegold,
    platinum: palette.platinum,
  },
  
  // Nutrition-specific colors - vibrant and modern
  nutrition: {
    protein: palette.royalPurple,    // Rich purple
    carbs: palette.boldOrange,       // Bold orange
    fat: palette.energyOrange,       // Energy orange
    fiber: palette.emeraldGreen,     // Emerald green
    vitamin: palette.richIndigo,     // Rich indigo
    mineral: palette.vibrantCoral,   // Vibrant coral
    calories: palette.champagneGold, // Premium gold
  }
}

// Dark theme definitions - sophisticated and bold
export const darkTheme = {
  // Core interface colors
  background: {
    primary: palette.charcoalBlack,
    secondary: palette.softBlack,
    tertiary: palette.gray[800],
  },
  text: {
    primary: palette.crispWhite,
    secondary: palette.elegantGray,
    tertiary: palette.lightGray,
    inverse: palette.charcoalBlack,
  },
  
  // Theme colors - enhanced for dark mode
  primary: {
    main: '#34D399', // Brighter emerald for dark mode
    light: '#6EE7B7', // Even brighter
    dark: palette.emeraldGreen,
    contrast: palette.charcoalBlack,
  },
  secondary: {
    main: '#A855F7', // Brighter purple for dark mode
    light: '#C084FC', // Even brighter
    dark: palette.royalPurple,
    contrast: palette.charcoalBlack,
  },
  accent: {
    main: '#FF8A80', // Softer coral for dark mode
    light: '#FFB3BA', // Even softer
    dark: palette.vibrantCoral,
    contrast: palette.charcoalBlack,
  },
  
  // UI element colors
  surface: palette.softBlack,
  divider: palette.gray[700],
  outline: palette.gray[600],
  
  // Semantic colors - enhanced for dark mode visibility
  success: '#34D399', // Brighter emerald
  warning: '#FBBF24', // Brighter amber
  error: '#F87171',   // Softer red for dark
  info: '#60A5FA',    // Brighter blue
  
  // Premium luxury accents
  luxury: {
    gold: '#F5D900', // Brighter gold for dark mode
    rosegold: '#FFB3A7', // Brighter rose gold
    platinum: palette.gray[300],
  },
  
  // Nutrition-specific colors - enhanced for dark mode
  nutrition: {
    protein: '#A855F7',    // Bright purple
    carbs: '#FB923C',      // Bright orange
    fat: '#FDBA74',        // Warm orange
    fiber: '#34D399',      // Bright emerald
    vitamin: '#6366F1',    // Bright indigo
    mineral: '#FF8A80',    // Soft coral
    calories: '#F5D900',   // Bright gold
  }
}

// Export these types for use elsewhere
export type ColorTheme = typeof lightTheme;
export type ThemeMode = 'light' | 'dark';

// Export palette for custom color needs
export { palette }; 