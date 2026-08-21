# ndef

Provides methods for accessing NDEF tag.

**起始版本：** 23

<!--Device-tag-namespace ndef--><!--Device-tag-namespace ndef-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## 导入模块

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [makeUriRecord](arkts-connectivity-ndef-makeurirecord-f.md) | 根据输入的URI，构建NDEF标签的Record数据对象。 |
| [makeTextRecord](arkts-connectivity-ndef-maketextrecord-f.md) | 根据输入的文本数据和语言类型，构建NDEF标签的Record。 |
| [makeMimeRecord](arkts-connectivity-ndef-makemimerecord-f.md) | 根据输入的MIME数据和类型，构建NDEF标签的Record。 |
| [makeExternalRecord](arkts-connectivity-ndef-makeexternalrecord-f.md) | 根据应用程序特定的外部数据，构建NDEF标签的Record。 |
| [createNdefMessage](arkts-connectivity-ndef-createndefmessage-f.md) | 使用原始字节数据创建NDEF标签的Message。该数据必须符合NDEF Record数据格式，如果不符合格式，则返回的NdefMessage数据对象，所包含的NDEF Record列表会为空。 |
| [createNdefMessageByData](arkts-connectivity-ndef-createndefmessagebydata-f.md) | Creates an NDEF message with raw bytes. |
| [createNdefMessage](arkts-connectivity-ndef-createndefmessage-f.md) | 使用NDEF Records列表，创建NDEF Message。 |
| [createNdefMessageByRecords](arkts-connectivity-ndef-createndefmessagebyrecords-f.md) | Creates an NDEF message with record list. |
| [messageToBytes](arkts-connectivity-ndef-messagetobytes-f.md) | 把输入的NDEF消息数据对象，转换为字节格式的数据。 |
| [makeApplicationRecord](arkts-connectivity-ndef-makeapplicationrecord-f.md) | 根据OpenHarmony应用的bundlename，构建NDEF标签的Record。 |

