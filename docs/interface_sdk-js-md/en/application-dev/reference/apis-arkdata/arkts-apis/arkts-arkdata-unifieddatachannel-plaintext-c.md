# PlainText

[Text](arkts-arkdata-unifieddatachannel-text-c.md)的子类，用于描述纯文本类数据。

**Inheritance/Implementation:** PlainText extends [Text](arkts-arkdata-unifieddatachannel-text-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class PlainText extends Text--><!--Device-unifiedDataChannel-class PlainText extends Text-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## abstract

```TypeScript
abstract?: string
```

纯文本摘要，非必填字段，默认值为空字符串。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PlainText-abstract?: string--><!--Device-PlainText-abstract?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## textAbstract

```TypeScript
set textAbstract(value: string | undefined)
```

表示文本摘要。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlainText-set textAbstract(value: string | undefined)--><!--Device-PlainText-set textAbstract(value: string | undefined)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## textContent

```TypeScript
set textContent(value: string)
```

纯文本内容。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PlainText-set textContent(value: string)--><!--Device-PlainText-set textContent(value: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

