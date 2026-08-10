# DataLoadParams

用于在延迟加载场景下描述发送方的数据加载策略。

当同时传入loadHandler和delayedDataLoadHandler时，优先使用delayedDataLoadHandler，loadHandler不生效。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-interface DataLoadParams--><!--Device-unifiedDataChannel-interface DataLoadParams-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## delayedDataLoadHandler

```TypeScript
delayedDataLoadHandler?: DelayedDataLoadHandler
```

表示用于延迟加载数据的异步处理函数。默认值为undefined，不填写时仅使用loadHandler。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-DataLoadParams-delayedDataLoadHandler?: DelayedDataLoadHandler--><!--Device-DataLoadParams-delayedDataLoadHandler?: DelayedDataLoadHandler-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## loadHandler

```TypeScript
loadHandler: DataLoadHandler
```

表示用于延迟加载数据的处理函数。该处理函数为同步函数，适用于处理简单业务逻辑，若函数业务逻辑较复杂、执行时间较长（3s以上），推荐使用  
[DelayedDataLoadHandler](arkts-arkdata-unifieddatachannel-delayeddataloadhandler-t.md)。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataLoadParams-loadHandler: DataLoadHandler--><!--Device-DataLoadParams-loadHandler: DataLoadHandler-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## dataLoadInfo

```TypeScript
dataLoadInfo: DataLoadInfo
```

用于描述当前发送方可生成的数据类型及数量信息。

**Type:** [DataLoadInfo](arkts-arkdata-unifieddatachannel-dataloadinfo-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataLoadParams-dataLoadInfo: DataLoadInfo--><!--Device-DataLoadParams-dataLoadInfo: DataLoadInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

