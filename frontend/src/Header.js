import {Jumbotron,Container} from 'react-bootstrap';

export default function Header() {
	return (
		<Jumbotron fluid>
			<Container>
				<h2>Emotion and activity detection</h2>
				<p>
					Upload an image or video or use the camera in real-time.
				</p>
			</Container>
		</Jumbotron>
	);
}