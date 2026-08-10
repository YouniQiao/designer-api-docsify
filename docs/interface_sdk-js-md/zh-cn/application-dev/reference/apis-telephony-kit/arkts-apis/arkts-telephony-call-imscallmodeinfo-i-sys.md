# ImsCallModeInfo（系统接口）

Indicates the ims call mode info of a video call.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-call-export interface ImsCallModeInfo--><!--Device-call-export interface ImsCallModeInfo-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## callId

```TypeScript
callId: int
```

Indicates the id of call.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-ImsCallModeInfo-callId: int--><!--Device-ImsCallModeInfo-callId: int-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## imsCallMode

```TypeScript
imsCallMode: ImsCallMode
```

Indicates the ImsCallMode of call.

**类型：** [ImsCallMode](arkts-telephony-call-imscallmode-e-sys.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-ImsCallModeInfo-imsCallMode: ImsCallMode--><!--Device-ImsCallModeInfo-imsCallMode: ImsCallMode-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## isRequestInfo

```TypeScript
isRequestInfo: boolean
```

Indicates if this is a request which received from remote,

**类型：** boolean

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-ImsCallModeInfo-isRequestInfo: boolean--><!--Device-ImsCallModeInfo-isRequestInfo: boolean-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## result

```TypeScript
result: VideoRequestResultType
```

Indicates the request result.

**类型：** [VideoRequestResultType](arkts-telephony-call-videorequestresulttype-e-sys.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-ImsCallModeInfo-result: VideoRequestResultType--><!--Device-ImsCallModeInfo-result: VideoRequestResultType-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

