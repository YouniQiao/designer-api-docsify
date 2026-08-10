# ScreenUnlockCallback (System API)

```TypeScript
type ScreenUnlockCallback = (finishCallback: WindowAnimationFinishedCallback) => void
```

屏幕解锁时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-windowAnimationManager-type ScreenUnlockCallback = (finishCallback: WindowAnimationFinishedCallback) => void--><!--Device-windowAnimationManager-type ScreenUnlockCallback = (finishCallback: WindowAnimationFinishedCallback) => void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes | 动画完成后的回调。 |

