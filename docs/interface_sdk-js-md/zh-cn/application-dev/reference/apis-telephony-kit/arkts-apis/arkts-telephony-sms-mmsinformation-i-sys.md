# MmsInformation（系统接口）

Defines the MMS message information.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface MmsInformation--><!--Device-sms-export interface MmsInformation-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## attachment

```TypeScript
attachment?: Array<MmsAttachment>
```

Indicates the attachment for the MMS message.

**类型：** Array&lt;MmsAttachment&gt;

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsInformation-attachment?: Array<MmsAttachment>--><!--Device-MmsInformation-attachment?: Array<MmsAttachment>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## messageType

```TypeScript
messageType: MessageType
```

Indicates the message type for the MMS message.

**类型：** [MessageType](../../apis-arkts/arkts-apis/arkts-arkts-messagetype-t.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsInformation-messageType: MessageType--><!--Device-MmsInformation-messageType: MessageType-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## mmsType

```TypeScript
mmsType: MmsSendReq | MmsSendConf | MmsNotificationInd | MmsRespInd | MmsRetrieveConf | MmsAcknowledgeInd | MmsDeliveryInd | MmsReadOrigInd | MmsReadRecInd
```

Indicates the PDU header type for the MMS message.

**类型：** [MmsSendReq](arkts-telephony-sms-mmssendreq-i-sys.md) \| MmsSendConf \| MmsNotificationInd \| MmsRespInd \| MmsRetrieveConf \| MmsAcknowledgeInd \| MmsDeliveryInd \| MmsReadOrigInd \| MmsReadRecInd

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsInformation-mmsType: MmsSendReq | MmsSendConf | MmsNotificationInd | MmsRespInd | MmsRetrieveConf | MmsAcknowledgeInd | MmsDeliveryInd | MmsReadOrigInd | MmsReadRecInd--><!--Device-MmsInformation-mmsType: MmsSendReq | MmsSendConf | MmsNotificationInd | MmsRespInd | MmsRetrieveConf | MmsAcknowledgeInd | MmsDeliveryInd | MmsReadOrigInd | MmsReadRecInd-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

