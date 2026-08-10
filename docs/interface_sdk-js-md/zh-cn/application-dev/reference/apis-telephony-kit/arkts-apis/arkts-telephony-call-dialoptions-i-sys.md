# DialOptions

Indicates the options of placing a call.

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-call-export interface DialOptions--><!--Device-call-export interface DialOptions-End-->

**系统能力：** SystemCapability.Telephony.CallManager

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## accountId

```TypeScript
accountId?: int
```

Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-DialOptions-accountId?: int--><!--Device-DialOptions-accountId?: int-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## dialScene

```TypeScript
dialScene?: DialScene
```

Indicates the scenario of the call to be made.

**类型：** [DialScene](arkts-telephony-call-dialscene-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-DialOptions-dialScene?: DialScene--><!--Device-DialOptions-dialScene?: DialScene-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## dialType

```TypeScript
dialType?: DialType
```

Indicates the type of the call to be made.

**类型：** [DialType](arkts-telephony-call-dialtype-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-DialOptions-dialType?: DialType--><!--Device-DialOptions-dialType?: DialType-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## videoState

```TypeScript
videoState?: VideoStateType
```

Indicates the type of Video state.

**类型：** [VideoStateType](arkts-telephony-call-videostatetype-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-DialOptions-videoState?: VideoStateType--><!--Device-DialOptions-videoState?: VideoStateType-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

