/**
 * NutriCam Typography System
 * 
 * Uses a type scale that works well across mobile devices
 * Supports various font weights, sizes and semantic usage
 */

import { Platform, TextStyle } from 'react-native';

// Font family definitions
const fontFamily = {
  // Using system fonts for best performance and native feel
  // regular: Platform.select({
  //   ios: 'SF Pro Display',
  //   android: 'Roboto',
  //   default: 'System',
  // }),
  // medium: Platform.select({
  //   ios: 'SF Pro Display',
  //   android: 'Roboto',
  //   default: 'System',
  // }),
  // semibold: Platform.select({
  //   ios: 'SF Pro Display',
  //   android: 'Roboto',
  //   default: 'System',
  // }),
  // bold: Platform.select({
  //   ios: 'SF Pro Display',
  //   android: 'Roboto',
  //   default: 'System',
  // }),
  dmSans: 'DM Sans', // For App Title / Headline
  inter: 'Inter',   // For Subheadings, Body Text, Microcopy
  manrope: 'Manrope', // For Button Text
};

// Font weights
const fontWeights = {
  light: '300',    // For Microcopy (Inter)
  regular: '400',  // For Body Text (Inter)
  medium: '500',   // For Subheadings (Inter), Button Text (Manrope)
  bold: '700',     // For App Title / Headline (DM Sans)
} as const;

// Font sizes (adjust if necessary based on the 24-32pt, 16-20pt etc. ranges)
const fontSize = {
  micro: 12,    // Microcopy (12-13pt)
  caption: 13,  // Microcopy (12-13pt)
  sm: 14,       // Body/Button (14-16pt)
  md: 15,       // Body/Button (14-16pt)
  lg: 16,       // Body/Button/Subheading (14-16pt, 16-20pt)
  xl: 18,       // Subheading (16-20pt)
  '2xl': 20,    // Subheading (16-20pt)
  '3xl': 24,    // App Title (24-32pt)
  '4xl': 28,    // App Title (24-32pt)
  '5xl': 32,    // App Title (24-32pt)
};

// Line heights (adjust for "relaxed" and 1.5x requirements)
const lineHeight = {
  micro: 18,      // Approx 1.5x for 12pt
  caption: 20,    // Approx 1.5x for 13pt (low-contrast if secondary - color handled in component)
  sm: 21,         // 1.5x for 14pt (Body Text)
  md: 22.5,       // 1.5x for 15pt (Body Text)
  lg: 24,         // 1.5x for 16pt (Body Text) / or for Button / or for Subheading
  xl: 27,         // Subheading (slight letter spacing)
  '2xl': 30,      // Subheading (slight letter spacing)
  '3xl': 34,      // App Title (relaxed, e.g., ~1.4x for 24pt)
  '4xl': 40,      // App Title (relaxed, e.g., ~1.4x for 28pt)
  '5xl': 48,      // App Title (relaxed, e.g., 1.5x for 32pt)
};

// Letter spacing (tracking)
const letterSpacing = {
  // tighter: -0.8, // Kept if other old variants use it
  // tight: -0.4,   // Kept if other old variants use it
  normal: 0,
  slight: 0.25, // For subheadings
  // wide: 0.4,     // Kept if other old variants use it
  // wider: 0.8,    // Kept if other old variants use it
};

// Base text styles
const createTextStyle = (
  fontFamilyValue: string,
  size: keyof typeof fontSize,
  weight: keyof typeof fontWeights,
  lineHeightValue?: number,
  spacing: keyof typeof letterSpacing = 'normal',
  textTransformValue?: 'none' | 'uppercase' | 'lowercase' | 'capitalize'
): TextStyle => ({
  fontFamily: fontFamilyValue,
  fontWeight: fontWeights[weight],
  fontSize: fontSize[size],
  lineHeight: lineHeightValue !== undefined ? lineHeightValue : lineHeight[size],
  letterSpacing: letterSpacing[spacing],
  ...(textTransformValue && { textTransform: textTransformValue }),
});

// Semantic text variants for different purposes
const variants = {
  // App Title / Headline: DM Sans / Bold, 24–32pt, relaxed line height
  appTitleLarge: createTextStyle(fontFamily.dmSans, '5xl', 'bold', lineHeight['5xl']), // 32pt
  appTitleMedium: createTextStyle(fontFamily.dmSans, '4xl', 'bold', lineHeight['4xl']), // 28pt
  appTitleSmall: createTextStyle(fontFamily.dmSans, '3xl', 'bold', lineHeight['3xl']),   // 24pt

  // Subheadings: Inter / Medium, 16–20pt, slight letter spacing
  subheadingLarge: createTextStyle(fontFamily.inter, '2xl', 'medium', lineHeight['2xl'], 'slight'), // 20pt
  subheadingMedium: createTextStyle(fontFamily.inter, 'xl', 'medium', lineHeight['xl'], 'slight'),  // 18pt
  subheadingSmall: createTextStyle(fontFamily.inter, 'lg', 'medium', lineHeight['lg'], 'slight'),   // 16pt

  // Body Text: Inter / Regular, 14–16pt, 1.5 line height
  bodyLarge: createTextStyle(fontFamily.inter, 'lg', 'regular', fontSize.lg * 1.5),    // 16pt
  bodyMedium: createTextStyle(fontFamily.inter, 'md', 'regular', fontSize.md * 1.5),   // 15pt
  bodySmall: createTextStyle(fontFamily.inter, 'sm', 'regular', fontSize.sm * 1.5),    // 14pt

  // Button Text: Manrope / Medium, 14–16pt, all caps optional
  // For all caps, set textTransformValue to 'uppercase' in the component or a new variant
  buttonLarge: createTextStyle(fontFamily.manrope, 'lg', 'medium', lineHeight.lg), // 16pt
  buttonMedium: createTextStyle(fontFamily.manrope, 'md', 'medium', lineHeight.md),// 15pt
  buttonSmall: createTextStyle(fontFamily.manrope, 'sm', 'medium', lineHeight.sm), // 14pt

  // Microcopy: Inter / Light, 12–13pt, low-contrast if secondary
  // Color for "low-contrast if secondary" should be handled by applying a theme color in the component
  microcopyLarge: createTextStyle(fontFamily.inter, 'caption', 'light', lineHeight.caption), // 13pt
  microcopySmall: createTextStyle(fontFamily.inter, 'micro', 'light', lineHeight.micro),   // 12pt
  
  // --- Existing variants from previous session - review if they are still needed or map to new ones ---
  // Display headings (Consider mapping to appTitle or removing)
  // displayLarge: createTextStyle(fontFamily.inter,'5xl', 'bold', 'tight'), // Example of old, needs font family
  // displayMedium: createTextStyle(fontFamily.inter,'4xl', 'bold', 'tight'),
  // displaySmall: createTextStyle(fontFamily.inter,'3xl', 'bold', 'tight'),
  
  // Headings (Consider mapping to appTitle or subheading)
  // headingLarge: createTextStyle(fontFamily.inter,'3xl', 'semibold'),
  // headingMedium: createTextStyle(fontFamily.inter,'2xl', 'semibold'),
  // headingSmall: createTextStyle(fontFamily.inter,'xl', 'semibold'),
  
  // Subtitles (Consider mapping to subheading)
  // subtitleLarge: createTextStyle(fontFamily.inter,'xl', 'medium'),
  // subtitleMedium: createTextStyle(fontFamily.inter,'lg', 'medium'),
  // subtitleSmall: createTextStyle(fontFamily.inter,'md', 'medium'),
  
  // Captions and auxiliary text (Consider mapping to microcopy)
  // captionLarge: createTextStyle(fontFamily.inter,'sm', 'medium'),
  // captionMedium: createTextStyle(fontFamily.inter,'xs', 'medium'),
  // captionSmall: createTextStyle(fontFamily.inter,'xs', 'regular'),
  
  // Interactive elements (Button variants are new)
  // buttonLargeOld: createTextStyle(fontFamily.inter,'lg', 'semibold'),
  // buttonMediumOld: createTextStyle(fontFamily.inter,'md', 'semibold'),
  // buttonSmallOld: createTextStyle(fontFamily.inter,'sm', 'semibold'),
  
  // Nutrition-specific (Review if these specific styles are still needed or can use general variants)
  // nutritionValue: createTextStyle(fontFamily.inter,'2xl', 'bold'),
  // nutritionLabel: createTextStyle(fontFamily.inter,'sm', 'medium'),
  // nutritionDetail: createTextStyle(fontFamily.inter,'xs', 'regular'),
  
  // Data visualization (Review if these specific styles are still needed or can use general variants)
  // dataValue: createTextStyle(fontFamily.inter,'xl', 'semibold'),
  // dataLabel: createTextStyle(fontFamily.inter,'sm', 'medium'),
};

// Utility function to create derived styles 
const createDerivedStyle = (
  baseStyle: TextStyle,
  overrides: Partial<TextStyle>
): TextStyle => ({
  ...baseStyle,
  ...overrides,
});

export default {
  fontFamily,
  fontWeights,
  fontSize,
  lineHeight,
  letterSpacing,
  variants,
  createTextStyle,
  createDerivedStyle,
}; 