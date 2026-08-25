# CustomComponentLifecycleObserver

CustomComponent LifecycleObserver. When a user registers a custom component lifecycle callback, the corresponding lifecycle callback will be triggered when the lifecycle changes.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToAppear

```TypeScript
default aboutToAppear(): void
```

The aboutToAppear function is extecuted after a new instance of the custom component is created, before its build() function is executed. Developers can modify state variables at this stage.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToDisappear

```TypeScript
default aboutToDisappear(): void
```

The aboutToDisappear function executes before a custom component is destroyed. It is not allowed to change state variables in aboutToDisappear.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToRecycle

```TypeScript
default aboutToRecycle(): void
```

Callback function invoked when the component is about to be recycled.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToReuse

```TypeScript
default aboutToReuse(params?: ReuseObject): void
```

Invoked when a reusable custom component is re-added to the node tree from the reuse cache to receive construction parameters of the component. When params is defined, it is the callback for reusing the V1 component. When params is undefined, it is the callback for reusing the V2 compoennt.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [ReuseObject](arkts-arkui-customcomponent-reuseobject-c.md) | No |

## onDidBuild

```TypeScript
default onDidBuild(): void
```

The onDidBuild function is executed after a new instance of the custom component is built, after its build() function is executed. Developers can implement functions that do not affect the actual UI, such as event data reporting, at this stage.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
