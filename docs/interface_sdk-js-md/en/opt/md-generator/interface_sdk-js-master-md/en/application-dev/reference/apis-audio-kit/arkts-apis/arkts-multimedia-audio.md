# @ohos.multimedia.audio

The module provides basic audio control capabilities, including volume adjustment, device management, data capture,and rendering.

This module provides the following common audio-related functions:

- [AudioManager](arkts-multimedia-audio.md): audio manager.  
- [AudioRenderer](arkts-multimedia-audio.md): audio renderer, used to play Pulse Code Modulation (PCM) audio  
data.  
- [AudioCapturer](arkts-multimedia-audio.md): audio capturer, used to record PCM audio data.

**Since:** 7

<!--Device-unnamed-declare namespace audio--><!--Device-unnamed-declare namespace audio-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md#createaudiocapturer) |
| [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md#createaudiocapturer-1) |
| [createAudioLoopback](arkts-audio-audio-createaudioloopback-f.md#createaudioloopback) |
| [createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md#createaudiorenderer) |
| [createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md#createaudiorenderer-1) |
| [getAudioManager](arkts-audio-audio-getaudiomanager-f.md#getaudiomanager) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createAsrProcessingController](arkts-audio-audio-createasrprocessingcontroller-f-sys.md#createasrprocessingcontroller) |
| [createGlobalAudioLoopback](arkts-audio-audio-createglobalaudioloopback-f-sys.md#createglobalaudioloopback) |
| [createMicInAudioCapturer](arkts-audio-audio-createmicinaudiocapturer-f-sys.md#createmicinaudiocapturer) |
| [createTonePlayer](arkts-audio-audio-createtoneplayer-f-sys.md#createtoneplayer) |
| [createTonePlayer](arkts-audio-audio-createtoneplayer-f-sys.md#createtoneplayer-1) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
| [AudioRendererTargetParams](arkts-audio-audio-audiorenderertargetparams-i-sys.md) |
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

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) |
| [AudioChannel](arkts-audio-audio-audiochannel-e.md) |
| [AudioChannelLayout](arkts-audio-audio-audiochannellayout-e.md) |
| [AudioConcurrencyMode](arkts-audio-audio-audioconcurrencymode-e.md) |
| [AudioDataCallbackResult](arkts-audio-audio-audiodatacallbackresult-e.md) |
| [AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md) |
| [AudioEncodingType](arkts-audio-audio-audioencodingtype-e.md) |
| [AudioErrors](arkts-audio-audio-audioerrors-e.md) |
| [AudioLatencyType](arkts-audio-audio-audiolatencytype-e.md) |
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
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AsrAecMode](arkts-audio-audio-asraecmode-e-sys.md) |
| [AsrNoiseSuppressionMode](arkts-audio-audio-asrnoisesuppressionmode-e-sys.md) |
| [AsrVoiceControlMode](arkts-audio-audio-asrvoicecontrolmode-e-sys.md) |
| [AsrVoiceMuteMode](arkts-audio-audio-asrvoicemutemode-e-sys.md) |
| [AsrWhisperDetectionMode](arkts-audio-audio-asrwhisperdetectionmode-e-sys.md) |
| [AudioDevcieSelectStrategy](arkts-audio-audio-audiodevcieselectstrategy-e-sys.md) |
| [AudioPlaybackCaptureMode](arkts-audio-audio-audioplaybackcapturemode-e-sys.md) |
| [AudioSeparationVolumeType](arkts-audio-audio-audioseparationvolumetype-e-sys.md) |
| [AudioSessionBehaviorFlags](arkts-audio-audio-audiosessionbehaviorflags-e-sys.md) |
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

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md) |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) |
| [AudioEffectInfoArray](arkts-audio-audio-audioeffectinfoarray-t.md) |
| [AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md) |
| [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) |
| [DeviceTypeArray](arkts-audio-audio-devicetypearray-t.md) |

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActiveStreamsVolumeInfoArray](arkts-audio-audio-activestreamsvolumeinfoarray-t-sys.md) |
| [StreamUsageArray](arkts-audio-audio-streamusagearray-t-sys.md) |
| [VolumeGroupInfos](arkts-audio-audio-volumegroupinfos-t-sys.md) |
<!--DelEnd-->

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DEFAULT_INTERRUPT_GROUP_ID](arkts-audio-audio-con.md#default_interrupt_group_id) |
| [DEFAULT_VOLUME_GROUP_ID](arkts-audio-audio-con.md#default_volume_group_id) |

<!--Del-->
### Constants（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LOCAL_NETWORK_ID](arkts-audio-audio-con-sys.md#local_network_id) |
<!--DelEnd-->
