# WindowAnimationTargetsUpdationCallback (System API)

```TypeScript
type WindowAnimationTargetsUpdationCallback = (fullScreenWindowTarget: WindowAnimationTarget,
    floatingWindowTargets: Array<WindowAnimationTarget>) => void
```

Callback function on window animation targets update.

**Since:** 23

**Deprecated since:** -1

<!--Device-windowAnimationManager-type WindowAnimationTargetsUpdationCallback = (fullScreenWindowTarget: WindowAnimationTarget,    floatingWindowTargets: Array<WindowAnimationTarget>) => void--><!--Device-windowAnimationManager-type WindowAnimationTargetsUpdationCallback = (fullScreenWindowTarget: WindowAnimationTarget,    floatingWindowTargets: Array<WindowAnimationTarget>) => void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fullScreenWindowTarget | [WindowAnimationTarget](../../apis-na/arkts-apis/arkts-na-remotewindow-windowanimationtarget-i-sys.md) | Yes |
| floatingWindowTargets | Array & lt;WindowAnimationTarget & gt; | Yes |
