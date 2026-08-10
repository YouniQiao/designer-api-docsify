# responsiveSpringMotion

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## responsiveSpringMotion

```TypeScript
export function responsiveSpringMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve
```

构造弹性跟手动画曲线对象，是[springMotion](../../../reference/apis-arkui/js-apis-curve_static.md#curvesspringmotion9)的一种特例，仅默认参数不同，可与springMotion混合使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function responsiveSpringMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve--><!--Device-curves-export function responsiveSpringMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | double | No | 解释同springMotion中的response。&lt;br/&gt;默认值：0.15&lt;br/&gt;单位：秒&lt;br/&gt;取值范围：(0, +∞)&lt;br/&gt;**说明：** &lt;br/ &gt;设置小于等于0的值时，按默认值0.15处理。 |
| dampingFraction | double | No | 解释同springMotion中的dampingFraction。&lt;br/&gt;默认值：0.86&lt;br/&gt;单位：秒&lt;br/&gt;取值范围： [0, +∞)&lt;br/&gt;**说明：** &lt;br/&gt;设置小于0的值时，按默认值0.86处理。 |
| overlapDuration | double | No | 解释同springMotion中的overlapDuration。&lt;br/&gt;默认值：0.25&lt;br/&gt;单位：秒&lt;br/&gt;取值范围： [0, +∞)&lt;br/&gt;**说明：** &lt;br/&gt;设置小于0的值时，按默认值0.25处理。&lt;br/&gt;弹性跟手动画曲线为springMotion的一种特例，仅默认值不同。如果使用自定义参数的弹性曲线，推荐使用springMotion构造曲线。如果使用跟手动画，推荐使用默认参数的弹性跟手动画曲线。&lt;br/&gt;[animation](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)、[animateTo](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)、[pageTransition](page_transition)中的duration参数不生效，动画持续时间取决于responsiveSpringMotion动画曲线参数和之前的速度，也不能通过该曲线的interpolate函数获得插值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) | 曲线对象。 &lt;br&gt;**说明:** &lt;br&gt;1、弹性跟手动画曲线为springMotion的一种特例，仅默认值不同。如果使用自定义参数的弹性曲线，推荐使用springMotion构造曲线；如果使用跟手动画，推荐使用默认参数的弹性跟手动画曲线。 &lt;br&gt;2、[animation]{ |

