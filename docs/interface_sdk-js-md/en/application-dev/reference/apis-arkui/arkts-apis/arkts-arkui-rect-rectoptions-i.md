# RectOptions

用于描述Rect组件绘制属性。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RectOptions--><!--Device-unnamed-export declare interface RectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Length
```

高度，取值范围≥0。默认值：0默认单位：vp异常值undefined、null、NaN和Infinity按照默认值处理。

Anonymous Object Rectification

**Type:** [Length](arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectOptions-height?: Length--><!--Device-RectOptions-height?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radius

```TypeScript
radius?: Length | Array<RadiusItem>
```

圆角半径，支持分别设置四个角的圆角度数，取值范围≥0。该属性和radiusWidth/radiusHeight属性效果类似，在组合使用时优先于radiusWidth/radiusHeight生效。默认值：0默认单位：vp异常值undefined、null、NaN和Infinity按照默认值处理。

Anonymous Object Rectification

**Type:** [Length](arkts-arkui-length-t.md) \| Array&lt;RadiusItem&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectOptions-radius?: Length | Array<RadiusItem>--><!--Device-RectOptions-radius?: Length | Array<RadiusItem>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Length
```

宽度，取值范围≥0。默认值：0默认单位：vp异常值undefined、null、NaN和Infinity按照默认值处理。

Anonymous Object Rectification

**Type:** [Length](arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectOptions-width?: Length--><!--Device-RectOptions-width?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

