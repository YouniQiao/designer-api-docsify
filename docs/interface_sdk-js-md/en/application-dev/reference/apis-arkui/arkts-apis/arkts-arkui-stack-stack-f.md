# Stack

## Stack

```TypeScript
export declare function Stack(
    options?: StackOptions,
    content_?: CustomBuilder,
): StackAttribute
```

Defines Stack Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Stack(    options?: StackOptions,    content_?: CustomBuilder,): StackAttribute--><!--Device-unnamed-export declare function Stack(    options?: StackOptions,    content_?: CustomBuilder,): StackAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [StackOptions](../arkts-components/arkts-arkui-stackoptions-i.md) | No | Stack options. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [StackAttribute](../arkts-components/arkts-arkui-stack-attribute.md) |  |


## Stack

```TypeScript
export declare function Stack(
    style: CustomBuilderT<StackAttribute>,
    content_?: CustomBuilder,
): StackAttribute
```

Defines Stack Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Stack(    style: CustomBuilderT<StackAttribute>,    content_?: CustomBuilder,): StackAttribute--><!--Device-unnamed-export declare function Stack(    style: CustomBuilderT<StackAttribute>,    content_?: CustomBuilder,): StackAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;StackAttribute&gt; | Yes | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [StackAttribute](../arkts-components/arkts-arkui-stack-attribute.md) |  |

