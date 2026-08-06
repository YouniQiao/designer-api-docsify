# KVManagerConfig

Provides the **KVManager** instance configuration, including the bundle name of the invoker and the application context.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-distributedKVStore-interface KVManagerConfig--><!--Device-distributedKVStore-interface KVManagerConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## bundleName

```TypeScript
bundleName: string
```

Bundle name.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManagerConfig-bundleName: string--><!--Device-KVManagerConfig-bundleName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## context

```TypeScript
context: BaseContext
```

Application context.

For details about the application context of the FA model, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

For details about the application context of the stage model, see  
\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.

Since API version 10, the parameter type of context is  
\_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_.

**Type:** BaseContext

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManagerConfig-context: BaseContext--><!--Device-KVManagerConfig-context: BaseContext-End-->

**System capability:** 
- API version 10 and later: SystemCapability.DistributedDataManager.KVStore.Core if swap the area, you should close all the KV store and use the new BaseContext to create the KVManager
- API version 9 to 23: SystemCapability.DistributedDataManager.KVStore.Core if swap the area, you should close all the KV store and use the new Context to create the KVManager

