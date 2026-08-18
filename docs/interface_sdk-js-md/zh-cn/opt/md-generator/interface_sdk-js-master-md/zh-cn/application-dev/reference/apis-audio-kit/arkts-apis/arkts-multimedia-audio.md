# @ohos.multimedia.audio

音频管理提供基础的音频控制能力，包括音量调节、设备管理、数据采集及渲染。 该模块提供以下音频相关的常用功能： - [AudioManager](arkts-audio-audio-audiomanager-i.md#audiomanager)：音频管理器。 - [AudioDeviceEnhanceManager](../../../reference/apis-audio-kit/arkts-apis-audio-AudioDeviceEnhanceManager.md)：音频设备增 强管理器。 - [AudioRenderer](arkts-audio-audio-audiorenderer-i.md#audiorenderer)：音频渲染，用于播放PCM（Pulse Code Modulation）音频数据。 - [AudioCapturer](arkts-audio-audio-audiocapturer-i.md#audiocapturer)：音频采集，用于录制PCM音频数据。

**起始版本：** 23

<!--Device-unnamed-declare namespace audio--><!--Device-unnamed-declare namespace audio-End-->

**系统能力：** 
- API版本12+：SystemCapability.Multimedia.Audio.Core

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md#createaudiocapturer) |
| [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md#createaudiocapturer) |
| [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md#createaudiocapturer) |
| [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md#createaudiocapturer) |
| [createAudioLoopback](arkts-audio-audio-createaudioloopback-f.md#createaudioloopback) |
| [createAudioLoopback](arkts-audio-audio-createaudioloopback-f.md#createaudioloopback) |
| [createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md#createaudiorenderer) |
| [createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md#createaudiorenderer) |
| [createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md#createaudiorenderer) |
| [createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md#createaudiorenderer) |
| [getAudioManager](arkts-audio-audio-getaudiomanager-f.md#getaudiomanager) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createAsrProcessingController](arkts-audio-audio-createasrprocessingcontroller-f-sys.md#createasrprocessingcontroller系统接口) |
| [createAsrProcessingController](arkts-audio-audio-createasrprocessingcontroller-f-sys.md#createasrprocessingcontroller系统接口) |
| [createGlobalAudioLoopback](arkts-audio-audio-createglobalaudioloopback-f-sys.md#createglobalaudioloopback系统接口) |
| [createMicInAudioCapturer](arkts-audio-audio-createmicinaudiocapturer-f-sys.md#createmicinaudiocapturer系统接口) |
| [createTonePlayer](arkts-audio-audio-createtoneplayer-f-sys.md#createtoneplayer系统接口) |
| [createTonePlayer](arkts-audio-audio-createtoneplayer-f-sys.md#createtoneplayer系统接口) |
| [createTonePlayer](arkts-audio-audio-createtoneplayer-f-sys.md#createtoneplayer系统接口) |
| [createTonePlayer](arkts-audio-audio-createtoneplayer-f-sys.md#createtoneplayer系统接口) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) |
| [AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md) |
| [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) |
| [AudioCapturerOptions](arkts-audio-audio-audiocaptureroptions-i.md) |
| [AudioDebuggingManager](arkts-audio-audio-audiodebuggingmanager-i.md) |
| [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) |
| [AudioDeviceEnhanceManager](arkts-audio-audio-audiodeviceenhancemanager-i.md) |
| [AudioDevicePair](arkts-audio-audio-audiodevicepair-i.md) |
| [AudioInterrupt](arkts-audio-audio-audiointerrupt-i.md) |
| [AudioLoopback](arkts-audio-audio-audioloopback-i.md) |
| [AudioManager](arkts-audio-audio-audiomanager-i.md) |
| [AudioPlaybackCaptureConfig](arkts-audio-audio-audioplaybackcaptureconfig-i.md) |
| [AudioRecordingManager](arkts-audio-audio-audiorecordingmanager-i.md) |
| [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) |
| [AudioRendererChangeInfo](arkts-audio-audio-audiorendererchangeinfo-i.md) |
| [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) |
| [AudioRendererOptions](arkts-audio-audio-audiorendereroptions-i.md) |
| [AudioRoutingManager](arkts-audio-audio-audioroutingmanager-i.md) |
| [AudioSessionDeactivatedEvent](arkts-audio-audio-audiosessiondeactivatedevent-i.md) |
| [AudioSessionManager](arkts-audio-audio-audiosessionmanager-i.md) |
| [AudioSessionStateChangedEvent](arkts-audio-audio-audiosessionstatechangedevent-i.md) |
| [AudioSessionStrategy](arkts-audio-audio-audiosessionstrategy-i.md) |
| [AudioSpatializationManager](arkts-audio-audio-audiospatializationmanager-i.md) |
| [AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md) |
| [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) |
| [AudioStreamManager](arkts-audio-audio-audiostreammanager-i.md) |
| [AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md) |
| [AudioVolumeGroupManager](arkts-audio-audio-audiovolumegroupmanager-i.md) |
| [AudioVolumeManager](arkts-audio-audio-audiovolumemanager-i.md) |
| [CaptureFilterOptions](arkts-audio-audio-capturefilteroptions-i.md) |
| [CurrentInputDeviceChangedEvent](arkts-audio-audio-currentinputdevicechangedevent-i.md) |
| [CurrentOutputDeviceChangedEvent](arkts-audio-audio-currentoutputdevicechangedevent-i.md) |
| [DeviceBlockStatusInfo](arkts-audio-audio-deviceblockstatusinfo-i.md) |
| [DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md) |
| [InterruptAction](arkts-audio-audio-interruptaction-i.md) |
| [InterruptEvent](arkts-audio-audio-interruptevent-i.md) |
| [MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md) |
| [StreamVolumeEvent](arkts-audio-audio-streamvolumeevent-i.md) |
| [SystemRecordControllerConfig](arkts-audio-audio-systemrecordcontrollerconfig-i.md) |
| [VolumeEvent](arkts-audio-audio-volumeevent-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ActiveStreamVolumeInfo](arkts-audio-audio-activestreamvolumeinfo-i-sys.md) |
| [AppIdInfo](arkts-audio-audio-appidinfo-i-sys.md) |
| [AsrProcessingController](arkts-audio-audio-asrprocessingcontroller-i-sys.md) |
| [AudioCapturer](arkts-audio-audio-audiocapturer-i-sys.md) |
| [AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i-sys.md) |
| [AudioCapturerFilter](arkts-audio-audio-audiocapturerfilter-i-sys.md) |
| [AudioCapturerMicInConfig](arkts-audio-audio-audiocapturermicinconfig-i-sys.md) |
| [AudioCapturerMicInData](arkts-audio-audio-audiocapturermicindata-i-sys.md) |
| [AudioCapturerOptions](arkts-audio-audio-audiocaptureroptions-i-sys.md) |
| [AudioCollaborativeManager](arkts-audio-audio-audiocollaborativemanager-i-sys.md) |
| [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i-sys.md) |
| [AudioDeviceEnhanceManager](arkts-audio-audio-audiodeviceenhancemanager-i-sys.md) |
| [AudioEffectManager](arkts-audio-audio-audioeffectmanager-i-sys.md) |
| [AudioEffectProperty](arkts-audio-audio-audioeffectproperty-i-sys.md) |
| [AudioHRTFAnonymousDescriptor](arkts-audio-audio-audiohrtfanonymousdescriptor-i-sys.md) |
| [AudioManager](arkts-audio-audio-audiomanager-i-sys.md) |
| [AudioPersonalizedSpatialEnabledChangeForAnyDevice](arkts-audio-audio-audiopersonalizedspatialenabledchangeforanydevice-i-sys.md) |
| [AudioRecordingManager](arkts-audio-audio-audiorecordingmanager-i-sys.md) |
| [AudioRenderer](arkts-audio-audio-audiorenderer-i-sys.md) |
| [AudioRendererChangeInfo](arkts-audio-audio-audiorendererchangeinfo-i-sys.md) |
| [AudioRendererFilter](arkts-audio-audio-audiorendererfilter-i-sys.md) |
| [AudioRendererOptions](arkts-audio-audio-audiorendereroptions-i-sys.md) |
| [AudioRoutingManager](arkts-audio-audio-audioroutingmanager-i-sys.md) |
| [AudioSpatialDeviceState](arkts-audio-audio-audiospatialdevicestate-i-sys.md) |
| [AudioSpatialEnabledStateForDevice](arkts-audio-audio-audiospatialenabledstatefordevice-i-sys.md) |
| [AudioSpatializationManager](arkts-audio-audio-audiospatializationmanager-i-sys.md) |
| [AudioVolumeGroupManager](arkts-audio-audio-audiovolumegroupmanager-i-sys.md) |
| [AudioVolumeManager](arkts-audio-audio-audiovolumemanager-i-sys.md) |
| [InterruptResult](arkts-audio-audio-interruptresult-i-sys.md) |
| [SoundCardInfo](arkts-audio-audio-soundcardinfo-i-sys.md) |
| [SystemRecordControllerChangeInfo](arkts-audio-audio-systemrecordcontrollerchangeinfo-i-sys.md) |
| [SystemVolumeFilter](arkts-audio-audio-systemvolumefilter-i-sys.md) |
| [TonePlayer](arkts-audio-audio-toneplayer-i-sys.md) |
| [VolumeEvent](arkts-audio-audio-volumeevent-i-sys.md) |
| [VolumeGroupInfo](arkts-audio-audio-volumegroupinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) |
| [AudioChannel](arkts-audio-audio-audiochannel-e.md) |
| [AudioChannelLayout](arkts-audio-audio-audiochannellayout-e.md) |
| [AudioConcurrencyMode](arkts-audio-audio-audioconcurrencymode-e.md) |
| [AudioDataCallbackResult](arkts-audio-audio-audiodatacallbackresult-e.md) |
| [AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md) |
| [AudioEncodingType](arkts-audio-audio-audioencodingtype-e.md) |
| [AudioErrors](arkts-audio-audio-audioerrors-e.md) |
| [AudioLatencyType](arkts-audio-audio-audiolatencytype-e.md) | 表示音频时延类型的枚举。 \| 名称 \| 值 \| 说明 \| \| ---- \| -- \| ---- \| \| LATENCY_TYPE_ALL \| 0 \| 计算包含软件和硬件在内的整体音频处理链路时延。 \| \| LATENCY_TYPE_SOFTWARE \| 1 \| 计算软件侧时延，包含软件音效。 \| \| LATENCY_TYPE_HARDWARE \| 2 \| 计算硬件侧时延，包含HAL、驱动和硬件。 \|
| [AudioLoopbackEqualizerPreset](arkts-audio-audio-audioloopbackequalizerpreset-e.md) |
| [AudioLoopbackMode](arkts-audio-audio-audioloopbackmode-e.md) |
| [AudioLoopbackReverbPreset](arkts-audio-audio-audioloopbackreverbpreset-e.md) |
| [AudioLoopbackStatus](arkts-audio-audio-audioloopbackstatus-e.md) |
| [AudioPlaybackCaptureMode](arkts-audio-audio-audioplaybackcapturemode-e.md) |
| [AudioPrivacyType](arkts-audio-audio-audioprivacytype-e.md) |
| [AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md) |
| [AudioRingMode](arkts-audio-audio-audioringmode-e.md) |
| [AudioSampleFormat](arkts-audio-audio-audiosampleformat-e.md) |
| [AudioSamplingRate](arkts-audio-audio-audiosamplingrate-e.md) |
| [AudioScene](arkts-audio-audio-audioscene-e.md) |
| [AudioSessionBehaviorFlags](arkts-audio-audio-audiosessionbehaviorflags-e.md) |
| [AudioSessionDeactivatedReason](arkts-audio-audio-audiosessiondeactivatedreason-e.md) |
| [AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md) |
| [AudioSessionStateChangeHint](arkts-audio-audio-audiosessionstatechangehint-e.md) |
| [AudioState](arkts-audio-audio-audiostate-e.md) |
| [AudioStreamDeviceChangeReason](arkts-audio-audio-audiostreamdevicechangereason-e.md) |
| [AudioVolumeMode](arkts-audio-audio-audiovolumemode-e.md) |
| [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) |
| [BluetoothAndNearlinkPreferredRecordCategory](arkts-audio-audio-bluetoothandnearlinkpreferredrecordcategory-e.md) |
| [ChannelBlendMode](arkts-audio-audio-channelblendmode-e.md) |
| [CommunicationDeviceType](arkts-audio-audio-communicationdevicetype-e.md) |
| [ContentType](arkts-audio-audio-contenttype-e.md) |
| [DeviceBlockStatus](arkts-audio-audio-deviceblockstatus-e.md) |
| [DeviceChangeType](arkts-audio-audio-devicechangetype-e.md) |
| [DeviceFlag](arkts-audio-audio-deviceflag-e.md) |
| [DeviceRole](arkts-audio-audio-devicerole-e.md) |
| [DeviceType](arkts-audio-audio-devicetype-e.md) |
| [DeviceUsage](arkts-audio-audio-deviceusage-e.md) |
| [InterruptActionType](arkts-audio-audio-interruptactiontype-e.md) |
| [InterruptForceType](arkts-audio-audio-interruptforcetype-e.md) |
| [InterruptHint](arkts-audio-audio-interrupthint-e.md) |
| [InterruptMode](arkts-audio-audio-interruptmode-e.md) |
| [InterruptType](arkts-audio-audio-interrupttype-e.md) |
| [NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md) |
| [OutputDeviceChangeRecommendedAction](arkts-audio-audio-outputdevicechangerecommendedaction-e.md) |
| [PlaybackCaptureStartState](arkts-audio-audio-playbackcapturestartstate-e.md) |
| [SourceType](arkts-audio-audio-sourcetype-e.md) |
| [StreamUsage](arkts-audio-audio-streamusage-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [AsrAecMode](arkts-audio-audio-asraecmode-e-sys.md) |
| [AsrNoiseSuppressionMode](arkts-audio-audio-asrnoisesuppressionmode-e-sys.md) |
| [AsrVoiceControlMode](arkts-audio-audio-asrvoicecontrolmode-e-sys.md) |
| [AsrVoiceMuteMode](arkts-audio-audio-asrvoicemutemode-e-sys.md) |
| [AsrWhisperDetectionMode](arkts-audio-audio-asrwhisperdetectionmode-e-sys.md) |
| [AudioDevcieSelectStrategy](arkts-audio-audio-audiodevcieselectstrategy-e-sys.md) |
| [AudioSeparationVolumeType](arkts-audio-audio-audioseparationvolumetype-e-sys.md) |
| [AudioSpatialDeviceType](arkts-audio-audio-audiospatialdevicetype-e-sys.md) |
| [AudioSpatializationSceneType](arkts-audio-audio-audiospatializationscenetype-e-sys.md) |
| [AudioVolumeType](arkts-audio-audio-audiovolumetype-e-sys.md) |
| [ConnectType](arkts-audio-audio-connecttype-e-sys.md) |
| [DeviceFlag](arkts-audio-audio-deviceflag-e-sys.md) |
| [DeviceType](arkts-audio-audio-devicetype-e-sys.md) |
| [EffectFlag](arkts-audio-audio-effectflag-e-sys.md) |
| [InterruptRequestResultType](arkts-audio-audio-interruptrequestresulttype-e-sys.md) |
| [InterruptRequestType](arkts-audio-audio-interruptrequesttype-e-sys.md) |
| [PolicyType](arkts-audio-audio-policytype-e-sys.md) |
| [RenderTarget](arkts-audio-audio-rendertarget-e-sys.md) |
| [SourceType](arkts-audio-audio-sourcetype-e-sys.md) |
| [SpatialAudioSourceType](arkts-audio-audio-spatialaudiosourcetype-e-sys.md) |
| [StreamUsage](arkts-audio-audio-streamusage-e-sys.md) |
| [ToneType](arkts-audio-audio-tonetype-e-sys.md) |
| [VolumeAdjustType](arkts-audio-audio-volumeadjusttype-e-sys.md) |
| [VolumeFlag](arkts-audio-audio-volumeflag-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md) |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) |
| [AudioEffectInfoArray](arkts-audio-audio-audioeffectinfoarray-t.md) |
| [AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md) |
| [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) |
| [DeviceTypeArray](arkts-audio-audio-devicetypearray-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [ActiveStreamsVolumeInfoArray](arkts-audio-audio-activestreamsvolumeinfoarray-t-sys.md) |
| [StreamUsageArray](arkts-audio-audio-streamusagearray-t-sys.md) |
| [VolumeGroupInfos](arkts-audio-audio-volumegroupinfos-t-sys.md) |
<!--DelEnd-->

### 常量

| 名称 |
| --- |
| [DEFAULT_INTERRUPT_GROUP_ID](arkts-audio-audio-con.md#defaultinterruptgroupid) |
| [DEFAULT_VOLUME_GROUP_ID](arkts-audio-audio-con.md#defaultvolumegroupid) |

<!--Del-->
### 常量（系统接口）

| 名称 |
| --- |
| [LOCAL_NETWORK_ID](arkts-audio-audio-con-sys.md#localnetworkid) |
<!--DelEnd-->
