# Hyperlink

[Text](arkts-arkdata-unifieddatachannel-text-c.md)的子类，用于描述超链接类型数据。

**Inheritance/Implementation:** Hyperlink extends [Text](arkts-arkdata-unifieddatachannel-text-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class Hyperlink extends Text--><!--Device-unifiedDataChannel-class Hyperlink extends Text-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## description

```TypeScript
description?: string
```

链接内容描述，非必填字段，默认值为空字符串。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Hyperlink-description?: string--><!--Device-Hyperlink-description?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## url

```TypeScript
set url(value: string)
```

链接url。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Hyperlink-set url(value: string)--><!--Device-Hyperlink-set url(value: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

