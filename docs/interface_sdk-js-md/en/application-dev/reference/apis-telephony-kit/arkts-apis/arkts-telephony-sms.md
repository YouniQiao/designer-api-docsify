# @ohos.telephony.sms(SMS)

The **sms** module provides basic SMS management functions. With the APIs provided by this module, you can create and send SMS messages, and obtain the ID of the default SIM card used to send and receive SMS messages, and check whether the current device can send and receive SMS messages.

**Since:** 6

**System capability:** SystemCapability.Telephony.SmsMms

## Modules to Import

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createMessage(SMS)](arkts-telephony-sms-createmessage-f.md) |
| [createMessage(SMS)](arkts-telephony-sms-createmessage-f.md) |
| [getDefaultSmsSimId(SMS)](arkts-telephony-sms-getdefaultsmssimid-f.md) |
| [getDefaultSmsSimId(SMS)](arkts-telephony-sms-getdefaultsmssimid-f.md) |
| [getDefaultSmsSlotId(SMS)](arkts-telephony-sms-getdefaultsmsslotid-f.md) |
| [getDefaultSmsSlotId(SMS)](arkts-telephony-sms-getdefaultsmsslotid-f.md) |
| [hasSmsCapability(SMS)](arkts-telephony-sms-hassmscapability-f.md) |
| [sendMessage(SMS)](arkts-telephony-sms-sendmessage-f.md) |
| [sendShortMessage(SMS)](arkts-telephony-sms-sendshortmessage-f.md) |
| [sendShortMessage(SMS)](arkts-telephony-sms-sendshortmessage-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSimMessage(SMS)](arkts-telephony-sms-addsimmessage-f-sys.md) |
| [addSimMessage(SMS)](arkts-telephony-sms-addsimmessage-f-sys.md) |
| [decodeMms(SMS)](arkts-telephony-sms-decodemms-f-sys.md) |
| [decodeMms(SMS)](arkts-telephony-sms-decodemms-f-sys.md) |
| [delSimMessage(SMS)](arkts-telephony-sms-delsimmessage-f-sys.md) |
| [delSimMessage(SMS)](arkts-telephony-sms-delsimmessage-f-sys.md) |
| [downloadMms(SMS)](arkts-telephony-sms-downloadmms-f-sys.md) |
| [downloadMms(SMS)](arkts-telephony-sms-downloadmms-f-sys.md) |
| [encodeMms(SMS)](arkts-telephony-sms-encodemms-f-sys.md) |
| [encodeMms(SMS)](arkts-telephony-sms-encodemms-f-sys.md) |
| [getAllSimMessages(SMS)](arkts-telephony-sms-getallsimmessages-f-sys.md) |
| [getAllSimMessages(SMS)](arkts-telephony-sms-getallsimmessages-f-sys.md) |
| [getImsShortMessageFormat(SMS)](arkts-telephony-sms-getimsshortmessageformat-f-sys.md) |
| [getImsShortMessageFormat(SMS)](arkts-telephony-sms-getimsshortmessageformat-f-sys.md) |
| [getSmscAddr(SMS)](arkts-telephony-sms-getsmscaddr-f-sys.md) |
| [getSmscAddr(SMS)](arkts-telephony-sms-getsmscaddr-f-sys.md) |
| [getSmsSegmentsInfo(SMS)](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md) |
| [getSmsSegmentsInfo(SMS)](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md) |
| [getSmsShortCodeType(SMS)](arkts-telephony-sms-getsmsshortcodetype-f-sys.md) |
| [isImsSmsSupported(SMS)](arkts-telephony-sms-isimssmssupported-f-sys.md) |
| [isImsSmsSupported(SMS)](arkts-telephony-sms-isimssmssupported-f-sys.md) |
| [sendMms(SMS)](arkts-telephony-sms-sendmms-f-sys.md) |
| [sendMms(SMS)](arkts-telephony-sms-sendmms-f-sys.md) |
| [setCBConfig(SMS)](arkts-telephony-sms-setcbconfig-f-sys.md) |
| [setCBConfig(SMS)](arkts-telephony-sms-setcbconfig-f-sys.md) |
| [setCBConfigList(SMS)](arkts-telephony-sms-setcbconfiglist-f-sys.md) |
| [setDefaultSmsSlotId(SMS)](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md) |
| [setDefaultSmsSlotId(SMS)](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md) |
| [setSmscAddr(SMS)](arkts-telephony-sms-setsmscaddr-f-sys.md) |
| [setSmscAddr(SMS)](arkts-telephony-sms-setsmscaddr-f-sys.md) |
| [splitMessage(SMS)](arkts-telephony-sms-splitmessage-f-sys.md) |
| [splitMessage(SMS)](arkts-telephony-sms-splitmessage-f-sys.md) |
| [updateSimMessage(SMS)](arkts-telephony-sms-updatesimmessage-f-sys.md) |
| [updateSimMessage(SMS)](arkts-telephony-sms-updatesimmessage-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [IDeliveryShortMessageCallback(SMS)](arkts-telephony-sms-ideliveryshortmessagecallback-i.md) |
| [ISendShortMessageCallback(SMS)](arkts-telephony-sms-isendshortmessagecallback-i.md) |
| [SendMessageOptions(SMS)](arkts-telephony-sms-sendmessageoptions-i.md) |
| [ShortMessage(SMS)](arkts-telephony-sms-shortmessage-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CBConfigListConfigs(SMS)](arkts-telephony-sms-cbconfiglistconfigs-i-sys.md) |
| [CBConfigOptions(SMS)](arkts-telephony-sms-cbconfigoptions-i-sys.md) |
| [MmsAcknowledgeInd(SMS)](arkts-telephony-sms-mmsacknowledgeind-i-sys.md) |
| [MmsAddress(SMS)](arkts-telephony-sms-mmsaddress-i-sys.md) |
| [MmsAttachment(SMS)](arkts-telephony-sms-mmsattachment-i-sys.md) |
| [MmsConfig(SMS)](arkts-telephony-sms-mmsconfig-i-sys.md) |
| [MmsDeliveryInd(SMS)](arkts-telephony-sms-mmsdeliveryind-i-sys.md) |
| [MmsInformation(SMS)](arkts-telephony-sms-mmsinformation-i-sys.md) |
| [MmsNotificationInd(SMS)](arkts-telephony-sms-mmsnotificationind-i-sys.md) |
| [MmsParams(SMS)](arkts-telephony-sms-mmsparams-i-sys.md) |
| [MmsReadOrigInd(SMS)](arkts-telephony-sms-mmsreadorigind-i-sys.md) |
| [MmsReadRecInd(SMS)](arkts-telephony-sms-mmsreadrecind-i-sys.md) |
| [MmsRespInd(SMS)](arkts-telephony-sms-mmsrespind-i-sys.md) |
| [MmsRetrieveConf(SMS)](arkts-telephony-sms-mmsretrieveconf-i-sys.md) |
| [MmsSendConf(SMS)](arkts-telephony-sms-mmssendconf-i-sys.md) |
| [MmsSendReq(SMS)](arkts-telephony-sms-mmssendreq-i-sys.md) |
| [SimMessageOptions(SMS)](arkts-telephony-sms-simmessageoptions-i-sys.md) |
| [SimShortMessage(SMS)](arkts-telephony-sms-simshortmessage-i-sys.md) |
| [SmsSegmentsInfo(SMS)](arkts-telephony-sms-smssegmentsinfo-i-sys.md) |
| [UpdateSimMessageOptions(SMS)](arkts-telephony-sms-updatesimmessageoptions-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SendSmsResult(SMS)](arkts-telephony-sms-sendsmsresult-e.md) |
| [ShortMessageClass(SMS)](arkts-telephony-sms-shortmessageclass-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DispositionType(SMS)](arkts-telephony-sms-dispositiontype-e-sys.md) |
| [MessageType(SMS)](arkts-telephony-sms-messagetype-e-sys.md) |
| [MmsCharSets(SMS)](arkts-telephony-sms-mmscharsets-e-sys.md) |
| [MmsPriorityType(SMS)](arkts-telephony-sms-mmsprioritytype-e-sys.md) |
| [MmsVersionType(SMS)](arkts-telephony-sms-mmsversiontype-e-sys.md) |
| [RanType(SMS)](arkts-telephony-sms-rantype-e-sys.md) |
| [ReportType(SMS)](arkts-telephony-sms-reporttype-e-sys.md) |
| [SimMessageStatus(SMS)](arkts-telephony-sms-simmessagestatus-e-sys.md) |
| [SmsEncodingScheme(SMS)](arkts-telephony-sms-smsencodingscheme-e-sys.md) |
| [SmsShortCodeType(SMS)](arkts-telephony-sms-smsshortcodetype-e-sys.md) |
<!--DelEnd-->
