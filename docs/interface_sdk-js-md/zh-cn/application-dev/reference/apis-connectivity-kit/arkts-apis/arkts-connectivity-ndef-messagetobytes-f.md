# messageToBytes

## 导入模块

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## messageToBytes

```TypeScript
function messageToBytes(ndefMessage: NdefMessage): number[]
```

把输入的NDEF消息数据对象，转换为字节格式的数据。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ndefMessage | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number[] |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
