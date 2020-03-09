import React from 'react';
import ReactDOM from 'react-dom';
import {Container, Card} from 'react-bootstrap';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";


class App extends React.Component {
    render() {
        return (
            <Router>
            <Container>
                <Navbar/>
                <Card>
                    <Switch>
                        <Route path="/admin/extra/bulk-predicted-task">
                            <Card.Body>
                                <h1>Predicted Tasks</h1>
                                <hr/>
                            </Card.Body>
                        </Route>
                        <Route path="/admin/extra/bulk-notification">
                            <Card.Body>
                                <h1>Notifications</h1>
                                <hr/>
                            </Card.Body>
                        </Route>
                      <Route path="/">
                      </Route>
                    </Switch>
                </Card>
            </Container>
            </Router>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('react-app'));
