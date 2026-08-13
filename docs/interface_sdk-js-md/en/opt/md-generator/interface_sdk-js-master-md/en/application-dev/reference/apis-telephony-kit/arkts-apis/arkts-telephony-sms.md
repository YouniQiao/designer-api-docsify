# @ohos.telephony.sms(SMS)

The **sms** module provides basic SMS management functions. With the APIs provided by this module, you can create and send SMS messages, and obtain the ID of the default SIM card used to send and receive SMS messages, and check whether the current device can send and receive SMS messages.

**Since:** 6

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
| [createMessage](arkts-telephony-sms-createmessage-f.md#createmessage) |
| [createMessage](arkts-telephony-sms-createmessage-f.md#createmessage-1) |
| [getDefaultSmsSimId](arkts-telephony-sms-getdefaultsmssimid-f.md#getdefaultsmssimid) |
| [getDefaultSmsSimId](arkts-telephony-sms-getdefaultsmssimid-f.md#getdefaultsmssimid-1) |
| [getDefaultSmsSlotId](arkts-telephony-sms-getdefaultsmsslotid-f.md#getdefaultsmsslotid) |
| [getDefaultSmsSlotId](arkts-telephony-sms-getdefaultsmsslotid-f.md#getdefaultsmsslotid-1) |
| [hasSmsCapability](arkts-telephony-sms-hassmscapability-f.md#hassmscapability) |
| [sendMessage](arkts-telephony-sms-sendmessage-f.md#sendmessage) |
| [sendShortMessage](arkts-telephony-sms-sendshortmessage-f.md#sendshortmessage) |
| [sendShortMessage](arkts-telephony-sms-sendshortmessage-f.md#sendshortmessage-1) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSimMessage](arkts-telephony-sms-addsimmessage-f-sys.md#addsimmessage) |
| [addSimMessage](arkts-telephony-sms-addsimmessage-f-sys.md#addsimmessage-1) |
| [decodeMms](arkts-telephony-sms-decodemms-f-sys.md#decodemms) |
| [decodeMms](arkts-telephony-sms-decodemms-f-sys.md#decodemms-1) |
| [delSimMessage](arkts-telephony-sms-delsimmessage-f-sys.md#delsimmessage) |
| [delSimMessage](arkts-telephony-sms-delsimmessage-f-sys.md#delsimmessage-1) |
| [downloadMms](arkts-telephony-sms-downloadmms-f-sys.md#downloadmms) |
| [downloadMms](arkts-telephony-sms-downloadmms-f-sys.md#downloadmms-1) |
| [encodeMms](arkts-telephony-sms-encodemms-f-sys.md#encodemms) |
| [encodeMms](arkts-telephony-sms-encodemms-f-sys.md#encodemms-1) |
| [getAllSimMessages](arkts-telephony-sms-getallsimmessages-f-sys.md#getallsimmessages) |
| [getAllSimMessages](arkts-telephony-sms-getallsimmessages-f-sys.md#getallsimmessages-1) |
| [getImsShortMessageFormat](arkts-telephony-sms-getimsshortmessageformat-f-sys.md#getimsshortmessageformat) |
| [getImsShortMessageFormat](arkts-telephony-sms-getimsshortmessageformat-f-sys.md#getimsshortmessageformat-1) |
| [getSmsSegmentsInfo](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md#getsmssegmentsinfo) |
| [getSmsSegmentsInfo](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md#getsmssegmentsinfo-1) |
| [getSmsShortCodeType](arkts-telephony-sms-getsmsshortcodetype-f-sys.md#getsmsshortcodetype) |
| [getSmscAddr](arkts-telephony-sms-getsmscaddr-f-sys.md#getsmscaddr) |
| [getSmscAddr](arkts-telephony-sms-getsmscaddr-f-sys.md#getsmscaddr-1) |
| [isImsSmsSupported](arkts-telephony-sms-isimssmssupported-f-sys.md#isimssmssupported) |
| [isImsSmsSupported](arkts-telephony-sms-isimssmssupported-f-sys.md#isimssmssupported-1) |
| [sendMms](arkts-telephony-sms-sendmms-f-sys.md#sendmms) |
| [sendMms](arkts-telephony-sms-sendmms-f-sys.md#sendmms-1) |
| [setCBConfig](arkts-telephony-sms-setcbconfig-f-sys.md#setcbconfig) |
| [setCBConfig](arkts-telephony-sms-setcbconfig-f-sys.md#setcbconfig-1) |
| [setCBConfigList](arkts-telephony-sms-setcbconfiglist-f-sys.md#setcbconfiglist) |
| [setDefaultSmsSlotId](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md#setdefaultsmsslotid) |
| [setDefaultSmsSlotId](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md#setdefaultsmsslotid-1) |
| [setSmscAddr](arkts-telephony-sms-setsmscaddr-f-sys.md#setsmscaddr) |
| [setSmscAddr](arkts-telephony-sms-setsmscaddr-f-sys.md#setsmscaddr-1) |
| [splitMessage](arkts-telephony-sms-splitmessage-f-sys.md#splitmessage) |
| [splitMessage](arkts-telephony-sms-splitmessage-f-sys.md#splitmessage-1) |
| [updateSimMessage](arkts-telephony-sms-updatesimmessage-f-sys.md#updatesimmessage) |
| [updateSimMessage](arkts-telephony-sms-updatesimmessage-f-sys.md#updatesimmessage-1) |
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
