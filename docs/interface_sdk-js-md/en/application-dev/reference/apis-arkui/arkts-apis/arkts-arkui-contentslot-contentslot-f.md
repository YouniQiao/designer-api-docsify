# ContentSlot

## ContentSlot

```TypeScript
export declare function ContentSlot(
    content: Content
): ContentSlotAttribute
```

ContentSlot is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ContentSlot(    content: Content): ContentSlotAttribute--><!--Device-unnamed-export declare function ContentSlot(    content: Content): ContentSlotAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | Content | Yes | Indicates the class object of NodeContent. |

**Return value:**

| Type | Description |
| --- | --- |
| [ContentSlotAttribute](arkts-arkui-contentslot-contentslotattribute-i.md) | The attribute of the ContentSlot. |


## ContentSlot

```TypeScript
export declare function ContentSlot(
    style: CustomBuilderT<ContentSlotAttribute>
): ContentSlotAttribute
```

Defines ContentSlot Component.It requires calling setContentSlotOptions at start of the component attribute set-up,and it requires calling applyAttributesFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ContentSlot(    style: CustomBuilderT<ContentSlotAttribute>): ContentSlotAttribute--><!--Device-unnamed-export declare function ContentSlot(    style: CustomBuilderT<ContentSlotAttribute>): ContentSlotAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[ContentSlotAttribute](arkts-arkui-contentslot-contentslotattribute-i.md)&gt; | Yes | the callback to set up ContentSlot's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [ContentSlotAttribute](arkts-arkui-contentslot-contentslotattribute-i.md) | The attribute of the ContentSlot. |

