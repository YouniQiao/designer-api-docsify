# Polyline

## Polyline

```TypeScript
export declare function Polyline(
    options?: PolylineOptions
): PolylineAttribute
```

用于绘制折线的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [PolylineOptions](arkts-arkui-polyline-polylineoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PolylineAttribute](arkts-arkui-polyline-polylineattribute-i.md) |


## Polyline

```TypeScript
export declare function Polyline(
    style: CustomBuilderT<PolylineAttribute>,
): PolylineAttribute
```

定义Polyline组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[PolylineAttribute](arkts-arkui-polyline-polylineattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [PolylineAttribute](arkts-arkui-polyline-polylineattribute-i.md) |
