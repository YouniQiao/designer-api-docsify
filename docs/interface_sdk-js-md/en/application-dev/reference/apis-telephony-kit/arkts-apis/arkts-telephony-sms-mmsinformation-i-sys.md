# MmsInformation (System API)

Defines the MMS message information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sms-export interface MmsInformation--><!--Device-sms-export interface MmsInformation-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## attachment

```TypeScript
attachment?: Array<MmsAttachment>
```

Attachment.

**Type:** Array&lt;[MmsAttachment](arkts-telephony-sms-mmsattachment-i-sys.md)&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsInformation-attachment?: Array<MmsAttachment>--><!--Device-MmsInformation-attachment?: Array<MmsAttachment>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## messageType

```TypeScript
messageType: MessageType
```

Message type.

**Type:** MessageType

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsInformation-messageType: MessageType--><!--Device-MmsInformation-messageType: MessageType-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## mmsType

```TypeScript
mmsType: MmsSendReq | MmsSendConf | MmsNotificationInd | MmsRespInd | MmsRetrieveConf | MmsAcknowledgeInd | MmsDeliveryInd | MmsReadOrigInd | MmsReadRecInd
```

PDU header type.

**Type:** [MmsSendReq](arkts-telephony-sms-mmssendreq-i-sys.md) \| [MmsSendConf](arkts-telephony-sms-mmssendconf-i-sys.md) \| [MmsNotificationInd](arkts-telephony-sms-mmsnotificationind-i-sys.md) \| [MmsRespInd](arkts-telephony-sms-mmsrespind-i-sys.md) \| [MmsRetrieveConf](arkts-telephony-sms-mmsretrieveconf-i-sys.md) \| [MmsAcknowledgeInd](arkts-telephony-sms-mmsacknowledgeind-i-sys.md) \| [MmsDeliveryInd](arkts-telephony-sms-mmsdeliveryind-i-sys.md) \| [MmsReadOrigInd](arkts-telephony-sms-mmsreadorigind-i-sys.md) \| [MmsReadRecInd](arkts-telephony-sms-mmsreadrecind-i-sys.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsInformation-mmsType: MmsSendReq | MmsSendConf | MmsNotificationInd | MmsRespInd | MmsRetrieveConf | MmsAcknowledgeInd | MmsDeliveryInd | MmsReadOrigInd | MmsReadRecInd--><!--Device-MmsInformation-mmsType: MmsSendReq | MmsSendConf | MmsNotificationInd | MmsRespInd | MmsRetrieveConf | MmsAcknowledgeInd | MmsDeliveryInd | MmsReadOrigInd | MmsReadRecInd-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

