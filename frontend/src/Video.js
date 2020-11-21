import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

let video;
let videoWrapper;
let localstream;

const startVideo = () => {

    if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
            localstream = stream;
            video.style.display = 'block';
            video.play();
        })
        .catch(function (error) {
            console.log("Something went wrong!",error);
        });
    }
}

const videoOff = () => {
	video.pause();
	video.src = "";
	localstream.getTracks()[0].stop();
    video.style.display = "none";
    videoWrapper.style.className = "";
}

function VideoElement() {
    const [isClicked, setIsClicked] = useState(false);

   	useEffect(() => {
   		video = document.getElementById('videoElement');
   		videoWrapper = document.getElementById('target');
   		console.log(video, videoWrapper);
   	});

	return(
		<div className="row justify-content-center align-items-center">
            <div id="target">
            	<canvas id="sketchpad"></canvas>
		        <video style={{display: 'none'}} autoplay="true" id="videoElement"></video>
		    </div>
            <div className="col-sm-2">
            	{!isClicked?
	                <button 
	                    className="btn btn-primary" 
	                    onClick={() => {
	                        setIsClicked(true);
	                        startVideo();
	                        videoWrapper.style.className = "col-sm-8";
	                    }}>
	                    Open camera
	                </button>:
	                <button 
	                    className="btn btn-primary" 
	                    onClick={() => {
	                        setIsClicked(false);
	                        videoOff();
	                    }}>
	                    Close camera
	                </button>
	            }
            </div>
        </div>
	);
}

export default VideoElement;