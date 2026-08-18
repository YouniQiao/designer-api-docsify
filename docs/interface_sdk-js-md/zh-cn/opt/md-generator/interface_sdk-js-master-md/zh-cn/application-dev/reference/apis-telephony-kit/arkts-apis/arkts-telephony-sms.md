# @ohos.telephony.sms

短信服务提供了管理短信的一些基础能力，包括创建、发送短信，获取发送短信的默认SIM卡槽ID、检查当前设备是否具备短信发送和接收能力等。

**起始版本：** 23

<!--Device-unnamed-declare namespace sms--><!--Device-unnamed-declare namespace sms-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [addSimMessage](arkts-telephony-sms-addsimmessage-f-sys.md#addsimmessage系统接口) |
| [addSimMessage](arkts-telephony-sms-addsimmessage-f-sys.md#addsimmessage系统接口) |
| [decodeMms](arkts-telephony-sms-decodemms-f-sys.md#decodemms系统接口) |
| [decodeMms](arkts-telephony-sms-decodemms-f-sys.md#decodemms系统接口) |
| [delSimMessage](arkts-telephony-sms-delsimmessage-f-sys.md#delsimmessage系统接口) |
| [delSimMessage](arkts-telephony-sms-delsimmessage-f-sys.md#delsimmessage系统接口) |
| [downloadMms](arkts-telephony-sms-downloadmms-f-sys.md#downloadmms系统接口) |
| [downloadMms](arkts-telephony-sms-downloadmms-f-sys.md#downloadmms系统接口) |
| [encodeMms](arkts-telephony-sms-encodemms-f-sys.md#encodemms系统接口) |
| [encodeMms](arkts-telephony-sms-encodemms-f-sys.md#encodemms系统接口) |
| [getAllSimMessages](arkts-telephony-sms-getallsimmessages-f-sys.md#getallsimmessages系统接口) |
| [getAllSimMessages](arkts-telephony-sms-getallsimmessages-f-sys.md#getallsimmessages系统接口) |
| [getImsShortMessageFormat](arkts-telephony-sms-getimsshortmessageformat-f-sys.md#getimsshortmessageformat系统接口) |
| [getImsShortMessageFormat](arkts-telephony-sms-getimsshortmessageformat-f-sys.md#getimsshortmessageformat系统接口) |
| [getSmsSegmentsInfo](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md#getsmssegmentsinfo系统接口) |
| [getSmsSegmentsInfo](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md#getsmssegmentsinfo系统接口) |
| [getSmsShortCodeType](arkts-telephony-sms-getsmsshortcodetype-f-sys.md#getsmsshortcodetype系统接口) |
| [getSmscAddr](arkts-telephony-sms-getsmscaddr-f-sys.md#getsmscaddr系统接口) |
| [getSmscAddr](arkts-telephony-sms-getsmscaddr-f-sys.md#getsmscaddr系统接口) |
| [isImsSmsSupported](arkts-telephony-sms-isimssmssupported-f-sys.md#isimssmssupported系统接口) |
| [isImsSmsSupported](arkts-telephony-sms-isimssmssupported-f-sys.md#isimssmssupported系统接口) |
| [sendMms](arkts-telephony-sms-sendmms-f-sys.md#sendmms系统接口) |
| [sendMms](arkts-telephony-sms-sendmms-f-sys.md#sendmms系统接口) |
| [setCBConfig](arkts-telephony-sms-setcbconfig-f-sys.md#setcbconfig系统接口) |
| [setCBConfig](arkts-telephony-sms-setcbconfig-f-sys.md#setcbconfig系统接口) |
| [setCBConfigList](arkts-telephony-sms-setcbconfiglist-f-sys.md#setcbconfiglist系统接口) |
| [setDefaultSmsSlotId](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md#setdefaultsmsslotid系统接口) |
| [setDefaultSmsSlotId](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md#setdefaultsmsslotid系统接口) |
| [setSmscAddr](arkts-telephony-sms-setsmscaddr-f-sys.md#setsmscaddr系统接口) |
| [setSmscAddr](arkts-telephony-sms-setsmscaddr-f-sys.md#setsmscaddr系统接口) |
| [splitMessage](arkts-telephony-sms-splitmessage-f-sys.md#splitmessage系统接口) |
| [splitMessage](arkts-telephony-sms-splitmessage-f-sys.md#splitmessage系统接口) |
| [updateSimMessage](arkts-telephony-sms-updatesimmessage-f-sys.md#updatesimmessage系统接口) |
| [updateSimMessage](arkts-telephony-sms-updatesimmessage-f-sys.md#updatesimmessage系统接口) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [IDeliveryShortMessageCallback](arkts-telephony-sms-ideliveryshortmessagecallback-i.md) |
| [ISendShortMessageCallback](arkts-telephony-sms-isendshortmessagecallback-i.md) |
| [SendMessageOptions](arkts-telephony-sms-sendmessageoptions-i.md) |
| [ShortMessage](arkts-telephony-sms-shortmessage-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
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

### 枚举

| 名称 |
| --- |
| [SendSmsResult](arkts-telephony-sms-sendsmsresult-e.md) |
| [ShortMessageClass](arkts-telephony-sms-shortmessageclass-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
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
