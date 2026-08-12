# DragEvent

Provides information about the drag event.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare interface DragEvent--><!--Device-unnamed-declare interface DragEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableInternalDropAnimation

```TypeScript
enableInternalDropAnimation(configuration: string): void
```

Sets whether to enable the system's built-in drop animation effect. This API is available only to system applications and can only be used during the **onDrop** phase.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-enableInternalDropAnimation(configuration: string): void--><!--Device-DragEvent-enableInternalDropAnimation(configuration: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| configuration | string | Yes | the internal drop animation's configuration. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [190003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-drag-event.md#190003-operation-not-allowed-in-the-current-phase) | Operation not allowed for current phase. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |

## executeFollowHandMorphDropAnimation

```TypeScript
executeFollowHandMorphDropAnimation(onAnimationFinished: Callback<void>, animationOption?: string): void
```

Sets a callback to be executed after the follow-hand morph drop animation is completed. This callback is triggered by the system after the drag framework animation ends. This callback uses an asynchronous callback.

> **NOTE：**
> 
> 1. This API takes effect only when [dragAnimationType](#dragAnimationType) is
> set to **DragAnimationType.FOLLOW_HAND_MORPH**.
> 
> 2. Do not implement logic unrelated to the animation in the callback to avoid affecting execution efficiency.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-executeFollowHandMorphDropAnimation(onAnimationFinished: Callback<void>, animationOption?: string): void--><!--Device-DragEvent-executeFollowHandMorphDropAnimation(onAnimationFinished: Callback<void>, animationOption?: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onAnimationFinished | [Callback](arkts-arkui-callback-i.md)&lt;void&gt; | Yes | Callback triggered after the drag framework animation ends. |
| animationOption | string | No | Drop animation parameters.&lt;br&gt;The parameter is a JSON string containing the following fields:&lt;br&gt;**CubicCurveEnable**: boolean, indicating whether to enable the cubic curve animation. Set to **true** to enable it, or **false** to disable it.&lt;br&gt;**SpringEnable**: boolean, indicating whether to enable the spring animation. Set to **true** to enable it, or **false** to disable it.&lt;br&gt; **dropAnimationCurve**: number[], indicating the drop animation curve parameters. Its meaning depends on **SpringEnable** and **CubicCurveEnable** (with **SpringEnable** having higher priority). When **SpringEnable** is **true**, the array length is 3, in the format of [response, dampingRatio, blendDuration], corresponding to the spring curve parameters of [curves.springMotion](../arkts-apis/arkts-arkui-curves-springmotion-f.md#springMotion). When **SpringEnable** is **false** and **CubicCurveEnable** is **true**, the array length is 4, in the format of [x1, y1, x2, y2], corresponding to the cubic Bezier curve control point parameters of [curves.cubicBezierCurve](../arkts-apis/arkts-arkui-curves-cubicbeziercurve-f.md#cubicBezierCurve).&lt;br&gt;**NOTE:** **SpringEnable** takes priority over **CubicCurveEnable**. When both are **true**, the spring animation prevails. When neither **SpringEnable** nor **CubicCurveEnable** is correctly set, the default spring animation is used.&lt;br&gt; **dropPosition**: number[], indicating the drop position coordinates. The array length is 2, in the format of [x, y], in px, representing the target position coordinates of the dragged element when it drops. Value range: (-∞, +∞).&lt;br&gt;**dropSize**: number[], indicating the drop size. The array length is 2, in the format of [width, height], in px, representing the target size of the dragged element when it drops. Value range: (0, +∞). |

## dragAnimationType

```TypeScript
dragAnimationType?: DragAnimationType
```

Sets the drag animation type. This attribute can only be set during the  
[onDragStart](arkts-arkui-commonmethod-c.md#onDragStart) phase and can be obtained in the  
[onDragStart](arkts-arkui-commonmethod-c.md#onDragStart), [onDragEnter](arkts-arkui-commonmethod-c.md#onDragEnter),  
[onDragMove](arkts-arkui-commonmethod-c.md#onDragMove), [onDragLeave](arkts-arkui-commonmethod-c.md#onDragLeave),  
[onDrop](CommonMethod#onDrop(event: (event: DragEvent, extraParams?: string) => void)), and  
[onDragEnd](arkts-arkui-commonmethod-c.md#onDragEnd) callbacks.

Default value: **DEFAULT**

**System API:** This is a system API.

**Type:** [DragAnimationType](arkts-arkui-draganimationtype-e-sys.md)

**Default:** DragAnimationType.DEFAULT

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-dragAnimationType?: DragAnimationType--><!--Device-DragEvent-dragAnimationType?: DragAnimationType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

