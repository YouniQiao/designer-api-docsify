# makeMimeRecord

## 导入模块

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## makeMimeRecord

```TypeScript
function makeMimeRecord(mimeType: string, mimeData: int[]): NdefRecord
```

Creates an NDEF record with mime data.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ndef-function makeMimeRecord(mimeType: string, mimeData: int[]): NdefRecord--><!--Device-ndef-function makeMimeRecord(mimeType: string, mimeData: int[]): NdefRecord-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | type of mime data for new an NDEF record. |
| mimeData | ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | 是 | mime data for new an NDEF record. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md) | The instance of NdefRecord. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

