import React, { Component } from "react";
import ProductList from "./components/ProductsList";
import ProductDetails from "./components/ProductDetails";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      productData: {}
    };
  }
  componentDidMount() {
    fetch("/data/data.json")
      .then(res => res.json())
      .then(data => this.setState({ productData: data }));
  }
  render() {
    return (
      <Router>
        <div className="container">
          <Switch>
            <Route
              path="/products/:productId"
              component={ProductDetails}
            ></Route>
            <Route path="/">
              <ProductList products={this.state.productData}></ProductList>
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
