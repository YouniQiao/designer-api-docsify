# ScrollSnapOffsetProvider

```TypeScript
declare interface ScrollSnapOffsetProvider
```

Used to customize the distance and suction position of the kickout roll. This API applies to the scrollSnapStrategy attribute of the Grid, WaterFlow, and List components, After implementing the API, you can transfer the object to scrollSnapStrategy. For a complete example, refer to [Example 24 (Custom Scroll Adsorption Position)](../../../reference/apis-arkui/arkui-ts/ts-container-grid.md# Example 24 Custom Scroll Adsorption Position).

Custom limit scrolling is divided into two phases: scrolling at the specified distance inertia, and then scrolling to the target adsorption position through the limit animation. The two callbacks are invoked at the start time of the two phases:  
- calculateApproachOffset: Called once at the beginning of inertial scrolling.  
- calculateSnapOffset: Called once before the end of the inertia phase and the start of the limit animation.

> **Note:** 

> - The unit of offset is vp, and the unit of speed is vp/s.
> - Both callbacks are called synchronously in the UI thread and should be used only for calculations, and should not modify the component layout or application state.
> - The callback does not provide the location and size of the item. Developers need to record or calculate the information.

**Since:** 26.1.0

<!--Device-unnamed-declare interface ScrollSnapOffsetProvider--><!--Device-unnamed-declare interface ScrollSnapOffsetProvider-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## calculateApproachOffset

```TypeScript
calculateApproachOffset(velocity: number, decayOffset: number): number
```

Callback used to calculate the scrolling distance of the inertia phase. It is called once when the inertia scrolling starts.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ScrollSnapOffsetProvider-calculateApproachOffset(velocity: number, decayOffset: number): number--><!--Device-ScrollSnapOffsetProvider-calculateApproachOffset(velocity: number, decayOffset: number): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| velocity | number | Yes | The speed at which inertial scrolling begins, which is positive when scrolling towards the end of the content. The reverse layout and RTL direction are handled by the component. <br>Unit: vp/s |
| decayOffset | number | Yes | Rolls the predicted coasting distance by default inertia. <br>Unit: vp <br>Value range: [0, +∞) |

**Return value:**

| Type | Description |
| --- | --- |
| number | Rolling distance in the inertia phase, which cannot be NaN or Infinity and can exceed decayOffset. When a negative number, NaN, or Infinity is returned, or an exception is thrown by a callback, the stage rolls by the default inertial glide distance and then enters the limit animation phase normally. <br>Unit: vp<br>Value range: [0, +∞) |

## calculateSnapOffset

```TypeScript
calculateSnapOffset(velocity: number): number
```

Callback used to calculate the final suction position, called once before the end of the inertia phase and the start of the limit animation.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ScrollSnapOffsetProvider-calculateSnapOffset(velocity: number): number--><!--Device-ScrollSnapOffsetProvider-calculateSnapOffset(velocity: number): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| velocity | number | Yes | Remaining speed at the end of inertia scrolling, positive when scrolling towards the end of the content. Reverse layout and RTL direction are handled by the component. <br>Unit: vp/s |

**Return value:**

| Type | Description |
| --- | --- |
| number | The scrolling offset of the final adsorption position relative to the starting point of the content, which must be a finite value. The offset along the logical axis towards the end of the content is positive, and the reverse direction is negative. 0 indicates the start of the content. The actual scrolling direction is determined by the target position and the current scrolling position. If the target offset is greater than the current offset, scroll towards the end of the content. If the target offset is less than the current offset, scroll towards the start of the content. If the target offset is equal, do not scroll. When the scrollable range is exceeded, the target position is limited to the boundary of the scrollable range. When the callback returns NaN, Infinity, or throws an exception, the component stops at the current scrolling position. <br>Unit: vp<br>Value range: scrolling offset corresponding to the scrolling range of the component. |
