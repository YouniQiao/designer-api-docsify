# VisibleAreaChangeCallback

```TypeScript
declare type VisibleAreaChangeCallback = (isExpanding: boolean, currentRatio: number) => void
```

Represents a callback for visible area changes of the component.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isExpanding | boolean | Yes |
| currentRatio | number | Yes |
