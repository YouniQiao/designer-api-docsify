# AppStartCallback (System API)

```TypeScript
type AppStartCallback = (startingWindowTarget: WindowAnimationTarget,
    finishCallback: WindowAnimationFinishedCallback) => void
```

Callback function on starting an application.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-windowAnimationManager-type AppStartCallback = (startingWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void--><!--Device-windowAnimationManager-type AppStartCallback = (startingWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startingWindowTarget | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Window target of the starting application.  |
| finishCallback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Animation finished callback.  |

