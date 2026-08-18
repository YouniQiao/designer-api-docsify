# PageTransitionEnter

Defines PageTransitionEnter Component.

## PageTransitionEnter

```TypeScript
PageTransitionEnter(value: PageTransitionOptions)
```

Sets the page entrance animation.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PageTransitionEnterInterface-(value: PageTransitionOptions): PageTransitionEnterInterface--><!--Device-PageTransitionEnterInterface-(value: PageTransitionOptions): PageTransitionEnterInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PageTransitionOptions](arkts-arkui-pagetransitionoptions-i.md) | Yes | pageTransition options |

## PageTransitionEnter

```TypeScript
PageTransitionEnter(event: PageTransitionCallback)
```

Invoked on a per-frame basis until the entrance animation is complete, with the **progress** parameter changing from 0 to 1.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PageTransitionEnterInterface-onEnter(event: PageTransitionCallback): PageTransitionEnterInterface--><!--Device-PageTransitionEnterInterface-onEnter(event: PageTransitionCallback): PageTransitionEnterInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md) | Yes | Callback invoked on a per-frame basis until the entrance animation is complete, with the **progress** parameter changing from 0 to 1. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [PageTransitionOptions](arkts-arkui-pagetransitionoptions-i.md) | Parameters of the exit or entrance animation. |

### Types

| Name | Description |
| --- | --- |
| [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md) | Represents the callback for page transition events. |

### Enums

| Name | Description |
| --- | --- |
| [RouteType](arkts-arkui-routetype-e.md) | Sets the type of page transition. |
| [SlideEffect](arkts-arkui-slideeffect-e.md) | Slide-in and slide-out effects for page transitions. |

