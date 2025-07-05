import React, { createContext, useContext, useEffect, useState } from 'react';
import { useColorScheme } from 'react-native';
import { lightTheme, darkTheme, ColorTheme, ThemeMode } from './colors';
import typography from './typography';
import spacing from './spacing';

// Define the Theme interface that will be used throughout the app
export interface Theme {
  colors: ColorTheme;
  typography: typeof typography;
  spacing: typeof spacing;
  mode: ThemeMode;
}

// Define the ThemeContextType interface
interface ThemeContextType {
  theme: Theme;
  toggleTheme: () => void;
  setThemeMode: (mode: ThemeMode) => void;
}

// Create the ThemeContext
const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

// ThemeProvider props interface
interface ThemeProviderProps {
  children: React.ReactNode;
  initialTheme?: ThemeMode;
}

/**
 * ThemeProvider component that wraps the app and provides theme values
 */
export const ThemeProvider: React.FC<ThemeProviderProps> = ({ 
  children, 
  initialTheme,
}) => {
  // Get the device color scheme
  const colorScheme = useColorScheme();
  
  // Initialize theme state
  const [themeMode, setThemeMode] = useState<ThemeMode>(
    initialTheme || (colorScheme as ThemeMode) || 'light'
  );

  // Create the theme object
  const theme: Theme = {
    colors: themeMode === 'dark' ? darkTheme : lightTheme,
    typography,
    spacing,
    mode: themeMode,
  };

  // Toggle between light and dark theme
  const toggleTheme = () => {
    setThemeMode(prevMode => (prevMode === 'light' ? 'dark' : 'light'));
  };

  // Update theme when system preference changes
  useEffect(() => {
    if (!initialTheme && colorScheme) {
      setThemeMode(colorScheme as ThemeMode);
    }
  }, [colorScheme, initialTheme]);

  // Context value
  const value = {
    theme,
    toggleTheme,
    setThemeMode,
  };

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
};

/**
 * Hook for using the theme in components
 */
export const useTheme = (): ThemeContextType => {
  const context = useContext(ThemeContext);
  
  if (context === undefined) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  
  return context;
};

// Export a default theme for use outside of the ThemeProvider
export const defaultTheme: Theme = {
  colors: lightTheme,
  typography,
  spacing,
  mode: 'light',
}; 