# @ohos.multimedia.media

媒体子系统为开发者提供一套简单且易于理解的接口，使得开发者能够方便接入系统并使用系统的媒体资源。

## 导入模块

```TypeScript
import { media } from '@kit.MediaKit';
```

## 汇总

### 命名空间

| 名称 | 说明 |
| --- | --- |
| [media](arkts-media-media-n.md) | 媒体子系统为开发者提供一套简单且易于理解的接口，使得开发者能够方便接入系统并使用系统的媒体资源。 |

### 函数

| 名称 | 说明 |
| --- | --- |
| [createAVDownloaderManager](arkts-media-multimedia-media-createavdownloadermanager-f.md) | 创建一个离线下载任务管理器实例。使用Promise异步回调。 |
| [createMediaSourceWithDirectory](arkts-media-multimedia-media-createmediasourcewithdirectory-f.md) | 根据指定目录路径创建一个媒体源对象。使用Promise异步回调。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [AVDataSrcDescriptor](arkts-media-multimediamedia-avdatasrcdescriptor-i.md) | Defines the descriptor of an audio and video file, which is used in DataSource playback mode. Use scenario: An application can create a playback instance and start playback before it finishes downloading the audio and video resources. |
| [AVDownloaderManager](arkts-media-multimediamedia-avdownloadermanager-i.md) | 离线下载任务管理接口，用于管理媒体资源的离线下载任务，包括创建、暂停、恢复、移除下载任务以及监听下载状态和进度变化事件。 |
| [AVFileDescriptor](arkts-media-multimediamedia-avfiledescriptor-i.md) | Media file descriptor. The caller needs to ensure that the fd is valid and the offset and length are correct. |
| [AVRecorder](arkts-media-multimediamedia-avrecorder-i.md) | AVRecorder是音视频录制管理类，用于音视频录制的全流程管理，支持音频录制、视频录制及音视频混合录制，可灵活配置编码参数、添加水印、设置元数据、监听录制状态和错误事件等。 适用于录制音视频并保存到文件的场景，包括需要在音频流打断期间保持录制连续性、实时监控音频振幅等场景。 在调用AVRecorder的方法前，需要先调用 [createAVRecorder](arkts-media-media-createavrecorder-f.md)接口构建一个AVRecorder实例。 典型录制流程： [createAVRecorder](arkts-media-media-createavrecorder-f.md) → prepare → getInputSurface（纯视频/音视频录制时） → start → pause/ resume → stop → release。 |
| [AVRecorderConfig](arkts-media-multimediamedia-avrecorderconfig-i.md) | 音视频录制的参数。 |
| [AVRecorderProfile](arkts-media-multimediamedia-avrecorderprofile-i.md) | 音视频录制配置参数。 |
| [AVScreenCaptureRecordConfig](arkts-media-multimediamedia-avscreencapturerecordconfig-i.md) | Defines the screen capture parameters. |
| [AVScreenCaptureRecorder](arkts-media-multimediamedia-avscreencapturerecorder-i.md) | 屏幕录制管理类，用于进行屏幕录制。在调用AVScreenCaptureRecorder的方法前，需要先通过 [createAVScreenCaptureRecorder()](arkts-media-media-createavscreencapturerecorder-f.md)创建一个 AVScreenCaptureRecorder实例。 |
| [AVScreenCaptureStrategy](arkts-media-multimediamedia-avscreencapturestrategy-i.md) | Provides the media AVScreenCaptureStrategy definition. |
| [AVTranscoder](arkts-media-multimediamedia-avtranscoder-i.md) | 视频转码管理类，用于视频转码。在调用AVTranscoder的方法前，需要先通过 [createAVTranscoder()](arkts-media-media-createavtranscoder-f.md)构建一个AVTranscoder实例。 |
| [AVTranscoderConfig](arkts-media-multimediamedia-avtranscoderconfig-i.md) | Describes the video transcoding parameters. |
| [AudioPlayer](arkts-media-multimediamedia-audioplayer-i.md) |  |
| [AudioRecorder](arkts-media-multimediamedia-audiorecorder-i.md) |  |
| [AudioRecorderConfig](arkts-media-multimediamedia-audiorecorderconfig-i.md) | 音频录制配置定义。 |
| [EncoderInfo](arkts-media-multimediamedia-encoderinfo-i.md) | 编码器信息描述。 |
| [Location](arkts-media-multimediamedia-location-i.md) | Provides the geographical location definitions for media resources. |
| [MediaDescription](arkts-media-multimediamedia-mediadescription-i.md) | Provides the container definition for media description key-value pairs. |
| [MediaSource](arkts-media-multimediamedia-mediasource-i.md) | 媒体数据信息。来源于 [createMediaSourceWithUrl](arkts-media-media-createmediasourcewithurl-f.md) 。 |
| [MediaSourceLoader](arkts-media-multimediamedia-mediasourceloader-i.md) | Defines a media data loader, which needs to be implemented by applications. |
| [MediaSourceLoadingRequest](arkts-media-multimediamedia-mediasourceloadingrequest-i.md) | 用于定义加载请求的对象。应用程序通过该对象来获取请求的资源位置，通过该对象和播放器进行数据交互。 |
| [MediaStream](arkts-media-multimediamedia-mediastream-i.md) | Media Stream. AVPlayer use this for mediaData access, current version only support live stream. |
| [PlaybackInfo](arkts-media-multimediamedia-playbackinfo-i.md) | Provides player statistic info. |
| [PlaybackStrategy](arkts-media-multimediamedia-playbackstrategy-i.md) | Provides preferred playback settings for player. |
| [Range](arkts-media-multimediamedia-range-i.md) | 包含上下限的范围。 |
| [SubtitleInfo](arkts-media-multimediamedia-subtitleinfo-i.md) | Provides subtitle information. When a subtitle update event is subscribed to, the information about the external subtitle is returned through a callback. Can be synchronized to the time reported by AVPlayer#timeUpdate event |
| [VideoPlayer](arkts-media-multimediamedia-videoplayer-i.md) | 视频播放管理类，用于管理和播放视频媒体。在调用VideoPlayer的方法前，需要先通过 [createVideoPlayer()](arkts-media-media-createvideoplayer-f.md)构建 一个VideoPlayer实例。 |
| [WatermarkConfiguration](arkts-media-multimediamedia-watermarkconfiguration-i.md) | 设置水印配置。水印位置从左上角开始计算。 |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [AVRecorder](arkts-media-multimediamedia-avrecorder-i-sys.md) | AVRecorder是音视频录制管理类，用于音视频录制的全流程管理，支持音频录制、视频录制及音视频混合录制，可灵活配置编码参数、添加水印、设置元数据、监听录制状态和错误事件等。 适用于录制音视频并保存到文件的场景，包括需要在音频流打断期间保持录制连续性、实时监控音频振幅等场景。 在调用AVRecorder的方法前，需要先调用 [createAVRecorder](arkts-media-media-createavrecorder-f.md)接口构建一个AVRecorder实例。 典型录制流程： [createAVRecorder](arkts-media-media-createavrecorder-f.md) → prepare → getInputSurface（纯视频/音视频录制时） → start → pause/ resume → stop → release。 |
| [AVRecorderConfig](arkts-media-multimediamedia-avrecorderconfig-i-sys.md) | 音视频录制的参数。 |
| [AVRecorderProfile](arkts-media-multimediamedia-avrecorderprofile-i-sys.md) | 音视频录制配置参数。 |
| [AVScreenCaptureStrategy](arkts-media-multimediamedia-avscreencapturestrategy-i-sys.md) | Provides the media AVScreenCaptureStrategy definition. |
| [PlaybackStrategy](arkts-media-multimediamedia-playbackstrategy-i-sys.md) | Provides preferred playback settings for player. |
| [ScreenCaptureMonitor](arkts-media-multimediamedia-screencapturemonitor-i-sys.md) | A class that provides APIs to query and monitor the system screen recorder status. Before calling any API, you must use getScreenCaptureMonitor() to obtain a ScreenCaptureMonitor instance. |
| [VideoRecorder](arkts-media-multimediamedia-videorecorder-i-sys.md) | 该接口自API version 9起停止维护，建议使用AVRecorder。 视频录制管理类，用于视频录制。在调用VideoRecorder的方法前，必须先通过createVideoRecorder()创建一个VideoRecorder实例。 |
| [VideoRecorderConfig](arkts-media-multimediamedia-videorecorderconfig-i-sys.md) | 视频录制配置定义。 |
| [VideoRecorderProfile](arkts-media-multimediamedia-videorecorderprofile-i-sys.md) | 视频录制配置参数定义。 |
| [WatermarkConfig](arkts-media-multimediamedia-watermarkconfig-i-sys.md) | 设置AVRecorder的水印配置。水印位置从左上角开始计算。 |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [AVMimeTypes](arkts-media-multimediamedia-avmimetypes-e.md) | 媒体MIME类型，通过setMimeType设置。 |
| [AVScreenCaptureFillMode](arkts-media-multimediamedia-avscreencapturefillmode-e.md) | 进行屏幕录制时视频填充模式的枚举。 |
| [AVScreenCaptureRecordPreset](arkts-media-multimediamedia-avscreencapturerecordpreset-e.md) | 进行屏幕录制时的编码、封装格式参数的枚举。 |
| [AVScreenCaptureStateCode](arkts-media-multimediamedia-avscreencapturestatecode-e.md) | 屏幕录制的状态回调。 |
| [AacProfile](arkts-media-multimediamedia-aacprofile-e.md) | 高级音频编码（AAC）类型枚举。 |
| [AudioEncoder](arkts-media-multimediamedia-audioencoder-e.md) |  |
| [AudioOutputFormat](arkts-media-multimediamedia-audiooutputformat-e.md) |  |
| [AudioSourceType](arkts-media-multimediamedia-audiosourcetype-e.md) | 表示视频录制中音频源类型的枚举。 |
| [BufferingInfoType](arkts-media-multimediamedia-bufferinginfotype-e.md) | 缓存事件类型枚举。 |
| [CodecMimeType](arkts-media-multimediamedia-codecmimetype-e.md) | Codec MIME类型枚举。 |
| [ContainerFormatType](arkts-media-multimediamedia-containerformattype-e.md) | 表示容器格式类型的枚举，缩写为CFT。 |
| [FileGenerationMode](arkts-media-multimediamedia-filegenerationmode-e.md) | 表示创建媒体文件模式的枚举。 |
| [LoadingRequestError](arkts-media-multimediamedia-loadingrequesterror-e.md) | 枚举，数据加载过程中状态变化的原因。 |
| [MediaDescriptionKey](arkts-media-multimediamedia-mediadescriptionkey-e.md) | 媒体信息描述枚举。 |
| [MediaErrorCode](arkts-media-multimediamedia-mediaerrorcode-e.md) | 媒体服务错误类型枚举。 |
| [MediaType](arkts-media-multimediamedia-mediatype-e.md) | 媒体类型枚举。 |
| [PickerMode](arkts-media-multimediamedia-pickermode-e.md) | 表示屏幕录制Picker模式的枚举。 |
| [PlaybackInfoKey](arkts-media-multimediamedia-playbackinfokey-e.md) | 播放信息描述枚举。 |
| [PlaybackMetricsKey](arkts-media-multimediamedia-playbackmetricskey-e.md) | 表示播放器指标信息的枚举。 |
| [PlaybackSpeed](arkts-media-multimediamedia-playbackspeed-e.md) | 视频播放的倍速枚举，可通过setSpeed方法作为参数传递下去。 |
| [PlaylistLoopMode](arkts-media-multimediamedia-playlistloopmode-e.md) | 表示播放列表循环模式的枚举。 |
| [SeekMode](arkts-media-multimediamedia-seekmode-e.md) | 视频播放的Seek模式枚举，可通过seek方法作为参数传递下去。 |
| [SwitchMode](arkts-media-multimediamedia-switchmode-e.md) | 表示视频播放的selectTrack模式枚举。 |
| [VideoScaleType](arkts-media-multimediamedia-videoscaletype-e.md) | 枚举，视频缩放模式。 |
| [VideoSourceType](arkts-media-multimediamedia-videosourcetype-e.md) | 表示视频录制中视频源类型的枚举。 |

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [MetaSourceType](arkts-media-multimediamedia-metasourcetype-e-sys.md) | 录制的元数据源类型枚举。 |
| [ScreenCaptureEvent](arkts-media-multimediamedia-screencaptureevent-e-sys.md) | Enumerates the states available for the system screen recorder. |
<!--DelEnd-->

### 类型

| 名称 | 说明 |
| --- | --- |
| [AVDownloadTaskState](arkts-media-avdownloadtaskstate-t.md) | 离线下载任务状态枚举。 |
| [AVRecorderState](arkts-media-avrecorderstate-t.md) | 音视频录制的状态机。可通过state属性获取当前状态。 |
| [AudioState](arkts-media-audiostate-t.md) | 音频播放的状态机。可通过state属性获取当前状态。 |
| [MediaDescription](arkts-media-mediadescription-t.md) | Provides the container definition for media description key-value pairs. |
| [OnAVDownloadProgressChangeHandle](arkts-media-onavdownloadprogresschangehandle-t.md) | 离线下载任务进度变化事件回调方法。当下载进度相比上次变化超过1%，且距上次触发时间超过500ms时，触发该事件。 |
| [OnAVDownloadTaskStateHandle](arkts-media-onavdownloadtaskstatehandle-t.md) | 离线下载任务状态变化事件回调方法。 |
| [OnAVRecorderStateChangeHandler](arkts-media-onavrecorderstatechangehandler-t.md) | 录制状态机切换事件回调方法。 |
| [PlaybackInfo](arkts-media-playbackinfo-t.md) | Provides the container definition for media description key-value pairs. |
| [PlaybackMetrics](arkts-media-playbackmetrics-t.md) | 提供播放器指标信息键值对的容器定义。 |
| [SourceCloseCallback](arkts-media-sourceclosecallback-t.md) | 由应用实现此回调函数，应用应释放相关资源。 |
| [SourceOpenCallback](arkts-media-sourceopencallback-t.md) | 由应用实现此回调函数，应用需处理传入的资源打开请求，并返回所打开资源对应的唯一句柄。 |
| [SourceReadCallback](arkts-media-sourcereadcallback-t.md) | 由应用实现此回调函数，应用需记录读取请求，并在数据充足时通过对应的MediaSourceLoadingRequest对象的 respondData 方法推送数据。 |
| [VideoPlayState](arkts-media-videoplaystate-t.md) | 视频播放的状态机，可通过state属性获取当前状态。 |

<!--Del-->
### 类型（系统接口）

| 名称 | 说明 |
| --- | --- |
| [VideoRecordState](arkts-media-videorecordstate-t-sys.md) | The maintenance of this interface has been stopped since version api 9. Please use AVRecorderState. Describes video recorder states. |
<!--DelEnd-->

