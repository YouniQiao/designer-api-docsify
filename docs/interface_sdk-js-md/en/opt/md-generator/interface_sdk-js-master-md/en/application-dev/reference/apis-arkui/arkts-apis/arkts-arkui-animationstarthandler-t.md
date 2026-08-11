# AnimationStartHandler

```TypeScript
declare type AnimationStartHandler = (index: number, targetIndex: number, event: SwiperAnimationEvent) => void
```

Defines the callback triggered when the page transition animation starts.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type AnimationStartHandler = (index: number, targetIndex: number, event: SwiperAnimationEvent) => void--><!--Device-unnamed-declare type AnimationStartHandler = (index: number, targetIndex: number, event: SwiperAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| targetIndex | number | Yes |
| event | [SwiperAnimationEvent](../arkts-components/arkts-arkui-swiperanimationevent-i.md) | Yes |
