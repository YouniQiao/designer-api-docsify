# FilterResult

This parameter specifies the selection result of a filtering dimension.The index starts from 0.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-export declare class FilterResult--><!--Device-unnamed-export declare class FilterResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { FilterType, Filter, FilterParams, FilterResult } from 'kits/@kit.ArkUI';
```

## index

```TypeScript
index: number
```

该维度筛选项选中项目的索引值。

取值范围：大于等于-1的整数。

默认值：-1，没有选中项。若设置数值小于-1，按没有选中项处理。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FilterResult-index: number--><!--Device-FilterResult-index: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name: ResourceStr
```

筛选项维度名称。

默认值：空字符串。

**说明：**如果文本大于列宽时，文本被截断。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FilterResult-name: ResourceStr--><!--Device-FilterResult-name: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: ResourceStr
```

该维度筛选项选中项目的值。

默认值：空字符串。

**说明：**如果文本大于列宽时，文本被截断。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FilterResult-value: ResourceStr--><!--Device-FilterResult-value: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

