import React, { Component } from "react";
import { Link, useParams } from "react-router-dom";

export default class index extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    let products = this.props.products;
    let listItems;
    if (products.length > 0) {
      listItems = products.map(product => (
        <Link
          type="button"
          className="list-group-item list-group-item-action"
          to={`/products/${product.productId}`}
          key={product.productId}
        >
          {product.productName}
        </Link>
      ));
    }
    return (
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center"
        }}
      >
        <h1>Products List</h1>
        <div style={{ marginTop: 20 }}>
          <div className="list-group">{listItems}</div>
        </div>
      </div>
    );
  }
}
