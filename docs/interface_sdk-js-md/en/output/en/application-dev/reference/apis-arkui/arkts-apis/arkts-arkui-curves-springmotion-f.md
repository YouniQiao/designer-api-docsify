# springMotion

## springMotion

```TypeScript
export function springMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve
```

Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function springMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve--><!--Device-curves-export function springMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | double | No | Duration of one complete oscillation. |
| dampingFraction | double | No | Damping coefficient. |
| overlapDuration | double | No | Duration for animations to overlap, in seconds. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

