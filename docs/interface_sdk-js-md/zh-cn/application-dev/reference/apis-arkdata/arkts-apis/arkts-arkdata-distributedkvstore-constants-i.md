# Constants

分布式键值数据库常量。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## 导入模块

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## MAX_BATCH_SIZE

```TypeScript
readonly MAX_BATCH_SIZE: number
```

值为128，表示最大批处理操作数量。

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_KEY_LENGTH

```TypeScript
readonly MAX_KEY_LENGTH: number
```

值为1024，表示数据库中Key允许的最大长度，单位字节。

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_KEY_LENGTH_DEVICE

```TypeScript
readonly MAX_KEY_LENGTH_DEVICE: number
```

值为896，表示设备协同数据库中Key允许的最大长度，单位字节。

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_QUERY_LENGTH

```TypeScript
readonly MAX_QUERY_LENGTH: number
```

值为512000，表示最大查询长度，单位字节。

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_STORE_ID_LENGTH

```TypeScript
readonly MAX_STORE_ID_LENGTH: number
```

值为128，表示数据库标识符允许的最大长度，单位字节。

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_VALUE_LENGTH

```TypeScript
readonly MAX_VALUE_LENGTH: number
```

值为4194303，表示数据库中Value允许的最大长度，单位字节。

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_BATCH_SIZE

```TypeScript
MAX_BATCH_SIZE = 128
```

值为128，表示最大批处理操作数量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_KEY_LENGTH

```TypeScript
MAX_KEY_LENGTH = 1024
```

值为1024，表示数据库中Key允许的最大长度，单位字节。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_KEY_LENGTH_DEVICE

```TypeScript
MAX_KEY_LENGTH_DEVICE = 896
```

值为896，表示设备协同数据库中Key允许的最大长度，单位字节。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_QUERY_LENGTH

```TypeScript
MAX_QUERY_LENGTH = 512000
```

值为512000，表示最大查询长度，单位字节。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_STORE_ID_LENGTH

```TypeScript
MAX_STORE_ID_LENGTH = 128
```

值为128，表示数据库标识符允许的最大长度，单位字节。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_VALUE_LENGTH

```TypeScript
MAX_VALUE_LENGTH = 4194303
```

值为4194303，表示数据库中Value允许的最大长度，单位字节。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core
