# TransitionFinishCallback

```TypeScript
declare type TransitionFinishCallback = (transitionIn: boolean) => void
```

Represents the type of callback for the end of a component's transition animation.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-unnamed-declare type TransitionFinishCallback = (transitionIn: boolean) => void--><!--Device-unnamed-declare type TransitionFinishCallback = (transitionIn: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transitionIn | boolean | Yes |
