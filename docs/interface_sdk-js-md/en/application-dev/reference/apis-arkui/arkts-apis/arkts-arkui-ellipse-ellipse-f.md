# Ellipse

## Ellipse

```TypeScript
export declare function Ellipse(
    options?: EllipseOptions
): EllipseAttribute
```

用于绘制椭圆的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Ellipse(    options?: EllipseOptions): EllipseAttribute--><!--Device-unnamed-export declare function Ellipse(    options?: EllipseOptions): EllipseAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EllipseOptions](../arkts-components/arkts-arkui-ellipseoptions-i.md) | No | 椭圆绘制尺寸。&lt;br/&gt;异常值undefined和null按照无效值处理，本次设置不生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| [EllipseAttribute](../arkts-components/arkts-arkui-ellipse-attribute.md) | 椭圆的属性。 |


## Ellipse

```TypeScript
export declare function Ellipse(
    style: CustomBuilderT<EllipseAttribute>
): EllipseAttribute
```

定义Ellipse组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Ellipse(    style: CustomBuilderT<EllipseAttribute>): EllipseAttribute--><!--Device-unnamed-export declare function Ellipse(    style: CustomBuilderT<EllipseAttribute>): EllipseAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;EllipseAttribute&gt; | Yes | 设置组件属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [EllipseAttribute](../arkts-components/arkts-arkui-ellipse-attribute.md) |  |

