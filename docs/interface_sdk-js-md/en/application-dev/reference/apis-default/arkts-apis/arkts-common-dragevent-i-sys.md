# DragEvent

DragEvent object description

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface DragEvent--><!--Device-unnamed-export declare interface DragEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableInternalDropAnimation

```TypeScript
enableInternalDropAnimation(configuration: string): void
```

Enable the internal drop animation, which is only avaiable for system applications.

The animations' configuration need to be provided through the input paramerter, and it is a string in json format.

This method can only be called in onDrop, and please do not use custom drop animation after this method, as it will reset the calling result, and use custom drop animation insteadly.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [190003](../../apis-arkui/errorcode-drag-event.md#190003-operation-not-allowed-in-the-current-phase) | Operation not allowed for current phase. |

## executeFollowHandMorphDropAnimation

```TypeScript
executeFollowHandMorphDropAnimation(onAnimationFinished: VoidCallback, animationOption?: string): void
```

Setup one follow-hand morph drop animation execution callback, which will be triggered by system after the drag framework animation ends. [Note]: 1. This method is effective only when dragAnimationType is FOLLOW_HAND_MORPH. 2. Do not implement animation no-related logic in the callback.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-executeFollowHandMorphDropAnimation(onAnimationFinished: VoidCallback, animationOption?: string): void--><!--Device-DragEvent-executeFollowHandMorphDropAnimation(onAnimationFinished: VoidCallback, animationOption?: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onAnimationFinished | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) | Yes | the callback triggered after framework animation ends. |
| animationOption | string | No | optional animation option payload that will be forwarded by framework. |

## dragAnimationType

```TypeScript
dragAnimationType?: DragAnimationType
```

Sets the drag animation type. This property can only be set during onDragStart, but can be retrieved in any onDragXXX callback.

**Type:** [DragAnimationType](arkts-common-draganimationtype-e-sys.md)

**Default:** DragAnimationType.DEFAULT

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-dragAnimationType?: DragAnimationType--><!--Device-DragEvent-dragAnimationType?: DragAnimationType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

