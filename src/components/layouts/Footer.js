import React from "react";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import Typography from "@material-ui/core/Typography";
import Link from "@material-ui/core/Link";
import GitHubIcon from "@material-ui/icons/GitHub";
import IconButton from "@material-ui/core/IconButton";

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {"Copyright © "}
      <Link color="inherit" href="https://tel-me.herokuapp.com">
        TelMe
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

const useStyles = makeStyles((theme) => ({
  footer: {
    backgroundColor: theme.palette.background.paper,
    // marginTop: theme.spacing(8),
    padding: theme.spacing(6, 0),
  },
}));

export default function Footer() {
  const classes = useStyles();
  const github = "https://github.com/BlondeBubblyBryan/TelMe";

  return (
    <footer className={classes.footer}>
      <Container>
        {/* <Typography variant="h6" align="center" gutterBottom>
          Placeholder text
        </Typography>
        <Typography
          variant="subtitle1"
          align="center"
          color="textSecondary"
          component="p"
        >
          Hello hello hello
        </Typography> */}
          <Container align="center">
          <IconButton size="medium" onClick={() => window.open(github, "_blank")}>
            <GitHubIcon/>
          </IconButton>
          </Container>
        <Copyright />
        <Typography variant="body2" color="textSecondary" align="center">
          An NUS Orbital project by Bryan and Ben.
        </Typography>
      </Container>
    </footer>
  );
}

Footer.propTypes = {
  description: PropTypes.string,
  title: PropTypes.string,
};
