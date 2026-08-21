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

<!--Device-ndef-function createNdefMessageByData(data: int[]): NdefMessage--><!--Device-ndef-function createNdefMessageByData(data: int[]): NdefMessage-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | int[] | 是 | The raw bytes to parse NDEF message. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| NdefMessage | The instance of NdefMessage. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

