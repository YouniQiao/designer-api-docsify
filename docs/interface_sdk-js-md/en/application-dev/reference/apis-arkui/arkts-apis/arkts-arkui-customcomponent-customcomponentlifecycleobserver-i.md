# CustomComponentLifecycleObserver

CustomComponent LifecycleObserver. When a user registers a custom component lifecycle callback,the corresponding lifecycle callback will be triggered when the lifecycle changes.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export declare interface CustomComponentLifecycleObserver--><!--Device-unnamed-export declare interface CustomComponentLifecycleObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToAppear

```TypeScript
default aboutToAppear(): void
```

The aboutToAppear function is extecuted after a new instance of the custom component is created,before its build() function is executed. Developers can modify state variables at this stage.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentLifecycleObserver-default aboutToAppear(): void--><!--Device-CustomComponentLifecycleObserver-default aboutToAppear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToDisappear

```TypeScript
default aboutToDisappear(): void
```

The aboutToDisappear function executes before a custom component is destroyed.It is not allowed to change state variables in aboutToDisappear.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentLifecycleObserver-default aboutToDisappear(): void--><!--Device-CustomComponentLifecycleObserver-default aboutToDisappear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToRecycle

```TypeScript
default aboutToRecycle(): void
```

Callback function invoked when the component is about to be recycled.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentLifecycleObserver-default aboutToRecycle(): void--><!--Device-CustomComponentLifecycleObserver-default aboutToRecycle(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToReuse

```TypeScript
default aboutToReuse(params?: ReuseObject): void
```

Invoked when a reusable custom component is re-added to the node tree from the reuse cache to receive construction parameters of the component.When params is defined, it is the callback for reusing the V1 component.When params is undefined, it is the callback for reusing the V2 compoennt.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentLifecycleObserver-default aboutToReuse(params?: ReuseObject): void--><!--Device-CustomComponentLifecycleObserver-default aboutToReuse(params?: ReuseObject): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [ReuseObject](arkts-arkui-customcomponent-reuseobject-c.md) | No | V1 component reuse data. |

## onDidBuild

```TypeScript
default onDidBuild(): void
```

The onDidBuild function is executed after a new instance of the custom component is built,after its build() function is executed. Developers can implement functions that do not affect the actual UI, such as event data reporting, at this stage.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentLifecycleObserver-default onDidBuild(): void--><!--Device-CustomComponentLifecycleObserver-default onDidBuild(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

