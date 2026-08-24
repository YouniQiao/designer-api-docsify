# ScrollBar

## ScrollBar

```TypeScript
@ComponentBuilder
export declare function ScrollBar(
    value: ScrollBarOptions,
    content_?: CustomBuilder,
): ScrollBarAttribute
```

Defines ScrollBar Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function ScrollBar(    value: ScrollBarOptions,    content_?: CustomBuilder,): ScrollBarAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ScrollBar(    value: ScrollBarOptions,    content_?: CustomBuilder,): ScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScrollBarOptions](arkts-scrollbar-scrollbaroptions-i.md) | Yes | value |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ScrollBarAttribute](arkts-scrollbar-attribute.md) |  |


## ScrollBar

```TypeScript
@Builder
export declare function ScrollBar(
    style_: CustomBuilderT<ScrollBarAttribute>,
    content_?: CustomBuilder
): ScrollBarAttribute
```

Defines ScrollBar Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ScrollBar(    style_: CustomBuilderT<ScrollBarAttribute>,    content_?: CustomBuilder): ScrollBarAttribute--><!--Device-unnamed-@Builderexport declare function ScrollBar(    style_: CustomBuilderT<ScrollBarAttribute>,    content_?: CustomBuilder): ScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[ScrollBarAttribute](arkts-scrollbar-attribute.md)&gt; | Yes | The style to create a ScrollBar. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ScrollBarAttribute](arkts-scrollbar-attribute.md) | The attribute of the ScrollBar. |

