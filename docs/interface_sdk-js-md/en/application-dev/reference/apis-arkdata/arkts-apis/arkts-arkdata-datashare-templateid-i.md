# TemplateId

标记模板的数据结构，TemplateId是在[addTemplate](arkts-arkdata-datashare-datasharehelper-i.md#addtemplate)中自动生成的，在  
[addTemplate](arkts-arkdata-datashare-datasharehelper-i.md#addtemplate)后，可以使用模板id来标记模板。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-dataShare-interface TemplateId--><!--Device-dataShare-interface TemplateId-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## bundleNameOfOwner

```TypeScript
bundleNameOfOwner: string
```

指定创建模板的模板所有者的bundleName，与[addTemplate](arkts-arkdata-datashare-datasharehelper-i.md#addtemplate)中的bundleName相同。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TemplateId-bundleNameOfOwner: string--><!--Device-TemplateId-bundleNameOfOwner: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## subscriberId

```TypeScript
subscriberId: string
```

指定处理回调的订阅者的id，与[addTemplate](arkts-arkdata-datashare-datasharehelper-i.md#addtemplate)中的subscriberId相同，每个订阅者的ID是唯一的。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TemplateId-subscriberId: string--><!--Device-TemplateId-subscriberId: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

