# CallAttributeOptions（系统接口）

Indicates the options of call attribute.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-call-export interface CallAttributeOptions--><!--Device-call-export interface CallAttributeOptions-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## accountId

```TypeScript
accountId: int
```

Indicates the id of account.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-accountId: int--><!--Device-CallAttributeOptions-accountId: int-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## accountNumber

```TypeScript
accountNumber: string
```

Indicates the number of account.

**类型：** string

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-accountNumber: string--><!--Device-CallAttributeOptions-accountNumber: string-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## callId

```TypeScript
callId: int
```

Indicates the id of call.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-callId: int--><!--Device-CallAttributeOptions-callId: int-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## callState

```TypeScript
callState: DetailedCallState
```

Indicates the detailed state of call.

**类型：** [DetailedCallState](arkts-telephony-call-detailedcallstate-e-sys.md)

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-callState: DetailedCallState--><!--Device-CallAttributeOptions-callState: DetailedCallState-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## callType

```TypeScript
callType: CallType
```

Indicates the type of call.

**类型：** [CallType](arkts-telephony-call-calltype-e-sys.md)

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-callType: CallType--><!--Device-CallAttributeOptions-callType: CallType-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## conferenceState

```TypeScript
conferenceState: ConferenceState
```

Indicates the state of conference.

**类型：** [ConferenceState](arkts-telephony-call-conferencestate-e-sys.md)

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-conferenceState: ConferenceState--><!--Device-CallAttributeOptions-conferenceState: ConferenceState-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## crsType

```TypeScript
crsType: int
```

Indicates the color tone type.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-crsType: int--><!--Device-CallAttributeOptions-crsType: int-End-->

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

<!--Device-CallAttributeOptions-extraParams?: Record<string, Object>--><!--Device-CallAttributeOptions-extraParams?: Record<string, Object>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## isCustomAccessibility

```TypeScript
isCustomAccessibility?: boolean
```

Indicates is custom accessibility enabled.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-CallAttributeOptions-isCustomAccessibility?: boolean--><!--Device-CallAttributeOptions-isCustomAccessibility?: boolean-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## isEcc

```TypeScript
isEcc: boolean
```

Indicates if this is an emergency call.

**类型：** boolean

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-isEcc: boolean--><!--Device-CallAttributeOptions-isEcc: boolean-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## numberLocation

```TypeScript
numberLocation?: string
```

Indicates the location of the phone number.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-numberLocation?: string--><!--Device-CallAttributeOptions-numberLocation?: string-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## numberMarkInfo

```TypeScript
numberMarkInfo?: NumberMarkInfo
```

Indicates the mark information of the phone number.

**类型：** [NumberMarkInfo](arkts-telephony-call-numbermarkinfo-i-sys.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-numberMarkInfo?: NumberMarkInfo--><!--Device-CallAttributeOptions-numberMarkInfo?: NumberMarkInfo-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## originalCallType

```TypeScript
originalCallType: int
```

Indicates the initial type of this call.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-originalCallType: int--><!--Device-CallAttributeOptions-originalCallType: int-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## rttState

```TypeScript
rttState?: RttState
```

Indicates the rtt state.

**类型：** [RttState](arkts-telephony-call-rttstate-e-sys.md)

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-rttState?: RttState--><!--Device-CallAttributeOptions-rttState?: RttState-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## speakerphoneOn

```TypeScript
speakerphoneOn: boolean
```

Indicates if the call is start with speaker.

**类型：** boolean

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-speakerphoneOn: boolean--><!--Device-CallAttributeOptions-speakerphoneOn: boolean-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## startTime

```TypeScript
startTime: int
```

Indicates the start time.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-startTime: int--><!--Device-CallAttributeOptions-startTime: int-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## videoState

```TypeScript
videoState: VideoStateType
```

Indicates the type of video state.

**类型：** [VideoStateType](arkts-telephony-call-videostatetype-e-sys.md)

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-videoState: VideoStateType--><!--Device-CallAttributeOptions-videoState: VideoStateType-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## voipCallAttribute

```TypeScript
voipCallAttribute?: VoipCallAttribute
```

Indicates the detail information of voip call.

**类型：** [VoipCallAttribute](arkts-telephony-call-voipcallattribute-i-sys.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-CallAttributeOptions-voipCallAttribute?: VoipCallAttribute--><!--Device-CallAttributeOptions-voipCallAttribute?: VoipCallAttribute-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## xCallType

```TypeScript
xCallType?: XCallType
```

Indicates the xcall type.

**类型：** [XCallType](arkts-telephony-call-xcalltype-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-CallAttributeOptions-xCallType?: XCallType--><!--Device-CallAttributeOptions-xCallType?: XCallType-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

