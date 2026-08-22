# Polyline

## Polyline

```TypeScript
@ComponentBuilder
export declare function Polyline(
    options?: PolylineOptions
): PolylineAttribute
```

Polyline is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Polyline(    options?: PolylineOptions): PolylineAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Polyline(    options?: PolylineOptions): PolylineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolylineOptions](arkts-arkui-polyline-polylineoptions-i.md) | No | The options to create a Polyline |

**Return value:**

| Type | Description |
| --- | --- |
| [PolylineAttribute](arkts-arkui-polyline-attribute.md) | The attribute of the Polyline. |


## Polyline

```TypeScript
@Builder
export declare function Polyline(
    style: CustomBuilderT<PolylineAttribute>,
): PolylineAttribute
```

Defines Polyline Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Polyline(    style: CustomBuilderT<PolylineAttribute>,): PolylineAttribute--><!--Device-unnamed-@Builderexport declare function Polyline(    style: CustomBuilderT<PolylineAttribute>,): PolylineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[PolylineAttribute](arkts-arkui-polyline-attribute.md)&gt; | Yes | the callback to set up component's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [PolylineAttribute](arkts-arkui-polyline-attribute.md) |  |

