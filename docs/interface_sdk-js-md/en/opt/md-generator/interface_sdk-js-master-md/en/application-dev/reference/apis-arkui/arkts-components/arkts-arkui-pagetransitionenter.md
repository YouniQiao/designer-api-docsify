# PageTransitionEnter

Defines PageTransitionEnter Component.

## PageTransitionEnter

```TypeScript
PageTransitionEnter(value: PageTransitionOptions)
```

Sets the page entrance animation.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PageTransitionEnterInterface-(value: PageTransitionOptions): PageTransitionEnterInterface--><!--Device-PageTransitionEnterInterface-(value: PageTransitionOptions): PageTransitionEnterInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PageTransitionOptions](arkts-arkui-pagetransitionoptions-i.md) | Yes |

## PageTransitionEnter

```TypeScript
PageTransitionEnter(event: PageTransitionCallback)
```

Invoked on a per-frame basis until the entrance animation is complete, with the **progress** parameter changing from 0 to 1.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PageTransitionEnterInterface-onEnter(event: PageTransitionCallback): PageTransitionEnterInterface--><!--Device-PageTransitionEnterInterface-onEnter(event: PageTransitionCallback): PageTransitionEnterInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md) | Yes |

## Summary

- [PageTransitionOptions](arkts-arkui-pagetransitionoptions-i.md)
- [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md)
- [RouteType](arkts-arkui-routetype-e.md)
- [SlideEffect](arkts-arkui-slideeffect-e.md)
