import React from "react";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Button from "@material-ui/core/Button";

import { appendQuery, removeQuery } from "./Filters/utils";

const useStyles = makeStyles(theme => ({
  paper: {
    padding: theme.spacing(1),
    marginBottom: theme.spacing(1)
  },
  button: {
    margin: theme.spacing(0.5)
  }
}));

const Ordering = ({ location }) => {
  const ordering = useSelector(state => state.products.ordering);
  const classes = useStyles();

  return (
    <Paper className={classes.paper}>
      <Button
        size="small"
        component={Link}
        to={removeQuery(location, "ordering")}
        className={classes.button}
        color="secondary"
        variant={ordering === null ? "contained" : "outlined"}
      >
        Newest
      </Button>
      <Button
        size="small"
        component={Link}
        to={appendQuery(location, { ordering: "min_price" })}
        className={classes.button}
        color="secondary"
        variant={ordering === "min_price" ? "contained" : "outlined"}
      >
        Cheapest
      </Button>
      <Button
        size="small"
        component={Link}
        to={appendQuery(location, { ordering: "max_data" })}
        className={classes.button}
        color="secondary"
        variant={ordering === "max_data" ? "contained" : "outlined"}
      >
        Most Data
      </Button>
      <Button
        size="small"
        component={Link}
        to={appendQuery(location, { ordering: "min_contract" })}
        className={classes.button}
        color="secondary"
        variant={ordering === "min_contract" ? "contained" : "outlined"}
      >
        Shortest Contract
      </Button>
    </Paper>
  );
};

export default Ordering;
