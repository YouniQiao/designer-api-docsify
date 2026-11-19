# ScrollSnapOffsetProvider

```TypeScript
declare interface ScrollSnapOffsetProvider
```

Provides custom offsets for two-stage scroll snapping with scrollSnapStrategy in Grid and WaterFlow.

Offsets are in vp and velocity is in vp/s. Callbacks are invoked synchronously on the UI thread and must be pure calculations. No layout snapshot is provided; a provider must maintain or derive item geometry itself. velocity is the time derivative of the logical content scroll offset, positive toward the content end. The component normalizes reversed layouts and RTL directions. decayOffset is the non-negative magnitude of the natural friction decay distance.

**Since:** 26.1.0

<!--Device-unnamed-declare interface ScrollSnapOffsetProvider--><!--Device-unnamed-declare interface ScrollSnapOffsetProvider-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## calculateApproachOffset

```TypeScript
calculateApproachOffset(velocity: number, decayOffset: number): number
```

Called once at the start of a fling to determine how far the content scrolls before snapping.

The return value is a non-negative finite distance magnitude and may be greater than or equal to decayOffset. A non-finite return value, a negative return value, or a callback exception uses the predicted fling distance instead. The snap phase still follows.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ScrollSnapOffsetProvider-calculateApproachOffset(velocity: number, decayOffset: number): number--><!--Device-ScrollSnapOffsetProvider-calculateApproachOffset(velocity: number, decayOffset: number): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| velocity | number | Yes | Initial fling velocity, positive toward the content end, in vp/s. |
| decayOffset | number | Yes | Predicted distance of the default fling, in vp. Always non-negative. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Distance to scroll during the fling, in vp. |

## calculateSnapOffset

```TypeScript
calculateSnapOffset(velocity: number): number
```

Called once when the approach motion hands off to the final snap animation.

Return a finite target offset on the logical scroll axis. Zero is the content start; offsets are positive toward the content end and negative in the opposite direction. A target outside the scrollable range is clamped to the nearest boundary. If the target exceeds the current offset, the component scrolls toward the content end; if smaller, toward the start. Equal offsets cause no scrolling. If the callback returns a non-finite value or throws an exception, the component stops at its current position.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ScrollSnapOffsetProvider-calculateSnapOffset(velocity: number): number--><!--Device-ScrollSnapOffsetProvider-calculateSnapOffset(velocity: number): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| velocity | number | Yes | Velocity at the start of this approach stage, positive toward the content end, in vp/s. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Absolute target scroll offset, in vp. |
