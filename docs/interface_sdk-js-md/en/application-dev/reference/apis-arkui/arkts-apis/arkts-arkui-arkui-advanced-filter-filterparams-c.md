# FilterParams

This parameter is used to define the input of each filtering dimension.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-export declare class FilterParams--><!--Device-unnamed-export declare class FilterParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { FilterType, Filter, FilterParams, FilterResult } from 'kits/@kit.ArkUI';
```

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

<!--Device-FilterParams-name: ResourceStr--><!--Device-FilterParams-name: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
options: Array<ResourceStr>
```

筛选项维度可选项列表。

默认值：空数组。

**说明：**文本超长显示省略号。

**Type:** Array&lt;[ResourceStr](arkts-arkui-resourcestr-t.md)&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FilterParams-options: Array<ResourceStr>--><!--Device-FilterParams-options: Array<ResourceStr>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

