# AudioCapturerOptions

Describes audio capturer configurations.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioCapturerOptions--><!--Device-audio-interface AudioCapturerOptions-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## playbackCaptureUid

```TypeScript
playbackCaptureUid?: int
```

The target application uid for voice/video communication playback capture.This parameter takes effect only when \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_is set in \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. In other playback capture modes,this parameter is ignored.The value should be an integer.

**Type:** int

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

Perfered input device for this audio capturer. The preferredInputDevice must be an input device, and the source type in \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ must be \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ or\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, otherwise this parameter will be ignored.If the user does not specify a device, the system automatically selects the recording device for the audio capturer. When the user specifies a prefer device to create a recongition or transcription recording,

1) If the prefer device is online, the current audiocapturer may use the preferred device for recording; if the prefer device goes offline during operation, the system automatically selects a recording device.2) If the prefer device is offline, the system automatically selects a recording device;if the prefer device comes online during operation, it may switch to the prefer device for recording.Users can query the device which is in use by \_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_.

**Type:** AudioDeviceDescriptor

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AudioCapturerOptions-preferredInputDevice?: AudioDeviceDescriptor--><!--Device-AudioCapturerOptions-preferredInputDevice?: AudioDeviceDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

