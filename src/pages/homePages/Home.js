import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import CssBaseline from "@material-ui/core/CssBaseline";
import Grid from "@material-ui/core/Grid";
import Container from "@material-ui/core/Container";

import MainFeaturedPost from "./components/MainFeaturedPost";
import FeaturedPost from "./components/FeaturedPost";
import ReviewCarousel from "./components/ReviewCarousel";

const useStyles = makeStyles((theme) => ({
  mainGrid: {
    marginTop: theme.spacing(3),
  },
}));

//these are hardcoded before the review feature is added in
const featuredPosts = [
  {
    title: "Does Your Telco Have The Cheapest Data Roaming Plan?",
    date: "22 Nov 2019",
    description:
      "In this day and age, we all need to stay connected. And in order to do so, we all need mobile data." +
      " Even if you’re not a social media addict, I’m sure you’ll still need to be able" +
      " to contact someone while you’re miles away from home?" +
      " And no, it’s not always possible to just rely on WiFi…",
    link:
      "https://blog.seedly.sg/data-roaming-travel-guide-singaporean-m1-singtel-starhub-circles-life-myrepublic?utm_source=product&utm_medium=banner&utm_campaign=experiment",
  },
  {
    title: "Best (And Cheapest) Unlimited Data Mobile Plan In Singapore 2019",
    date: "26 Apr 2019",
    description:
      "After Circles.Life, Zero probably offers the next best-value," +
      " unlimited data plan through the Zero Xs Unlimited Date ($39.95 per month)" +
      " which comes with a 45GB cap for 4G data. If you want to get unlimited talktime and SMS," +
      " it’ll cost you $10 more for the Zero X Unlimited Everything.",
    link: "https://blog.seedly.sg/best-unlimited-data-mobile-plan-singapore/",
  },
];

export default function Home() {
  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="lg">
        <main>
          <MainFeaturedPost />
          <h2>Featured</h2>
          <ReviewCarousel />

          <h2>Trending topics</h2>
          <Grid container spacing={4}>
            {featuredPosts.map((post) => (
              <FeaturedPost key={post.title} post={post} />
            ))}
          </Grid>
          <Grid container spacing={5} className={classes.mainGrid}></Grid>
        </main>
      </Container>
    </React.Fragment>
  );
}
