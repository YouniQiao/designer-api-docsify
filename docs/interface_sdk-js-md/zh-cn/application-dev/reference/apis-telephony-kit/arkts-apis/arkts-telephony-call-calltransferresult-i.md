# CallTransferResult

Indicates the result of call transfer.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-call-export interface CallTransferResult--><!--Device-call-export interface CallTransferResult-End-->

**系统能力：** SystemCapability.Telephony.CallManager

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## endHour

```TypeScript
endHour: int
```

Indicates the end time hours of call forwarding.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-CallTransferResult-endHour: int--><!--Device-CallTransferResult-endHour: int-End-->

**系统能力：** SystemCapability.Telephony.CallManager

## endMinute

```TypeScript
endMinute: int
```

Indicates the end time minutes of call forwarding.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-CallTransferResult-endMinute: int--><!--Device-CallTransferResult-endMinute: int-End-->

**系统能力：** SystemCapability.Telephony.CallManager

## number

```TypeScript
number: string
```

Indicates the phone number of call forwarding.

**类型：** string

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

<!--Device-CallTransferResult-number: string--><!--Device-CallTransferResult-number: string-End-->

**系统能力：** SystemCapability.Telephony.CallManager

## startHour

```TypeScript
startHour: int
```

Indicates the start time hours of call forwarding.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-CallTransferResult-startHour: int--><!--Device-CallTransferResult-startHour: int-End-->

**系统能力：** SystemCapability.Telephony.CallManager

## startMinute

```TypeScript
startMinute: int
```

Indicates the start time minutes of call forwarding.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-CallTransferResult-startMinute: int--><!--Device-CallTransferResult-startMinute: int-End-->

**系统能力：** SystemCapability.Telephony.CallManager

## status

```TypeScript
status: TransferStatus
```

Indicates the status of call forwarding.

**类型：** [TransferStatus](arkts-telephony-call-transferstatus-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-CallTransferResult-status: TransferStatus--><!--Device-CallTransferResult-status: TransferStatus-End-->

**系统能力：** SystemCapability.Telephony.CallManager

## teleNumber

```TypeScript
teleNumber: string
```

Indicates the phone number of call forwarding.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-CallTransferResult-teleNumber: string--><!--Device-CallTransferResult-teleNumber: string-End-->

**系统能力：** SystemCapability.Telephony.CallManager

