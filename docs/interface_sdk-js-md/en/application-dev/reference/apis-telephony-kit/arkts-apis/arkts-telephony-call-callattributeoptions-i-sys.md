# CallAttributeOptions (System API)

Defines the call attribute options.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-call-export interface CallAttributeOptions--><!--Device-call-export interface CallAttributeOptions-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { call } from 'call';
```

## accountId

```TypeScript
accountId: int
```

Account ID.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-accountId: int--><!--Device-CallAttributeOptions-accountId: int-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## accountNumber

```TypeScript
accountNumber: string
```

Account number.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-accountNumber: string--><!--Device-CallAttributeOptions-accountNumber: string-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## callId

```TypeScript
callId: int
```

Call ID.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-callId: int--><!--Device-CallAttributeOptions-callId: int-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## callState

```TypeScript
callState: DetailedCallState
```

Detailed call state.

**Type:** [DetailedCallState](arkts-telephony-call-detailedcallstate-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-callState: DetailedCallState--><!--Device-CallAttributeOptions-callState: DetailedCallState-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## callType

```TypeScript
callType: CallType
```

Enumerates call types.

**Type:** [CallType](arkts-telephony-call-calltype-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-callType: CallType--><!--Device-CallAttributeOptions-callType: CallType-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## conferenceState

```TypeScript
conferenceState: ConferenceState
```

Enumerates conference states.

**Type:** [ConferenceState](arkts-telephony-call-conferencestate-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-conferenceState: ConferenceState--><!--Device-CallAttributeOptions-conferenceState: ConferenceState-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## crsType

```TypeScript
crsType: int
```

Video RBT type.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-crsType: int--><!--Device-CallAttributeOptions-crsType: int-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## extraParams

```TypeScript
extraParams?: Record<string, Object>
```

Indicates the extra call parameters.

**Type:** Record&lt;string, Object&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-extraParams?: Record<string, Object>--><!--Device-CallAttributeOptions-extraParams?: Record<string, Object>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## isCustomAccessibility

```TypeScript
isCustomAccessibility?: boolean
```

Indicates is custom accessibility enabled.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-isCustomAccessibility?: boolean--><!--Device-CallAttributeOptions-isCustomAccessibility?: boolean-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## isEcc

```TypeScript
isEcc: boolean
```

Whether the call is an ECC. The default value is **false**. - **true**: yes - **false**: no

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-isEcc: boolean--><!--Device-CallAttributeOptions-isEcc: boolean-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## numberLocation

```TypeScript
numberLocation?: string
```

Home location area of the number.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-numberLocation?: string--><!--Device-CallAttributeOptions-numberLocation?: string-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## numberMarkInfo

```TypeScript
numberMarkInfo?: NumberMarkInfo
```

Number mark.

**Type:** [NumberMarkInfo](arkts-telephony-call-numbermarkinfo-i-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-numberMarkInfo?: NumberMarkInfo--><!--Device-CallAttributeOptions-numberMarkInfo?: NumberMarkInfo-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## originalCallType

```TypeScript
originalCallType: int
```

Original call type of the Video RBT service.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-originalCallType: int--><!--Device-CallAttributeOptions-originalCallType: int-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## rttState

```TypeScript
rttState?: RttState
```

Indicates the rtt state.

**Type:** [RttState](arkts-telephony-call-rttstate-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-rttState?: RttState--><!--Device-CallAttributeOptions-rttState?: RttState-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## speakerphoneOn

```TypeScript
speakerphoneOn: boolean
```

Whether the speakerphone is used to answer a call. The default value is **false**. - **true**: yes - **false**: no

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-speakerphoneOn: boolean--><!--Device-CallAttributeOptions-speakerphoneOn: boolean-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## startTime

```TypeScript
startTime: int
```

Start time.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-startTime: int--><!--Device-CallAttributeOptions-startTime: int-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## videoState

```TypeScript
videoState: VideoStateType
```

Video state type.

**Type:** [VideoStateType](arkts-telephony-call-videostatetype-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-videoState: VideoStateType--><!--Device-CallAttributeOptions-videoState: VideoStateType-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## voipCallAttribute

```TypeScript
voipCallAttribute?: VoipCallAttribute
```

Defines the VoIP call information.

**Type:** [VoipCallAttribute](arkts-telephony-call-voipcallattribute-i-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-voipCallAttribute?: VoipCallAttribute--><!--Device-CallAttributeOptions-voipCallAttribute?: VoipCallAttribute-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## xCallType

```TypeScript
xCallType?: XCallType
```

X-Call type.

**Type:** [XCallType](arkts-telephony-call-xcalltype-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-CallAttributeOptions-xCallType?: XCallType--><!--Device-CallAttributeOptions-xCallType?: XCallType-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

