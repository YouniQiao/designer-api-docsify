# @ohos.multimedia.media

媒体子系统为开发者提供一套简单且易于理解的接口，使得开发者能够方便接入系统并使用系统的媒体资源。

## 汇总

### 命名空间

| 名称 |
| --- |
| [media](arkts-media-media-n.md) |

### 接口

| 名称 |
| --- |
| [AVDataSrcDescriptor](arkts-media-multimedia-media-avdatasrcdescriptor-i.md) |
| [AVFileDescriptor](arkts-media-multimedia-media-avfiledescriptor-i.md) |
| [AVRecorder](arkts-media-multimedia-media-avrecorder-i.md) |
| [AVRecorderConfig](arkts-media-multimedia-media-avrecorderconfig-i.md) |
| [AVRecorderProfile](arkts-media-multimedia-media-avrecorderprofile-i.md) |
| [AVScreenCaptureRecordConfig](arkts-media-multimedia-media-avscreencapturerecordconfig-i.md) |
| [AVScreenCaptureRecorder](arkts-media-multimedia-media-avscreencapturerecorder-i.md) |
| [AVScreenCaptureStrategy](arkts-media-multimedia-media-avscreencapturestrategy-i.md) |
| [AVTranscoder](arkts-media-multimedia-media-avtranscoder-i.md) |
| [AVTranscoderConfig](arkts-media-multimedia-media-avtranscoderconfig-i.md) |
| [AudioPlayer](arkts-media-multimedia-media-audioplayer-i.md) |
| [AudioRecorder](arkts-media-multimedia-media-audiorecorder-i.md) |
| [AudioRecorderConfig](arkts-media-multimedia-media-audiorecorderconfig-i.md) |
| [EncoderInfo](arkts-media-multimedia-media-encoderinfo-i.md) |
| [Location](arkts-media-multimedia-media-location-i.md) |
| [MediaDescription](arkts-media-multimedia-media-mediadescription-i.md) |
| [MediaSource](arkts-media-multimedia-media-mediasource-i.md) |
| [MediaSourceLoader](arkts-media-multimedia-media-mediasourceloader-i.md) |
| [MediaSourceLoadingRequest](arkts-media-multimedia-media-mediasourceloadingrequest-i.md) |
| [MediaStream](arkts-media-multimedia-media-mediastream-i.md) |
| [PlaybackInfo](arkts-media-multimedia-media-playbackinfo-i.md) |
| [PlaybackStrategy](arkts-media-multimedia-media-playbackstrategy-i.md) |
| [Range](arkts-media-multimedia-media-range-i.md) |
| [SubtitleInfo](arkts-media-multimedia-media-subtitleinfo-i.md) |
| [VideoPlayer](arkts-media-multimedia-media-videoplayer-i.md) |
| [WatermarkConfiguration](arkts-media-multimedia-media-watermarkconfiguration-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AVRecorder](arkts-media-multimedia-media-avrecorder-i-sys.md) |
| [AVRecorderConfig](arkts-media-multimedia-media-avrecorderconfig-i-sys.md) |
| [AVRecorderProfile](arkts-media-multimedia-media-avrecorderprofile-i-sys.md) |
| [AVScreenCaptureStrategy](arkts-media-multimedia-media-avscreencapturestrategy-i-sys.md) |
| [PlaybackStrategy](arkts-media-multimedia-media-playbackstrategy-i-sys.md) |
| [ScreenCaptureMonitor](arkts-media-multimedia-media-screencapturemonitor-i-sys.md) |
| [VideoRecorder](arkts-media-multimedia-media-videorecorder-i-sys.md) |
| [VideoRecorderConfig](arkts-media-multimedia-media-videorecorderconfig-i-sys.md) |
| [VideoRecorderProfile](arkts-media-multimedia-media-videorecorderprofile-i-sys.md) |
| [WatermarkConfig](arkts-media-multimedia-media-watermarkconfig-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AVMimeTypes](arkts-media-multimedia-media-avmimetypes-e.md) |
| [AVScreenCaptureFillMode](arkts-media-multimedia-media-avscreencapturefillmode-e.md) |
| [AVScreenCaptureRecordPreset](arkts-media-multimedia-media-avscreencapturerecordpreset-e.md) |
| [AVScreenCaptureStateCode](arkts-media-multimedia-media-avscreencapturestatecode-e.md) |
| [AacProfile](arkts-media-multimedia-media-aacprofile-e.md) |
| [AudioEncoder](arkts-media-multimedia-media-audioencoder-e.md) |
| [AudioOutputFormat](arkts-media-multimedia-media-audiooutputformat-e.md) |
| [AudioSourceType](arkts-media-multimedia-media-audiosourcetype-e.md) |
| [BufferingInfoType](arkts-media-multimedia-media-bufferinginfotype-e.md) |
| [CodecMimeType](arkts-media-multimedia-media-codecmimetype-e.md) |
| [ContainerFormatType](arkts-media-multimedia-media-containerformattype-e.md) |
| [FileGenerationMode](arkts-media-multimedia-media-filegenerationmode-e.md) |
| [LoadingRequestError](arkts-media-multimedia-media-loadingrequesterror-e.md) |
| [MediaDescriptionKey](arkts-media-multimedia-media-mediadescriptionkey-e.md) |
| [MediaErrorCode](arkts-media-multimedia-media-mediaerrorcode-e.md) |
| [MediaType](arkts-media-multimedia-media-mediatype-e.md) |
| [PickerMode](arkts-media-multimedia-media-pickermode-e.md) |
| [PlaybackInfoKey](arkts-media-multimedia-media-playbackinfokey-e.md) |
| [PlaybackMetricsKey](arkts-media-multimedia-media-playbackmetricskey-e.md) |
| [PlaybackSpeed](arkts-media-multimedia-media-playbackspeed-e.md) |
| [PlaylistLoopMode](arkts-media-multimedia-media-playlistloopmode-e.md) |
| [SeekMode](arkts-media-multimedia-media-seekmode-e.md) |
| [SwitchMode](arkts-media-multimedia-media-switchmode-e.md) |
| [VideoScaleType](arkts-media-multimedia-media-videoscaletype-e.md) |
| [VideoSourceType](arkts-media-multimedia-media-videosourcetype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [MetaSourceType](arkts-media-multimedia-media-metasourcetype-e-sys.md) |
| [ScreenCaptureEvent](arkts-media-multimedia-media-screencaptureevent-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [AVRecorderState](arkts-media-avrecorderstate-t.md) |
| [AudioState](arkts-media-audiostate-t.md) |
| [MediaDescription](arkts-media-mediadescription-t.md) |
| [OnAVRecorderStateChangeHandler](arkts-media-onavrecorderstatechangehandler-t.md) |
| [PlaybackInfo](arkts-media-playbackinfo-t.md) |
| [PlaybackMetrics](arkts-media-playbackmetrics-t.md) |
| [SourceCloseCallback](arkts-media-sourceclosecallback-t.md) |
| [SourceOpenCallback](arkts-media-sourceopencallback-t.md) |
| [SourceReadCallback](arkts-media-sourcereadcallback-t.md) |
| [VideoPlayState](arkts-media-videoplaystate-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [VideoRecordState](arkts-media-videorecordstate-t-sys.md) |
<!--DelEnd-->
