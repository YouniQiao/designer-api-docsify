# responsiveSpringMotion

## Modules to Import

```TypeScript
import curves from '@kit.ArkUI';
```

## responsiveSpringMotion

```TypeScript
function responsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve
```

Creates a responsive spring animation curve. It is a special case of [springMotion](arkts-arkui-curves-springmotion-f.md), with the only difference in the default values. It can be used together with **springMotion**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | number | No | See **response** in **springMotion**.Default value: **0.15**Unit: second Value range: (0, +∞)   **NOTE：**If this parameter is set to a value less than or equal to 0, the default value **0.15** is used. |
| dampingFraction | number | No | See **dampingFraction** in **springMotion**.Default value: **0.86**Unit: second Value range: 0, +∞)   **NOTE：**A value less than 0 evaluates to the default value **0.86**. |
| overlapDuration | number | No | See **overlapDuration** in **springMotion**.Default value: **0.25**Unit: second Value range: [0, +∞)   **NOTE：**A value less than 0 evaluates to the default value **0.25**. **ResponsiveSpringMotion** is a special case of **springMotion**, with the only difference in the default values. To apply custom settings for a spring animation, you are advised to use **springMotion**. When using **responsiveSpringMotion**, you are advised to retain the default settings.The duration of the responsive spring animation depends on the **responsiveSpringMotion** parameters and the previous velocity, rather than the duration parameter in [animation, animateTo, or pageTransition. In addition, the interpolation cannot be obtained using the **interpolate** function of the curve. |

**Return value:**

| Type | Description |
| --- | --- |
| [ICurve](../arkts-components/arkts-arkui-icurve-i.md) | Curve. |

**Examples**

```TypeScript
import { curves } from '@kit.ArkUI';
curves.responsiveSpringMotion(); // Create a responsive spring animation curve with default settings.
```
