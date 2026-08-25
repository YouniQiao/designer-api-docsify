# PageTransitionExitInterface

Provide an interface to set transition style when a page exits.@extends CommonTransition&lt;PageTransitionExitInterface&gt; @interface PageTransitionExitInterface

**Inheritance/Implementation:** PageTransitionExitInterface extends CommonTransition<PageTransitionExitInterface>

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## [[Call]]

```TypeScript
(value: PageTransitionOptions): PageTransitionExitInterface
```

Sets the page exit animation.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PageTransitionOptions](arkts-arkui-pagetransitionoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PageTransitionExitInterface](arkts-arkui-pagetransitionexitinterface-i.md) |

## onExit

```TypeScript
onExit(event: PageTransitionCallback): PageTransitionExitInterface
```

Invoked on a per-frame basis until the exit animation is complete, with the **progress** parameter changing from 0 to 1.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PageTransitionExitInterface](arkts-arkui-pagetransitionexitinterface-i.md) |

**Examples**

```TypeScript
pageTransition() {
    PageTransitionExit({ duration: 1200, curve: Curve.Linear })
      // During the transition animation, the exit animation has a type that represents the route type, and a progress that increases from 0 to 1.
      .onExit((type: RouteType, progress: number) => {
        // Service logic
      })
  }
```
