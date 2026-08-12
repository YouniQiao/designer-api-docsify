# CustomComponentLifecycle

CustomComponent Lifecycle. It is used to monitor changes in the lifecycle of the custom component.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export declare interface CustomComponentLifecycle--><!--Device-unnamed-export declare interface CustomComponentLifecycle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addObserver

```TypeScript
addObserver(observer: CustomComponentLifecycleObserver): void
```

Register a lifecycle listener. When the lifecycle state of a custom component changes, the corresponding lifecycle callback will be triggered.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentLifecycle-addObserver(observer: CustomComponentLifecycleObserver): void--><!--Device-CustomComponentLifecycle-addObserver(observer: CustomComponentLifecycleObserver): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [CustomComponentLifecycleObserver](arkts-arkui-customcomponent-customcomponentlifecycleobserver-i.md) | Yes | Custom component lifecycle observer |

## getCurrentState

```TypeScript
getCurrentState(): CustomComponentLifecycleState
```

Get the current lifecycle state.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentLifecycle-getCurrentState(): CustomComponentLifecycleState--><!--Device-CustomComponentLifecycle-getCurrentState(): CustomComponentLifecycleState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [CustomComponentLifecycleState](arkts-arkui-customcomponent-customcomponentlifecyclestate-e.md) | lifecycle state |

## removeObserver

```TypeScript
removeObserver(observer: CustomComponentLifecycleObserver): void
```

Remove custom component lifecycle callbacks. Even if the custom component's lifecycle state changes, the lifecycle callback will not be triggered.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentLifecycle-removeObserver(observer: CustomComponentLifecycleObserver): void--><!--Device-CustomComponentLifecycle-removeObserver(observer: CustomComponentLifecycleObserver): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [CustomComponentLifecycleObserver](arkts-arkui-customcomponent-customcomponentlifecycleobserver-i.md) | Yes | Custom component lifecycle observer. |

