import React, { Component } from "react";
import ReviewItem from "../ReviewItem";

export default class index extends Component {
  constructor(props) {
    super(props);
    this.state = {
      reviews: [],
      filters: {},
      category: "",
      appliedFilters: []
    };
  }

  mostFrequentElement(array) {
    if (array.length == 0) return null;
    var modeMap = {};
    var maxEl = array[0],
      maxCount = 1;
    for (var i = 0; i < array.length; i++) {
      var el = array[i];
      if (modeMap[el] == null) modeMap[el] = 1;
      else modeMap[el]++;
      if (modeMap[el] > maxCount) {
        maxEl = el;
        maxCount = modeMap[el];
      }
    }
    return maxEl;
  }

  findCategory() {
    let alltags = [];
    this.state.reviews.forEach(r => (alltags = alltags.concat(r.tags)));
    return this.mostFrequentElement(alltags);
  }

  componentWillReceiveProps(newProps) {
    this.setState({ reviews: newProps.reviews }, () => {
      fetch("/data/common-tags.json")
        .then(res => res.json())
        .then(data => {
          const category = this.findCategory();
          this.setState({ filters: data[category] });
        });
    });
  }

  onFilterButtonClick(filter) {
    let appliedFilters = this.state.appliedFilters;

    if (!appliedFilters.includes(filter)) {
      appliedFilters.push(filter);
    } else {
      var index = appliedFilters.indexOf(filter);
      if (index > -1) {
        appliedFilters.splice(index, 1);
      }
    }

    this.setState({ appliedFilters });
  }

  isApplicable(tags) {
    const filters = this.state.appliedFilters;

    if (filters.length == 0) return true;
    for (let i = 0; i < filters.length; i++) {
      if (tags.includes(filters[i])) {
        return true;
      }
    }
    return false;
  }

  render() {
    let reviewsSection = this.state.reviews.map(review => {
      if (this.isApplicable(review.tags)) {
        return (
          <ReviewItem
            review={review}
            filters={this.state.appliedFilters}
            key={review.review}
          ></ReviewItem>
        );
      }
    });

    let buttonClass;
    let tagsSection;
    if (this.state.filters.length > 0) {
      tagsSection = this.state.filters.map(filter => {
        let appliedFilters = this.state.appliedFilters;
        if (appliedFilters.includes(filter)) {
          buttonClass = "btn btn-primary btn-sm";
        } else {
          buttonClass = "btn btn-sm btn-outline-primary";
        }

        return (
          <button
            style={{ marginLeft: 10 }}
            type="button"
            className={buttonClass}
            key={filter}
            onClick={() => this.onFilterButtonClick(filter)}
          >
            {filter}
          </button>
        );
      });
    }

    return (
      <div>
        <h2>Reviews</h2>
        {tagsSection}
        <div></div>
        {reviewsSection}
      </div>
    );
  }
}
