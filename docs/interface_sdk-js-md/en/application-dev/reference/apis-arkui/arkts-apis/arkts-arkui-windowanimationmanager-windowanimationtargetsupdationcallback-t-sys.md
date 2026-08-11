# WindowAnimationTargetsUpdationCallback (System API)

```TypeScript
type WindowAnimationTargetsUpdationCallback = (fullScreenWindowTarget: WindowAnimationTarget,
    floatingWindowTargets: Array<WindowAnimationTarget>) => void
```

Callback function on window animation targets update.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-windowAnimationManager-type WindowAnimationTargetsUpdationCallback = (fullScreenWindowTarget: WindowAnimationTarget,    floatingWindowTargets: Array<WindowAnimationTarget>) => void--><!--Device-windowAnimationManager-type WindowAnimationTargetsUpdationCallback = (fullScreenWindowTarget: WindowAnimationTarget,    floatingWindowTargets: Array<WindowAnimationTarget>) => void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fullScreenWindowTarget | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | The fullscreen window target. |
| floatingWindowTargets | Array&lt;WindowAnimationTarget&gt; | Yes | All the floating window targets. |

