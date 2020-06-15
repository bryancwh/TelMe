import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Swiper from "react-id-swiper";
import "swiper/css/swiper.css";

import singtel from "../../../../../public/images/singtel.jpg";
import starhub from "../../../../../public/images/starhub.jpg";
import m1 from "../../../../../public/images/m1.jpg";
import circles from "../../../../../public/images/circles-life.png";
import myrepublic from "../../../../../public/images/myrepublic.jpg";

const useStyles = makeStyles((theme) => ({
  image: {
    width: "100%",
    height: "100%",
    maxHeight: "500px",
    display: "block",
    margin: "0 auto",
    objectFit: "contain",
  },
}));

const ProductImages = ({ product }) => {
  const classes = useStyles();

  // List of just available product photos (remove nulls)

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

  const params = {
    spaceBetween: 30,
    rebuildOnUpdate: true,
    pagination: {
      el: ".swiper-pagination",
      type: "fraction",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  };

  return (
    <Swiper {...params}>
      <div key={product.id}>
        <img
          src={getTelcoIconImage(product.telco)}
          alt={product.telco}
          className={classes.image}
        />
      </div>
    </Swiper>
  );
};

export default ProductImages;
