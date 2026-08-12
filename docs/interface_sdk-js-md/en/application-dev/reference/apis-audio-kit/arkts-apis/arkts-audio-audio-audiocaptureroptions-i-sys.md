# AudioCapturerOptions

Describes audio capturer configurations.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioCapturerOptions--><!--Device-audio-interface AudioCapturerOptions-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## playbackCaptureUid

```TypeScript
playbackCaptureUid?: int
```

The target application uid for voice/video communication playback capture.This parameter takes effect only when [MODE_ONLY_VOIP](arkts-audio-audio-audioplaybackcapturemode-e-sys.md#MODE_ONLY_VOIP)is set in [playbackCaptureMode](arkts-audio-audio-audiocaptureroptions-i.md#playbackCaptureMode). In other playback capture modes,this parameter is ignored.The value should be an integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerOptions-playbackCaptureUid?: int--><!--Device-AudioCapturerOptions-playbackCaptureUid?: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

**System API:** This is a system API.

## preferredInputDevice

```TypeScript
preferredInputDevice?: AudioDeviceDescriptor
```

Perfered input device for this audio capturer. The preferredInputDevice must be an input device, and the source type in [captureInfo](captureInfo) must be [SOURCE_TYPE_RECONGITION](SourceType#SOURCE_TYPE_RECONGITION) or[SOURCE_TYPE_VOICE_TRANSCRIPTION](arkts-audio-audio-sourcetype-e-sys.md#SOURCE_TYPE_VOICE_TRANSCRIPTION), otherwise this parameter will be ignored.If the user does not specify a device, the system automatically selects the recording device for the audio capturer. When the user specifies a prefer device to create a recongition or transcription recording,

1) If the prefer device is online, the current audiocapturer may use the preferred device for recording; if the prefer device goes offline during operation, the system automatically selects a recording device.2) If the prefer device is offline, the system automatically selects a recording device;if the prefer device comes online during operation, it may switch to the prefer device for recording.Users can query the device which is in use by [getCurrentAudioCapturerChangeInfo](arkts-audio-audio-audiocapturer-i.md#getCurrentAudioCapturerChangeInfo).

**Type:** [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AudioCapturerOptions-preferredInputDevice?: AudioDeviceDescriptor--><!--Device-AudioCapturerOptions-preferredInputDevice?: AudioDeviceDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

