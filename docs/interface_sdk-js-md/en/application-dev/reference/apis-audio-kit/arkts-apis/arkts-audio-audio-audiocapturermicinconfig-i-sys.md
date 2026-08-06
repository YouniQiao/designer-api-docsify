# AudioCapturerMicInConfig (System API)

Describes audio capturer configuration that can capture microphone input (mic-in) audio data before any processing.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-audio-interface AudioCapturerMicInConfig--><!--Device-audio-interface AudioCapturerMicInConfig-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## capturerInfo

```TypeScript
capturerInfo: AudioCapturerInfo
```

Capturer attribute information.

**Type:** AudioCapturerInfo

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerMicInConfig-capturerInfo: AudioCapturerInfo--><!--Device-AudioCapturerMicInConfig-capturerInfo: AudioCapturerInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## ecStreamInfo

```TypeScript
ecStreamInfo?: AudioStreamInfo
```

Stream information that describes echo reference signal.If not set this attribute, the capturer will only record Mic-In audio stream.

**Type:** AudioStreamInfo

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerMicInConfig-ecStreamInfo?: AudioStreamInfo--><!--Device-AudioCapturerMicInConfig-ecStreamInfo?: AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## micInStreamInfo

```TypeScript
micInStreamInfo: AudioStreamInfo
```

Stream information that describes Mic-In audio stream.

**Type:** AudioStreamInfo

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerMicInConfig-micInStreamInfo: AudioStreamInfo--><!--Device-AudioCapturerMicInConfig-micInStreamInfo: AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## preferredInputDevice

```TypeScript
preferredInputDevice?: AudioDeviceDescriptor
```

Prefered input device for this audio capturer.The preferred device must be an input device, and the source type in\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ must be \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_,\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ or \_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_,otherwise this parameter will be ignored.If the user does not specify a device, the system will automatically select the recording device for the audio capturer.When the user specifies a preferred device:1) If the preferred device is online, the current audio capturer may use the preferred device for recording. If the preferred device becomes offline during recording, the system will select another device.2) If the preferred device is offline, the system will select a recording device.If the preferred device becomes online during recording, it may switch to the preferred device.The user can query the selected device by \_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_.

**Type:** AudioDeviceDescriptor

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerMicInConfig-preferredInputDevice?: AudioDeviceDescriptor--><!--Device-AudioCapturerMicInConfig-preferredInputDevice?: AudioDeviceDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## processedStreamInfo

```TypeScript
processedStreamInfo?: AudioStreamInfo
```

Stream information that describes the processed audio stream.

**Type:** AudioStreamInfo

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerMicInConfig-processedStreamInfo?: AudioStreamInfo--><!--Device-AudioCapturerMicInConfig-processedStreamInfo?: AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

