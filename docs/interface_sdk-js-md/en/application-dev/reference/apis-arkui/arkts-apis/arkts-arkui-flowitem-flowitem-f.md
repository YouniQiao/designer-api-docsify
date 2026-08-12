# FlowItem

## FlowItem

```TypeScript
export declare function FlowItem(
    content_?: CustomBuilder,
): FlowItemAttribute
```

Defines FlowItem Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function FlowItem(    content_?: CustomBuilder,): FlowItemAttribute--><!--Device-unnamed-export declare function FlowItem(    content_?: CustomBuilder,): FlowItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [FlowItemAttribute](arkts-arkui-flowitem-flowitemattribute-i.md) |  |


## FlowItem

```TypeScript
export declare function FlowItem(
    style_: CustomBuilderT<FlowItemAttribute>,
    content_?: CustomBuilder
): FlowItemAttribute
```

Defines FlowItem Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function FlowItem(    style_: CustomBuilderT<FlowItemAttribute>,    content_?: CustomBuilder): FlowItemAttribute--><!--Device-unnamed-export declare function FlowItem(    style_: CustomBuilderT<FlowItemAttribute>,    content_?: CustomBuilder): FlowItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[FlowItemAttribute](arkts-arkui-flowitem-flowitemattribute-i.md)&gt; | Yes | The style to create a FlowItem. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [FlowItemAttribute](arkts-arkui-flowitem-flowitemattribute-i.md) | The attribute of the FlowItem. |

