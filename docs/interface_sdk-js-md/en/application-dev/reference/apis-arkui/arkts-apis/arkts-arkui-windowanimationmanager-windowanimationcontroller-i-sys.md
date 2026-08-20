# WindowAnimationController (System API)

Window animation controller.

@interface WindowAnimationController

**Since:** 23

<!--Device-windowAnimationManager-export interface WindowAnimationController--><!--Device-windowAnimationManager-export interface WindowAnimationController-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { windowAnimationManager } from '@kit.ArkUI';
```

## onAppTransition

```TypeScript
onAppTransition(fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,
      finishCallback: WindowAnimationFinishedCallback): void
```

Called on application transition.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onAppTransition(fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onAppTransition(fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fromWindowTarget | WindowAnimationTarget | Yes | Window target of the source application. |
| toWindowTarget | WindowAnimationTarget | Yes | Window target of the destination application. |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | Animation finished callback. |

**Examples**

For details, see the sample code under windowAnimationManager.setController.

## onCloseWindow

```TypeScript
onCloseWindow(closingWindowTarget: WindowAnimationTarget, finishCallback: WindowAnimationFinishedCallback): void
```

Called on closing a window.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onCloseWindow(closingWindowTarget: WindowAnimationTarget, finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onCloseWindow(closingWindowTarget: WindowAnimationTarget, finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| closingWindowTarget | WindowAnimationTarget | Yes |  |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | Animation finished callback. |

**Examples**

For details, see the sample code under windowAnimationManager.setController.

## onMinimizeWindow

```TypeScript
onMinimizeWindow(minimizingWindowTarget: WindowAnimationTarget,
      finishCallback: WindowAnimationFinishedCallback): void
```

Called on minimizing a window.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onMinimizeWindow(minimizingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onMinimizeWindow(minimizingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minimizingWindowTarget | WindowAnimationTarget | Yes | Window target of the minimizing window. |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | Animation finished callback. |

**Examples**

For details, see the sample code under windowAnimationManager.setController.

## onScreenUnlock

```TypeScript
onScreenUnlock(finishCallback: WindowAnimationFinishedCallback): void
```

Called on unlocking the screen.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onScreenUnlock(finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onScreenUnlock(finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | Animation finished callback. |

## onStartAppFromLauncher

```TypeScript
onStartAppFromLauncher(startingWindowTarget: WindowAnimationTarget,
      finishCallback: WindowAnimationFinishedCallback): void
```

Called on starting an application form launcher.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onStartAppFromLauncher(startingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onStartAppFromLauncher(startingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startingWindowTarget | WindowAnimationTarget | Yes | indicates Window target of the starting application. |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | Animation finished callback. |

**Examples**

For details, see the sample code under windowAnimationManager.setController.

## onStartAppFromOther

```TypeScript
onStartAppFromOther(startingWindowTarget: WindowAnimationTarget,
      finishCallback: WindowAnimationFinishedCallback): void
```

Called on starting an application form other.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onStartAppFromOther(startingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onStartAppFromOther(startingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startingWindowTarget | WindowAnimationTarget | Yes | Window target of the starting application. |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | Animation finished callback. |

**Examples**

For details, see the sample code under windowAnimationManager.setController.

## onStartAppFromRecent

```TypeScript
onStartAppFromRecent(startingWindowTarget: WindowAnimationTarget,
      finishCallback: WindowAnimationFinishedCallback): void
```

Called on starting an application form recent.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onStartAppFromRecent(startingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void--><!--Device-WindowAnimationController-onStartAppFromRecent(startingWindowTarget: WindowAnimationTarget,      finishCallback: WindowAnimationFinishedCallback): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startingWindowTarget | WindowAnimationTarget | Yes | Window target of the starting application. |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | Animation finished callback. |

**Examples**

For details, see the sample code under windowAnimationManager.setController.

## onWindowAnimationTargetsUpdate

```TypeScript
onWindowAnimationTargetsUpdate(fullScreenWindowTarget: WindowAnimationTarget,
      floatingWindowTargets: Array<WindowAnimationTarget>): void
```

Called on window animation targets update.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnimationController-onWindowAnimationTargetsUpdate(fullScreenWindowTarget: WindowAnimationTarget,      floatingWindowTargets: Array<WindowAnimationTarget>): void--><!--Device-WindowAnimationController-onWindowAnimationTargetsUpdate(fullScreenWindowTarget: WindowAnimationTarget,      floatingWindowTargets: Array<WindowAnimationTarget>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fullScreenWindowTarget | WindowAnimationTarget | Yes | The fullscreen window target. |
| floatingWindowTargets | Array&lt;WindowAnimationTarget&gt; | Yes | All the floating window targets. |

**Examples**

For details, see the sample code under windowAnimationManager.setController.

## onAppTransition

```TypeScript
onAppTransition?: AppTransitionCallback
```

Callback function on application transition.

**Type:** [AppTransitionCallback](arkts-arkui-windowanimationmanager-apptransitioncallback-t-sys.md)

**Since:** 23

<!--Device-WindowAnimationController-onAppTransition?: AppTransitionCallback--><!--Device-WindowAnimationController-onAppTransition?: AppTransitionCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onCloseWindow

```TypeScript
onCloseWindow?: WindowCloseCallback
```

Callback function on closing a window.

**Type:** [WindowCloseCallback](arkts-arkui-windowanimationmanager-windowclosecallback-t-sys.md)

**Since:** 23

<!--Device-WindowAnimationController-onCloseWindow?: WindowCloseCallback--><!--Device-WindowAnimationController-onCloseWindow?: WindowCloseCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onMinimizeWindow

```TypeScript
onMinimizeWindow?: WindowMinimizationCallback
```

Callback function on minimizing a window.

**Type:** [WindowMinimizationCallback](arkts-arkui-windowanimationmanager-windowminimizationcallback-t-sys.md)

**Since:** 23

<!--Device-WindowAnimationController-onMinimizeWindow?: WindowMinimizationCallback--><!--Device-WindowAnimationController-onMinimizeWindow?: WindowMinimizationCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onScreenUnlock

```TypeScript
onScreenUnlock?: ScreenUnlockCallback
```

Callback function on unlocking the screen.

**Type:** [ScreenUnlockCallback](arkts-arkui-windowanimationmanager-screenunlockcallback-t-sys.md)

**Since:** 23

<!--Device-WindowAnimationController-onScreenUnlock?: ScreenUnlockCallback--><!--Device-WindowAnimationController-onScreenUnlock?: ScreenUnlockCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onStartAppFromLauncher

```TypeScript
onStartAppFromLauncher?: AppStartCallback
```

Callback function on starting an application form launcher.

**Type:** [AppStartCallback](arkts-arkui-windowanimationmanager-appstartcallback-t-sys.md)

**Since:** 23

<!--Device-WindowAnimationController-onStartAppFromLauncher?: AppStartCallback--><!--Device-WindowAnimationController-onStartAppFromLauncher?: AppStartCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onStartAppFromOther

```TypeScript
onStartAppFromOther?: AppStartCallback
```

Callback function on starting an application form other.

**Type:** [AppStartCallback](arkts-arkui-windowanimationmanager-appstartcallback-t-sys.md)

**Since:** 23

<!--Device-WindowAnimationController-onStartAppFromOther?: AppStartCallback--><!--Device-WindowAnimationController-onStartAppFromOther?: AppStartCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onStartAppFromRecent

```TypeScript
onStartAppFromRecent?: AppStartCallback
```

Callback function on starting an application form recent.

**Type:** [AppStartCallback](arkts-arkui-windowanimationmanager-appstartcallback-t-sys.md)

**Since:** 23

<!--Device-WindowAnimationController-onStartAppFromRecent?: AppStartCallback--><!--Device-WindowAnimationController-onStartAppFromRecent?: AppStartCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## onWindowAnimationTargetsUpdate

```TypeScript
onWindowAnimationTargetsUpdate?: WindowAnimationTargetsUpdationCallback
```

Callback function on window animation targets update.

**Type:** [WindowAnimationTargetsUpdationCallback](arkts-arkui-windowanimationmanager-windowanimationtargetsupdationcallback-t-sys.md)

**Since:** 23

<!--Device-WindowAnimationController-onWindowAnimationTargetsUpdate?: WindowAnimationTargetsUpdationCallback--><!--Device-WindowAnimationController-onWindowAnimationTargetsUpdate?: WindowAnimationTargetsUpdationCallback-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

