# createNdefMessageByData

## 导入模块

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## createNdefMessageByData

```TypeScript
function createNdefMessageByData(data: int[]): NdefMessage
```

Creates an NDEF message with raw bytes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | int[] | 是 |

**返回值：**

| 类型 |
| --- |
| [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
