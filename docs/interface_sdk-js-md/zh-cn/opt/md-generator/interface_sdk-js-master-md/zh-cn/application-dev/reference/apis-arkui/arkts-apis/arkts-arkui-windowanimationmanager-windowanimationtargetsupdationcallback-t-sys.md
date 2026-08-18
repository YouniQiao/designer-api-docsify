# WindowAnimationTargetsUpdationCallback（系统接口）

```TypeScript
type WindowAnimationTargetsUpdationCallback = (fullScreenWindowTarget: WindowAnimationTarget,
    floatingWindowTargets: Array<WindowAnimationTarget>) => void
```

动画目标窗口更新时的回调。

**起始版本：** 23

<!--Device-windowAnimationManager-type WindowAnimationTargetsUpdationCallback = (fullScreenWindowTarget: WindowAnimationTarget,    floatingWindowTargets: Array<WindowAnimationTarget>) => void--><!--Device-windowAnimationManager-type WindowAnimationTargetsUpdationCallback = (fullScreenWindowTarget: WindowAnimationTarget,    floatingWindowTargets: Array<WindowAnimationTarget>) => void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fullScreenWindowTarget | [WindowAnimationTarget](../../apis-na/arkts-apis/arkts-na-remotewindow-windowanimationtarget-i-sys.md) | 是 |
| floatingWindowTargets | Array & lt;WindowAnimationTarget & gt; | 是 |
