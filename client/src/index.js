import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from "axios";

import AddImage from './components/AddImage';

class App extends Component {
  constructor() {
    super();
    this.state = {
      images: [],
      image: "",

    };
    this.addImage = this.addImage.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }
  componentDidMount() {
    this.getImages();
  };

  handleChange(event) {
    const obj = {};
    obj[event.target.name] = event.target.files[0];
    console.log("Object", obj)
    this.setState(obj);
  };


  getImages() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/image`)
        .then((res) => { this.setState({ images: res.data }); })
        .catch((err) => {
          console.log(err);
        });
  };
  addImage(event) {
    event.preventDefault();
    // const data = {original: this.state.image}
    // console.log(data)
    const formData = new FormData();
    formData.append("original", this.state.image);

    axios.post(
        `${process.env.REACT_APP_USERS_SERVICE_URL}/image`,
        formData,
        { headers: {"Content-Type": "multipart/form-data", "Accept": "multipart/form-data"} })
        .then((res) => {
          this.getImages()
          this.setState({ image: ""})
        })
        .catch((err) => { console.log(err); });


  };

  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-full">
              <br/>
              <h1 className="title is-1">Images</h1>
              <hr/><br/>
              <AddImage
                  image={this.state.image}
                  addUser={this.addImage}
                  handleChange={this.handleChange}
              />
              <br/><br/>
            {
              this.state.images.map((img) => {
                return (
                    <div className="box" key={img.id}>
                      <article className="media">
                        <div className="media-content">
                          <figure className="image is-64x64">
                            <img src={img.negative_url} alt="Img" />
                          </figure>
                        </div>
                        <div className="media-content">
                          <figure className="image is-64x64">
                            <img src={img.original_url} alt="Img" />
                          </figure>
                        </div>
                      </article>
                    </div>
                )
              })
            }

            </div>
          </div>
        </div>
      </section>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
