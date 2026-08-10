# ndef

Provides methods for accessing NDEF tag.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-tag-namespace ndef--><!--Device-tag-namespace ndef-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## 导入模块

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [makeUriRecord](arkts-connectivity-ndef-makeurirecord-f.md#makeurirecord) | Creates an NDEF record with uri data. |
| [makeTextRecord](arkts-connectivity-ndef-maketextrecord-f.md#maketextrecord) | Creates an NDEF record with text data. |
| [makeApplicationRecord](arkts-connectivity-ndef-makeapplicationrecord-f.md#makeapplicationrecord) | Creates an NDEF Record with OpenHarmony application bundle name. |
| [makeMimeRecord](arkts-connectivity-ndef-makemimerecord-f.md#makemimerecord) | Creates an NDEF record with mime data. |
| [makeExternalRecord](arkts-connectivity-ndef-makeexternalrecord-f.md#makeexternalrecord) | Creates an NDEF record with external data. |
| [createNdefMessage](arkts-connectivity-ndef-createndefmessage-f.md#createndefmessage) | Creates an NDEF message with raw bytes. |
| [createNdefMessageByData](arkts-connectivity-ndef-createndefmessagebydata-f.md#createndefmessagebydata) | Creates an NDEF message with raw bytes. |
| [createNdefMessage](arkts-connectivity-ndef-createndefmessage-f.md#createndefmessage-1) | Creates an NDEF message with record list. |
| [createNdefMessageByRecords](arkts-connectivity-ndef-createndefmessagebyrecords-f.md#createndefmessagebyrecords) | Creates an NDEF message with record list. |
| [messageToBytes](arkts-connectivity-ndef-messagetobytes-f.md#messagetobytes) | Parses an NDEF message into raw bytes. |

