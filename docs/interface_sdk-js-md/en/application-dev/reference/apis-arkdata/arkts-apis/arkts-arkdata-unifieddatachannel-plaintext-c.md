# PlainText

Represents the plain text data. It is a child class of [Text](arkts-arkdata-unifieddatachannel-text-c.md).

**Inheritance/Implementation:** PlainText extends [Text](arkts-arkdata-unifieddatachannel-text-c.md)

**Since:** 23

<!--Device-unifiedDataChannel-class PlainText--><!--Device-unifiedDataChannel-class PlainText-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

## abstract

```TypeScript
abstract?: string
```

Indicates the abstract of text

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PlainText-abstract?: string--><!--Device-PlainText-abstract?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Examples**

```TypeScript
let text = new unifiedDataChannel.PlainText();
text.textContent = 'this is textContent';
text.abstract = 'This is abstract';
```

