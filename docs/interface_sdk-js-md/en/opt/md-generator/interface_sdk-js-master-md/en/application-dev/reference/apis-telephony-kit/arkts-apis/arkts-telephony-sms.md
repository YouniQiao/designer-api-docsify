# @ohos.telephony.sms

The **sms** module provides basic SMS management functions. With the APIs provided by this module, you can create and send SMS messages, and obtain the ID of the default SIM card used to send and receive SMS messages, and check whether the current device can send and receive SMS messages.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace sms--><!--Device-unnamed-declare namespace sms-End-->

**System capability:** SystemCapability.Telephony.SmsMms

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createMessage](arkts-telephony-sms-createmessage-f.md#createMessage) |
| [createMessage](arkts-telephony-sms-createmessage-f.md#createMessage) |
| [getDefaultSmsSimId](arkts-telephony-sms-getdefaultsmssimid-f.md#getDefaultSmsSimId) |
| [getDefaultSmsSimId](arkts-telephony-sms-getdefaultsmssimid-f.md#getDefaultSmsSimId) |
| [getDefaultSmsSlotId](arkts-telephony-sms-getdefaultsmsslotid-f.md#getDefaultSmsSlotId) |
| [getDefaultSmsSlotId](arkts-telephony-sms-getdefaultsmsslotid-f.md#getDefaultSmsSlotId) |
| [hasSmsCapability](arkts-telephony-sms-hassmscapability-f.md#hasSmsCapability) |
| [sendMessage](arkts-telephony-sms-sendmessage-f.md#sendMessage) |
| [sendShortMessage](arkts-telephony-sms-sendshortmessage-f.md#sendShortMessage) |
| [sendShortMessage](arkts-telephony-sms-sendshortmessage-f.md#sendShortMessage) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSimMessage](arkts-telephony-sms-addsimmessage-f-sys.md#addSimMessage-(System-API)) |
| [addSimMessage](arkts-telephony-sms-addsimmessage-f-sys.md#addSimMessage-(System-API)) |
| [decodeMms](arkts-telephony-sms-decodemms-f-sys.md#decodeMms-(System-API)) |
| [decodeMms](arkts-telephony-sms-decodemms-f-sys.md#decodeMms-(System-API)) |
| [delSimMessage](arkts-telephony-sms-delsimmessage-f-sys.md#delSimMessage-(System-API)) |
| [delSimMessage](arkts-telephony-sms-delsimmessage-f-sys.md#delSimMessage-(System-API)) |
| [downloadMms](arkts-telephony-sms-downloadmms-f-sys.md#downloadMms-(System-API)) |
| [downloadMms](arkts-telephony-sms-downloadmms-f-sys.md#downloadMms-(System-API)) |
| [encodeMms](arkts-telephony-sms-encodemms-f-sys.md#encodeMms-(System-API)) |
| [encodeMms](arkts-telephony-sms-encodemms-f-sys.md#encodeMms-(System-API)) |
| [getAllSimMessages](arkts-telephony-sms-getallsimmessages-f-sys.md#getAllSimMessages-(System-API)) |
| [getAllSimMessages](arkts-telephony-sms-getallsimmessages-f-sys.md#getAllSimMessages-(System-API)) |
| [getImsShortMessageFormat](arkts-telephony-sms-getimsshortmessageformat-f-sys.md#getImsShortMessageFormat-(System-API)) |
| [getImsShortMessageFormat](arkts-telephony-sms-getimsshortmessageformat-f-sys.md#getImsShortMessageFormat-(System-API)) |
| [getSmsSegmentsInfo](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md#getSmsSegmentsInfo-(System-API)) |
| [getSmsSegmentsInfo](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md#getSmsSegmentsInfo-(System-API)) |
| [getSmsShortCodeType](arkts-telephony-sms-getsmsshortcodetype-f-sys.md#getSmsShortCodeType-(System-API)) |
| [getSmscAddr](arkts-telephony-sms-getsmscaddr-f-sys.md#getSmscAddr-(System-API)) |
| [getSmscAddr](arkts-telephony-sms-getsmscaddr-f-sys.md#getSmscAddr-(System-API)) |
| [isImsSmsSupported](arkts-telephony-sms-isimssmssupported-f-sys.md#isImsSmsSupported-(System-API)) |
| [isImsSmsSupported](arkts-telephony-sms-isimssmssupported-f-sys.md#isImsSmsSupported-(System-API)) |
| [sendMms](arkts-telephony-sms-sendmms-f-sys.md#sendMms-(System-API)) |
| [sendMms](arkts-telephony-sms-sendmms-f-sys.md#sendMms-(System-API)) |
| [setCBConfig](arkts-telephony-sms-setcbconfig-f-sys.md#setCBConfig-(System-API)) |
| [setCBConfig](arkts-telephony-sms-setcbconfig-f-sys.md#setCBConfig-(System-API)) |
| [setCBConfigList](arkts-telephony-sms-setcbconfiglist-f-sys.md#setCBConfigList-(System-API)) |
| [setDefaultSmsSlotId](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md#setDefaultSmsSlotId-(System-API)) |
| [setDefaultSmsSlotId](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md#setDefaultSmsSlotId-(System-API)) |
| [setSmscAddr](arkts-telephony-sms-setsmscaddr-f-sys.md#setSmscAddr-(System-API)) |
| [setSmscAddr](arkts-telephony-sms-setsmscaddr-f-sys.md#setSmscAddr-(System-API)) |
| [splitMessage](arkts-telephony-sms-splitmessage-f-sys.md#splitMessage-(System-API)) |
| [splitMessage](arkts-telephony-sms-splitmessage-f-sys.md#splitMessage-(System-API)) |
| [updateSimMessage](arkts-telephony-sms-updatesimmessage-f-sys.md#updateSimMessage-(System-API)) |
| [updateSimMessage](arkts-telephony-sms-updatesimmessage-f-sys.md#updateSimMessage-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [IDeliveryShortMessageCallback](arkts-telephony-sms-ideliveryshortmessagecallback-i.md) |
| [ISendShortMessageCallback](arkts-telephony-sms-isendshortmessagecallback-i.md) |
| [SendMessageOptions](arkts-telephony-sms-sendmessageoptions-i.md) |
| [ShortMessage](arkts-telephony-sms-shortmessage-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CBConfigListConfigs](arkts-telephony-sms-cbconfiglistconfigs-i-sys.md) |
| [CBConfigOptions](arkts-telephony-sms-cbconfigoptions-i-sys.md) |
| [MmsAcknowledgeInd](arkts-telephony-sms-mmsacknowledgeind-i-sys.md) |
| [MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md) |
| [MmsAttachment](arkts-telephony-sms-mmsattachment-i-sys.md) |
| [MmsConfig](arkts-telephony-sms-mmsconfig-i-sys.md) |
| [MmsDeliveryInd](arkts-telephony-sms-mmsdeliveryind-i-sys.md) |
| [MmsInformation](arkts-telephony-sms-mmsinformation-i-sys.md) |
| [MmsNotificationInd](arkts-telephony-sms-mmsnotificationind-i-sys.md) |
| [MmsParams](arkts-telephony-sms-mmsparams-i-sys.md) |
| [MmsReadOrigInd](arkts-telephony-sms-mmsreadorigind-i-sys.md) |
| [MmsReadRecInd](arkts-telephony-sms-mmsreadrecind-i-sys.md) |
| [MmsRespInd](arkts-telephony-sms-mmsrespind-i-sys.md) |
| [MmsRetrieveConf](arkts-telephony-sms-mmsretrieveconf-i-sys.md) |
| [MmsSendConf](arkts-telephony-sms-mmssendconf-i-sys.md) |
| [MmsSendReq](arkts-telephony-sms-mmssendreq-i-sys.md) |
| [SimMessageOptions](arkts-telephony-sms-simmessageoptions-i-sys.md) |
| [SimShortMessage](arkts-telephony-sms-simshortmessage-i-sys.md) |
| [SmsSegmentsInfo](arkts-telephony-sms-smssegmentsinfo-i-sys.md) |
| [UpdateSimMessageOptions](arkts-telephony-sms-updatesimmessageoptions-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SendSmsResult](arkts-telephony-sms-sendsmsresult-e.md) |
| [ShortMessageClass](arkts-telephony-sms-shortmessageclass-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DispositionType](arkts-telephony-sms-dispositiontype-e-sys.md) |
| [MessageType](arkts-telephony-sms-messagetype-e-sys.md) |
| [MmsCharSets](arkts-telephony-sms-mmscharsets-e-sys.md) |
| [MmsPriorityType](arkts-telephony-sms-mmsprioritytype-e-sys.md) |
| [MmsVersionType](arkts-telephony-sms-mmsversiontype-e-sys.md) |
| [RanType](arkts-telephony-sms-rantype-e-sys.md) |
| [ReportType](arkts-telephony-sms-reporttype-e-sys.md) |
| [SimMessageStatus](arkts-telephony-sms-simmessagestatus-e-sys.md) |
| [SmsEncodingScheme](arkts-telephony-sms-smsencodingscheme-e-sys.md) |
| [SmsShortCodeType](arkts-telephony-sms-smsshortcodetype-e-sys.md) |
<!--DelEnd-->
