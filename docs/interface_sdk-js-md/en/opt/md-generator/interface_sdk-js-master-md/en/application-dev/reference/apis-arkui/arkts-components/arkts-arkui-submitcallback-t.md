# SubmitCallback

```TypeScript
declare type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void
```

Represents the callback invoked when the Enter key on the soft keyboard is pressed.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void--><!--Device-unnamed-declare type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enterKey | [EnterKeyType](../arkts-apis/arkts-arkui-textinput-enterkeytype-e.md) | Yes |
| event | [SubmitEvent](arkts-arkui-submitevent-i.md) | Yes |
