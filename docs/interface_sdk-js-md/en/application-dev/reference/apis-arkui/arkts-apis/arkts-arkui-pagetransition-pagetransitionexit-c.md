# PageTransitionExit

Provide an interface to set transition style when a page exits.

**Inheritance/Implementation:** PageTransitionExit extends [CommonTransition](arkts-arkui-pagetransition-commontransition-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class PageTransitionExit extends CommonTransition--><!--Device-unnamed-export declare class PageTransitionExit extends CommonTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_invoke

```TypeScript
static $_invoke(value: PageTransitionOptions): PageTransitionExit
```

Called when page Jump animation is used.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransitionExit-static $_invoke(value: PageTransitionOptions): PageTransitionExit--><!--Device-PageTransitionExit-static $_invoke(value: PageTransitionOptions): PageTransitionExit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PageTransitionOptions](arkts-arkui-pagetransition-pagetransitionoptions-i.md) | Yes | pageTransition options |

**Return value:**

| Type | Description |
| --- | --- |
| [PageTransitionExit](arkts-arkui-pagetransition-pagetransitionexit-c.md) |  |

## onExit

```TypeScript
onExit(event: PageTransitionCallback): this
```

Called frame by frame to customize pageTransition animation when the page exits.The input parameter is the normalized progress of the current exit animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransitionExit-onExit(event: PageTransitionCallback): this--><!--Device-PageTransitionExit-onExit(event: PageTransitionCallback): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

