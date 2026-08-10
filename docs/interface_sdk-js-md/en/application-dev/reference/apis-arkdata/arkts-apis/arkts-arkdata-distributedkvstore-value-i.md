# Value

存储在数据库中的值对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-distributedKVStore-interface Value--><!--Device-distributedKVStore-interface Value-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## type

```TypeScript
type: ValueType
```

值类型。

**Type:** [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Value-type: ValueType--><!--Device-Value-type: ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## value

```TypeScript
value: Uint8Array | string | long | double | boolean
```

键值对中的值。Uint8Array、string类型的长度范围为0-[MAX_VALUE_LENGTH](arkts-arkdata-distributedkvstore-constants-i.md)，number和boolean类型的取值范围由其自身类型决定。

**Type:** ArkTS-Dyn: Uint8Array \| string \| number \| number \| boolean  <br>ArkTS-Sta：Uint8Array \| string \| long \| double \| boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Value-value: Uint8Array | string | long | double | boolean--><!--Device-Value-value: Uint8Array | string | long | double | boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

