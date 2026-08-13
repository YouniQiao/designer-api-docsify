# WindowMinimizationCallback (System API)

```TypeScript
type WindowMinimizationCallback = (minimizingWindowTarget: WindowAnimationTarget,
    finishCallback: WindowAnimationFinishedCallback) => void
```

Callback function on minimizing a window.

**Since:** 23

**Deprecated since:** -1

<!--Device-windowAnimationManager-type WindowMinimizationCallback = (minimizingWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void--><!--Device-windowAnimationManager-type WindowMinimizationCallback = (minimizingWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| minimizingWindowTarget | [WindowAnimationTarget](../../apis-na/arkts-apis/arkts-na-remotewindow-windowanimationtarget-i-sys.md) | Yes |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes |
