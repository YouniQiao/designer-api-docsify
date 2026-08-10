# hasVoiceCapability

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## hasVoiceCapability

```TypeScript
function hasVoiceCapability(): boolean
```

Checks whether a device supports voice calls.

The system checks whether the device has the capability to initiate a circuit switching (CS) or IP multimedia subsystem domain (IMS) call on a telephone service network. If the device supports only packet switching(even if the device supports OTT calls), {@code false} is returned.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-call-function hasVoiceCapability(): boolean--><!--Device-call-function hasVoiceCapability(): boolean-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

