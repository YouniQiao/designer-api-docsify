# Value

存储在数据库中的值对象。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-distributedKVStore-interface Value--><!--Device-distributedKVStore-interface Value-End-->

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## type

```TypeScript
type: ValueType
```

值类型。

**类型：** ValueType

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Value-type: ValueType--><!--Device-Value-type: ValueType-End-->

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## value

```TypeScript
value: Uint8Array | string | long | double | boolean
```

键值对中的值。Uint8Array、string类型的长度范围为0-[MAX_VALUE_LENGTH](arkts-arkdata-distributedkvstore-constants-i.md#Constants)，number和boolean类型的取值范围由其自身类型决定。

**类型：** ArkTS-Dyn: Uint8Array \| string \| number \| number \| boolean  <br>ArkTS-Sta：Uint8Array \| string \| long \| double \| boolean

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Value-value: Uint8Array | string | long | double | boolean--><!--Device-Value-value: Uint8Array | string | long | double | boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

