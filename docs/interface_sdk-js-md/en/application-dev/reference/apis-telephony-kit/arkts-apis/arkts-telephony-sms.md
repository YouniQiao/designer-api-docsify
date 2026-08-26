# @ohos.telephony.sms(SMS)

The **sms** module provides basic SMS management functions. With the APIs provided by this module, you can create and send SMS messages, and obtain the ID of the default SIM card used to send and receive SMS messages, and check whether the current device can send and receive SMS messages.

**Since:** 6

**System capability:** SystemCapability.Telephony.SmsMms

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createMessage(SMS)](arkts-telephony-sms-createmessage-f.md) | Creates an SMS instance based on the protocol data unit (PDU) and specified SMS protocol. This API uses an asynchronous callback to return the result. |
| [createMessage(SMS)](arkts-telephony-sms-createmessage-f.md) | Creates an SMS instance based on the protocol data unit (PDU) and specified SMS protocol. This API uses a promise to return the result. |
| [getDefaultSmsSimId(SMS)](arkts-telephony-sms-getdefaultsmssimid-f.md) | Obtains the default ID of the SIM card used to send SMS messages. This API uses an asynchronous callback to return the result. |
| [getDefaultSmsSimId(SMS)](arkts-telephony-sms-getdefaultsmssimid-f.md) | Obtains the default ID of the SIM card used to send SMS messages. This API uses a promise to return the result. |
| [getDefaultSmsSlotId(SMS)](arkts-telephony-sms-getdefaultsmsslotid-f.md) | Obtains the default slot ID of the SIM card used to send SMS messages. This API uses an asynchronous callback to return the result. |
| [getDefaultSmsSlotId(SMS)](arkts-telephony-sms-getdefaultsmsslotid-f.md) | Obtains the default slot ID of the SIM card used to send SMS messages. This API uses a promise to return the result. |
| [hasSmsCapability(SMS)](arkts-telephony-sms-hassmscapability-f.md) | Checks whether the current device can send and receive SMS messages. This API works in synchronous mode. |
| [sendMessage(SMS)](arkts-telephony-sms-sendmessage-f.md) | Sends an SMS message. |
| [sendShortMessage(SMS)](arkts-telephony-sms-sendshortmessage-f.md) | Sends an SMS message. This API uses an asynchronous callback to return the result. |
| [sendShortMessage(SMS)](arkts-telephony-sms-sendshortmessage-f.md) | Sends an SMS message. This API uses a promise to return the result. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [addSimMessage(SMS)](arkts-telephony-sms-addsimmessage-f-sys.md) | Adds a message to the SIM card. If the SIM card is full, an error is reported. This API uses an asynchronous callback to return the result. |
| [addSimMessage(SMS)](arkts-telephony-sms-addsimmessage-f-sys.md) | Adds a message to the SIM card. If the SIM card is full, an error is reported. This API uses a promise to return the result. |
| [decodeMms(SMS)](arkts-telephony-sms-decodemms-f-sys.md) | Decodes MMS messages. This API uses an asynchronous callback to return the result. |
| [decodeMms(SMS)](arkts-telephony-sms-decodemms-f-sys.md) | Decodes MMS messages. This API uses a promise to return the result. |
| [delSimMessage(SMS)](arkts-telephony-sms-delsimmessage-f-sys.md) | Deletes a message from the SIM card. If the specified **msgIndex** is invalid, an error is reported. This API uses an asynchronous callback to return the result. |
| [delSimMessage(SMS)](arkts-telephony-sms-delsimmessage-f-sys.md) | Deletes a message from the SIM card. If the specified **msgIndex** is invalid, an error is reported. This API uses a promise to return the result. |
| [downloadMms(SMS)](arkts-telephony-sms-downloadmms-f-sys.md) | Downloads an MMS message. This API uses an asynchronous callback to return the result. |
| [downloadMms(SMS)](arkts-telephony-sms-downloadmms-f-sys.md) | Downloads an MMS message. This API uses a promise to return the result. |
| [encodeMms(SMS)](arkts-telephony-sms-encodemms-f-sys.md) | MMS message code. This API uses an asynchronous callback to return the result. |
| [encodeMms(SMS)](arkts-telephony-sms-encodemms-f-sys.md) | MMS message code. This API uses a promise to return the result. |
| [getAllSimMessages(SMS)](arkts-telephony-sms-getallsimmessages-f-sys.md) | Obtains all SIM card messages. This API uses an asynchronous callback to return the result. |
| [getAllSimMessages(SMS)](arkts-telephony-sms-getallsimmessages-f-sys.md) | Obtains all SIM card messages. This API uses a promise to return the result. |
| [getImsShortMessageFormat(SMS)](arkts-telephony-sms-getimsshortmessageformat-f-sys.md) | Obtains the SMS format supported by the IMS, for example, **3gpp**, **3gpp2**, or **unknown**. This API uses an asynchronous callback to return the result. |
| [getImsShortMessageFormat(SMS)](arkts-telephony-sms-getimsshortmessageformat-f-sys.md) | Obtains the SMS format supported by the IMS, for example, **3gpp**, **3gpp2**, or **unknown**. This API uses a promise to return the result. |
| [getSmscAddr(SMS)](arkts-telephony-sms-getsmscaddr-f-sys.md) | Obtains the SMSC address. This API uses an asynchronous callback to return the result. |
| [getSmscAddr(SMS)](arkts-telephony-sms-getsmscaddr-f-sys.md) | Obtains the SMSC address. This API uses a promise to return the result. |
| [getSmsSegmentsInfo(SMS)](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md) | Obtains SMS message segment information. This API uses an asynchronous callback to return the result. |
| [getSmsSegmentsInfo(SMS)](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md) | Obtains SMS message segment information. This API uses a promise to return the result. |
| [getSmsShortCodeType(SMS)](arkts-telephony-sms-getsmsshortcodetype-f-sys.md) | Get the SMS short code type of the destination address. |
| [isImsSmsSupported(SMS)](arkts-telephony-sms-isimssmssupported-f-sys.md) | Checks whether SMS is supported on IMS. This API uses an asynchronous callback to return the result. |
| [isImsSmsSupported(SMS)](arkts-telephony-sms-isimssmssupported-f-sys.md) | Checks whether SMS is supported on IMS. This API uses a promise to return the result. |
| [sendMms(SMS)](arkts-telephony-sms-sendmms-f-sys.md) | Sends an MMS message. This API uses an asynchronous callback to return the result. |
| [sendMms(SMS)](arkts-telephony-sms-sendmms-f-sys.md) | Sends an MMS message. This API uses a promise to return the result. |
| [setCBConfig(SMS)](arkts-telephony-sms-setcbconfig-f-sys.md) | Sets the cell broadcast configuration. This API uses an asynchronous callback to return the result. |
| [setCBConfig(SMS)](arkts-telephony-sms-setcbconfig-f-sys.md) | Sets the cell broadcast configuration. This API uses a promise to return the result. |
| [setCBConfigList(SMS)](arkts-telephony-sms-setcbconfiglist-f-sys.md) | Turn on Cell BroadCast by list. |
| [setDefaultSmsSlotId(SMS)](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md) | Sets the default slot ID of the SIM card used to send SMS messages. This API uses an asynchronous callback to return the result. |
| [setDefaultSmsSlotId(SMS)](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md) | Sets the default slot ID of the SIM card used to send SMS messages. This API uses a promise to return the result. |
| [setSmscAddr(SMS)](arkts-telephony-sms-setsmscaddr-f-sys.md) | Sets the short message service center (SMSC) address. This API uses an asynchronous callback to return the result. |
| [setSmscAddr(SMS)](arkts-telephony-sms-setsmscaddr-f-sys.md) | Sets the SMSC address. This API uses a promise to return the result. |
| [splitMessage(SMS)](arkts-telephony-sms-splitmessage-f-sys.md) | Splits an SMS message into multiple segments. This API uses an asynchronous callback to return the result. |
| [splitMessage(SMS)](arkts-telephony-sms-splitmessage-f-sys.md) | Splits an SMS message into multiple segments. This API uses a promise to return the result. |
| [updateSimMessage(SMS)](arkts-telephony-sms-updatesimmessage-f-sys.md) | Updates a SIM message. This API uses an asynchronous callback to return the result. |
| [updateSimMessage(SMS)](arkts-telephony-sms-updatesimmessage-f-sys.md) | Updates a SIM message. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [IDeliveryShortMessageCallback(SMS)](arkts-telephony-sms-ideliveryshortmessagecallback-i.md) | Provides the callback for the SMS message delivery report. |
| [ISendShortMessageCallback(SMS)](arkts-telephony-sms-isendshortmessagecallback-i.md) | Provides the callback for the SMS message sending result. It consists of three parts: SMS message sending result, URI for storing the sent SMS message, and whether the SMS message is the last part of a number SMS message. |
| [SendMessageOptions(SMS)](arkts-telephony-sms-sendmessageoptions-i.md) | Provides the options (including callbacks) for sending SMS messages. For example, you can specify the SMS message type by the optional parameter **content**. |
| [ShortMessage(SMS)](arkts-telephony-sms-shortmessage-i.md) | Defines an SMS message instance. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [CBConfigListConfigs(SMS)](arkts-telephony-sms-cbconfiglistconfigs-i-sys.md) | Defines the cell broadcast configuration list configs. |
| [CBConfigOptions(SMS)](arkts-telephony-sms-cbconfigoptions-i-sys.md) | Defines the cell broadcast configuration options. |
| [MmsAcknowledgeInd(SMS)](arkts-telephony-sms-mmsacknowledgeind-i-sys.md) | Defines an MMS confirmation index. |
| [MmsAddress(SMS)](arkts-telephony-sms-mmsaddress-i-sys.md) | Defines an MMSC address. |
| [MmsAttachment(SMS)](arkts-telephony-sms-mmsattachment-i-sys.md) | Defines the attachment of an MMS message. |
| [MmsConfig(SMS)](arkts-telephony-sms-mmsconfig-i-sys.md) | MMS configuration file. |
| [MmsDeliveryInd(SMS)](arkts-telephony-sms-mmsdeliveryind-i-sys.md) | Defines an MMS message delivery index. |
| [MmsInformation(SMS)](arkts-telephony-sms-mmsinformation-i-sys.md) | Defines the MMS message information. |
| [MmsNotificationInd(SMS)](arkts-telephony-sms-mmsnotificationind-i-sys.md) | Defines an MMS notification index. |
| [MmsParams(SMS)](arkts-telephony-sms-mmsparams-i-sys.md) | Defines the parameters for sending SMS messages. |
| [MmsReadOrigInd(SMS)](arkts-telephony-sms-mmsreadorigind-i-sys.md) | Defines the original MMS message reading index. |
| [MmsReadRecInd(SMS)](arkts-telephony-sms-mmsreadrecind-i-sys.md) | Defines the MMS message reading index. |
| [MmsRespInd(SMS)](arkts-telephony-sms-mmsrespind-i-sys.md) | Defines an MMS response index. |
| [MmsRetrieveConf(SMS)](arkts-telephony-sms-mmsretrieveconf-i-sys.md) | Defines the MMS message retrieval configuration. |
| [MmsSendConf(SMS)](arkts-telephony-sms-mmssendconf-i-sys.md) | Defines the MMS message sending configuration. |
| [MmsSendReq(SMS)](arkts-telephony-sms-mmssendreq-i-sys.md) | Defines an MMS message sending request. |
| [SimMessageOptions(SMS)](arkts-telephony-sms-simmessageoptions-i-sys.md) | Defines the SIM message options. |
| [SimShortMessage(SMS)](arkts-telephony-sms-simshortmessage-i-sys.md) | Defines a SIM message. |
| [SmsSegmentsInfo(SMS)](arkts-telephony-sms-smssegmentsinfo-i-sys.md) | Defines the SMS message segment information. |
| [UpdateSimMessageOptions(SMS)](arkts-telephony-sms-updatesimmessageoptions-i-sys.md) | Defines the updating SIM message options. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [SendSmsResult(SMS)](arkts-telephony-sms-sendsmsresult-e.md) | Enumerates SMS message sending results. |
| [ShortMessageClass(SMS)](arkts-telephony-sms-shortmessageclass-e.md) | Enumerates SMS message types. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [DispositionType(SMS)](arkts-telephony-sms-dispositiontype-e-sys.md) | Enumerates disposition types. |
| [MessageType(SMS)](arkts-telephony-sms-messagetype-e-sys.md) | Message type. |
| [MmsCharSets(SMS)](arkts-telephony-sms-mmscharsets-e-sys.md) | Enumerates MMS character sets. |
| [MmsPriorityType(SMS)](arkts-telephony-sms-mmsprioritytype-e-sys.md) | Enumerates MMS message priorities. |
| [MmsVersionType(SMS)](arkts-telephony-sms-mmsversiontype-e-sys.md) | Enumerates MMS versions. |
| [RanType(SMS)](arkts-telephony-sms-rantype-e-sys.md) | RAN type. |
| [ReportType(SMS)](arkts-telephony-sms-reporttype-e-sys.md) | Enumerates report types. |
| [SimMessageStatus(SMS)](arkts-telephony-sms-simmessagestatus-e-sys.md) | Defines the SIM message status. |
| [SmsEncodingScheme(SMS)](arkts-telephony-sms-smsencodingscheme-e-sys.md) | Enumerates SMS encoding schemes. |
| [SmsShortCodeType(SMS)](arkts-telephony-sms-smsshortcodetype-e-sys.md) | Enumerates SMS short code types. |
<!--DelEnd-->
