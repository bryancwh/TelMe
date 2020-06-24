import React from "react";
import { useDispatch, useSelector } from "react-redux";
import clsx from "clsx";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import CardHeader from "@material-ui/core/CardHeader";
import CardActions from "@material-ui/core/CardActions";
import Collapse from "@material-ui/core/Collapse";
import Avatar from "@material-ui/core/Avatar";
import IconButton from "@material-ui/core/IconButton";
import { red } from "@material-ui/core/colors";
import FavoriteIcon from "@material-ui/icons/Favorite";
import FavoriteBorderIcon from "@material-ui/icons/FavoriteBorder";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import MoreVertIcon from "@material-ui/icons/MoreVert";
import Grid from "@material-ui/core/grid";
import Tooltip from "@material-ui/core/Tooltip";
import Paper from "@material-ui/core/Paper";

import { Rating } from "@material-ui/lab";

import { updateFavoriteProducts } from "@actions/profileActions/FavoriteProductsActions";

import singtel from "../../../../../public/images/singtel.jpg";
import starhub from "../../../../../public/images/starhub.jpg";
import m1 from "../../../../../public/images/m1.jpg";
import circles from "../../../../../public/images/circles-life.png";
import myrepublic from "../../../../../public/images/myrepublic.jpg";

const useStyles = makeStyles((theme) => ({
  root: {
    maxWidth: 345,
  },
  media: {
    height: 0,
    paddingTop: "56.25%", // 16:9
  },
  expand: {
    transform: "rotate(0deg)",
    marginLeft: "auto",
    transition: theme.transitions.create("transform", {
      duration: theme.transitions.duration.shortest,
    }),
  },
  expandOpen: {
    transform: "rotate(180deg)",
  },
  avatar: {
    backgroundColor: red[500],
  },
  top: {
    paddingTop: "5px",
  },
  bottom: {
    paddingBottom: "5px",
  },
  info: {
    paddingBottom: "15px",
  },
}));

function TelcoRating() {
  const classes = useStyles();
  const [value, setValue] = React.useState(2.5);
  return (
    <Rating
      precision={0.1}
      size="small"
      name="simple-controlled"
      value={value}
      onChange={(event, newValue) => {
        setValue(newValue);
      }}
    />
  );
}

const ProductItem = ({ product, history }) => {
  const classes = useStyles();
  const [expanded, setExpanded] = React.useState(false);
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  const handleAddToFavProducts = () => {
    if (isAuthenticated) {
      dispatch(updateFavoriteProducts(product.id));
      return;
    }
    history.push("/login");
  };

  const getTelcoIconImage = (telco) => {
    switch (telco) {
      case "Singtel":
        return singtel;
      case "Starhub":
        return starhub;
      case "M1":
        return m1;
      case "Circles.Life":
        return circles;
      case "MyRepublic":
        return myrepublic;
      default:
        break;
    }
  };

  return (
    <Card className={classes.root}>
      <CardHeader
        avatar={
          <Avatar
            variant="square"
            aria-label="telco"
            className={classes.avatar}
            src={getTelcoIconImage(product.telco)}
          />
        }
        action={
          <Tooltip title="Visit Site" arrow>
            <IconButton aria-label="settings" href="#">
              <MoreVertIcon />
            </IconButton>
          </Tooltip>
        }
        title={product.title}
        subheader={<TelcoRating />}
      />
      <CardContent>
        <div className={classes.multi}>
          <Grid container spacing={1} className={classes.info}>
            <Grid item md={4}>
              <Paper variant="outlined">
                <Typography
                  variant="body2"
                  color="textSecondary"
                  component="p"
                  align="center"
                  className={classes.top}
                >
                  Data
                </Typography>
                <Typography
                  variant="body2"
                  color="textSecondary"
                  component="p"
                  align="center"
                  className={classes.bottom}
                >
                  {product.data}GB
                </Typography>
              </Paper>
            </Grid>
            <Grid item md={4}>
              <Paper variant="outlined">
                <Typography
                  variant="body2"
                  color="textSecondary"
                  component="p"
                  align="center"
                  className={classes.top}
                >
                  SMS{"\n"}
                </Typography>
                <Typography
                  variant="body2"
                  color="textSecondary"
                  component="p"
                  align="center"
                  className={classes.bottom}
                >
                  {product.sms}
                </Typography>
              </Paper>
            </Grid>
            <Grid item md={4}>
              <Paper variant="outlined">
                <Typography
                  variant="body2"
                  color="textSecondary"
                  component="p"
                  align="center"
                  className={classes.top}
                >
                  Call Time
                </Typography>
                <Typography
                  variant="body2"
                  color="textSecondary"
                  component="p"
                  align="center"
                  className={classes.bottom}
                >
                  {product.call_time + " mins"}
                </Typography>
              </Paper>
            </Grid>
          </Grid>
        </div>
        <Typography
          gutterBottom
          variant="subtitle1"
          color="textSecondary"
          component="h2"
        >
          ${product.price} <small>per mth</small>
        </Typography>
        <Typography
          gutterBottom
          variant="subtitle1"
          color="textSecondary"
          component="h2"
        >
          {product.contract_length} years
        </Typography>
        <Typography variant="body2" color="textSecondary" component="p">
          {product.description}
        </Typography>
      </CardContent>
      <CardActions disableSpacing>
        <IconButton onClick={handleAddToFavProducts} color="secondary">
          {product.is_favorite_product === false ? (
            <FavoriteBorderIcon />
          ) : (
            <FavoriteIcon />
          )}
        </IconButton>
        <IconButton
          className={clsx(classes.expand, {
            [classes.expandOpen]: expanded,
          })}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <ExpandMoreIcon />
        </IconButton>
      </CardActions>
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
          {/* this is for any additional info we may wanna add */}
          <Typography paragraph>Additional Info:</Typography>
          <Typography paragraph>Comes with a $60 voucher</Typography>
          <Typography paragraph>
            Customers who port over their number from another telco get $100 off
          </Typography>
          <Typography paragraph>bl bla bla</Typography>
          <Typography>negative effects</Typography>
        </CardContent>
      </Collapse>
    </Card>
  );
};

export default ProductItem;

{
  /* <div className={classes.root}>
      <Card
        className={classes.height}
        onClick={() => history.push(`/products/${product.slug}`)}
      >
        <CardActionArea className={classes.height}>
          <div>
            <CardMedia
              component="img"
              className={classes.image}
              src={getTelcoIconImage(product.telco)}
              title={product.telco}
            />
          </div>
          <CardContent>
            <Typography noWrap gutterBottom variant="h6" component="h2">
              {product.title}
            </Typography>
            <Typography gutterBottom variant="subtitle1" component="h2">
              ${product.price} {product.contract}years {product.data}GB{" "}
              {product.call_time}mins {product.sms}sms
            </Typography>
            <Typography gutterBottom variant="subtitle1" component="h2">
              {product.description}
            </Typography>
          </CardContent>
        </CardActionArea>
      </Card>
    </div> */
}
