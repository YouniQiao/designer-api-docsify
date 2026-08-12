# ImsCallModeInfo (System API)

Indicates the ims call mode info of a video call.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-call-export interface ImsCallModeInfo--><!--Device-call-export interface ImsCallModeInfo-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## callId

```TypeScript
callId: int
```

Indicates the id of call.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ImsCallModeInfo-callId: int--><!--Device-ImsCallModeInfo-callId: int-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## imsCallMode

```TypeScript
imsCallMode: ImsCallMode
```

Indicates the ImsCallMode of call.

**Type:** [ImsCallMode](arkts-telephony-call-imscallmode-e-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

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

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ImsCallModeInfo-isRequestInfo: boolean--><!--Device-ImsCallModeInfo-isRequestInfo: boolean-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## result

```TypeScript
result: VideoRequestResultType
```

Indicates the request result.

**Type:** [VideoRequestResultType](arkts-telephony-call-videorequestresulttype-e-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ImsCallModeInfo-result: VideoRequestResultType--><!--Device-ImsCallModeInfo-result: VideoRequestResultType-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

