# AppTransitionCallback (System API)

```TypeScript
type AppTransitionCallback = (fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,
    finishCallback: WindowAnimationFinishedCallback) => void
```

Callback function on application transition.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-windowAnimationManager-type AppTransitionCallback = (fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void--><!--Device-windowAnimationManager-type AppTransitionCallback = (fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fromWindowTarget | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | Window target of the source application. |
| toWindowTarget | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | Window target of the destination application. |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | Animation finished callback. |

