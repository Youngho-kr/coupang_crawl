import React, { Component } from "react";

/* My App */
class App extends Component {
  state = {
    posts: []
  };

  async componentDidMount() {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/");
      const posts = await res.json();
      this.setState({
        posts
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.posts.map(item => (
          <div key={item.id}>
            <h1>{item.name}</h1>
            <span>{item.old_price}</span>
          </div>
        ))}
      </div>
    )
  }
}

export default App;