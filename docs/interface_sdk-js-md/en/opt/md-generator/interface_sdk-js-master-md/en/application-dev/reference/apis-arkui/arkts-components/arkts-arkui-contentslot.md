# ContentSlot

The **ContentSlot** component is a component designed to render and manage components created on the native layer using C APIs. With support for hybrid development, the **ContentSlot** component is recommended when the container is an ArkTS component and the child component is created on the native side.

## ContentSlot

```TypeScript
ContentSlot(content: Content)
```

Called when content is added to a placeholder component

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ContentSlotInterface-(content: Content): ContentSlotAttribute--><!--Device-ContentSlotInterface-(content: Content): ContentSlotAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [Content](arkts-arkui-content-t.md) | Yes |

## Summary

- [Content](arkts-arkui-content-t.md)
