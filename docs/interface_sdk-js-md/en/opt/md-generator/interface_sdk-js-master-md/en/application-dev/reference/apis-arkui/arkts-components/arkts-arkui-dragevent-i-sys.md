# DragEvent

Provides information about the drag event.

**Since:** 7

<!--Device-unnamed-declare interface DragEvent--><!--Device-unnamed-declare interface DragEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableInternalDropAnimation

```TypeScript
enableInternalDropAnimation(configuration: string): void
```

Sets whether to enable the system's built-in drop animation effect. This API is available only to system applications and can only be used during the **onDrop** phase.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-enableInternalDropAnimation(configuration: string): void--><!--Device-DragEvent-enableInternalDropAnimation(configuration: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configuration | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [190003](../errorcode-drag-event.md#190003-operation-not-allowed-in-the-current-phase) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## executeFollowHandMorphDropAnimation

```TypeScript
executeFollowHandMorphDropAnimation(onAnimationFinished: Callback<void>, animationOption?: string): void
```

Sets a callback to be executed after the follow-hand morph drop animation is completed. This callback is triggered by the system after the drag framework animation ends. This callback uses an asynchronous callback.

> **NOTE：**
> 
> 1. This API takes effect only when [dragAnimationType](arkts-arkui-dragevent-i-sys.md#draganimationtype) is
> set to **DragAnimationType.FOLLOW_HAND_MORPH**.
> 
> 2. Do not implement logic unrelated to the animation in the callback to avoid affecting execution efficiency.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-executeFollowHandMorphDropAnimation(onAnimationFinished: Callback<void>, animationOption?: string): void--><!--Device-DragEvent-executeFollowHandMorphDropAnimation(onAnimationFinished: Callback<void>, animationOption?: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| onAnimationFinished | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |
| animationOption | string | No |

## dragAnimationType

```TypeScript
dragAnimationType?: DragAnimationType
```

Sets the drag animation type. This attribute can only be set during the  
[onDragStart](arkts-arkui-commonmethod-c.md#ondragstart) phase and can be obtained in the  
[onDragStart](arkts-arkui-commonmethod-c.md#ondragstart), [onDragEnter](arkts-arkui-commonmethod-c.md#ondragenter),  
[onDragMove](arkts-arkui-commonmethod-c.md#ondragmove), [onDragLeave](arkts-arkui-commonmethod-c.md#ondragleave),  
[onDrop](arkts-arkui-commonmethod-c.md#ondrop), and  
[onDragEnd](arkts-arkui-commonmethod-c.md#ondragend) callbacks.

Default value: **DEFAULT**

**System API:** This is a system API.

**Type:** [DragAnimationType](arkts-arkui-draganimationtype-e-sys.md)

**Default:** DragAnimationType.DEFAULT

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-dragAnimationType?: DragAnimationType--><!--Device-DragEvent-dragAnimationType?: DragAnimationType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.
