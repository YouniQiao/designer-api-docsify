# KVManagerConfig

提供KVManager实例的配置信息，包括调用方的包名和应用的上下文。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-distributedKVStore-interface KVManagerConfig--><!--Device-distributedKVStore-interface KVManagerConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## bundleName

```TypeScript
bundleName: string
```

调用方的包名，不可为空且长度范围为1-256字节。

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

应用的上下文。

FA模型的应用Context定义见[Context](arkts-arkdata-distributedkvstore-kvmanagerconfig-i.md#context)。

Stage模型的应用Context定义见[Context](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md/arkts-ability-uiabilitycontext-c.md)。

从API version 10开始，context的参数类型为[BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md/arkts-ability-basecontext-c.md)。

**Type:** [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManagerConfig-context: BaseContext--><!--Device-KVManagerConfig-context: BaseContext-End-->

**System capability:** 
- API version 10 and later: SystemCapability.DistributedDataManager.KVStore.Core if swap the area, you should close all the KV store and use the new BaseContext to create the KVManager
- API version 9: SystemCapability.DistributedDataManager.KVStore.Core if swap the area, you should close all the KV store and use the new Context to create the KVManager

