# @ohos.multimedia.media

媒体子系统为开发者提供一套简单且易于理解的接口，使得开发者能够方便接入系统并使用系统的媒体资源。

**起始版本：** 6

**系统能力：** 
- API版本12+：SystemCapability.Multimedia.Media.Core

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createAudioPlayer](arkts-media-media-createaudioplayer-f.md) |
| [createAudioRecorder](arkts-media-media-createaudiorecorder-f.md) |
| [createAVAdsController](arkts-media-media-createavadscontroller-f.md) |
| [createAVDownloaderManager](arkts-media-media-createavdownloadermanager-f.md) |
| [createAVImageGenerator](arkts-media-media-createavimagegenerator-f.md) |
| [createAVImageGenerator](arkts-media-media-createavimagegenerator-f.md) |
| [createAVMetadataExtractor](arkts-media-media-createavmetadataextractor-f.md) |
| [createAVMetadataExtractor](arkts-media-media-createavmetadataextractor-f.md) |
| [createAVPlayer](arkts-media-media-createavplayer-f.md) |
| [createAVPlayer](arkts-media-media-createavplayer-f.md) |
| [createAVRecorder](arkts-media-media-createavrecorder-f.md) |
| [createAVRecorder](arkts-media-media-createavrecorder-f.md) |
| [createAVScreenCaptureRecorder](arkts-media-media-createavscreencapturerecorder-f.md) |
| [createAVTranscoder](arkts-media-media-createavtranscoder-f.md) |
| [createMediaSourceWithDataSource](arkts-media-media-createmediasourcewithdatasource-f.md) |
| [createMediaSourceWithDirectory](arkts-media-media-createmediasourcewithdirectory-f.md) |
| [createMediaSourceWithFd](arkts-media-media-createmediasourcewithfd-f.md) |
| [createMediaSourceWithStreamData](arkts-media-media-createmediasourcewithstreamdata-f.md) |
| [createMediaSourceWithUrl](arkts-media-media-createmediasourcewithurl-f.md) |
| [createSoundPool](arkts-media-media-createsoundpool-f.md) |
| [createSoundPool](arkts-media-media-createsoundpool-f.md) |
| [createVideoPlayer](arkts-media-media-createvideoplayer-f.md) |
| [createVideoPlayer](arkts-media-media-createvideoplayer-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createParallelSoundPool](arkts-media-media-createparallelsoundpool-f-sys.md) |
| [createVideoRecorder](arkts-media-media-createvideorecorder-f-sys.md) |
| [createVideoRecorder](arkts-media-media-createvideorecorder-f-sys.md) |
| [getAVScreenCaptureConfigurableParameters](arkts-media-media-getavscreencaptureconfigurableparameters-f-sys.md) |
| [getScreenCaptureMonitor](arkts-media-media-getscreencapturemonitor-f-sys.md) |
| [reportAVScreenCaptureUserChoice](arkts-media-media-reportavscreencaptureuserchoice-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AudioPlayer](arkts-media-media-audioplayer-i.md) |
| [AudioRecorder](arkts-media-media-audiorecorder-i.md) |
| [AudioRecorderConfig](arkts-media-media-audiorecorderconfig-i.md) |
| [AVAdsController](arkts-media-media-avadscontroller-i.md) |
| [AVDataSrcDescriptor](arkts-media-media-avdatasrcdescriptor-i.md) |
| [AVDownloaderManager](arkts-media-media-avdownloadermanager-i.md) |
| [AVFileDescriptor](arkts-media-media-avfiledescriptor-i.md) |
| [AVImageGenerator](arkts-media-media-avimagegenerator-i.md) |
| [AVMetadata](arkts-media-media-avmetadata-i.md) |
| [AVMetadataExtractor](arkts-media-media-avmetadataextractor-i.md) |
| [AVMetricsEvent](arkts-media-media-avmetricsevent-i.md) |
| [AVPlayer](arkts-media-media-avplayer-i.md) |
| [AVRecorder](arkts-media-media-avrecorder-i.md) |
| [AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md) |
| [AVRecorderProfile](arkts-media-media-avrecorderprofile-i.md) |
| [AVScreenCaptureRecordConfig](arkts-media-media-avscreencapturerecordconfig-i.md) |
| [AVScreenCaptureRecorder](arkts-media-media-avscreencapturerecorder-i.md) |
| [AVScreenCaptureStrategy](arkts-media-media-avscreencapturestrategy-i.md) |
| [AVTimedMetaData](arkts-media-media-avtimedmetadata-i.md) |
| [AVTranscoder](arkts-media-media-avtranscoder-i.md) |
| [AVTranscoderConfig](arkts-media-media-avtranscoderconfig-i.md) |
| [EncoderInfo](arkts-media-media-encoderinfo-i.md) |
| [FrameInfo](arkts-media-media-frameinfo-i.md) |
| [Location](arkts-media-media-location-i.md) |
| [MediaDescription](arkts-media-media-mediadescription-i.md) |
| [MediaSource](arkts-media-media-mediasource-i.md) |
| [MediaSourceLoader](arkts-media-media-mediasourceloader-i.md) |
| [MediaSourceLoadingRequest](arkts-media-media-mediasourceloadingrequest-i.md) |
| [MediaStream](arkts-media-media-mediastream-i.md) |
| [OutputSize](arkts-media-media-outputsize-i.md) |
| [PixelMapParams](arkts-media-media-pixelmapparams-i.md) |
| [PlaybackInfo](arkts-media-media-playbackinfo-i.md) |
| [PlaybackStrategy](arkts-media-media-playbackstrategy-i.md) |
| [Range](arkts-media-media-range-i.md) |
| [SeiMessage](arkts-media-media-seimessage-i.md) |
| [SubtitleInfo](arkts-media-media-subtitleinfo-i.md) |
| [TrackSelectionFilter](arkts-media-media-trackselectionfilter-i.md) |
| [VideoPlayer](arkts-media-media-videoplayer-i.md) |
| [VideoSize](arkts-media-media-videosize-i.md) |
| [WatermarkConfiguration](arkts-media-media-watermarkconfiguration-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AVMetadata](arkts-media-media-avmetadata-i-sys.md) |
| [AVMetadataExtractor](arkts-media-media-avmetadataextractor-i-sys.md) |
| [AVPlayer](arkts-media-media-avplayer-i-sys.md) |
| [AVRecorder](arkts-media-media-avrecorder-i-sys.md) |
| [AVRecorderConfig](arkts-media-media-avrecorderconfig-i-sys.md) |
| [AVRecorderProfile](arkts-media-media-avrecorderprofile-i-sys.md) |
| [AVScreenCaptureStrategy](arkts-media-media-avscreencapturestrategy-i-sys.md) |
| [PixelMapParams](arkts-media-media-pixelmapparams-i-sys.md) |
| [PlaybackStrategy](arkts-media-media-playbackstrategy-i-sys.md) |
| [ScreenCaptureMonitor](arkts-media-media-screencapturemonitor-i-sys.md) |
| [VideoRecorder](arkts-media-media-videorecorder-i-sys.md) |
| [VideoRecorderConfig](arkts-media-media-videorecorderconfig-i-sys.md) |
| [VideoRecorderProfile](arkts-media-media-videorecorderprofile-i-sys.md) |
| [WatermarkConfig](arkts-media-media-watermarkconfig-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AacProfile](arkts-media-media-aacprofile-e.md) |
| [AudioEncoder](arkts-media-media-audioencoder-e.md) |
| [AudioOutputFormat](arkts-media-media-audiooutputformat-e.md) |
| [AudioSourceType](arkts-media-media-audiosourcetype-e.md) |
| [AVErrorCode](arkts-media-media-averrorcode-e.md) |
| [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) |
| [AVMetricsEventType](arkts-media-media-avmetricseventtype-e.md) |
| [AVMimeTypes](arkts-media-media-avmimetypes-e.md) |
| [AVScreenCaptureFillMode](arkts-media-media-avscreencapturefillmode-e.md) |
| [AVScreenCaptureRecordPreset](arkts-media-media-avscreencapturerecordpreset-e.md) |
| [AVScreenCaptureStateCode](arkts-media-media-avscreencapturestatecode-e.md) |
| [BufferingInfoType](arkts-media-media-bufferinginfotype-e.md) |
| [CodecMimeType](arkts-media-media-codecmimetype-e.md) |
| [ContainerFormatType](arkts-media-media-containerformattype-e.md) |
| [FetchResult](arkts-media-media-fetchresult-e.md) |
| [FileGenerationMode](arkts-media-media-filegenerationmode-e.md) |
| [HdrType](arkts-media-media-hdrtype-e.md) |
| [LoadingRequestError](arkts-media-media-loadingrequesterror-e.md) |
| [MediaDescriptionKey](arkts-media-media-mediadescriptionkey-e.md) |
| [MediaErrorCode](arkts-media-media-mediaerrorcode-e.md) |
| [MediaType](arkts-media-media-mediatype-e.md) |
| [PickerMode](arkts-media-media-pickermode-e.md) |
| [PlaybackInfoKey](arkts-media-media-playbackinfokey-e.md) |
| [PlaybackMetricsKey](arkts-media-media-playbackmetricskey-e.md) |
| [PlaybackSpeed](arkts-media-media-playbackspeed-e.md) |
| [PlaylistLoopMode](arkts-media-media-playlistloopmode-e.md) |
| [SeekMode](arkts-media-media-seekmode-e.md) |
| [SoundInterruptMode](arkts-media-media-soundinterruptmode-e.md) |
| [StateChangeReason](arkts-media-media-statechangereason-e.md) |
| [SwitchMode](arkts-media-media-switchmode-e.md) |
| [VideoScaleType](arkts-media-media-videoscaletype-e.md) |
| [VideoSourceType](arkts-media-media-videosourcetype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [AVErrorCode](arkts-media-media-averrorcode-e-sys.md) |
| [MetaSourceType](arkts-media-media-metasourcetype-e-sys.md) |
| [PixelFormat](arkts-media-media-pixelformat-e-sys.md) |
| [ScreenCaptureEvent](arkts-media-media-screencaptureevent-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [AudioState](arkts-media-media-audiostate-t.md) |
| [AVDownloadTaskState](arkts-media-media-avdownloadtaskstate-t.md) |
| [AVPlayerState](arkts-media-media-avplayerstate-t.md) |
| [AVRecorderState](arkts-media-media-avrecorderstate-t.md) |
| [OnAdsEventAdsStartedHandle](arkts-media-media-onadseventadsstartedhandle-t.md) |
| [OnAdsEventLoadingErrorHandle](arkts-media-media-onadseventloadingerrorhandle-t.md) |
| [OnAVDownloadProgressChangeHandle](arkts-media-media-onavdownloadprogresschangehandle-t.md) |
| [OnAVDownloadTaskStateHandle](arkts-media-media-onavdownloadtaskstatehandle-t.md) |
| [OnAVPlayerStateChangeHandle](arkts-media-media-onavplayerstatechangehandle-t.md) |
| [OnAVRecorderStateChangeHandler](arkts-media-media-onavrecorderstatechangehandler-t.md) |
| [OnBufferingUpdateHandler](arkts-media-media-onbufferingupdatehandler-t.md) |
| [OnFrameFetched](arkts-media-media-onframefetched-t.md) |
| [OnPlaybackRateDone](arkts-media-media-onplaybackratedone-t.md) |
| [OnSeiMessageHandle](arkts-media-media-onseimessagehandle-t.md) |
| [OnSuperResolutionChanged](arkts-media-media-onsuperresolutionchanged-t.md) |
| [OnTrackChangeHandler](arkts-media-media-ontrackchangehandler-t.md) |
| [OnVideoSizeChangeHandler](arkts-media-media-onvideosizechangehandler-t.md) |
| [PlaybackMetrics](arkts-media-media-playbackmetrics-t.md) |
| [PlayParameters](arkts-media-media-playparameters-t.md) |
| [SoundPool](arkts-media-media-soundpool-t.md) |
| [SourceCloseCallback](arkts-media-media-sourceclosecallback-t.md) |
| [SourceOpenCallback](arkts-media-media-sourceopencallback-t.md) |
| [SourceReadCallback](arkts-media-media-sourcereadcallback-t.md) |
| [VideoPlayState](arkts-media-media-videoplaystate-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [VideoRecordState](arkts-media-media-videorecordstate-t-sys.md) |
<!--DelEnd-->
