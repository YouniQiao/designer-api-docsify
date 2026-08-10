# ShortMessage

Defines an SMS message instance.

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface ShortMessage--><!--Device-sms-export interface ShortMessage-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## hasReplyPath

```TypeScript
hasReplyPath: boolean
```

Indicates whether the received SMS contains "TP-Reply-Path".

**类型：** boolean

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ShortMessage-hasReplyPath: boolean--><!--Device-ShortMessage-hasReplyPath: boolean-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## isReplaceMessage

```TypeScript
isReplaceMessage: boolean
```

Indicates whether the received SMS is a "replace short message".

**类型：** boolean

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ShortMessage-isReplaceMessage: boolean--><!--Device-ShortMessage-isReplaceMessage: boolean-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## isSmsStatusReportMessage

```TypeScript
isSmsStatusReportMessage: boolean
```

Indicates whether the current message is SMS-STATUS-REPORT.

**类型：** boolean

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ShortMessage-isSmsStatusReportMessage: boolean--><!--Device-ShortMessage-isSmsStatusReportMessage: boolean-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## messageClass

```TypeScript
messageClass: ShortMessageClass
```

Indicates the SMS type.

**类型：** [ShortMessageClass](arkts-telephony-sms-shortmessageclass-e.md)

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ShortMessage-messageClass: ShortMessageClass--><!--Device-ShortMessage-messageClass: ShortMessageClass-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## pdu

```TypeScript
pdu: Array<int>
```

Indicates Protocol Data Units (PDUs) from an SMS message.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ShortMessage-pdu: Array<int>--><!--Device-ShortMessage-pdu: Array<int>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## protocolId

```TypeScript
protocolId: int
```

Indicates the protocol identifier.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ShortMessage-protocolId: int--><!--Device-ShortMessage-protocolId: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## scAddress

```TypeScript
scAddress: string
```

Indicates the short message service center (SMSC) address.

**类型：** string

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ShortMessage-scAddress: string--><!--Device-ShortMessage-scAddress: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## scTimestamp

```TypeScript
scTimestamp: long
```

Indicates the SMSC timestamp.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ShortMessage-scTimestamp: long--><!--Device-ShortMessage-scTimestamp: long-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## status

```TypeScript
status: int
```

Indicates the SMS message status from the SMS-STATUS-REPORT message sent by the Short Message Service Center (SMSC).

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ShortMessage-status: int--><!--Device-ShortMessage-status: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## visibleMessageBody

```TypeScript
visibleMessageBody: string
```

Indicates the SMS message body.

**类型：** string

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ShortMessage-visibleMessageBody: string--><!--Device-ShortMessage-visibleMessageBody: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## visibleRawAddress

```TypeScript
visibleRawAddress: string
```

Indicates the address of the sender, which is to be displayed on the UI.

**类型：** string

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ShortMessage-visibleRawAddress: string--><!--Device-ShortMessage-visibleRawAddress: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

