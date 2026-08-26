# PageTransitionEnter

Defines PageTransitionEnter Component.

## PageTransitionEnter

```TypeScript
PageTransitionEnter(value: PageTransitionOptions)
```

Sets the page entrance animation.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

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

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md) | Yes | Callback invoked on a per-frame basis until the entrance animation is complete, with the **progress** parameter changing from 0 to 1. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |

### Types

| Name | Description |
| --- | --- |

### Enums

| Name | Description |
| --- | --- |

## Examples

```TypeScript
pageTransition() {
    PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
      // During the transition animation, the entrance animation has a type that represents the route type, and a progress that increases from 0 to 1.
      .onEnter((type: RouteType, progress: number) => {
        // Service logic
      })
  }
```
