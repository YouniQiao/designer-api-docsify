# WindowAnimationController (System API)

窗口动画控制器。在创建一个WindowAnimationController对象时，需要实现其中的所有回调函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-windowAnimationManager-export interface WindowAnimationController--><!--Device-windowAnimationManager-export interface WindowAnimationController-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { windowAnimationManager } from 'kits/@kit.ArkUI';
```

## onAppTransition

```TypeScript
onAppTransition(fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,
      finishCallback: WindowAnimationFinishedCallback): void
```

应用转场时的回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onAppTransition(fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onAppTransition(fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fromWindowTarget | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | 转场前的动画窗口。 |
| toWindowTarget | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | 转场后的动画窗口。 |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | 动画完成后的回调。 |

## Examples

For details, see the sample code under [windowAnimationManager.setController](#windowanimationmanagersetcontroller).

## onAppTransition

```TypeScript
onAppTransition?: AppTransitionCallback
```

应用转场时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WindowAnimationController-onAppTransition?: AppTransitionCallback--><!--Device-WindowAnimationController-onAppTransition?: AppTransitionCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onCloseWindow

```TypeScript
onCloseWindow(closingWindowTarget: WindowAnimationTarget, finishCallback: WindowAnimationFinishedCallback): void
```

关闭窗口时的回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onCloseWindow(closingWindowTarget: WindowAnimationTarget, finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onCloseWindow(closingWindowTarget: WindowAnimationTarget, finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| closingWindowTarget | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | 动画目标窗口。 |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | 动画完成后的回调。 |

## Examples

For details, see the sample code under [windowAnimationManager.setController](#windowanimationmanagersetcontroller).

## onCloseWindow

```TypeScript
onCloseWindow?: WindowCloseCallback
```

关闭窗口时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WindowAnimationController-onCloseWindow?: WindowCloseCallback--><!--Device-WindowAnimationController-onCloseWindow?: WindowCloseCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onMinimizeWindow

```TypeScript
onMinimizeWindow(minimizingWindowTarget: WindowAnimationTarget,
      finishCallback: WindowAnimationFinishedCallback): void
```

最小化窗口时的回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onMinimizeWindow(minimizingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onMinimizeWindow(minimizingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minimizingWindowTarget | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | 动画目标窗口。 |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | 动画完成后的回调。 |

## Examples

For details, see the sample code under [windowAnimationManager.setController](#windowanimationmanagersetcontroller).

## onMinimizeWindow

```TypeScript
onMinimizeWindow?: WindowMinimizationCallback
```

最小化窗口时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WindowAnimationController-onMinimizeWindow?: WindowMinimizationCallback--><!--Device-WindowAnimationController-onMinimizeWindow?: WindowMinimizationCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onScreenUnlock

```TypeScript
onScreenUnlock(finishCallback: WindowAnimationFinishedCallback): void
```

屏幕解锁时的回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onScreenUnlock(finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onScreenUnlock(finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | 动画完成后的回调。 |

## onScreenUnlock

```TypeScript
onScreenUnlock?: ScreenUnlockCallback
```

屏幕解锁时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WindowAnimationController-onScreenUnlock?: ScreenUnlockCallback--><!--Device-WindowAnimationController-onScreenUnlock?: ScreenUnlockCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onStartAppFromLauncher

```TypeScript
onStartAppFromLauncher(startingWindowTarget: WindowAnimationTarget,
      finishCallback: WindowAnimationFinishedCallback): void
```

从桌面启动应用时的回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onStartAppFromLauncher(startingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onStartAppFromLauncher(startingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startingWindowTarget | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | 动画目标窗口。 |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | 动画完成后的回调。 |

## Examples

For details, see the sample code under [windowAnimationManager.setController](#windowanimationmanagersetcontroller).

## onStartAppFromLauncher

```TypeScript
onStartAppFromLauncher?: AppStartCallback
```

从桌面启动应用时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WindowAnimationController-onStartAppFromLauncher?: AppStartCallback--><!--Device-WindowAnimationController-onStartAppFromLauncher?: AppStartCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onStartAppFromOther

```TypeScript
onStartAppFromOther(startingWindowTarget: WindowAnimationTarget,
      finishCallback: WindowAnimationFinishedCallback): void
```

从除了桌面和最近任务列表以外其他地方启动应用时的回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onStartAppFromOther(startingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onStartAppFromOther(startingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startingWindowTarget | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | 动画目标窗口。 |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | 动画完成后的回调 |

## Examples

For details, see the sample code under [windowAnimationManager.setController](#windowanimationmanagersetcontroller).

## onStartAppFromOther

```TypeScript
onStartAppFromOther?: AppStartCallback
```

从除了桌面和最近任务列表以外其他地方启动应用时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WindowAnimationController-onStartAppFromOther?: AppStartCallback--><!--Device-WindowAnimationController-onStartAppFromOther?: AppStartCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onStartAppFromRecent

```TypeScript
onStartAppFromRecent(startingWindowTarget: WindowAnimationTarget,
      finishCallback: WindowAnimationFinishedCallback): void
```

从最近任务列表启动应用时的回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onStartAppFromRecent(startingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onStartAppFromRecent(startingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startingWindowTarget | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | 动画目标窗口。 |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | 动画完成后的回调。 |

## Examples

For details, see the sample code under [windowAnimationManager.setController](#windowanimationmanagersetcontroller).

## onStartAppFromRecent

```TypeScript
onStartAppFromRecent?: AppStartCallback
```

从最近任务列表启动应用时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WindowAnimationController-onStartAppFromRecent?: AppStartCallback--><!--Device-WindowAnimationController-onStartAppFromRecent?: AppStartCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onWindowAnimationTargetsUpdate

```TypeScript
onWindowAnimationTargetsUpdate(fullScreenWindowTarget: WindowAnimationTarget,
      floatingWindowTargets: Array<WindowAnimationTarget>): void
```

动画目标窗口更新时的回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onWindowAnimationTargetsUpdate(fullScreenWindowTarget: WindowAnimationTarget,      floatingWindowTargets: Array<WindowAnimationTarget>): void--><!--Device-WindowAnimationController-onWindowAnimationTargetsUpdate(fullScreenWindowTarget: WindowAnimationTarget,      floatingWindowTargets: Array<WindowAnimationTarget>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fullScreenWindowTarget | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | 全屏状态的动画目标窗口。 |
| floatingWindowTargets | Array&lt;WindowAnimationTarget&gt; | Yes | 悬浮状态的动画目标窗口。 |

## Examples

For details, see the sample code under [windowAnimationManager.setController](#windowanimationmanagersetcontroller).

## onWindowAnimationTargetsUpdate

```TypeScript
onWindowAnimationTargetsUpdate?: WindowAnimationTargetsUpdationCallback
```

动画目标窗口更新时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WindowAnimationController-onWindowAnimationTargetsUpdate?: WindowAnimationTargetsUpdationCallback--><!--Device-WindowAnimationController-onWindowAnimationTargetsUpdate?: WindowAnimationTargetsUpdationCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

