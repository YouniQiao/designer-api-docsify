# media

媒体子系统为开发者提供一套简单且易于理解的接口，使得开发者能够方便接入系统并使用系统的媒体资源。

**起始版本：** 6

<!--Device-unnamed-declare namespace media--><!--Device-unnamed-declare namespace media-End-->

**系统能力：** 
- API版本12+：SystemCapability.Multimedia.Media.Core

## 汇总

### 函数

| 名称 |
| --- |
| [createAVPlayer](arkts-media-media-createavplayer-f.md#createavplayer) |
| [createAVPlayer](arkts-media-media-createavplayer-f.md#createavplayer-1) |
| [createAVRecorder](arkts-media-media-createavrecorder-f.md#createavrecorder) |
| [createAVRecorder](arkts-media-media-createavrecorder-f.md#createavrecorder-1) |
| [createAudioPlayer](arkts-media-media-createaudioplayer-f.md#createaudioplayer) |
| [createAudioRecorder](arkts-media-media-createaudiorecorder-f.md#createaudiorecorder) |
| [createMediaSourceWithFd](arkts-media-media-createmediasourcewithfd-f.md#createmediasourcewithfd) |
| [createMediaSourceWithDataSource](arkts-media-media-createmediasourcewithdatasource-f.md#createmediasourcewithdatasource) |
| [createMediaSourceWithUrl](arkts-media-media-createmediasourcewithurl-f.md#createmediasourcewithurl) |
| [createMediaSourceWithStreamData](arkts-media-media-createmediasourcewithstreamdata-f.md#createmediasourcewithstreamdata) |
| [createVideoPlayer](arkts-media-media-createvideoplayer-f.md#createvideoplayer) |
| [createVideoPlayer](arkts-media-media-createvideoplayer-f.md#createvideoplayer-1) |
| [createSoundPool](arkts-media-media-createsoundpool-f.md#createsoundpool) |
| [createSoundPool](arkts-media-media-createsoundpool-f.md#createsoundpool-1) |
| [createAVScreenCaptureRecorder](arkts-media-media-createavscreencapturerecorder-f.md#createavscreencapturerecorder) |
| [createAVTranscoder](arkts-media-media-createavtranscoder-f.md#createavtranscoder) |
| [createAVMetadataExtractor](arkts-media-media-createavmetadataextractor-f.md#createavmetadataextractor) |
| [createAVMetadataExtractor](arkts-media-media-createavmetadataextractor-f.md#createavmetadataextractor-1) |
| [createAVImageGenerator](arkts-media-media-createavimagegenerator-f.md#createavimagegenerator) |
| [createAVImageGenerator](arkts-media-media-createavimagegenerator-f.md#createavimagegenerator-1) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createVideoRecorder](arkts-media-media-createvideorecorder-f-sys.md#createvideorecorder) |
| [createVideoRecorder](arkts-media-media-createvideorecorder-f-sys.md#createvideorecorder-1) |
| [createParallelSoundPool](arkts-media-media-createparallelsoundpool-f-sys.md#createparallelsoundpool) |
| [reportAVScreenCaptureUserChoice](arkts-media-media-reportavscreencaptureuserchoice-f-sys.md#reportavscreencaptureuserchoice) |
| [getAVScreenCaptureConfigurableParameters](arkts-media-media-getavscreencaptureconfigurableparameters-f-sys.md#getavscreencaptureconfigurableparameters) |
| [getScreenCaptureMonitor](arkts-media-media-getscreencapturemonitor-f-sys.md#getscreencapturemonitor) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AVTimedMetaData](arkts-media-media-avtimedmetadata-i.md) |
| [AVMetadataExtractor](arkts-media-media-avmetadataextractor-i.md) |
| [AVMetadata](arkts-media-media-avmetadata-i.md) |
| [OutputSize](arkts-media-media-outputsize-i.md) |
| [AVImageGenerator](arkts-media-media-avimagegenerator-i.md) |
| [PixelMapParams](arkts-media-media-pixelmapparams-i.md) |
| [FrameInfo](arkts-media-media-frameinfo-i.md) |
| [VideoSize](arkts-media-media-videosize-i.md) |
| [TrackSelectionFilter](arkts-media-media-trackselectionfilter-i.md) |
| [SeiMessage](arkts-media-media-seimessage-i.md) |
| [AVMetricsEvent](arkts-media-media-avmetricsevent-i.md) |
| [AVPlayer](arkts-media-media-avplayer-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AVMetadataExtractor](arkts-media-media-avmetadataextractor-i-sys.md) |
| [AVMetadata](arkts-media-media-avmetadata-i-sys.md) |
| [PixelMapParams](arkts-media-media-pixelmapparams-i-sys.md) |
| [AVPlayer](arkts-media-media-avplayer-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [SoundInterruptMode](arkts-media-media-soundinterruptmode-e.md) |
| [StateChangeReason](arkts-media-media-statechangereason-e.md) |
| [HdrType](arkts-media-media-hdrtype-e.md) |
| [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) |
| [FetchResult](arkts-media-media-fetchresult-e.md) |
| [AVErrorCode](arkts-media-media-averrorcode-e.md) |
| [AVMetricsEventType](arkts-media-media-avmetricseventtype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [PixelFormat](arkts-media-media-pixelformat-e-sys.md) |
| [AVErrorCode](arkts-media-media-averrorcode-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [SoundPool](arkts-media-media-soundpool-t.md) |
| [PlayParameters](arkts-media-media-playparameters-t.md) |
| [OnFrameFetched](arkts-media-media-onframefetched-t.md) |
| [AVPlayerState](arkts-media-media-avplayerstate-t.md) |
| [OnTrackChangeHandler](arkts-media-media-ontrackchangehandler-t.md) |
| [OnAVPlayerStateChangeHandle](arkts-media-media-onavplayerstatechangehandle-t.md) |
| [OnBufferingUpdateHandler](arkts-media-media-onbufferingupdatehandler-t.md) |
| [OnVideoSizeChangeHandler](arkts-media-media-onvideosizechangehandler-t.md) |
| [OnSuperResolutionChanged](arkts-media-media-onsuperresolutionchanged-t.md) |
| [OnSeiMessageHandle](arkts-media-media-onseimessagehandle-t.md) |
| [OnPlaybackRateDone](arkts-media-media-onplaybackratedone-t.md) |
