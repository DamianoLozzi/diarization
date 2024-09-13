from simple_diarizer.diarizer import Diarizer
from typing import TypedDict,Optional
import soundfile as sf

class SegmentDict(TypedDict):
    num: int
    label: int
    start: float
    end: float
    start_sample: float
    end_sample: float
    duration: float
    
class DiarizationDict(TypedDict):
    file_path: str
    sample_rate: int
    channels: int
    duration: float
    format: str
    subtype: str
    total_segments: int
    segments: list[SegmentDict]


class Diarization:
    
    def __init__(self) -> None:
        self.diar: Diarizer = Diarizer(embed_model='xvec', cluster_method='sc')
    
    
    async def diarize_audio(self, file_path: str, num_speakers: Optional[int] =None, threshold: Optional[float]=None) -> dict:
        """This function diarizes an audio file and returns the diarization result

        Args:
            file_path (str): the path to the audio file
            num_speakers (Optional[int], optional): the number of speakers in the audio file. Defaults to None.
            treshold (Optional[float], optional): the treshold for the diarization. Defaults to None.

        Returns:
            dict: the diarization result: file_path, sample_rate, channels, duration, format, subtype, total_segments, segments
        """
        if num_speakers is None and threshold is None:
            raise ValueError("num_speakers or treshold is required")
        
        info= sf.info(file_path)
        
        segments = self.diar.join_samespeaker_segments(
            self.diar.diarize(
                file_path, 
                num_speakers=num_speakers if num_speakers is not None else None, 
                threshold=None if num_speakers is not None else threshold, 
                silence_tolerance=0.5
            )
        )       
        
        diarization_result : DiarizationDict = {
            "file_path": file_path,
            "sample_rate": info.samplerate,
            "channels": info.channels,
            "duration": info.duration,
            "format": info.format,
            "subtype": info.subtype,
            "total_segments": len(segments),
            "segments": []
        }
        
        segment_count = 0
        
        for segment in segments:
            segment_dict: SegmentDict = {
                "num": int(segment_count),
                "label": int(segment['label']),
                "start": float(segment['start']),
                "end": float(segment['end']),
                "start_sample": float(segment['start'] * info.samplerate),
                "end_sample": float(segment['end'] * info.samplerate),
                "duration": float(segment['end'] - segment['start']),
            }
            diarization_result["segments"].append(segment_dict)
            segment_count += 1
            
        return diarization_result
        
        
        
            
