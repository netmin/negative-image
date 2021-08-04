import React from 'react';

const AddImage = (props) => {
  return (
    <form onSubmit={(event) => props.addUser(event)}>
      <div className="field">
        <label
          className="label is-large"
          htmlFor="input-image"
        >Image</label>
        <input
          name="image"
          id="input-image"
          className="input is-large"
          type="file"
          placeholder="Choice file"
          required
          onChange={props.handleChange}
        />
      </div>
      <input
        type="submit"
        className="button is-primary is-large is-fullwidth"
        value="Submit"
      />
    </form>
  )
};

export default AddImage;
