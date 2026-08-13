# KVManagerConfig

Provides the **KVManager** instance configuration, including the bundle name of the invoker and the application context.

**Since:** 23

**Deprecated since:** -1

<!--Device-distributedKVStore-interface KVManagerConfig--><!--Device-distributedKVStore-interface KVManagerConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## bundleName

```TypeScript
bundleName: string
```

Bundle name.

**Type:** string

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManagerConfig-bundleName: string--><!--Device-KVManagerConfig-bundleName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## context

```TypeScript
context: BaseContext
```

Application context. For details about the application context of the FA model, see Context. For details about the application context of the stage model, see [Context](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md#UIAbilityContext). Since API version 10, the parameter type of context is [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md#BaseContext).

**Type:** [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md)

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManagerConfig-context: BaseContext--><!--Device-KVManagerConfig-context: BaseContext-End-->

**System capability:** 
- API version 10 and later: SystemCapability.DistributedDataManager.KVStore.Core if swap the area, you should close all the KV store and use the new BaseContext to create the KVManager
- API version 9 to 23: SystemCapability.DistributedDataManager.KVStore.Core if swap the area, you should close all the KV store and use the new Context to create the KVManager
