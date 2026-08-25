# CustomComponentLifecycle

CustomComponent Lifecycle. It is used to monitor changes in the lifecycle of the custom component.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addObserver

```TypeScript
addObserver(observer: CustomComponentLifecycleObserver): void
```

Register a lifecycle listener. When the lifecycle state of a custom component changes, the corresponding lifecycle callback will be triggered.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](arkts-arkui-viewmodel-observer-i.md) | [CustomComponentLifecycleObserver](arkts-arkui-customcomponent-customcomponentlifecycleobserver-i.md) | Yes |

## getCurrentState

```TypeScript
getCurrentState(): CustomComponentLifecycleState
```

Get the current lifecycle state.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CustomComponentLifecycleState](arkts-arkui-customcomponent-customcomponentlifecyclestate-e.md) |

## removeObserver

```TypeScript
removeObserver(observer: CustomComponentLifecycleObserver): void
```

Remove custom component lifecycle callbacks. Even if the custom component's lifecycle state changes, the lifecycle callback will not be triggered.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](arkts-arkui-viewmodel-observer-i.md) | [CustomComponentLifecycleObserver](arkts-arkui-customcomponent-customcomponentlifecycleobserver-i.md) | Yes |
