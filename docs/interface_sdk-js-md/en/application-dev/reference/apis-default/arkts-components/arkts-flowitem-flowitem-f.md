# FlowItem

## FlowItem

```TypeScript
@ComponentBuilder
export declare function FlowItem(
    content_?: CustomBuilder,
): FlowItemAttribute
```

Defines FlowItem Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function FlowItem(    content_?: CustomBuilder,): FlowItemAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function FlowItem(    content_?: CustomBuilder,): FlowItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [FlowItemAttribute](arkts-flowitem-attribute.md) |  |


## FlowItem

```TypeScript
@Builder
export declare function FlowItem(
    style_: CustomBuilderT<FlowItemAttribute>,
    content_?: CustomBuilder
): FlowItemAttribute
```

Defines FlowItem Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function FlowItem(    style_: CustomBuilderT<FlowItemAttribute>,    content_?: CustomBuilder): FlowItemAttribute--><!--Device-unnamed-@Builderexport declare function FlowItem(    style_: CustomBuilderT<FlowItemAttribute>,    content_?: CustomBuilder): FlowItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[FlowItemAttribute](arkts-flowitem-attribute.md)&gt; | Yes | The style to create a FlowItem. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [FlowItemAttribute](arkts-flowitem-attribute.md) | The attribute of the FlowItem. |

