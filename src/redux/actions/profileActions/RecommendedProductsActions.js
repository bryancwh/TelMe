import axios from "axios";

import {
  FETCH_RECOMMENDED_PRODUCTS,
  START_LOADING_UI,
  STOP_LOADING_UI
} from "../../types";

export const fetchRecommendedProducts = () => dispatch => {
  dispatch({ type: START_LOADING_UI });
  axios.get("/api/user/recommended-products/").then(response => {
    dispatch({ type: FETCH_RECOMMENDED_PRODUCTS, payload: response.data });
    dispatch({ type: STOP_LOADING_UI });
  });
};
