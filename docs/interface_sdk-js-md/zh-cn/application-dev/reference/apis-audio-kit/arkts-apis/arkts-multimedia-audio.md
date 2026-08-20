# @ohos.multimedia.audio

音频管理提供基础的音频控制能力，包括音量调节、设备管理、数据采集及渲染。

该模块提供以下音频相关的常用功能：

- [AudioManager](arkts-audio-audio-audiomanager-i.md)：音频管理器。 - [AudioDeviceEnhanceManager](../../../reference/apis-audio-kit/arkts-apis-audio-AudioDeviceEnhanceManager.md)：音频设备增 强管理器。 - [AudioRenderer](arkts-audio-audio-audiorenderer-i.md)：音频渲染，用于播放PCM（Pulse Code Modulation）音频数据。 - [AudioCapturer](arkts-audio-audio-audiocapturer-i.md)：音频采集，用于录制PCM音频数据。

**起始版本：** 23

<!--Device-unnamed-declare namespace audio--><!--Device-unnamed-declare namespace audio-End-->

**系统能力：** 
- API版本12+：SystemCapability.Multimedia.Audio.Core

## 导入模块

```TypeScript
import { audio } from '@kit.AudioKit';
import { audioHaptic } from '@kit.AudioKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md) | 获取音频采集器。使用callback异步回调。 |
| [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md) | Obtains an [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) instance. This method uses an asynchronous callback to return the capturer instance. Using [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) to record audio will need permission according to different Sourcetype in options parameter, like MICROPHONE for the most microphone recording cases. |
| [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md) | 获取音频采集器。使用Promise异步回调。 |
| [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md) | Obtains an [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) instance. This method uses a promise to return the capturer instance. Using [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) to record audio will need permission according to different Sourcetype in options parameter, like MICROPHONE for the most microphone recording cases. |
| [createAudioLoopback](arkts-audio-audio-createaudioloopback-f.md) | 创建音频返听器。使用Promise异步回调。 |
| [createAudioLoopback](arkts-audio-audio-createaudioloopback-f.md) | Creates an &lt;b&gt;AudioLoopback&lt;/b&gt; instance, which provides low-latency in-ear monitoring using a fast capturer and renderer. |
| [createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md) | 获取音频渲染器。使用callback异步回调。 |
| [createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md) | Obtains an [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) instance. This method uses a promise to return the renderer instance. |
| [createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md) | 获取音频渲染器。使用Promise异步回调。 |
| [createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md) | Obtains an [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) instance. This method uses a promise to return the renderer instance. |
| [getAudioManager](arkts-audio-audio-getaudiomanager-f.md) | 获取音频管理器。 |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [createAsrProcessingController](arkts-audio-audio-createasrprocessingcontroller-f-sys.md) | Create ASR processing controller on one audio capturer. |
| [createAsrProcessingController](arkts-audio-audio-createasrprocessingcontroller-f-sys.md) | Create ASR processing controller on one audio capturer. |
| [createGlobalAudioLoopback](arkts-audio-audio-createglobalaudioloopback-f-sys.md) | 创建全局音频环回实例，提供低时延入耳监听功能。 硬件音频环回只能在支持的平台中创建，应用程序可以使用 |
| [createMicInAudioCapturer](arkts-audio-audio-createmicinaudiocapturer-f-sys.md) | 获取一个特殊的[AudioCapturer](arkts-audio-audio-audiocapturer-i.md)实例。该方法使用promise返回录音实例。 此捕获可用于记录Mic-In音频数据和回声参考信号，以便应用处理算法。 Mic-In音频数据和回声参考信号将根据应用程序设置的配置被放入一个或多个缓冲。 当应用程序处于后台时，不允许创建录音实例。 |
| [createTonePlayer](arkts-audio-audio-createtoneplayer-f-sys.md) | Obtains a [TonePlayer](arkts-audio-audio-toneplayer-i-sys.md) instance. This method uses an asynchronous callback to return the renderer instance. |
| [createTonePlayer](arkts-audio-audio-createtoneplayer-f-sys.md) | Obtains a [TonePlayer](arkts-audio-audio-toneplayer-i-sys.md) instance. This method uses an asynchronous callback to return the renderer instance. |
| [createTonePlayer](arkts-audio-audio-createtoneplayer-f-sys.md) | Obtains a [TonePlayer](arkts-audio-audio-toneplayer-i-sys.md) instance. This method uses a promise to return the renderer instance. |
| [createTonePlayer](arkts-audio-audio-createtoneplayer-f-sys.md) | Obtains a [TonePlayer](arkts-audio-audio-toneplayer-i-sys.md) instance. This method uses a promise to return the renderer instance. |
<!--DelEnd-->

### 接口

| 名称 | 说明 |
| --- | --- |
| [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) | 提供音频采集的相关接口。 |
| [AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md) | 描述音频采集器更改信息。 |
| [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) | 描述音频采集器信息。 |
| [AudioCapturerOptions](arkts-audio-audio-audiocaptureroptions-i.md) | 音频采集器选项信息。 |
| [AudioDebuggingManager](arkts-audio-audio-audiodebuggingmanager-i.md) | 实现音频调试功能。 |
| [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 描述音频设备。 |
| [AudioDeviceEnhanceManager](arkts-audio-audio-audiodeviceenhancemanager-i.md) | 提供增强的音频设备管理能力。 |
| [AudioDevicePair](arkts-audio-audio-audiodevicepair-i.md) | 描述返听使用的音频设备对，包含输入设备和输出设备。 |
| [AudioInterrupt](arkts-audio-audio-audiointerrupt-i.md) | 音频监听事件传入的参数。 |
| [AudioLoopback](arkts-audio-audio-audioloopback-i.md) | 提供音频返听的相关接口。 |
| [AudioManager](arkts-audio-audio-audiomanager-i.md) | 音频音量和设备管理。 |
| [AudioPlaybackCaptureConfig](arkts-audio-audio-audioplaybackcaptureconfig-i.md) | 音频内录的配置信息。 |
| [AudioRecordingManager](arkts-audio-audio-audiorecordingmanager-i.md) | 提供录像策略管理，包括协同录音 和录制控制能力。 |
| [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) | 提供音频渲染的相关接口。 |
| [AudioRendererChangeInfo](arkts-audio-audio-audiorendererchangeinfo-i.md) | 描述音频渲染器更改信息。 |
| [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) | 音频渲染器信息。 |
| [AudioRendererOptions](arkts-audio-audio-audiorendereroptions-i.md) | 音频渲染器选项信息。 |
| [AudioRoutingManager](arkts-audio-audio-audioroutingmanager-i.md) | 音频路由管理。 |
| [AudioSessionDeactivatedEvent](arkts-audio-audio-audiosessiondeactivatedevent-i.md) | 音频会话停用事件。 |
| [AudioSessionManager](arkts-audio-audio-audiosessionmanager-i.md) | 音频会话管理。 |
| [AudioSessionStateChangedEvent](arkts-audio-audio-audiosessionstatechangedevent-i.md) | 音频会话状态变更事件。 |
| [AudioSessionStrategy](arkts-audio-audio-audiosessionstrategy-i.md) | 音频会话策略。 |
| [AudioSpatializationManager](arkts-audio-audio-audiospatializationmanager-i.md) | 空间音频管理。 |
| [AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md) | 流设备变更时，应用接收到的事件。 |
| [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | 音频流信息。 |
| [AudioStreamManager](arkts-audio-audio-audiostreammanager-i.md) | 音频流管理。 |
| [AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md) | 音频流时间戳和当前数据帧位置信息。 |
| [AudioVolumeGroupManager](arkts-audio-audio-audiovolumegroupmanager-i.md) | 管理音频组音量。 |
| [AudioVolumeManager](arkts-audio-audio-audiovolumemanager-i.md) | 音量管理。 |
| [CaptureFilterOptions](arkts-audio-audio-capturefilteroptions-i.md) | 待录制的播放音频流的筛选信息。 |
| [CurrentInputDeviceChangedEvent](arkts-audio-audio-currentinputdevicechangedevent-i.md) | 应用接收到输入设备的变更事件。 |
| [CurrentOutputDeviceChangedEvent](arkts-audio-audio-currentoutputdevicechangedevent-i.md) | 应用接收到输出设备的变更事件。 |
| [DeviceBlockStatusInfo](arkts-audio-audio-deviceblockstatusinfo-i.md) | 描述音频设备被堵塞状态和设备信息。 |
| [DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md) | 描述设备连接状态变化和设备信息。 |
| [InterruptAction](arkts-audio-audio-interruptaction-i.md) | 音频打断/获取焦点事件的回调方法。 |
| [InterruptEvent](arkts-audio-audio-interruptevent-i.md) | 音频中断时，应用接收的中断事件。 |
| [MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md) | 麦克风状态变化时，应用接收到的事件。 |
| [StreamVolumeEvent](arkts-audio-audio-streamvolumeevent-i.md) | 音频流音量变化时，应用接收到的事件。 |
| [SystemRecordControllerConfig](arkts-audio-audio-systemrecordcontrollerconfig-i.md) | 定义系统录像控制器面板配置。 |
| [VolumeEvent](arkts-audio-audio-volumeevent-i.md) | 音量改变时，应用接收到的事件。 |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [ActiveStreamVolumeInfo](arkts-audio-audio-activestreamvolumeinfo-i-sys.md) | 用于激活音频流的音量信息。 |
| [AppIdInfo](arkts-audio-audio-appidinfo-i-sys.md) | 描述app id信息。 |
| [AsrProcessingController](arkts-audio-audio-asrprocessingcontroller-i-sys.md) |  |
| [AudioCapturer](arkts-audio-audio-audiocapturer-i-sys.md) | 提供音频采集的相关接口。 |
| [AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i-sys.md) | 描述音频采集器更改信息。 |
| [AudioCapturerFilter](arkts-audio-audio-audiocapturerfilter-i-sys.md) |  |
| [AudioCapturerMicInConfig](arkts-audio-audio-audiocapturermicinconfig-i-sys.md) | Describes audio capturer configuration options that can capture microphone input (mic-in) audio data before any processing. |
| [AudioCapturerMicInData](arkts-audio-audio-audiocapturermicindata-i-sys.md) | 描述音频录音数据，其中包含已处理的音频数据和 进行音频处理前的纯净麦克风输入（mic-in）音频数据。 |
| [AudioCapturerOptions](arkts-audio-audio-audiocaptureroptions-i-sys.md) | 音频采集器选项信息。 |
| [AudioCollaborativeManager](arkts-audio-audio-audiocollaborativemanager-i-sys.md) | Implements audio collaborative management. |
| [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i-sys.md) | 描述音频设备。 |
| [AudioDeviceEnhanceManager](arkts-audio-audio-audiodeviceenhancemanager-i-sys.md) | 提供增强的音频设备管理能力。 |
| [AudioEffectManager](arkts-audio-audio-audioeffectmanager-i-sys.md) | Implements audio effect management. |
| [AudioEffectProperty](arkts-audio-audio-audioeffectproperty-i-sys.md) |  |
| [AudioHRTFAnonymousDescriptor](arkts-audio-audio-audiohrtfanonymousdescriptor-i-sys.md) | 匿名的HRTF文件描述符，用于跨进程传输。 |
| [AudioManager](arkts-audio-audio-audiomanager-i-sys.md) | 音频音量和设备管理。 |
| [AudioPersonalizedSpatialEnabledChangeForAnyDevice](arkts-audio-audio-audiopersonalizedspatialenabledchangeforanydevice-i-sys.md) | 通知监听器开启个性化空间 任何设备的状态变化。 |
| [AudioRecordingManager](arkts-audio-audio-audiorecordingmanager-i-sys.md) | 提供录像策略管理，包括协同录音 和录制控制能力。 |
| [AudioRenderer](arkts-audio-audio-audiorenderer-i-sys.md) | 提供音频渲染的相关接口。 |
| [AudioRendererChangeInfo](arkts-audio-audio-audiorendererchangeinfo-i-sys.md) | 描述音频渲染器更改信息。 |
| [AudioRendererFilter](arkts-audio-audio-audiorendererfilter-i-sys.md) |  |
| [AudioRendererOptions](arkts-audio-audio-audiorendereroptions-i-sys.md) | 音频渲染器选项信息。 |
| [AudioRoutingManager](arkts-audio-audio-audioroutingmanager-i-sys.md) | 音频路由管理。 |
| [AudioSpatialDeviceState](arkts-audio-audio-audiospatialdevicestate-i-sys.md) |  |
| [AudioSpatialEnabledStateForDevice](arkts-audio-audio-audiospatialenabledstatefordevice-i-sys.md) | This interface is used to notify the listener of any device Spatialization or Head Tracking enable or Adaptive Spatial Rendering state change. @interface AudioSpatialEnabledStateForDevice |
| [AudioSpatializationManager](arkts-audio-audio-audiospatializationmanager-i-sys.md) | 空间音频管理。 |
| [AudioVolumeGroupManager](arkts-audio-audio-audiovolumegroupmanager-i-sys.md) | 管理音频组音量。 |
| [AudioVolumeManager](arkts-audio-audio-audiovolumemanager-i-sys.md) | 音量管理。 |
| [InterruptResult](arkts-audio-audio-interruptresult-i-sys.md) |  |
| [SoundCardInfo](arkts-audio-audio-soundcardinfo-i-sys.md) | 描述声卡信息。 |
| [SystemRecordControllerChangeInfo](arkts-audio-audio-systemrecordcontrollerchangeinfo-i-sys.md) | 定义系统录像控制器状态改变时携带的信息。 它包括启用状态、应用程序UID和预期的音频源类型。 |
| [SystemVolumeFilter](arkts-audio-audio-systemvolumefilter-i-sys.md) | 系统音量过滤器信息。 |
| [TonePlayer](arkts-audio-audio-toneplayer-i-sys.md) |  |
| [VolumeEvent](arkts-audio-audio-volumeevent-i-sys.md) | 音量改变时，应用接收到的事件。 |
| [VolumeGroupInfo](arkts-audio-audio-volumegroupinfo-i-sys.md) | Describes an audio volume group. |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | 表示活跃设备类型的枚举。 |
| [AudioChannel](arkts-audio-audio-audiochannel-e.md) | 表示音频声道的枚举。 |
| [AudioChannelLayout](arkts-audio-audio-audiochannellayout-e.md) | 表示音频文件声道布局类型的枚举。 |
| [AudioConcurrencyMode](arkts-audio-audio-audioconcurrencymode-e.md) | 表示音频并发模式的枚举。 |
| [AudioDataCallbackResult](arkts-audio-audio-audiodatacallbackresult-e.md) | 表示音频数据回调结果的枚举。 |
| [AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md) | 表示音效模式的枚举。 |
| [AudioEncodingType](arkts-audio-audio-audioencodingtype-e.md) | 表示音频编码类型的枚举。 |
| [AudioErrors](arkts-audio-audio-audioerrors-e.md) | 表示音频错误码的枚举。 |
| [AudioLatencyType](arkts-audio-audio-audiolatencytype-e.md) | 表示音频时延类型的枚举。 |
| [AudioLoopbackEqualizerPreset](arkts-audio-audio-audioloopbackequalizerpreset-e.md) | 表示返听均衡器类型的枚举。 |
| [AudioLoopbackMode](arkts-audio-audio-audioloopbackmode-e.md) | 表示返听模式的枚举。 |
| [AudioLoopbackReverbPreset](arkts-audio-audio-audioloopbackreverbpreset-e.md) | 表示返听混响模式的枚举。 |
| [AudioLoopbackStatus](arkts-audio-audio-audioloopbackstatus-e.md) | 表示返听状态的枚举。 |
| [AudioPlaybackCaptureMode](arkts-audio-audio-audioplaybackcapturemode-e.md) | 表示内录（录制设备内部应用的声音）模式的枚举。不同模式决定可录制的目标播放流类型。支持通过按位或组合枚举值，当前仅支持MODE_DEFAULT（0x0）、MODE_MEDIA（0x1）、MODE_EXCLUDING_SELF（0x 8000），以及MODE_MEDIA和MODE_EXCLUDING_SELF的按位或组合（0x8001）。 |
| [AudioPrivacyType](arkts-audio-audio-audioprivacytype-e.md) | 表示对应播放音频流是否支持被其他应用录制的枚举。 |
| [AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md) | 表示音频渲染速度的枚举。 |
| [AudioRingMode](arkts-audio-audio-audioringmode-e.md) | 表示铃声模式的枚举。 |
| [AudioSampleFormat](arkts-audio-audio-audiosampleformat-e.md) | 表示音频采样格式的枚举。 |
| [AudioSamplingRate](arkts-audio-audio-audiosamplingrate-e.md) | 表示音频采样率的枚举（具体设备支持的采样率规格会存在差异）。 |
| [AudioScene](arkts-audio-audio-audioscene-e.md) | 表示音频场景的枚举。 |
| [AudioSessionBehaviorFlags](arkts-audio-audio-audiosessionbehaviorflags-e.md) | 表示音频会话行为的枚举。 |
| [AudioSessionDeactivatedReason](arkts-audio-audio-audiosessiondeactivatedreason-e.md) | 表示音频会话停用原因的枚举。 |
| [AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md) | 枚举音频会话场景。 |
| [AudioSessionStateChangeHint](arkts-audio-audio-audiosessionstatechangehint-e.md) | 枚举用于音频会话状态变更提示。 |
| [AudioState](arkts-audio-audio-audiostate-e.md) | 表示音频状态的枚举。 |
| [AudioStreamDeviceChangeReason](arkts-audio-audio-audiostreamdevicechangereason-e.md) | 表示流设备变更原因的枚举。 |
| [AudioVolumeMode](arkts-audio-audio-audiovolumemode-e.md) | 表示音量模式的枚举。 |
| [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 表示音频音量类型的枚举。 |
| [BluetoothAndNearlinkPreferredRecordCategory](arkts-audio-audio-bluetoothandnearlinkpreferredrecordcategory-e.md) | 表示在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类枚举。 |
| [ChannelBlendMode](arkts-audio-audio-channelblendmode-e.md) | 表示声道混合模式类型的枚举。 |
| [CommunicationDeviceType](arkts-audio-audio-communicationdevicetype-e.md) | 表示用于通信的可用设备类型的枚举。 |
| [ContentType](arkts-audio-audio-contenttype-e.md) | 表示音频内容类型的枚举。 |
| [DeviceBlockStatus](arkts-audio-audio-deviceblockstatus-e.md) | 表示音频设备是否被堵塞的枚举。 |
| [DeviceChangeType](arkts-audio-audio-devicechangetype-e.md) | 表示设备连接状态变化的枚举。 |
| [DeviceFlag](arkts-audio-audio-deviceflag-e.md) | 表示音频设备类型的枚举。 |
| [DeviceRole](arkts-audio-audio-devicerole-e.md) | 表示设备角色的枚举。 |
| [DeviceType](arkts-audio-audio-devicetype-e.md) | 表示设备类型的枚举。 |
| [DeviceUsage](arkts-audio-audio-deviceusage-e.md) | 表示音频设备类型的枚举（根据用途分类）。 |
| [InterruptActionType](arkts-audio-audio-interruptactiontype-e.md) | 表示中断事件返回类型的枚举。 |
| [InterruptForceType](arkts-audio-audio-interruptforcetype-e.md) | 表示音频打断类型的枚举。 |
| [InterruptHint](arkts-audio-audio-interrupthint-e.md) | 表示中断提示的枚举。 |
| [InterruptMode](arkts-audio-audio-interruptmode-e.md) | 表示焦点模型的枚举。 |
| [InterruptType](arkts-audio-audio-interrupttype-e.md) | 表示中断类型的枚举。 |
| [NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md) | 降噪模式枚举。 |
| [OutputDeviceChangeRecommendedAction](arkts-audio-audio-outputdevicechangerecommendedaction-e.md) | 表示输出设备变更后推荐操作的枚举。 |
| [PlaybackCaptureStartState](arkts-audio-audio-playbackcapturestartstate-e.md) | 表示调用[requestPlaybackCaptureStart](arkts-audio-audio-audiocapturer-i.md#requestplaybackcapturestart)后异步返回的内录启动状态的枚举。 |
| [SourceType](arkts-audio-audio-sourcetype-e.md) | 表示录制音频流类型的枚举。 |
| [StreamUsage](arkts-audio-audio-streamusage-e.md) | 表示播放音频流类型的枚举。 |

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [AsrAecMode](arkts-audio-audio-asraecmode-e-sys.md) | ASR AEC mode. @enum { int } |
| [AsrNoiseSuppressionMode](arkts-audio-audio-asrnoisesuppressionmode-e-sys.md) | ASR noise suppression mode. @enum { int } |
| [AsrVoiceControlMode](arkts-audio-audio-asrvoicecontrolmode-e-sys.md) | ASR voice control mode. |
| [AsrVoiceMuteMode](arkts-audio-audio-asrvoicemutemode-e-sys.md) | ASR voice mute mode. |
| [AsrWhisperDetectionMode](arkts-audio-audio-asrwhisperdetectionmode-e-sys.md) | ASR whisper detection mode. |
| [AudioDevcieSelectStrategy](arkts-audio-audio-audiodevcieselectstrategy-e-sys.md) | Enumerates the device select strategy. |
| [AudioSeparationVolumeType](arkts-audio-audio-audioseparationvolumetype-e-sys.md) | 音频分离效果的音量类型。 |
| [AudioSpatialDeviceType](arkts-audio-audio-audiospatialdevicetype-e-sys.md) | Describes a spatial device type group. |
| [AudioSpatializationSceneType](arkts-audio-audio-audiospatializationscenetype-e-sys.md) | Describes a spatialization scene type group. |
| [AudioVolumeType](arkts-audio-audio-audiovolumetype-e-sys.md) | 表示音频音量类型的枚举。 |
| [ConnectType](arkts-audio-audio-connecttype-e-sys.md) | Connect type for device. @enum { int } |
| [DeviceFlag](arkts-audio-audio-deviceflag-e-sys.md) | 表示音频设备类型的枚举。 |
| [DeviceType](arkts-audio-audio-devicetype-e-sys.md) | 表示设备类型的枚举。 |
| [EffectFlag](arkts-audio-audio-effectflag-e-sys.md) | Enumerates audio effect flags. @enum { int } |
| [InterruptRequestResultType](arkts-audio-audio-interruptrequestresulttype-e-sys.md) | Enumerates audio interrupt request result type. |
| [InterruptRequestType](arkts-audio-audio-interruptrequesttype-e-sys.md) | Enumerates the audio interrupt request type. |
| [PolicyType](arkts-audio-audio-policytype-e-sys.md) | Enumerates type. @enum { int } |
| [RenderTarget](arkts-audio-audio-rendertarget-e-sys.md) | Audio render target. @enum { int } |
| [SourceType](arkts-audio-audio-sourcetype-e-sys.md) | 表示录制音频流类型的枚举。 |
| [SpatialAudioSourceType](arkts-audio-audio-spatialaudiosourcetype-e-sys.md) | 枚举空间音频源类型。 |
| [StreamUsage](arkts-audio-audio-streamusage-e-sys.md) | 表示播放音频流类型的枚举。 |
| [ToneType](arkts-audio-audio-tonetype-e-sys.md) | Enumerates tone types for player. |
| [VolumeAdjustType](arkts-audio-audio-volumeadjusttype-e-sys.md) | Enumerates volume adjustment types. |
| [VolumeFlag](arkts-audio-audio-volumeflag-e-sys.md) | Enumerates volume related operations. Flags should be powers of 2! |
<!--DelEnd-->

### 类型

| 名称 | 说明 |
| --- | --- |
| [AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md) | 数组类型，AudioCapturerChangeInfo数组，只读。 |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) | 设备属性数组类型，为[AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md)的数组，只读。 |
| [AudioEffectInfoArray](arkts-audio-audio-audioeffectinfoarray-t.md) | 待查询ContentType和StreamUsage组合场景下的音效模式数组类型，[AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md)数组，只读。 |
| [AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md) | 数组类型，AudioRendererChangeInfo数组，只读。 |
| [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | Type definition of callback function for audio renderer write data. |
| [DeviceTypeArray](arkts-audio-audio-devicetypearray-t.md) | 数组类型，[DeviceType](arkts-audio-audio-devicetype-e.md)数组。 |

<!--Del-->
### 类型（系统接口）

| 名称 | 说明 |
| --- | --- |
| [ActiveStreamsVolumeInfoArray](arkts-audio-audio-activestreamsvolumeinfoarray-t-sys.md) | ActiveStreamVolumeInfo数组。 |
| [StreamUsageArray](arkts-audio-audio-streamusagearray-t-sys.md) | Array of StreamUsages. |
| [VolumeGroupInfos](arkts-audio-audio-volumegroupinfos-t-sys.md) | Array of VolumeGroupInfos, which is read-only. |
<!--DelEnd-->

### 常量

| 名称 | 说明 |
| --- | --- |
| [DEFAULT_INTERRUPT_GROUP_ID](arkts-audio-audio-con.md#default_interrupt_group_id) | Define default interrupt group id for audio |
| [DEFAULT_VOLUME_GROUP_ID](arkts-audio-audio-con.md#default_volume_group_id) | Define default volume group id for audio |

<!--Del-->
### 常量（系统接口）

| 名称 | 说明 |
| --- | --- |
| [LOCAL_NETWORK_ID](arkts-audio-audio-con-sys.md#local_network_id) | Define local device network id for audio |
<!--DelEnd-->

