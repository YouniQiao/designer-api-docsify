# makeExternalRecord

## 导入模块

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## makeExternalRecord

```TypeScript
function makeExternalRecord(domainName: string, type: string, externalData: int[]): NdefRecord
```

根据应用程序特定的外部数据，构建NDEF标签的Record。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainName](../../apis-mdm-kit/arkts-apis/arkts-mdm-networkmanager-domainfilterrule-i.md) | string | 是 |
| type | string | 是 |
| externalData | ArkTS-Dyn: number[]<br>ArkTS-Sta：int[] | 是 |

**返回值：**

| 类型 |
| --- |
| [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
