# PublishedItem

指定发布的数据类型。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-dataShare-interface PublishedItem--><!--Device-dataShare-interface PublishedItem-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## data

```TypeScript
data: string | ArrayBuffer
```

指定发布的数据。如果发布数据大小超过20KB，建议使用ArrayBuffer。

**Type:** string \| ArrayBuffer

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PublishedItem-data: string | ArrayBuffer--><!--Device-PublishedItem-data: string | ArrayBuffer-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## key

```TypeScript
key: string
```

指定发布数据的键。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PublishedItem-key: string--><!--Device-PublishedItem-key: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## subscriberId

```TypeScript
subscriberId: string
```

指定订阅者id。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PublishedItem-subscriberId: string--><!--Device-PublishedItem-subscriberId: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

