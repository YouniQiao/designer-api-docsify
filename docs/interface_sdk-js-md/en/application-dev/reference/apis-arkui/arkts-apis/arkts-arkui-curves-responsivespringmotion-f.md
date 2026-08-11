# responsiveSpringMotion

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## responsiveSpringMotion

```TypeScript
export function responsiveSpringMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve
```

Creates a responsive spring animation curve. It is a special case of [springMotion](#curvesspringmotion9),with the only difference in the default values. It can be used together with **springMotion**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function responsiveSpringMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve--><!--Device-curves-export function responsiveSpringMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | double | No | See **response** in **springMotion**.&lt;br&gt;Default value: **0.15**. Unit: second&lt;br&gt;Value range: (0, +∞). &lt;p&gt;**NOTE：**: &lt;br&gt;If this parameter is set to a value less than or equal to 0, the default value **0.15** is used. &lt;/p&gt; |
| dampingFraction | double | No | See **dampingFraction** in **springMotion**.&lt;br&gt;Default value: **0.86**. Unit: second&lt;br&gt;Value range: [0, +∞). &lt;p&gt;**NOTE：**&lt;br&gt;A value less than 0 evaluates to the default value **0.86**. &lt;/p&gt; |
| overlapDuration | double | No | See **overlapDuration** in **springMotion**.&lt;br&gt;Default value: **0.25**. Unit: second&lt;br&gt;Value range: [0, +∞). &lt;p&gt;**NOTE：**: &lt;br&gt;A value less than 0 evaluates to the default value **0.25**. &lt;br&gt;To apply custom settings for a spring animation, you are advised to use **springMotion**. &lt;br&gt;When using **responsiveSpringMotion**, you are advised to retain the default settings. &lt;br&gt;The duration of the responsive spring animation depends on the **responsiveSpringMotion** parameters and the previous velocity, rather than the duration parameter in animation, animateTo, or pageTransition. &lt;br&gt;In addition, the interpolation cannot be obtained using the **interpolate** function of the curve. &lt;/p&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |  |

