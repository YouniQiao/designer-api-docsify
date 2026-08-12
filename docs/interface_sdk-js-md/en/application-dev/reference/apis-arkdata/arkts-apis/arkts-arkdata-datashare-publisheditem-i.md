# PublishedItem

Defines the data to publish.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-dataShare-interface PublishedItem--><!--Device-dataShare-interface PublishedItem-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from '@kit.ArkData';
```

## data

```TypeScript
data: string | ArrayBuffer
```

Data to publish. If the data to publish exceeds 20 KB, you are advised to use the data in ArrayBuffer format.

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

Key of the data to publish.

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

Subscriber ID.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PublishedItem-subscriberId: string--><!--Device-PublishedItem-subscriberId: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

