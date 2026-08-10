# ContentSlot

## ContentSlot

```TypeScript
export declare function ContentSlot(
    content: Content
): ContentSlotAttribute
```

当内容添加到占位符组件时调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ContentSlot(    content: Content): ContentSlotAttribute--><!--Device-unnamed-export declare function ContentSlot(    content: Content): ContentSlotAttribute-End-->

**System capability:** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [Content](../arkts-components/arkts-arkui-content-t.md) | Yes | Content作为ContentSlot的管理器，通过Native侧提供的接口，可以注册并触发ContentSlot的上下树事件回调以及管理ContentSlot的子组件。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ContentSlotAttribute](arkts-arkui-contentslot-contentslotattribute-i.md) |  |


## ContentSlot

```TypeScript
export declare function ContentSlot(
    style: CustomBuilderT<ContentSlotAttribute>
): ContentSlotAttribute
```

定义ContentSlot组件。需要在组件属性设置开始时调用setContentSlotOptions，并在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ContentSlot(    style: CustomBuilderT<ContentSlotAttribute>): ContentSlotAttribute--><!--Device-unnamed-export declare function ContentSlot(    style: CustomBuilderT<ContentSlotAttribute>): ContentSlotAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ContentSlotAttribute&gt; | Yes | 用于设置ContentSlot属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ContentSlotAttribute](arkts-arkui-contentslot-contentslotattribute-i.md) | ContentSlot属性对象。 |

