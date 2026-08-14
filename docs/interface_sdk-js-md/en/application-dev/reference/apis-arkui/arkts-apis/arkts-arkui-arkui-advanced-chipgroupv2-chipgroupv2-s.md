# ChipGroupV2

Defines chipGroupV2.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare struct ChipGroupV2--><!--Device-unnamed-export declare struct ChipGroupV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ChipGroupV2ItemConfig } from 'ChipGroupV2ItemConfig';
import { ChipGroupV2Item } from 'ChipGroupV2Item';
import { ChipGroupV2Items } from 'ChipGroupV2Items';
import { ChipGroupV2ItemStyleConfig } from 'ChipGroupV2ItemStyleConfig';
import { ChipGroupV2ItemStyle } from 'ChipGroupV2ItemStyle';
import { ChipGroupV2SpaceConfig } from 'ChipGroupV2SpaceConfig';
import { ChipGroupV2Space } from 'ChipGroupV2Space';
import { ChipGroupV2IconItemConfig } from 'ChipGroupV2IconItemConfig';
import { ChipGroupV2SymbolItemConfig } from 'ChipGroupV2SymbolItemConfig';
import { ChipGroupV2PaddingConfig } from 'ChipGroupV2PaddingConfig';
import { ChipGroupV2Padding } from 'ChipGroupV2Padding';
import { ChipGroupV2IconGroupSuffix } from 'ChipGroupV2IconGroupSuffix';
import { ChipGroupV2 } from 'ChipGroupV2';
```

## $items

```TypeScript
@Event
    $items?: Callback<ChipGroupV2Items>
```

Two-way binding callback method for ChipV2 item.

**Type:** Callback&lt;[ChipGroupV2Items](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2items-c.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2-@Event    $items?: Callback<ChipGroupV2Items>--><!--Device-ChipGroupV2-@Event    $items?: Callback<ChipGroupV2Items>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $selectedIndexes

```TypeScript
@Event
    $selectedIndexes?: Callback<Array<number>>
```

Two-way binding callback method for selected ChipV2 item indexes.

**Type:** Callback&lt;Array&lt;number&gt;&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2-@Event    $selectedIndexes?: Callback<Array<number>>--><!--Device-ChipGroupV2-@Event    $selectedIndexes?: Callback<Array<number>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## chipGroupPadding

```TypeScript
@Param
     chipGroupPadding?: ChipGroupV2Padding
```

ChipGroupV2 padding (only support top and bottom).

**Type:** [ChipGroupV2Padding](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2padding-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2-@Param     chipGroupPadding?: ChipGroupV2Padding--><!--Device-ChipGroupV2-@Param     chipGroupPadding?: ChipGroupV2Padding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## chipGroupSpace

```TypeScript
@Param
    chipGroupSpace?: ChipGroupV2Space
```

Left and right inner margins and spacing between ChipV2.

**Type:** [ChipGroupV2Space](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2space-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2-@Param    chipGroupSpace?: ChipGroupV2Space--><!--Device-ChipGroupV2-@Param    chipGroupSpace?: ChipGroupV2Space-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemStyle

```TypeScript
@Param
    itemStyle?: ChipGroupV2ItemStyle
```

ChipV2 item style.

**Type:** [ChipGroupV2ItemStyle](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2itemstyle-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2-@Param    itemStyle?: ChipGroupV2ItemStyle--><!--Device-ChipGroupV2-@Param    itemStyle?: ChipGroupV2ItemStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
    @Param
    items: ChipGroupV2Items
```

ChipV2 item.

**Type:** [ChipGroupV2Items](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2items-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2-@Require    @Param    items: ChipGroupV2Items--><!--Device-ChipGroupV2-@Require    @Param    items: ChipGroupV2Items-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## multiple

```TypeScript
@Param
    multiple?: boolean
```

Support multiple ChipV2 item selection.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2-@Param    multiple?: boolean--><!--Device-ChipGroupV2-@Param    multiple?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
@Event
    onChange?: Callback<Array<number>>
```

Callback method when the chipV2 status changes

**Type:** Callback&lt;Array&lt;number&gt;&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2-@Event    onChange?: Callback<Array<number>>--><!--Device-ChipGroupV2-@Event    onChange?: Callback<Array<number>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndexes

```TypeScript
@Param
    selectedIndexes?: Array<number>
```

Selected ChipV2 item indexes.

**Type:** Array&lt;number&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2-@Param    selectedIndexes?: Array<number>--><!--Device-ChipGroupV2-@Param    selectedIndexes?: Array<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## suffix

```TypeScript
@BuilderParam
    suffix?: Callback<void>
```

The builder function which will be rendered in the suffix of ChipGroupV2.

**Type:** Callback&lt;void&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2-@BuilderParam    suffix?: Callback<void>--><!--Device-ChipGroupV2-@BuilderParam    suffix?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

