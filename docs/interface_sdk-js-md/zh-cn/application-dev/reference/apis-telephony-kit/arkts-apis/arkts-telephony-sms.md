# @ohos.telephony.sms(短信服务)

短信服务提供了管理短信的一些基础能力，包括创建、发送短信，获取发送短信的默认SIM卡槽ID、检查当前设备是否具备短信发送和接收能力等。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.SmsMms

## 导入模块

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createMessage(短信服务)](arkts-telephony-sms-createmessage-f.md) |
| [createMessage(短信服务)](arkts-telephony-sms-createmessage-f.md) |
| [getDefaultSmsSimId(短信服务)](arkts-telephony-sms-getdefaultsmssimid-f.md) |
| [getDefaultSmsSimId(短信服务)](arkts-telephony-sms-getdefaultsmssimid-f.md) |
| [getDefaultSmsSlotId(短信服务)](arkts-telephony-sms-getdefaultsmsslotid-f.md) |
| [getDefaultSmsSlotId(短信服务)](arkts-telephony-sms-getdefaultsmsslotid-f.md) |
| [hasSmsCapability(短信服务)](arkts-telephony-sms-hassmscapability-f.md) |
| [sendMessage(短信服务)](arkts-telephony-sms-sendmessage-f.md) |
| [sendShortMessage(短信服务)](arkts-telephony-sms-sendshortmessage-f.md) |
| [sendShortMessage(短信服务)](arkts-telephony-sms-sendshortmessage-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addSimMessage(短信服务)](arkts-telephony-sms-addsimmessage-f-sys.md) |
| [addSimMessage(短信服务)](arkts-telephony-sms-addsimmessage-f-sys.md) |
| [decodeMms(短信服务)](arkts-telephony-sms-decodemms-f-sys.md) |
| [decodeMms(短信服务)](arkts-telephony-sms-decodemms-f-sys.md) |
| [delSimMessage(短信服务)](arkts-telephony-sms-delsimmessage-f-sys.md) |
| [delSimMessage(短信服务)](arkts-telephony-sms-delsimmessage-f-sys.md) |
| [downloadMms(短信服务)](arkts-telephony-sms-downloadmms-f-sys.md) |
| [downloadMms(短信服务)](arkts-telephony-sms-downloadmms-f-sys.md) |
| [encodeMms(短信服务)](arkts-telephony-sms-encodemms-f-sys.md) |
| [encodeMms(短信服务)](arkts-telephony-sms-encodemms-f-sys.md) |
| [getAllSimMessages(短信服务)](arkts-telephony-sms-getallsimmessages-f-sys.md) |
| [getAllSimMessages(短信服务)](arkts-telephony-sms-getallsimmessages-f-sys.md) |
| [getImsShortMessageFormat(短信服务)](arkts-telephony-sms-getimsshortmessageformat-f-sys.md) |
| [getImsShortMessageFormat(短信服务)](arkts-telephony-sms-getimsshortmessageformat-f-sys.md) |
| [getSmscAddr(短信服务)](arkts-telephony-sms-getsmscaddr-f-sys.md) |
| [getSmscAddr(短信服务)](arkts-telephony-sms-getsmscaddr-f-sys.md) |
| [getSmsSegmentsInfo(短信服务)](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md) |
| [getSmsSegmentsInfo(短信服务)](arkts-telephony-sms-getsmssegmentsinfo-f-sys.md) |
| [getSmsShortCodeType(短信服务)](arkts-telephony-sms-getsmsshortcodetype-f-sys.md) |
| [isImsSmsSupported(短信服务)](arkts-telephony-sms-isimssmssupported-f-sys.md) |
| [isImsSmsSupported(短信服务)](arkts-telephony-sms-isimssmssupported-f-sys.md) |
| [sendMms(短信服务)](arkts-telephony-sms-sendmms-f-sys.md) |
| [sendMms(短信服务)](arkts-telephony-sms-sendmms-f-sys.md) |
| [setCBConfig(短信服务)](arkts-telephony-sms-setcbconfig-f-sys.md) |
| [setCBConfig(短信服务)](arkts-telephony-sms-setcbconfig-f-sys.md) |
| [setCBConfigList(短信服务)](arkts-telephony-sms-setcbconfiglist-f-sys.md) |
| [setDefaultSmsSlotId(短信服务)](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md) |
| [setDefaultSmsSlotId(短信服务)](arkts-telephony-sms-setdefaultsmsslotid-f-sys.md) |
| [setSmscAddr(短信服务)](arkts-telephony-sms-setsmscaddr-f-sys.md) |
| [setSmscAddr(短信服务)](arkts-telephony-sms-setsmscaddr-f-sys.md) |
| [splitMessage(短信服务)](arkts-telephony-sms-splitmessage-f-sys.md) |
| [splitMessage(短信服务)](arkts-telephony-sms-splitmessage-f-sys.md) |
| [updateSimMessage(短信服务)](arkts-telephony-sms-updatesimmessage-f-sys.md) |
| [updateSimMessage(短信服务)](arkts-telephony-sms-updatesimmessage-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [IDeliveryShortMessageCallback(短信服务)](arkts-telephony-sms-ideliveryshortmessagecallback-i.md) |
| [ISendShortMessageCallback(短信服务)](arkts-telephony-sms-isendshortmessagecallback-i.md) |
| [SendMessageOptions(短信服务)](arkts-telephony-sms-sendmessageoptions-i.md) |
| [ShortMessage(短信服务)](arkts-telephony-sms-shortmessage-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [CBConfigListConfigs(短信服务)](arkts-telephony-sms-cbconfiglistconfigs-i-sys.md) |
| [CBConfigOptions(短信服务)](arkts-telephony-sms-cbconfigoptions-i-sys.md) |
| [MmsAcknowledgeInd(短信服务)](arkts-telephony-sms-mmsacknowledgeind-i-sys.md) |
| [MmsAddress(短信服务)](arkts-telephony-sms-mmsaddress-i-sys.md) |
| [MmsAttachment(短信服务)](arkts-telephony-sms-mmsattachment-i-sys.md) |
| [MmsConfig(短信服务)](arkts-telephony-sms-mmsconfig-i-sys.md) |
| [MmsDeliveryInd(短信服务)](arkts-telephony-sms-mmsdeliveryind-i-sys.md) |
| [MmsInformation(短信服务)](arkts-telephony-sms-mmsinformation-i-sys.md) |
| [MmsNotificationInd(短信服务)](arkts-telephony-sms-mmsnotificationind-i-sys.md) |
| [MmsParams(短信服务)](arkts-telephony-sms-mmsparams-i-sys.md) |
| [MmsReadOrigInd(短信服务)](arkts-telephony-sms-mmsreadorigind-i-sys.md) |
| [MmsReadRecInd(短信服务)](arkts-telephony-sms-mmsreadrecind-i-sys.md) |
| [MmsRespInd(短信服务)](arkts-telephony-sms-mmsrespind-i-sys.md) |
| [MmsRetrieveConf(短信服务)](arkts-telephony-sms-mmsretrieveconf-i-sys.md) |
| [MmsSendConf(短信服务)](arkts-telephony-sms-mmssendconf-i-sys.md) |
| [MmsSendReq(短信服务)](arkts-telephony-sms-mmssendreq-i-sys.md) |
| [SimMessageOptions(短信服务)](arkts-telephony-sms-simmessageoptions-i-sys.md) |
| [SimShortMessage(短信服务)](arkts-telephony-sms-simshortmessage-i-sys.md) |
| [SmsSegmentsInfo(短信服务)](arkts-telephony-sms-smssegmentsinfo-i-sys.md) |
| [UpdateSimMessageOptions(短信服务)](arkts-telephony-sms-updatesimmessageoptions-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [SendSmsResult(短信服务)](arkts-telephony-sms-sendsmsresult-e.md) |
| [ShortMessageClass(短信服务)](arkts-telephony-sms-shortmessageclass-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [DispositionType(短信服务)](arkts-telephony-sms-dispositiontype-e-sys.md) |
| [MessageType(短信服务)](arkts-telephony-sms-messagetype-e-sys.md) |
| [MmsCharSets(短信服务)](arkts-telephony-sms-mmscharsets-e-sys.md) |
| [MmsPriorityType(短信服务)](arkts-telephony-sms-mmsprioritytype-e-sys.md) |
| [MmsVersionType(短信服务)](arkts-telephony-sms-mmsversiontype-e-sys.md) |
| [RanType(短信服务)](arkts-telephony-sms-rantype-e-sys.md) |
| [ReportType(短信服务)](arkts-telephony-sms-reporttype-e-sys.md) |
| [SimMessageStatus(短信服务)](arkts-telephony-sms-simmessagestatus-e-sys.md) |
| [SmsEncodingScheme(短信服务)](arkts-telephony-sms-smsencodingscheme-e-sys.md) |
| [SmsShortCodeType(短信服务)](arkts-telephony-sms-smsshortcodetype-e-sys.md) |
<!--DelEnd-->
