# PublishedDataChangeNode

Defines the subscription/unsubscription result of the changes in the published data.

**Since:** 10

<!--Device-dataShare-interface PublishedDataChangeNode--><!--Device-dataShare-interface PublishedDataChangeNode-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## bundleName

```TypeScript
bundleName: string
```

Bundle name of the callback.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-PublishedDataChangeNode-bundleName: string--><!--Device-PublishedDataChangeNode-bundleName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## data

```TypeScript
data: Array<PublishedItem>
```

Data of the callback.

**Type:** Array&lt;PublishedItem&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-PublishedDataChangeNode-data: Array<PublishedItem>--><!--Device-PublishedDataChangeNode-data: Array<PublishedItem>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer
