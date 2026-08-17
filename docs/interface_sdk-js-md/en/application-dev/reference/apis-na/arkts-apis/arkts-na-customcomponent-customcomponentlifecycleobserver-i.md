# CustomComponentLifecycleObserver

CustomComponent LifecycleObserver. When a user registers a custom component lifecycle callback, the corresponding lifecycle callback will be triggered when the lifecycle changes.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-unnamed-export declare interface CustomComponentLifecycleObserver--><!--Device-unnamed-export declare interface CustomComponentLifecycleObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToAppear

```TypeScript
aboutToAppear(): void
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CustomComponentLifecycleObserver-aboutToAppear(): void--><!--Device-CustomComponentLifecycleObserver-aboutToAppear(): void-End-->

## aboutToDisappear

```TypeScript
aboutToDisappear(): void
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CustomComponentLifecycleObserver-aboutToDisappear(): void--><!--Device-CustomComponentLifecycleObserver-aboutToDisappear(): void-End-->

## aboutToRecycle

```TypeScript
aboutToRecycle(): void
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CustomComponentLifecycleObserver-aboutToRecycle(): void--><!--Device-CustomComponentLifecycleObserver-aboutToRecycle(): void-End-->

## aboutToReuse

```TypeScript
aboutToReuse(params?: ReuseObject): void
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CustomComponentLifecycleObserver-aboutToReuse(params?: ReuseObject): void--><!--Device-CustomComponentLifecycleObserver-aboutToReuse(params?: ReuseObject): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [ReuseObject](arkts-na-customcomponent-reuseobject-c.md) | No |  |

## onDidBuild

```TypeScript
onDidBuild(): void
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CustomComponentLifecycleObserver-onDidBuild(): void--><!--Device-CustomComponentLifecycleObserver-onDidBuild(): void-End-->

## default

```TypeScript
default
```

Callback function invoked when the component is about to be recycled.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentLifecycleObserver-default--><!--Device-CustomComponentLifecycleObserver-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

