# ImsCallModeInfo (System API)

Indicates the ims call mode info of a video call.

**Since:** 11

<!--Device-call-export interface ImsCallModeInfo--><!--Device-call-export interface ImsCallModeInfo-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## callId

```TypeScript
callId: number
```

Indicates the id of call.

**Type:** number

**Since:** 11

<!--Device-ImsCallModeInfo-callId: int--><!--Device-ImsCallModeInfo-callId: int-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## imsCallMode

```TypeScript
imsCallMode: ImsCallMode
```

Indicates the ImsCallMode of call.

**Type:** ImsCallMode

**Since:** 11

<!--Device-ImsCallModeInfo-imsCallMode: ImsCallMode--><!--Device-ImsCallModeInfo-imsCallMode: ImsCallMode-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## isRequestInfo

```TypeScript
isRequestInfo: boolean
```

Indicates if this is a request which received from remote,

**Type:** boolean

**Since:** 11

<!--Device-ImsCallModeInfo-isRequestInfo: boolean--><!--Device-ImsCallModeInfo-isRequestInfo: boolean-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## result

```TypeScript
result: VideoRequestResultType
```

Indicates the request result.

**Type:** VideoRequestResultType

**Since:** 11

<!--Device-ImsCallModeInfo-result: VideoRequestResultType--><!--Device-ImsCallModeInfo-result: VideoRequestResultType-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

