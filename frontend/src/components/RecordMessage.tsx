import { ReactMediaRecorder } from "react-media-recorder"
import { useState } from "react"

import RecordIcon from "./RecordIcon"

type Props = {
  handleStop: any
}

function RecordMessage({ handleStop }: Props) {
  const [recording, setRecording] = useState(false)

  const handleRecording = (
    startRecording: Function,
    stopRecording: Function
  ) => {
    if (recording) {
      stopRecording()
    } else {
      startRecording()
    }
    setRecording(!recording)
  }

  return (
    <ReactMediaRecorder
      audio
      onStop={handleStop}
      render={({ status, startRecording, stopRecording }) => (
        <div className="mt-2">
          <button
            onClick={() => handleRecording(startRecording, stopRecording)}
            className="bg-white p-4 rounded-full"
          >
            <RecordIcon
              classText={
                status == "recording"
                  ? "animate-pulse text-red-500"
                  : "text-sky-500"
              }
            />
          </button>
          <p className="mt-2 text-white font-light">{status}</p>
        </div>
      )}
    />
  )
}

export default RecordMessage
