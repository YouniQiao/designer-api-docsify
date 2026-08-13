# AppTransitionCallback (System API)

```TypeScript
type AppTransitionCallback = (fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,
    finishCallback: WindowAnimationFinishedCallback) => void
```

Callback function on application transition.

**Since:** 23

**Deprecated since:** -1

<!--Device-windowAnimationManager-type AppTransitionCallback = (fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void--><!--Device-windowAnimationManager-type AppTransitionCallback = (fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fromWindowTarget | [WindowAnimationTarget](../../apis-na/arkts-apis/arkts-na-remotewindow-windowanimationtarget-i-sys.md) | Yes |
| toWindowTarget | [WindowAnimationTarget](../../apis-na/arkts-apis/arkts-na-remotewindow-windowanimationtarget-i-sys.md) | Yes |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | Yes |
