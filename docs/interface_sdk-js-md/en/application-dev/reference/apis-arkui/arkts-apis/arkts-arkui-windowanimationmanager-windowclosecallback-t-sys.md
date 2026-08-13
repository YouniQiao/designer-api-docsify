# WindowCloseCallback (System API)

```TypeScript
type WindowCloseCallback = (closingWindowTarget: WindowAnimationTarget,
    finishCallback: WindowAnimationFinishedCallback) => void
```

Callback function on closing a window.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-windowAnimationManager-type WindowCloseCallback = (closingWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void--><!--Device-windowAnimationManager-type WindowCloseCallback = (closingWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| closingWindowTarget | WindowAnimationTarget | Yes |  |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | Animation finished callback. |

