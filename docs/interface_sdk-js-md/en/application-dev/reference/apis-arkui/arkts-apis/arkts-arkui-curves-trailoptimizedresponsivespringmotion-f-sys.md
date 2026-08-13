# trailOptimizedResponsiveSpringMotion (System API)

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## trailOptimizedResponsiveSpringMotion

```TypeScript
function trailOptimizedResponsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number, trail?: TrailOptimization): ICurve
```

Creates a responsive spring animation curve. It is a special case of [springMotion](../../apis-na/arkts-apis/arkts-na-curves-springmotion-f.md#springMotion), with the only difference in the default values. It can be used together with **springMotion**.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-function trailOptimizedResponsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number, trail?: TrailOptimization): ICurve--><!--Device-curves-function trailOptimizedResponsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number, trail?: TrailOptimization): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | number | No | See **response** in **springMotion**.&lt;br&gt;Default value: **0.15**&lt;br&gt;Unit: second&lt;br&gt; Value range: (0, +∞)&lt;br&gt;**NOTE：**&lt;br&gt;If this parameter is set to a value less than or equal to 0, the default value **0.15** is used. |
| dampingFraction | number | No | See **dampingFraction** in **springMotion**.&lt;br&gt;Default value: **0.86**&lt;br&gt; Unit: second&lt;br&gt;Value range: 0, +∞)&lt;br&gt;**NOTE：**&lt;br&gt;A value less than 0 evaluates to the default value **0.86**. |
| overlapDuration | number | No | See **overlapDuration** in **springMotion**.&lt;br&gt;Default value: **0.25**&lt;br&gt; Unit: second&lt;br&gt;Value range: [0, +∞)&lt;br&gt;**NOTE：**&lt;br&gt;A value less than 0 evaluates to the default value **0.25**.&lt;br&gt;**ResponsiveSpringMotion** is a special case of **springMotion**, with the only difference in the default values. To apply custom settings for a spring animation, you are advised to use **springMotion**. When using **responsiveSpringMotion**, you are advised to retain the default settings.&lt;br&gt;The duration of the responsive spring animation depends on the **responsiveSpringMotion** parameters and the previous velocity, rather than the duration parameter in [animation, animateTo, or pageTransition. In addition, the interpolation cannot be obtained using the **interpolate** function of the curve. |
| trail | [TrailOptimization](arkts-arkui-curves-trailoptimization-i-sys.md) | No | Trail optimization configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| ICurve | Curve. &lt;br&gt;**NOTE：**&lt;br&gt;1. To apply custom settings for a spring animation, you are advised to use **springMotion**. When using **responsiveSpringMotion**, you are advised to retain the default settings. &lt;br&gt;2. The duration of the responsive spring animation depends on the **responsiveSpringMotion** parameters and the previous velocity, rather than the duration parameter in [animation]{ |

