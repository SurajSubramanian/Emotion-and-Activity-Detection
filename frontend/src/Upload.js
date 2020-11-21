import React, {useState, useEffect} from 'react';
import {Modal,Button,Alert} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
// matichilok
let img;
let imgWrapper;
let input;
let output;
let outputWrapper;

const validateFile = (event,setSelectedImage,setImageSelected,handleClose) => {
    let extension = event.target.files[0].name.substring(event.target.files[0].name.lastIndexOf('.')+1).toLowerCase();

    if(extension === 'jpg' || extension === 'png' || extension === 'jpeg'){
        img.src = URL.createObjectURL(event.target.files[0]);
        console.log('img: ',event.target.files[0]);
        imgWrapper.style.display = 'block';
        imgWrapper.className = 'col-sm-6';
        setImageSelected(false);
        let file = event.target.files[0];
        let reader = new FileReader();
        reader.onloadend = () => {
            console.log(reader.result);
            setSelectedImage(reader.result);
        }
        reader.readAsDataURL(file);
    }
    else {
    	setImageSelected(true);
    	img.src = '';
        img.style.display = 'none';
        input.value = '';
        handleClose(true);
    }
}

const sendToServer = (image,setImageSelected) => {
    let data = {
        image: image
    };
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        output.src = 'data:image/jpeg;base64,'+data.image;
        outputWrapper.style.display = 'block';
        outputWrapper.className = 'col-sm-6';
        setImageSelected(true);
        input.value = '';
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function Upload() {
	const [imageSelected, setImageSelected] = useState(true);
	const [selectedImage, setSelectedImage] = useState('');
	const [showModal, handleClose] = useState(false);

	useEffect(() => {
		img = document.getElementById('imgElement');
		imgWrapper = document.getElementById('target');
		input = document.getElementById('input');
        output = document.getElementById('imgOutput')
        outputWrapper = document.getElementById('targetOutput');
		console.log(img,imgWrapper);
	},[]);

    return(
    	<div>
			<div className="row justify-content-center align-items-center">
				<div className="col-sm-3">
					<input type="file" id="input" 
						onChange={(event) => {
							validateFile(event,setSelectedImage,setImageSelected,handleClose);
						}} 
					/> 
				</div>
		        <div className="col-sm-2">
		            <button 
		                className="btn btn-primary"
		                disabled={imageSelected}
                        onClick={() => sendToServer(selectedImage,setImageSelected)}
		                >
		                Upload
		            </button>
		        </div>
		    </div>
			<br/>
		    <div className="row justify-content-center align-items-center">
		        <div style={{display: 'none'}} id="target">
                    <div className="row justify-content-center">
                        Before
                    </div>
                    <div className="row justify-content-center">
    			        <img alt="input" id="imgElement" height="300" width="400"></img>
                    </div>
			    </div>
                <div style={{display: 'none'}} id="targetOutput">
                    <div className="row justify-content-center">
                        After
                    </div>
                    <div className="row justify-content-center">
                        <img alt="output" id="imgOutput" height="300" width="400"></img>
                    </div>
                </div>
		    </div>
		    <Modal 
                show={showModal}
                onHide={() => handleClose(false)}
                size="lg"
                aria-labelledby="contained-modal-title-vcenter"
            >
                <Modal.Header closeButton>
                    <Modal.Title>
                    	<Alert variant="danger">
	                        The selected file is not an image. Please select an image.
	                    </Alert>
                    </Modal.Title>
                </Modal.Header>
                <Modal.Footer>
                    <Button variant="secondary" onClick={() => handleClose(false)}>
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>
		</div>
	);
}

export default Upload;