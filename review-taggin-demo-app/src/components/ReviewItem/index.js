import React, { Component } from "react";

export default class index extends Component {
  constructor(props) {
    super(props);
    this.state = {
      review: {},
      filters: []
    };
  }

  componentWillMount() {
    this.setState({ review: this.props.review, filters: this.props.filters });
  }

  render() {
    return (
      <div
        style={{
          fontSize: 14,
          margin: 0,
          marginTop: 10
        }}
      >
        <div className="card">
          <div className="card-body">
            <p>{this.state.review.review}</p>
            <p style={{ fontWeight: "bold" }}>
              {this.state.review.tags.join(" / ")}
            </p>
          </div>
        </div>
      </div>
    );
  }
}
