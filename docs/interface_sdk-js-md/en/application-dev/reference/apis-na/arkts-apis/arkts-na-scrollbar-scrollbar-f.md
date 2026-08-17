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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function ScrollBar(    value: ScrollBarOptions,    content_?: CustomBuilder,): ScrollBarAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ScrollBar(    value: ScrollBarOptions,    content_?: CustomBuilder,): ScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScrollBarOptions](arkts-na-scrollbar-scrollbaroptions-i.md) | Yes | value |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| ScrollBarAttribute |  |


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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ScrollBar(    style_: CustomBuilderT<ScrollBarAttribute>,    content_?: CustomBuilder): ScrollBarAttribute--><!--Device-unnamed-@Builderexport declare function ScrollBar(    style_: CustomBuilderT<ScrollBarAttribute>,    content_?: CustomBuilder): ScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;ScrollBarAttribute&gt; | Yes | The style to create a ScrollBar. |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| ScrollBarAttribute | The attribute of the ScrollBar. |

