# PublishedDataChangeNode

订阅/取消订阅已发布数据变更的结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

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

指定回调的bundleName。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PublishedDataChangeNode-bundleName: string--><!--Device-PublishedDataChangeNode-bundleName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## data

```TypeScript
data: Array<PublishedItem>
```

指定回调的数据。

**Type:** Array&lt;PublishedItem&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PublishedDataChangeNode-data: Array<PublishedItem>--><!--Device-PublishedDataChangeNode-data: Array<PublishedItem>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

