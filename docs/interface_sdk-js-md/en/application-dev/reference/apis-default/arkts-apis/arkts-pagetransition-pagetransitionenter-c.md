# PageTransitionEnter

Provides an interface to set transition style when a page enters.

@extends CommonTransition

**Inheritance/Implementation:** PageTransitionEnter extends [CommonTransition](arkts-pagetransition-commontransition-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class PageTransitionEnter--><!--Device-unnamed-export declare class PageTransitionEnter-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_invoke

```TypeScript
static $_invoke(value: PageTransitionOptions): PageTransitionEnter
```

Called when page Jump animation is used.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransitionEnter-static $_invoke(value: PageTransitionOptions): PageTransitionEnter--><!--Device-PageTransitionEnter-static $_invoke(value: PageTransitionOptions): PageTransitionEnter-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PageTransitionOptions](arkts-pagetransition-pagetransitionoptions-i.md) | Yes | pageTransition options |

**Return value:**

| Type | Description |
| --- | --- |
| [PageTransitionEnter](arkts-pagetransition-pagetransitionenter-c.md) |  |

## onEnter

```TypeScript
onEnter(event: PageTransitionCallback): this
```

Called frame by frame to customize pageTransition animation when the page enters. The incoming parameter is the normalized progress of the current incoming animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransitionEnter-onEnter(event: PageTransitionCallback): this--><!--Device-PageTransitionEnter-onEnter(event: PageTransitionCallback): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [PageTransitionCallback](arkts-pagetransitioncallback-t.md) | Yes | animation callback frame by frame |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

