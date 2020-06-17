import React from "react";
import Grid from "@material-ui/core/Grid";

import PersonalInfo from "../personalInfo";
import Sidebar from "../Sidebar";

const Profile = () => {
  return (
      <Grid container spacing={2}>
        <Grid item md>
          <PersonalInfo />
        </Grid>
      </Grid>
  );
};

export default Profile;
