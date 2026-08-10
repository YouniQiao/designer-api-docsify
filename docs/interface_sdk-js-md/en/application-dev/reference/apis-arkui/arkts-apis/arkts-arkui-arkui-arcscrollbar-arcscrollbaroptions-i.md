# ArcScrollBarOptions

ArcScrollBar的构造函数参数。

> **说明：**
> 
> ArcScrollBar与可滚动组件需通过scroller进行绑定后方能实现联动，且ArcScrollBar与可滚动组件仅限于一对一的绑定方式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ArcScrollBarOptions--><!--Device-unnamed-export declare interface ArcScrollBarOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcScrollBarAttribute, ArcScrollBar } from 'kits/@kit.ArkUI';
```

## scroller

```TypeScript
scroller: Scroller
```

可滚动组件的控制器，用于与可滚动组件进行绑定。

**Type:** [Scroller](../arkts-components/arkts-arkui-scroller-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcScrollBarOptions-scroller: Scroller--><!--Device-ArcScrollBarOptions-scroller: Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## state

```TypeScript
state?: BarState
```

滚动条状态。

**Type:** [BarState](arkts-arkui-barstate-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcScrollBarOptions-state?: BarState--><!--Device-ArcScrollBarOptions-state?: BarState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

