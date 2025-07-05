/**
 * Theme exports
 * Central export file for all theme-related components and utilities
 */

// Export theme context and hook
export { 
  ThemeProvider, 
  useTheme, 
  defaultTheme,
  type Theme 
} from './ThemeContext';

// Export color system
export { 
  lightTheme, 
  darkTheme, 
  palette,
  type ColorTheme,
  type ThemeMode
} from './colors';

// Export typography system
export { default as typography } from './typography';

// Export spacing system
export { default as spacing } from './spacing';

// Utility styled component function (convenience export)
export const themed = <Props extends {}>(
  Component: React.ComponentType<Props & { theme?: any }>
) => {
  return Component;
};

// Re-export everything as a default object as well
import { defaultTheme } from './ThemeContext';
import typography from './typography';
import spacing from './spacing';

export default {
  ...defaultTheme,
  typography,
  spacing,
}; 