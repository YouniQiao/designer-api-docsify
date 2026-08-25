# @ohos.data.sendableRelationalStore

该模块针对关系型数据库（Relational Database，RDB）提供了sendable支持。支持从查询结果集中获取sendable类型ValuesBucket用于并发实例间传递。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## 导入模块

```TypeScript
import { sendableRelationalStore } from '@kit.ArkData';
```

## 汇总

### 函数

| 名称 |
| --- |
| [fromSendableAsset](arkts-arkdata-sendablerelationalstore-fromsendableasset-f.md) |
| [fromSendableValues](arkts-arkdata-sendablerelationalstore-fromsendablevalues-f.md) |
| [fromSendableValuesBucket](arkts-arkdata-sendablerelationalstore-fromsendablevaluesbucket-f.md) |
| [toSendableAsset](arkts-arkdata-sendablerelationalstore-tosendableasset-f.md) |
| [toSendableValues](arkts-arkdata-sendablerelationalstore-tosendablevalues-f.md) |
| [toSendableValuesBucket](arkts-arkdata-sendablerelationalstore-tosendablevaluesbucket-f.md) |

### 接口

| 名称 |
| --- |
| [Asset](arkts-arkdata-sendablerelationalstore-asset-i.md) |

### 类型

| 名称 |
| --- |
| [Assets](arkts-arkdata-sendablerelationalstore-assets-t.md) |
| [NonSendableAsset](arkts-arkdata-sendablerelationalstore-nonsendableasset-t.md) |
| [NonSendableBucket](arkts-arkdata-sendablerelationalstore-nonsendablebucket-t.md) |
| [NonSendableValues](arkts-arkdata-sendablerelationalstore-nonsendablevalues-t.md) |
| [ValuesBucket](arkts-arkdata-sendablerelationalstore-valuesbucket-t.md) |
| [ValueType](arkts-arkdata-sendablerelationalstore-valuetype-t.md) |
