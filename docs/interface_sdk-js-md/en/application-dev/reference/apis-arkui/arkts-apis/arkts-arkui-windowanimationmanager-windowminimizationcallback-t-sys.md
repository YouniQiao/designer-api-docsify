# WindowMinimizationCallback (System API)

```TypeScript
type WindowMinimizationCallback = (minimizingWindowTarget: WindowAnimationTarget,
    finishCallback: WindowAnimationFinishedCallback) => void
```

Callback function on minimizing a window.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-windowAnimationManager-type WindowMinimizationCallback = (minimizingWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void--><!--Device-windowAnimationManager-type WindowMinimizationCallback = (minimizingWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minimizingWindowTarget | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | Window target of the minimizing window. |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | Animation finished callback. |

