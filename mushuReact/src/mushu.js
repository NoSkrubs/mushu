//Component
import React, { Component } from 'react';
import logo from './logo.svg';
import { Link, IndexLink } from 'react-router-dom'

//CSS
import './mushu.css';

class Mushu extends Component {
  render() {
    return (
    <div>
      <header>
        <p className="logo"><img src="mushuGong.gif" alt="mushu shadow" style={{"width" : "50%"}}/></p>
        <h1>Mushu:</h1>
        <h2>A Sentiment Analysor for Amazon</h2>
        <nav>
          <ul>
            <a href="Mushuhome.html"><li>Home</li></a>
            <a href="aboutMushu.html"><li>About</li></a>
            <li className="currentPage">Review</li>
            <li>News</li>
            <li>Contact</li>
            <li>
              <form>
                <fieldset>
                  <legend>Check an Amazon Review</legend>
                  <input type="text" name="url" placeholder="Enter URL Here"/>
                  <input type="submit" value="search"/>
                </fieldset>
              </form>
            </li>
          </ul>
        </nav>
      </header>
      <aside>
        <h3>Departments</h3>
        <ul className="departments">
          <li>Movies</li>
          <li>Clothing</li>
          <li>Food</li>
          <li>Home</li>
          <li>Misc.</li>
        </ul>
      </aside>
      <content>
        <h2>Object Title</h2>
        <p className="img">The Image of the object would go here</p>
        <p className="desc">price and maybe its descripion</p>
        <div className="findings">
          <table>
            <tr>
              <th>Star Rating</th>
              <th>Sentiment Rating</th>
              <th>Difference</th>
            </tr>
            <tr>
              <td>2.54</td>
              <td>3.45</td>
              <td>1.43</td>
            </tr>
          </table>
          <p>You could also have a scale and put markeres where it lines up on the scale with js. This would be for later. Aslo I can make it so that thwhen you scroll over one of the data pieces it hieghlights the data that made it that wayon the articles or something like that. </p>
        </div>
        <div className="reviews">
          <article>
            <h3 className="l1">title of review</h3>
            <div className="ratings">
              <p>The user star rating and the sentiment rating maybe some other data to compare it too.</p>
            </div>
            <p>The review's content</p>
            <ul className="reviewComments">
              <li>Comments(to figure out what they think accounts for the difference)</li>
              <li>See on Amazon</li>
              <li>Send to us</li>
              <li>Vote on whih review you think is more accurate</li>
            </ul>
          </article>
          <article>
            <h3 className="l1">title of review</h3>
            <div className="ratings">
              <p>The user star rating and the sentiment rating maybe some other data to compare it too.</p>
            </div>
            <p>The review's content</p>
            <ul className="reviewComments">
              <li>Comments(to figure out what they think accounts for the difference)</li>
              <li>See on Amazon</li>
              <li>Send to us</li>
              <li>Vote on whih review you think is more accurate</li>
            </ul>
          </article>
          <article>
            <h3 className="l1">title of review</h3>
            <div className="ratings">
              <p>The user star rating and the sentiment rating maybe some other data to compare it too.</p>
            </div>
            <p>The review's content</p>
            <ul className="reviewComments">
              <li>Comments(to figure out what they think accounts for the difference)</li>
              <li>See on Amazon</li>
              <li>Send to us</li>
              <li>Vote on whih review  you think is more accurate</li>
            </ul>
          </article>
          <article>
            <h3 className="l1">title of review</h3>
            <div className="ratings">
              <p>The user star rating and the sentiment rating maybe some other data to compare it too.</p>
            </div>
            <p>The review's content</p>
            <ul className="reviewComments">
              <li>Comments(to figure out what they think accounts for the difference)</li>
              <li>See on Amazon</li>
              <li>Send to us</li>
              <li>Vote on whih review  you think is more accurate</li>
            </ul>
          </article>
          <article>
            <h3 className="l1">title of review</h3>
            <div className="ratings">
              <p>The user star rating and the sentiment rating maybe some other data to compare it too.</p>
            </div>
            <p>The review's content</p>
            <ul className="reviewComments">
              <li>Comments(to figure out what they think accounts for the difference)</li>
              <li>See on Amazon</li>
              <li>Send to us</li>
              <li>Vote on whih review you think is more accurate</li>
            </ul>
          </article>
        </div>
        <h2>This would be so that they could send us interesting stats.</h2>
        <p>note:I will also put a little button on each article so that they can either link it or send it from that article. This is just so that we have another set of eyes looking over what could be missing from out data. </p>
      </content>
    </div>
    );
  }
}
export default Mushu;
