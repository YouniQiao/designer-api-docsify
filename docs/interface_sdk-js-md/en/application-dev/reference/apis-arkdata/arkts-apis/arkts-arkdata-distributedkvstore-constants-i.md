# Constants

分布式键值数据库常量。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-distributedKVStore-interface Constants--><!--Device-distributedKVStore-interface Constants-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## MAX_BATCH_SIZE

```TypeScript
readonly MAX_BATCH_SIZE: number
```

值为128，表示最大批处理操作数量。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Constants-readonly MAX_BATCH_SIZE: number--><!--Device-Constants-readonly MAX_BATCH_SIZE: number-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_KEY_LENGTH

```TypeScript
readonly MAX_KEY_LENGTH: number
```

值为1024，表示数据库中Key允许的最大长度，单位字节。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Constants-readonly MAX_KEY_LENGTH: number--><!--Device-Constants-readonly MAX_KEY_LENGTH: number-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_KEY_LENGTH_DEVICE

```TypeScript
readonly MAX_KEY_LENGTH_DEVICE: number
```

值为896，表示设备协同数据库中Key允许的最大长度，单位字节。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Constants-readonly MAX_KEY_LENGTH_DEVICE: number--><!--Device-Constants-readonly MAX_KEY_LENGTH_DEVICE: number-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_QUERY_LENGTH

```TypeScript
readonly MAX_QUERY_LENGTH: number
```

值为512000，表示最大查询长度，单位字节。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Constants-readonly MAX_QUERY_LENGTH: number--><!--Device-Constants-readonly MAX_QUERY_LENGTH: number-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_STORE_ID_LENGTH

```TypeScript
readonly MAX_STORE_ID_LENGTH: number
```

值为128，表示数据库标识符允许的最大长度，单位字节。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Constants-readonly MAX_STORE_ID_LENGTH: number--><!--Device-Constants-readonly MAX_STORE_ID_LENGTH: number-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## MAX_VALUE_LENGTH

```TypeScript
readonly MAX_VALUE_LENGTH: number
```

值为4194303，表示数据库中Value允许的最大长度，单位字节。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Constants-readonly MAX_VALUE_LENGTH: number--><!--Device-Constants-readonly MAX_VALUE_LENGTH: number-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

