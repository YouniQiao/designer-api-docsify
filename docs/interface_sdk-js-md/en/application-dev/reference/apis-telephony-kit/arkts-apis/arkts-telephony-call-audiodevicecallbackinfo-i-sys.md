# AudioDeviceCallbackInfo (System API)

Defines the audio device information.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## audioDeviceList

```TypeScript
audioDeviceList: Array<AudioDevice>
```

Audio device list.

**Type:** Array&lt;[AudioDevice](arkts-telephony-call-audiodevice-i-sys.md)&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## currentAudioDevice

```TypeScript
currentAudioDevice: AudioDevice
```

Current audio device.

**Type:** [AudioDevice](arkts-telephony-call-audiodevice-i-sys.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## isMicDisabled

```TypeScript
isMicDisabled?: boolean
```

Whether to disable the microphone.  
- **true**: yes. - **false**: no.

**Type:** boolean

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## isMuted

```TypeScript
isMuted: boolean
```

Whether the audio device is muted.

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.
