# Polygon

## Polygon

```TypeScript
export declare function Polygon(
    options?: PolygonOptions
): PolygonAttribute
```

用于绘制多边形的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Polygon(    options?: PolygonOptions): PolygonAttribute--><!--Device-unnamed-export declare function Polygon(    options?: PolygonOptions): PolygonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolygonOptions](../arkts-components/arkts-arkui-polygonoptions-i.md) | No | Polygon绘制区域。&lt;br/&gt;异常值undefined和null按照无效值处理，本次设置不生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PolygonAttribute](../arkts-components/arkts-arkui-polygon-attribute.md) | 多边形的属性。 |


## Polygon

```TypeScript
export declare function Polygon(
    style: CustomBuilderT<PolygonAttribute>,
): PolygonAttribute
```

定义Polygon组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Polygon(    style: CustomBuilderT<PolygonAttribute>,): PolygonAttribute--><!--Device-unnamed-export declare function Polygon(    style: CustomBuilderT<PolygonAttribute>,): PolygonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;PolygonAttribute&gt; | Yes | 设置组件属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PolygonAttribute](../arkts-components/arkts-arkui-polygon-attribute.md) |  |

