# RdbDataChangeNode

订阅/取消订阅RDB数据变更的结果，回调支持传输不大于10M的数据。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-dataShare-interface RdbDataChangeNode--><!--Device-dataShare-interface RdbDataChangeNode-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## data

```TypeScript
data: Array<string>
```

指定回调的数据。若处理回调数据时发生错误，则回调将不会被触发。

**Type:** Array&lt;string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbDataChangeNode-data: Array<string>--><!--Device-RdbDataChangeNode-data: Array<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## templateId

```TypeScript
templateId: TemplateId
```

处理回调的templateId。

**Type:** [TemplateId](arkts-arkdata-datashare-templateid-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbDataChangeNode-templateId: TemplateId--><!--Device-RdbDataChangeNode-templateId: TemplateId-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## uri

```TypeScript
uri: string
```

指定回调的uri。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbDataChangeNode-uri: string--><!--Device-RdbDataChangeNode-uri: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

