# @ohos.telephony.sms

The **sms** module provides basic SMS management functions. With the APIs provided by this module, you can create and send SMS messages, and obtain the ID of the default SIM card used to send and receive SMS messages, and check whether the current device can send and receive SMS messages.

**Since:** 23

<!--Device-unnamed-declare namespace sms--><!--Device-unnamed-declare namespace sms-End-->

**System capability:** SystemCapability.Telephony.SmsMms

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createMessage](arkts-telephony-sms-createmessage-f.md#createmessage) |
| [createMessage](arkts-telephony-sms-createmessage-f.md#createmessage) |
| [getDefaultSmsSimId](arkts-telephony-sms-getdefaultsmssimid-f.md#getdefaultsmssimid) |
| [getDefaultSmsSimId](arkts-telephony-sms-getdefaultsmssimid-f.md#getdefaultsmssimid) |
| [getDefaultSmsSlotId](arkts-telephony-sms-getdefaultsmsslotid-f.md#getdefaultsmsslotid) |
| [getDefaultSmsSlotId](arkts-telephony-sms-getdefaultsmsslotid-f.md#getdefaultsmsslotid) |
| [hasSmsCapability](arkts-telephony-sms-hassmscapability-f.md#hassmscapability) |
| [sendMessage](arkts-telephony-sms-sendmessage-f.md#sendmessage) |
| [sendShortMessage](arkts-telephony-sms-sendshortmessage-f.md#sendshortmessage) |
| [sendShortMessage](arkts-telephony-sms-sendshortmessage-f.md#sendshortmessage) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSimMessage](arkts-telephony-sms-addsimmessage-f-sys.md#addsimmessage-system-api) |
| [addSimMessage](arkts-telephony-sms-addsimmessage-f-sys.md#addsimmessage-system-api) |
| [decodeMms](arkts-telephony-sms-decodemms-f-sys.md#decodemms-system-api) |
| [decodeMms](arkts-telephony-sms-decodemms-f-sys.md#decodemms-system-api) |
| [delSimMessage](arkts-telephony-sms-delsimmessage-f-sys.md#delsimmessage-system-api) |
| [delSimMessage](arkts-telephony-sms-delsimmessage-f-sys.md#delsimmessage-system-api) |
| [downloadMms](arkts-telephony-sms-downloadmms-f-sys.md#downloadmms-system-api) |
| [downloadMms](arkts-telephony-sms-downloadmms-f-sys.md#downloadmms-system-api) |
| [encodeMms](arkts-telephony-sms-encodemms-f-sys.md#encodemms-system-api) |
| [encodeMms](arkts-telephony-sms-encodemms-f-sys.md#encodemms-system-api) |
| [getAllSimMessages](arkts-telephony-sms-getallsimmessages-f-sys.md#getallsimmessages-system-api) |
| [getAllSimMessages](arkts-telephony-sms-getallsimmessages-f-sys.md#getallsimmessages-system-api) |
| [getImsShortMessageFormat](arkts-telephony-sms-getimsshortmessageformat-f-sys.md#getimsshortmessageformat-system-api) |
| [getImsShortMessageFormat](arkts-telephony-sms-getimsshortmessageformat-f-sys.md#getimsshortmessageformat-system-api) |
| [getSmsSegmentsInfo](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md#getsmssegmentsinfo-system-api) |
| [getSmsSegmentsInfo](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md#getsmssegmentsinfo-system-api) |
| [getSmsShortCodeType](arkts-telephony-sms-getsmsshortcodetype-f-sys.md#getsmsshortcodetype-system-api) |
| [getSmscAddr](arkts-telephony-sms-getsmscaddr-f-sys.md#getsmscaddr-system-api) |
| [getSmscAddr](arkts-telephony-sms-getsmscaddr-f-sys.md#getsmscaddr-system-api) |
| [isImsSmsSupported](arkts-telephony-sms-isimssmssupported-f-sys.md#isimssmssupported-system-api) |
| [isImsSmsSupported](arkts-telephony-sms-isimssmssupported-f-sys.md#isimssmssupported-system-api) |
| [sendMms](arkts-telephony-sms-sendmms-f-sys.md#sendmms-system-api) |
| [sendMms](arkts-telephony-sms-sendmms-f-sys.md#sendmms-system-api) |
| [setCBConfig](arkts-telephony-sms-setcbconfig-f-sys.md#setcbconfig-system-api) |
| [setCBConfig](arkts-telephony-sms-setcbconfig-f-sys.md#setcbconfig-system-api) |
| [setCBConfigList](arkts-telephony-sms-setcbconfiglist-f-sys.md#setcbconfiglist-system-api) |
| [setDefaultSmsSlotId](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md#setdefaultsmsslotid-system-api) |
| [setDefaultSmsSlotId](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md#setdefaultsmsslotid-system-api) |
| [setSmscAddr](arkts-telephony-sms-setsmscaddr-f-sys.md#setsmscaddr-system-api) |
| [setSmscAddr](arkts-telephony-sms-setsmscaddr-f-sys.md#setsmscaddr-system-api) |
| [splitMessage](arkts-telephony-sms-splitmessage-f-sys.md#splitmessage-system-api) |
| [splitMessage](arkts-telephony-sms-splitmessage-f-sys.md#splitmessage-system-api) |
| [updateSimMessage](arkts-telephony-sms-updatesimmessage-f-sys.md#updatesimmessage-system-api) |
| [updateSimMessage](arkts-telephony-sms-updatesimmessage-f-sys.md#updatesimmessage-system-api) |
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
