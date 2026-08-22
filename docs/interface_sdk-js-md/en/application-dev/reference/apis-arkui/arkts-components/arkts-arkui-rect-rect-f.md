# Rect

## Rect

```TypeScript
@ComponentBuilder
export declare function Rect(
    options?: RectOptions | RoundedRectOptions
): RectAttribute
```

Rect is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Rect(    options?: RectOptions | RoundedRectOptions): RectAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Rect(    options?: RectOptions | RoundedRectOptions): RectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectOptions](arkts-arkui-rect-rectoptions-i.md) \| [RoundedRectOptions](arkts-arkui-rect-roundedrectoptions-i.md) | No | The options to create a Rect |

**Return value:**

| Type | Description |
| --- | --- |
| [RectAttribute](arkts-arkui-rect-attribute.md) | The attribute of the Rect |


## Rect

```TypeScript
@Builder
export declare function Rect(
    style: CustomBuilderT<RectAttribute>,
): RectAttribute
```

Defines Rect Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Rect(    style: CustomBuilderT<RectAttribute>,): RectAttribute--><!--Device-unnamed-@Builderexport declare function Rect(    style: CustomBuilderT<RectAttribute>,): RectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[RectAttribute](arkts-arkui-rect-attribute.md)&gt; | Yes | the callback to set up component's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [RectAttribute](arkts-arkui-rect-attribute.md) |  |

