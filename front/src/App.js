import React, { useState, Component } from "react";

/* My App */
class App extends Component {
  state = {
    posts: [],
    search: "",
  };

  tag = "->";

  async componentDidMount() {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/");
      const posts = await res.json();
      this.setState({
        posts: posts,
      });
    } catch (e) {
      console.log(e);
    }
  }

  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange(e) {
    this.setState({
      search: e.target.value,
    })
    // console.log(this.state.search)
  }

  handleSubmit = async(e) => {
    e.preventDefault();
    await this.componentDidMount();
    /* Search for name */
    const new_posts = this.state.posts.filter(data => data["name"].includes(this.state.search))
    // console.log(new_posts)
    this.setState({
      posts: new_posts,
    });
    // console.log(this.state.posts)
  }

  render() {
    return (
      <div onSubmit={this.searchSubmit}>
        Search: <input type="text" name="myinput" value={this.state.search} onChange={this.handleChange}/>
        <button type="submit" onClick={this.handleSubmit}>GO</button>
        <hr/>
        {this.state.posts.map(item => (
          <div key={item.name}>
            <a href={item.link}>
              <h2>{item.name}</h2>
            </a>
            <h1>{item.discount_percent}</h1>
            <div>
              <span>{item.old_price}</span>
              <span>{this.tag}</span>
              <span>{item.new_price}</span>
            </div>
            <hr/>
          </div>
        ))}
      </div>
    )
  }
}

export default App;