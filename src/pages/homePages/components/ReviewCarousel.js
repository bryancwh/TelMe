import React from "react";
import Carousel from "react-material-ui-carousel";
import autoBind from "auto-bind";

import "../style/carousel.css";
import m1apple from "@public/images/m1promo.jpg";
import m1huawei from "@public/images/m1promo2.jpg";

import {
  Card,
  CardContent,
  CardMedia,
  Typography,
  Grid,
  Button,
} from "@material-ui/core";

function Banner(props) {
  if (props.newProp) console.log(props.newProp);
  const contentPosition = props.contentPosition
    ? props.contentPosition
    : "left";
  const totalItems = props.length ? props.length : 3;
  const mediaLength = totalItems - 1;

  let items = [];
  const content = (
    <Grid item xs={12 / totalItems} key="content">
      <CardContent className="Content">
        <Typography className="Title">{props.item.Name}</Typography>

        <Typography className="Caption">{props.item.Caption}</Typography>

        <Button variant="outlined" className="ViewButton">
          View Now
        </Button>
      </CardContent>
    </Grid>
  );

  for (let i = 0; i < mediaLength; i++) {
    const item = props.item.Items[i];

    const media = (
      <Grid item xs={12 / totalItems} key={item.Name}>
        <CardMedia className="Media" image={item.Image} title={item.Name}>
          {/* <Typography className="MediaCaption">{item.Name}</Typography> */}
        </CardMedia>
      </Grid>
    );

    items.push(media);
  }

  if (contentPosition === "left") {
    items.unshift(content);
  } else if (contentPosition === "right") {
    items.push(content);
  } else if (contentPosition === "middle") {
    items.splice(items.length / 2, 0, content);
  }

  return (
    <Card raised className="Banner">
      <Grid container spacing={0} className="BannerGrid">
        {items}
      </Grid>
    </Card>
  );
}

const items = [
  {
    Name: "Mobile Plans",
    Caption: "The latest deals!",
    contentPosition: "left",
    Items: [
      {
        Name: "M1 iPhone 11 Pro Max",
        Image: m1apple,
      },
      {
        Name: "M1 HuaWei nova 7 SE",
        Image: m1huawei,
      },
    ],
  },
  {
    Name: "Home Appliances",
    Caption: "Say no to manual home labour!",
    contentPosition: "middle",
    Items: [
      {
        Name: "Washing Machine WX9102",
        Image: "https://source.unsplash.com/featured/?washingmachine",
      },
      {
        Name: "Learus Vacuum Cleaner",
        Image: "https://source.unsplash.com/featured/?vacuum,cleaner",
      },
    ],
  },
  {
    Name: "Decoratives",
    Caption: "Give style and color to your living room!",
    contentPosition: "right",
    Items: [
      {
        Name: "Living Room Lamp",
        Image: "https://source.unsplash.com/featured/?lamp",
      },
      {
        Name: "Floral Vase",
        Image: "https://source.unsplash.com/featured/?vase",
      },
    ],
  },
];

class ReviewCarousel extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      autoPlay: false,
      timer: 500,
      animation: "slide",
      indicators: false,
      timeout: 200,
      navButtonsAlwaysVisible: true,
    };

    autoBind(this);
  }

  render() {
    return (
      <div style={{ marginBottom: "50px", color: "#494949" }}>
        {/* <h2>What others are saying</h2> */}

        <Carousel
          className="Example"
          autoPlay={this.state.autoPlay}
          timer={this.state.timer}
          animation={this.state.animation}
          indicators={this.state.indicators}
          timeout={this.state.timeout}
          navButtonsAlwaysVisible={this.state.navButtonsAlwaysVisible}
        >
          {items.map((item, index) => {
            return (
              <Banner
                item={item}
                key={index}
                contentPosition={item.contentPosition}
              />
            );
          })}
        </Carousel>
      </div>
    );
  }
}

export default ReviewCarousel;