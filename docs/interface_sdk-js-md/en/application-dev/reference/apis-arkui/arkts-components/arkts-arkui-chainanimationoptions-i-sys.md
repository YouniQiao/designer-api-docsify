# ChainAnimationOptions (System API)

链式联动动效属性集合，用于设置List最大间距、最小间距、动效强度、传导系数、边缘效果、刚度和阻尼。当列表需要精细控制链式联动弹性效果时，可通过调整本对象中的参数实现不同动效手感。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface ChainAnimationOptions--><!--Device-unnamed-declare interface ChainAnimationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## conductivity

```TypeScript
conductivity?: number
```

设置链式联动动效传导系数，控制联动影响范围。取值范围[0,1]，数值越大，链式联动影响的列表项数量越多；超出范围时使用默认值。

默认值：0.7

**Type:** number

**Default:** 0.7

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChainAnimationOptions-conductivity?: number--><!--Device-ChainAnimationOptions-conductivity?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## damping

```TypeScript
damping?: number
```

设置链式联动动效效果阻尼，控制振荡衰减速度。

取值范围：(0, +∞)，数值越大，动效衰减越快，震荡次数越少；数值越小，动效越容易产生震荡。设置为小于或等于0的值时，保持当前值不变；未设置过时使用默认值。

默认值：30

**Type:** number

**Default:** 30

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChainAnimationOptions-damping?: number--><!--Device-ChainAnimationOptions-damping?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## edgeEffect

```TypeScript
edgeEffect?: ChainEdgeEffect
```

设置链式联动动效边缘效果，控制列表滚动到边缘后的间距变化方式。DEFAULT呈现方向性拉伸、回弹反馈，STRETCH呈现所有列表项同步拉伸反馈。

默认值：ChainEdgeEffect.DEFAULT

**Type:** [ChainEdgeEffect](arkts-arkui-chainedgeeffect-e-sys.md)

**Default:** ChainEdgeEffect.DEFAULT

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChainAnimationOptions-edgeEffect?: ChainEdgeEffect--><!--Device-ChainAnimationOptions-edgeEffect?: ChainEdgeEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## intensity

```TypeScript
intensity?: number
```

设置链式联动动效效果强度，控制列表项在链式联动中的位移幅度。取值范围[0,1]，数值越大，列表项在链式联动中的位移幅度越大；超出范围时使用默认值。

默认值：0.3

**Type:** number

**Default:** 0.3

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChainAnimationOptions-intensity?: number--><!--Device-ChainAnimationOptions-intensity?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## maxSpace

```TypeScript
maxSpace: Length
```

设置链式联动动效最大间距。

单位：与Length一致。小于当前列表项间距（space）时按当前列表项间距处理。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChainAnimationOptions-maxSpace: Length--><!--Device-ChainAnimationOptions-maxSpace: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## minSpace

```TypeScript
minSpace: Length
```

设置链式联动动效最小间距。

单位：与Length一致。小于0时按0处理；大于当前列表项间距（space）时按当前列表项间距处理。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChainAnimationOptions-minSpace: Length--><!--Device-ChainAnimationOptions-minSpace: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## stiffness

```TypeScript
stiffness?: number
```

设置链式联动动效效果刚度，控制回弹速度和动画硬度。

取值范围：(0, +∞)，数值越大，回弹速度越快，动画表现越硬；数值越小，动画越柔和。设置为小于或等于0的值时，保持当前值不变；未设置过时使用默认值。

默认值：228

**Type:** number

**Default:** 228

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChainAnimationOptions-stiffness?: number--><!--Device-ChainAnimationOptions-stiffness?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

