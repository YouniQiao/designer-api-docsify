# ArkListOptions

Provides basic parameters for creating an **ArcList** component.

**Since:** 18

<!--Device-unnamed-declare interface ArkListOptions--><!--Device-unnamed-declare interface ArkListOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcListItemAttribute, ArcList, ArcListItem, ArcListAttribute } from 'kits/@kit.ArkUI';
```

## header

```TypeScript
header?: ComponentContent
```

Header component.

**Type:** [ComponentContent](arkts-arkui-componentcontent-c.md)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArkListOptions-header?: ComponentContent--><!--Device-ArkListOptions-header?: ComponentContent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## initialIndex

```TypeScript
initialIndex?: number
```

Item displayed at the beginning of the viewport when the **ArcList** component is loaded for the first time, that is, the first item to be displayed.&lt;br/&gt;Default value: **0**&lt;br/&gt;  
**NOTE：**&lt;br/&gt;If the set value is a negative number or is greater than the index of the last item, the value is invalid. In this case, the default value will be used.

**Type:** number

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArkListOptions-initialIndex?: number--><!--Device-ArkListOptions-initialIndex?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## scroller

```TypeScript
scroller?: Scroller
```

Controller of the scrollable component. After being bound to **ArcList**, the controller can control the scrolling of **ArcList**.&lt;br/&gt;**NOTE：**&lt;br/&gt;The scroller cannot be bound to other scrollable components.

**Type:** [Scroller](../arkts-components/arkts-arkui-scroller-c.md)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArkListOptions-scroller?: Scroller--><!--Device-ArkListOptions-scroller?: Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle
