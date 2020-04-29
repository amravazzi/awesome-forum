import React, { useState, useEffect } from 'react';
import { IoMdText, IoMdTime, IoIosThumbsUp } from 'react-icons/io';
import "./styles.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col, Button, Card, Form, InputGroup } from 'react-bootstrap';

export default function App() {
  return (
    <Container style={{ backgroundColor: '#FFF', marginTop: '20px' }}>
      <Row>
        <Col>
          <h1 style={{ marginTop: '20px', marginBottom: '20px'}} >Awesome Forum</h1>
         </Col>
      </Row>

      <Row>
        <Col md="auto">
          <Form.Control type="text" placeholder="Search" />
        </Col>
        <Col md="auto">
          <Form.Control as="select">
            <option>Order by</option>
            <option>Most recent</option>
            <option>Most upvoted</option>
            <option>Not Answered</option>
          </Form.Control>
        </Col>
        <Col>
          <Button style={{ float: 'right' }} variant="primary">New Question</Button>
        </Col>
      </Row>

      <Row style={{ marginTop: '50px' }}>
        <Col>
          <Card style={{ backgroundColor: '#FFF', cursor: 'pointer' }}>
            <Card.Body>
              <Card.Title>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent vitae nulla pretium, euismod neque ut, feugiat est. Curabitur eleifend lacus vel malesuada ornare. Suspendisse volutpat turpis elit, a facilisis orci facilisis sed. Praesent sed nulla non massa tempor tincidunt. Curabitur lobortis ac elit non ullamcorper. Fusce auctor egestas libero. Aliquam vel rutrum tellus. Phasellus ut quam condimentum, tempus tellus vel, faucibus nulla. Duis eu ligula sodales, viverra dolor at, tincidunt elit. Nunc ut pharetra tellus, sit amet euismod quam. Suspendisse aliquet ligula fermentum, suscipit lacus vitae, imperdiet est. In consectetur lacus at dignissim facilisis.</Card.Title>
              <Card.Link>
                <IoIosThumbsUp/>
                <small style={{ marginLeft: '5px' }}>23 upvotes</small>
              </Card.Link>
              <Card.Link>
                <IoMdText/>
                <small style={{ marginLeft: '5px' }}>3 answers</small>
              </Card.Link>
              <Card.Link>
                <IoMdTime/>
                <small style={{ marginLeft: '5px' }}>Last answer 25/03/2020 11:34:22</small>
               </Card.Link>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}
