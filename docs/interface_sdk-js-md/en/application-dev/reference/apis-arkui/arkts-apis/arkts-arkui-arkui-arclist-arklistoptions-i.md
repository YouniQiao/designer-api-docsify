# ArkListOptions

包含创建ArcList组件的基础参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ArkListOptions--><!--Device-unnamed-export declare interface ArkListOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcListItemAttribute, ArcList, ArcListItem, ArcListAttribute } from 'kits/@kit.ArkUI';
```

## header

```TypeScript
header?: ComponentContentBase
```

支持标题设置。

**Type:** [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArkListOptions-header?: ComponentContentBase--><!--Device-ArkListOptions-header?: ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## initialIndex

```TypeScript
initialIndex?: int
```

设置当前ArcList初次加载时视窗起始位置显示的item的索引值。&lt;br/&gt;。取值限定为整数。默认值：0&lt;br/&gt;设置为负数或超过了当前ArcList最后一个item的索引值时视为无效取值，无效取值按默认值显示。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArkListOptions-initialIndex?: int--><!--Device-ArkListOptions-initialIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## scroller

```TypeScript
scroller?: Scroller
```

可滚动组件的控制器。与ArcList绑定后，可以通过它控制ArcList的滚动。&lt;br/&gt;不允许和其他滚动类组件绑定同一个滚动控制对象。

**Type:** [Scroller](../arkts-components/arkts-arkui-scroller-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArkListOptions-scroller?: Scroller--><!--Device-ArkListOptions-scroller?: Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

