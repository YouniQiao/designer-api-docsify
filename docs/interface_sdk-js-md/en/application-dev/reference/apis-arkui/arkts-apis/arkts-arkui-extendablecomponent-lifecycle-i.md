# LifeCycle

自定义组件和自定义对话框的生命周期接口。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface LifeCycle--><!--Device-unnamed-export declare interface LifeCycle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToAppear

```TypeScript
default aboutToAppear(): void
```

aboutToAppear Method.

The aboutToAppear function is executed after a new instance of the custom component is created,before its build() function is executed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LifeCycle-default aboutToAppear(): void--><!--Device-LifeCycle-default aboutToAppear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToDisappear

```TypeScript
default aboutToDisappear(): void
```

aboutToDisappear Method.

The aboutToDisappear function executes before a custom component is destroyed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LifeCycle-default aboutToDisappear(): void--><!--Device-LifeCycle-default aboutToDisappear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## build

```TypeScript
build(): void
```

Customize the build process of the custom component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-LifeCycle-build(): void--><!--Device-LifeCycle-build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidBuild

```TypeScript
default onDidBuild(): void
```

onDidBuild函数在执行自定义组件的build()函数之后执行，开发者可以在这个阶段进行埋点数据上报等不影响实际UI的功能。不建议在onDidBuild函数中更改状态变量、使用animateTo等功能，这可能会导致不稳定的UI表现。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LifeCycle-default onDidBuild(): void--><!--Device-LifeCycle-default onDidBuild(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

