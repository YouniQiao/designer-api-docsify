# Select

## Select

```TypeScript
export declare function Select(
    options: Array<SelectOption>,
    content_?: CustomBuilder,
): SelectAttribute
```

Defines Select Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Select(    options: Array<SelectOption>,    content_?: CustomBuilder,): SelectAttribute--><!--Device-unnamed-export declare function Select(    options: Array<SelectOption>,    content_?: CustomBuilder,): SelectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | Array&lt;SelectOption&gt; | Yes | the options of Select. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SelectAttribute](../arkts-components/arkts-arkui-select-attribute.md) |  |


## Select

```TypeScript
export declare function Select(
    style_: CustomBuilderT<SelectAttribute>,
    content_?: CustomBuilder,
): SelectAttribute
```

Defines Select Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Select(    style_: CustomBuilderT<SelectAttribute>,    content_?: CustomBuilder,): SelectAttribute--><!--Device-unnamed-export declare function Select(    style_: CustomBuilderT<SelectAttribute>,    content_?: CustomBuilder,): SelectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;SelectAttribute&gt; | Yes | select attribute instance |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SelectAttribute](../arkts-components/arkts-arkui-select-attribute.md) |  |

