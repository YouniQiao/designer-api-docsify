# createNdefMessage

## 导入模块

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## createNdefMessage

```TypeScript
function createNdefMessage(data: int[]): NdefMessage
```

Creates an NDEF message with raw bytes.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ndef-function createNdefMessage(data: int[]): NdefMessage--><!--Device-ndef-function createNdefMessage(data: int[]): NdefMessage-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | int[] | 是 | The raw bytes to parse NDEF message. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | The instance of NdefMessage. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |


## createNdefMessage

```TypeScript
function createNdefMessage(ndefRecords: NdefRecord[]): NdefMessage
```

Creates an NDEF message with record list.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ndef-function createNdefMessage(ndefRecords: NdefRecord[]): NdefMessage--><!--Device-ndef-function createNdefMessage(ndefRecords: NdefRecord[]): NdefMessage-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ndefRecords | [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md)[] | 是 | The NDEF records to parse NDEF message. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | The instance of NdefMessage. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

