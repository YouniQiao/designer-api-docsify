# createKVManager

## 导入模块

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## createKVManager

```TypeScript
function createKVManager(config: KVManagerConfig): KVManager
```

创建一个KVManager对象实例，用于管理数据库对象。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [KVManagerConfig](arkts-arkdata-distributedkvstore-kvmanagerconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [KVManager](arkts-arkdata-distributeddata-kvmanager-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
