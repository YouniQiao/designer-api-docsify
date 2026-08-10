# EdgeLightParams (System API)

定义边缘流光效果参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare interface EdgeLightParams--><!--Device-unnamed-declare interface EdgeLightParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## color

```TypeScript
color?: ResourceColor
```

边缘流光颜色。

默认值：#FFFFFF，显示为白色。

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** #FFFFFF

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EdgeLightParams-color?: ResourceColor--><!--Device-EdgeLightParams-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## intensity

```TypeScript
intensity?: double
```

边缘流光效果的发光强度。

取值范围：[0, 1]

默认值：1

**说明：**

值为0时，流光效果完全不可见。

值为1时，流光效果达到最大亮度。

设置大于1的值时，按值为1处理。

设置小于0的值时，按值为0处理。

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EdgeLightParams-intensity?: double--><!--Device-EdgeLightParams-intensity?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## length

```TypeScript
length: Length
```

沿流动方向的边缘流光的投影长度（不支持百分比）。

取值范围：[0, +∞)

单位：vp

**说明：**

设置小于0的值时，按值为0处理。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EdgeLightParams-length: Length--><!--Device-EdgeLightParams-length: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## position

```TypeScript
position: EdgeLightPosition
```

边缘流光位置。

**Type:** [EdgeLightPosition](../arkts-apis/arkts-arkui-edgelightposition-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EdgeLightParams-position: EdgeLightPosition--><!--Device-EdgeLightParams-position: EdgeLightPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## thickness

```TypeScript
thickness?: Length
```

边缘流光线条粗细（不支持百分比）。

取值范围：[0, +∞)

单位：vp

默认值：0

**说明：**

设置小于0的值时，按值为0处理。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Default:** 0vp

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EdgeLightParams-thickness?: Length--><!--Device-EdgeLightParams-thickness?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

