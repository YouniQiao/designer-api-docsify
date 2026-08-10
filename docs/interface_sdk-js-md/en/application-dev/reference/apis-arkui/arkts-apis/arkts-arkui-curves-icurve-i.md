# ICurve

曲线对象，支持通过本模块中的  
[curves.cubicBezierCurve](../../../reference/apis-arkui/js-apis-curve_static.md#curvescubicbeziercurve9)、  
[curves.interpolatingSpring](../../../reference/apis-arkui/js-apis-curve_static.md#curvesinterpolatingspring10)等方法创建不同类型的曲线对象，并可通过曲线对象调用其[interpolate](../../../reference/apis-arkui/js-apis-curve_static.md#interpolate9)的成员方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-curves-export interface ICurve--><!--Device-curves-export interface ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## interpolate

```TypeScript
interpolate(fraction: double): double
```

插值曲线的插值计算函数，可以通过传入的归一化时间参数返回当前的插值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ICurve-interpolate(fraction: double): double--><!--Device-ICurve-interpolate(fraction: double): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fraction | double | Yes | 当前的归一化时间参数。&lt;br/&gt;取值范围：[0,1]&lt;br/&gt;**说明：** &lt;br/&gt;设置的值小于0时，按0处理；设置的值大于1时，按1处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| double | 返回归一化time时间点对应的曲线插值。 |

