import React from "react";

import MyExpansionPanel from "@components/layouts/MyExpansionPanel";
import PriceFilter from "./PriceFilter";
import DataFilter from "./DataFilter";
import ContractFilter from "./ContractFilter";
import SearchInResults from "./SearchInResults";
import SubmittedFilters from "./SubmittedFilters";

const Filters = () => {
  return (
    <React.Fragment>
      <SubmittedFilters />
      <SearchInResults />
        <MyExpansionPanel title="Price range">
          <PriceFilter />
        </MyExpansionPanel>
        <MyExpansionPanel title="Data range">
          <DataFilter />
        </MyExpansionPanel>
        <MyExpansionPanel title="Contract Length range">
          <ContractFilter />
        </MyExpansionPanel>
    </React.Fragment>
  );
};

export default Filters;
