# Text

文本类型数据，是[UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md)的子类，也是文本类型数据的基类，用于描述文本类数据，推荐开发者优先使用Text的子类描述数据，如  
[PlainText](arkts-arkdata-unifieddatachannel-plaintext-c.md)、[Hyperlink](arkts-arkdata-unifieddatachannel-hyperlink-c.md)、  
[HTML](arkts-arkdata-unifieddatachannel-html-c.md)等具体子类。

**Inheritance/Implementation:** Text extends [UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class Text extends UnifiedRecord--><!--Device-unifiedDataChannel-class Text extends UnifiedRecord-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## details

```TypeScript
details?: Record<string, string>
```

是一个字典类型对象，key和value都是string类型，用于描述文本内容。例如，可生成一个details内容为

{

"title":"标题",

"content":"内容"

}

的数据对象，用于描述一篇文章。非必填字段，默认值为空字典对象。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Text-details?: Record<string, string>--><!--Device-Text-details?: Record<string, string>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

