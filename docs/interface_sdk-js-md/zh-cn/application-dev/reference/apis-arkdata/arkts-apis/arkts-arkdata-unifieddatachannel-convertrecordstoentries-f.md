# convertRecordsToEntries

## 导入模块

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## convertRecordsToEntries

```TypeScript
function convertRecordsToEntries(data: UnifiedData): void
```

本接口用于将传入的data转换成多样式数据结构。若原data使用多个record去承载同一份数据的不同数据格式，则可以使用此接口将原data转换为多样式数据结构。当满足以下规则时进行转换，传入的data经转换后变为多样式数据结构：
1. data中的record数量大于1；
2. data中的properties中的tag值为"records_to_entries_data_format"。
否则不会产生任何行为。

**起始版本：** 17

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本17开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [UnifiedData](../../apis-arkui/arkts-components/arkts-arkui-unifieddata-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
