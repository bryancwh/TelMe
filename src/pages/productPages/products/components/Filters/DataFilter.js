import React, { useEffect } from "react";
import { useSelector } from "react-redux";
import { withStyles, makeStyles } from "@material-ui/core/styles";
import queryString from "query-string";
import useReactRouter from "use-react-router";
import Typography from "@material-ui/core/Typography";
import MUISlider from "@material-ui/core/Slider";

import { appendQuery } from "./utils";

const Slider = withStyles(theme => ({
  root: {
    color: "#2979ff",
    height: 8
  },
  thumb: {
    height: 24,
    width: 24,
    backgroundColor: "#fff",
    border: "2px solid currentColor",
    marginTop: -8,
    marginLeft: -12,
    "&:focus,&:hover,&$active": {
      boxShadow: "inherit"
    }
  },
  active: {},
  valueLabel: {
    left: "calc(-50% + 4px)"
  },
  track: {
    height: 8,
    borderRadius: 4
  },
  rail: {
    height: 8,
    borderRadius: 4
  }
}))(MUISlider);

const useStyles = makeStyles(theme => ({
  root: {
    width: 300 + theme.spacing(3) * 2
  }
}));

const DataFilter = () => {
  const { history, location } = useReactRouter();
  const { max_data, min_data } = useSelector(state => state.products);
  const [value, setValue] = React.useState([0, 0]);
  const classes = useStyles();
  const parsed = queryString.parse(location.search);

  useEffect(() => {
    setValue([parsed.min_data || min_data, parsed.max_data || max_data]);
  }, [parsed.min_data, parsed.max_data, min_data, max_data]);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const handleSubmit = (event, value) => {
    if (value) {
      history.push(
        appendQuery(location, { min_data: value[0], max_data: value[1] })
      );
    }
  };

  return (
    <div className={classes.root}>
      <Slider
        max={max_data}
        min={min_data}
        value={value}
        onChange={handleChange}
        onChangeCommitted={handleSubmit}
        valueLabelDisplay="auto"
      />
      <Typography gutterBottom>
        <span>from {value[0]}GB</span>
        <span style={{ float: "right" }}>to {value[1]}GB</span>
      </Typography>
    </div>
  );
};

export default DataFilter;
