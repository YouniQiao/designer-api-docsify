# responsiveSpringMotion

## responsiveSpringMotion

```TypeScript
export function responsiveSpringMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve
```

Creates a responsive spring animation curve. It is a special case of springMotion, with the only difference in the default values. It can be used together with **springMotion**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function responsiveSpringMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve--><!--Device-curves-export function responsiveSpringMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | double | No | See **response** in **springMotion**.<br>Default value: **0.15**. Unit: second<br>Value range: (0, +∞). &lt;p&gt;**NOTE：**: <br>If this parameter is set to a value less than or equal to 0, the default value **0.15** is used. &lt;/p&gt; |
| dampingFraction | double | No | See **dampingFraction** in **springMotion**.<br>Default value: **0.86**. Unit: second<br>Value range: [0, +∞). &lt;p&gt;**NOTE：**<br>A value less than 0 evaluates to the default value **0.86**. &lt;/p&gt; |
| overlapDuration | double | No | See **overlapDuration** in **springMotion**.<br>Default value: **0.25**. Unit: second<br>Value range: [0, +∞). &lt;p&gt;**NOTE：**: <br>A value less than 0 evaluates to the default value **0.25**. <br>To apply custom settings for a spring animation, you are advised to use **springMotion**. <br>When using **responsiveSpringMotion**, you are advised to retain the default settings. <br>The duration of the responsive spring animation depends on the **responsiveSpringMotion** parameters and the previous velocity, rather than the duration parameter in animation, animateTo, or pageTransition. <br>In addition, the interpolation cannot be obtained using the **interpolate** function of the curve. &lt;/p&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| ICurve |  |

