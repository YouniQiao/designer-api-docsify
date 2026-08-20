# Ellipse

## Ellipse

```TypeScript
@ComponentBuilder
export declare function Ellipse(
    options?: EllipseOptions
): EllipseAttribute
```

Ellipse is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Ellipse(    options?: EllipseOptions): EllipseAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Ellipse(    options?: EllipseOptions): EllipseAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EllipseOptions](arkts-arkui-ellipse-ellipseoptions-i.md) | No | The options to create an Ellipse |

**Return value:**

| Type | Description |
| --- | --- |
| [EllipseAttribute](arkts-arkui-ellipse-attribute.md) | The attribute of the Ellipse. |


## Ellipse

```TypeScript
@Builder
export declare function Ellipse(
    style: CustomBuilderT<EllipseAttribute>
): EllipseAttribute
```

Defines Ellipse Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Ellipse(    style: CustomBuilderT<EllipseAttribute>): EllipseAttribute--><!--Device-unnamed-@Builderexport declare function Ellipse(    style: CustomBuilderT<EllipseAttribute>): EllipseAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[EllipseAttribute](arkts-arkui-ellipse-attribute.md)&gt; | Yes | the callback to set up component's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [EllipseAttribute](arkts-arkui-ellipse-attribute.md) |  |

