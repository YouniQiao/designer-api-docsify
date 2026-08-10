# DialCallOptions（系统接口）

Indicates the options for initiating a call.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-call-export interface DialCallOptions--><!--Device-call-export interface DialCallOptions-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-DialCallOptions-accountId?: int--><!--Device-DialCallOptions-accountId?: int-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## dialScene

```TypeScript
dialScene?: DialScene
```

Indicates the scenario of the call.

**类型：** [DialScene](arkts-telephony-call-dialscene-e-sys.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-DialCallOptions-dialScene?: DialScene--><!--Device-DialCallOptions-dialScene?: DialScene-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## dialType

```TypeScript
dialType?: DialType
```

Indicates the type of the call.

**类型：** [DialType](arkts-telephony-call-dialtype-e-sys.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-DialCallOptions-dialType?: DialType--><!--Device-DialCallOptions-dialType?: DialType-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## extraParams

```TypeScript
extraParams?: Record<string, Object>
```

Indicates the extra call parameters.

**类型：** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

<!--Device-DialCallOptions-extraParams?: Record<string, Object>--><!--Device-DialCallOptions-extraParams?: Record<string, Object>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## videoState

```TypeScript
videoState?: VideoStateType
```

Indicates the type of Video state.

**类型：** [VideoStateType](arkts-telephony-call-videostatetype-e-sys.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-DialCallOptions-videoState?: VideoStateType--><!--Device-DialCallOptions-videoState?: VideoStateType-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## xCallType

```TypeScript
xCallType?: XCallType
```

Indicates the type of the xcall.

**类型：** [XCallType](arkts-telephony-call-xcalltype-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-DialCallOptions-xCallType?: XCallType--><!--Device-DialCallOptions-xCallType?: XCallType-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

