# ArcScrollBarOptions

Represents the parameters used to construct an **ArcScrollBar** component.

> **NOTE：**&gt;
> **ArcScrollBar** must be bound to a scrollable component through **scroller** to achieve synchronization. Only a
> one-to-one binding is allowed between **ArcScrollBar** and a scrollable component.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcScrollBar, ArcScrollBarAttribute } from '@kit.ArkUI';
```

## scroller

```TypeScript
scroller: Scroller
```

Scroller, which can be bound to scrollable components for scrolling control.

**Type:** Scroller

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## state

```TypeScript
state?: BarState
```

State of the scrollbar.<br/>Default value: **BarState.Auto**

**Type:** BarState

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle
