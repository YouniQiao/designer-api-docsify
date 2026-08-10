# AudioDeviceCallbackInfo（系统接口）

Indicates the information of the audio device.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-call-export interface AudioDeviceCallbackInfo--><!--Device-call-export interface AudioDeviceCallbackInfo-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## audioDeviceList

```TypeScript
audioDeviceList: Array<AudioDevice>
```

Indicates the list of support audio device.

**类型：** Array&lt;AudioDevice&gt;

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-AudioDeviceCallbackInfo-audioDeviceList: Array<AudioDevice>--><!--Device-AudioDeviceCallbackInfo-audioDeviceList: Array<AudioDevice>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## currentAudioDevice

```TypeScript
currentAudioDevice: AudioDevice
```

Indicates the type of current audio device.

**类型：** [AudioDevice](arkts-telephony-call-audiodevice-i-sys.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-AudioDeviceCallbackInfo-currentAudioDevice: AudioDevice--><!--Device-AudioDeviceCallbackInfo-currentAudioDevice: AudioDevice-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## isMicDisabled

```TypeScript
isMicDisabled?: boolean
```

Indicates the status of microphone disabled.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-AudioDeviceCallbackInfo-isMicDisabled?: boolean--><!--Device-AudioDeviceCallbackInfo-isMicDisabled?: boolean-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## isMuted

```TypeScript
isMuted: boolean
```

Indicates the status of mute.

**类型：** boolean

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-AudioDeviceCallbackInfo-isMuted: boolean--><!--Device-AudioDeviceCallbackInfo-isMuted: boolean-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

