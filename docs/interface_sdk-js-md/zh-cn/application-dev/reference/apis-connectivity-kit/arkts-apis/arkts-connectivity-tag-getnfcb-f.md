# getNfcB

## 导入模块

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getNfcB

```TypeScript
function getNfcB(tagInfo: TagInfo): NfcBTag
```

获取NFC B类型Tag对象，通过该对象可访问NfcB技术类型的Tag。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |
