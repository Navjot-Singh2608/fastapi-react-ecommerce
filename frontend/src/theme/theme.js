import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    mode: "light",

    primary: {
      main: "#4f46e5",
      light: "#818cf8",
      dark: "#3730a3",
      contrastText: "#ffffff",
    },

    secondary: {
      main: "#0f172a",
    },

    background: {
      default: "#f8fafc",
      paper: "#ffffff",
    },

    text: {
      primary: "#0f172a",
      secondary: "#64748b",
    },

    success: {
      main: "#16a34a",
    },

    error: {
      main: "#dc2626",
    },
  },

  typography: {
    fontFamily:
      '"Inter", "Segoe UI", "Roboto", "Helvetica", "Arial", sans-serif',

    h1: {
      fontWeight: 800,
      letterSpacing: "-0.04em",
    },

    h2: {
      fontWeight: 800,
      letterSpacing: "-0.03em",
    },

    h3: {
      fontWeight: 700,
    },

    h4: {
      fontWeight: 700,
    },

    h5: {
      fontWeight: 700,
    },

    h6: {
      fontWeight: 700,
    },

    button: {
      fontWeight: 700,
      textTransform: "none",
    },
  },

  shape: {
    borderRadius: 14,
  },

  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 12,
          boxShadow: "none",
          padding: "10px 22px",
          fontSize: "0.95rem",
        },
      },
    },

    MuiTextField: {
      defaultProps: {
        variant: "outlined",
      },
    },

    MuiOutlinedInput: {
      styleOverrides: {
        root: {
          borderRadius: 12,
          backgroundColor: "#ffffff",
        },
      },
    },

    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 20,
        },
      },
    },

    MuiPaper: {
      styleOverrides: {
        root: {
          backgroundImage: "none",
        },
      },
    },
  },
});

export default theme;