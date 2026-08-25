# makeApplicationRecord

## 导入模块

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## makeApplicationRecord

```TypeScript
function makeApplicationRecord(bundleName: string): NdefRecord
```

根据OpenHarmony应用的bundlename，构建NDEF标签的Record。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
