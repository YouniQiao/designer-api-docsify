# trailOptimizedResponsiveSpringMotion (System API)

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## trailOptimizedResponsiveSpringMotion

```TypeScript
function trailOptimizedResponsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number, trail?: TrailOptimization): ICurve
```

Creates a responsive spring animation curve. It is a special case of [springMotion](arkts-arkui-curves-springmotion-f.md), with the only difference in the default values. It can be used together with **springMotion**.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | number | No | See **response** in **springMotion**.Default value: **0.15**Unit: second Value range: (0, +∞)   **NOTE：**If this parameter is set to a value less than or equal to 0, the default value **0.15** is used. |
| dampingFraction | number | No | See **dampingFraction** in **springMotion**.Default value: **0.86**Unit: second Value range: 0, +∞)   **NOTE：**A value less than 0 evaluates to the default value **0.86**. |
| overlapDuration | number | No | See **overlapDuration** in **springMotion**.Default value: **0.25**Unit: second Value range: [0, +∞)   **NOTE：**A value less than 0 evaluates to the default value **0.25**. **ResponsiveSpringMotion** is a special case of **springMotion**, with the only difference in the default values. To apply custom settings for a spring animation, you are advised to use **springMotion**. When using **responsiveSpringMotion**, you are advised to retain the default settings.The duration of the responsive spring animation depends on the **responsiveSpringMotion** parameters and the previous velocity, rather than the duration parameter in [animation, animateTo, or pageTransition. In addition, the interpolation cannot be obtained using the **interpolate** function of the curve. |
| trail | [TrailOptimization](arkts-arkui-curves-trailoptimization-i-sys.md) | No | Trail optimization configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| ICurve | Curve. |
