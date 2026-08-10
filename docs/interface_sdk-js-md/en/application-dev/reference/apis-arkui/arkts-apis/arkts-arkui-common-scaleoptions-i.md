# ScaleOptions

> **说明：**
> 
> 当组件同时设置了[rotate](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#rotate)和[scale](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#scale)属性时，centerX和centerY的取值会发生冲突，此时centerX和
> centerY的值以最后设定的属性的值为准。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ScaleOptions--><!--Device-unnamed-export declare interface ScaleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## centerX

```TypeScript
centerX?: double | string
```

变换中心点x轴坐标。表示组件变换中心点（即锚点）的x方向坐标。取值可为string类型，如'50'，'50%'。

单位：vp

默认值：'50%'

**Type:** double \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScaleOptions-centerX?: double | string--><!--Device-ScaleOptions-centerX?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## centerY

```TypeScript
centerY?: double | string
```

变换中心点y轴坐标。表示组件变换中心点（即锚点）的y方向坐标。取值可为string类型，如'50'，'50%'。

单位：vp

默认值：'50%'

**Type:** double \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScaleOptions-centerY?: double | string--><!--Device-ScaleOptions-centerY?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x?: double
```

x轴的缩放倍数。x>1时以x轴方向放大，0<x<1时以x轴方向缩小，x<0时沿x轴反向并缩放。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScaleOptions-x?: double--><!--Device-ScaleOptions-x?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## y

```TypeScript
y?: double
```

y轴的缩放倍数。y>1时以y轴方向放大，0<y<1时以y轴方向缩小，y<0时沿y轴反向并缩放。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScaleOptions-y?: double--><!--Device-ScaleOptions-y?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## z

```TypeScript
z?: double
```

z轴的缩放倍数。z>1时以z轴方向放大，0<z<1时以z轴方向缩小，z<0时沿z轴反向并缩放。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScaleOptions-z?: double--><!--Device-ScaleOptions-z?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

