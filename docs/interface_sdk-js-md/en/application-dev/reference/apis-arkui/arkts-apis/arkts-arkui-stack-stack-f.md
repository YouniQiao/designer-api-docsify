# Stack

## Stack

```TypeScript
@ComponentBuilder
export declare function Stack(
    options?: StackOptions,
    content_?: CustomBuilder,
): StackAttribute
```

Defines Stack Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Stack(    options?: StackOptions,    content_?: CustomBuilder,): StackAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Stack(    options?: StackOptions,    content_?: CustomBuilder,): StackAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [StackOptions](arkts-arkui-stack-stackoptions-i.md) | No | Stack options. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| StackAttribute |  |


## Stack

```TypeScript
@Builder
export declare function Stack(
    style: CustomBuilderT<StackAttribute>,
    content_?: CustomBuilder,
): StackAttribute
```

Defines Stack Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Stack(    style: CustomBuilderT<StackAttribute>,    content_?: CustomBuilder,): StackAttribute--><!--Device-unnamed-@Builderexport declare function Stack(    style: CustomBuilderT<StackAttribute>,    content_?: CustomBuilder,): StackAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;StackAttribute&gt; | Yes | the callback to set up component's attributes. |
| content_ | CustomBuilder | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| StackAttribute |  |

