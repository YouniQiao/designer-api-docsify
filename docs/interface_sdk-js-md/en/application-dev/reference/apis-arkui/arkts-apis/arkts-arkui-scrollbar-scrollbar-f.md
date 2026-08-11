# ScrollBar

## ScrollBar

```TypeScript
export declare function ScrollBar(
    value: ScrollBarOptions,
    content_?: CustomBuilder,
): ScrollBarAttribute
```

Defines ScrollBar Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ScrollBar(    value: ScrollBarOptions,    content_?: CustomBuilder,): ScrollBarAttribute--><!--Device-unnamed-export declare function ScrollBar(    value: ScrollBarOptions,    content_?: CustomBuilder,): ScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScrollBarOptions](arkts-arkui-scrollbar-scrollbaroptions-i.md) | Yes | value |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ScrollBarAttribute](../arkts-components/arkts-arkui-scrollbar-attribute.md) |  |


## ScrollBar

```TypeScript
export declare function ScrollBar(
    style_: CustomBuilderT<ScrollBarAttribute>,
    content_?: CustomBuilder
): ScrollBarAttribute
```

Defines ScrollBar Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ScrollBar(    style_: CustomBuilderT<ScrollBarAttribute>,    content_?: CustomBuilder): ScrollBarAttribute--><!--Device-unnamed-export declare function ScrollBar(    style_: CustomBuilderT<ScrollBarAttribute>,    content_?: CustomBuilder): ScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ScrollBarAttribute&gt; | Yes | The style to create a ScrollBar. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ScrollBarAttribute](../arkts-components/arkts-arkui-scrollbar-attribute.md) | The attribute of the ScrollBar. |

