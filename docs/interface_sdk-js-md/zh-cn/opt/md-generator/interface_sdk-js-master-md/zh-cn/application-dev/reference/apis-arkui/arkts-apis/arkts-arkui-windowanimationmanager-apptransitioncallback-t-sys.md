# AppTransitionCallback（系统接口）

```TypeScript
type AppTransitionCallback = (fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,
    finishCallback: WindowAnimationFinishedCallback) => void
```

应用转场时的回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-windowAnimationManager-type AppTransitionCallback = (fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void--><!--Device-windowAnimationManager-type AppTransitionCallback = (fromWindowTarget: WindowAnimationTarget, toWindowTarget: WindowAnimationTarget,    finishCallback: WindowAnimationFinishedCallback) => void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fromWindowTarget | [WindowAnimationTarget](../../apis-na/arkts-apis/arkts-na-remotewindow-windowanimationtarget-i-sys.md) | 是 |
| toWindowTarget | [WindowAnimationTarget](../../apis-na/arkts-apis/arkts-na-remotewindow-windowanimationtarget-i-sys.md) | 是 |
| finishCallback | [WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md) | 是 |
