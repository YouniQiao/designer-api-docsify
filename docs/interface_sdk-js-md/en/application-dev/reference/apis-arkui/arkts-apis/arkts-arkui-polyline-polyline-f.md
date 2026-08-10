# Polyline

## Polyline

```TypeScript
export declare function Polyline(
    options?: PolylineOptions
): PolylineAttribute
```

用于绘制折线的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Polyline(    options?: PolylineOptions): PolylineAttribute--><!--Device-unnamed-export declare function Polyline(    options?: PolylineOptions): PolylineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolylineOptions](../arkts-components/arkts-arkui-polylineoptions-i.md) | No | Polyline绘制区域。&lt;br/&gt;异常值undefined和null按照无效值处理，本次设置不生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PolylineAttribute](../arkts-components/arkts-arkui-polyline-attribute.md) | 折线的属性。 |


## Polyline

```TypeScript
export declare function Polyline(
    style: CustomBuilderT<PolylineAttribute>,
): PolylineAttribute
```

定义Polyline组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Polyline(    style: CustomBuilderT<PolylineAttribute>,): PolylineAttribute--><!--Device-unnamed-export declare function Polyline(    style: CustomBuilderT<PolylineAttribute>,): PolylineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;PolylineAttribute&gt; | Yes | 设置组件属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PolylineAttribute](../arkts-components/arkts-arkui-polyline-attribute.md) |  |

