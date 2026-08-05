# AudioDeviceCallbackInfo (System API)

Indicates the information of the audio device.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-call-export interface AudioDeviceCallbackInfo--><!--Device-call-export interface AudioDeviceCallbackInfo-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## audioDeviceList

```TypeScript
audioDeviceList: Array<AudioDevice>
```

Indicates the list of support audio device.

**Type:** Array&lt;AudioDevice&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AudioDeviceCallbackInfo-audioDeviceList: Array<AudioDevice>--><!--Device-AudioDeviceCallbackInfo-audioDeviceList: Array<AudioDevice>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## currentAudioDevice

```TypeScript
currentAudioDevice: AudioDevice
```

Indicates the type of current audio device.

**Type:** AudioDevice

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AudioDeviceCallbackInfo-currentAudioDevice: AudioDevice--><!--Device-AudioDeviceCallbackInfo-currentAudioDevice: AudioDevice-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## isMicDisabled

```TypeScript
isMicDisabled?: boolean
```

Indicates the status of microphone disabled.

**Type:** boolean

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-AudioDeviceCallbackInfo-isMicDisabled?: boolean--><!--Device-AudioDeviceCallbackInfo-isMicDisabled?: boolean-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## isMuted

```TypeScript
isMuted: boolean
```

Indicates the status of mute.

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AudioDeviceCallbackInfo-isMuted: boolean--><!--Device-AudioDeviceCallbackInfo-isMuted: boolean-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

