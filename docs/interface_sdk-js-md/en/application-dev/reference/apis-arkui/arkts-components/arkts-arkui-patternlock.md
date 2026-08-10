# PatternLock

图案密码锁组件，以九宫格图案的方式输入密码，用于密码验证场景。组件支持自定义九宫格尺寸、圆点及连线样式、选中/激活状态颜色等外观属性，支持密码输入过程中的实时反馈以及密码验证结果（正确/错误）的状态设置。手指在PatternLock组
件区域按下时开始进入输入状态，手指离开屏幕时结束输入状态完成密码输入。

> **说明：**
>
> - 如果开发者有其他功能需求，可以使用[自定义组件](docroot://ui/state-management/arkts-create-custom-components.md)。例如自定义组件<!--RP1-->
> [CustomPatternLock](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/UI/CustomPatternLock)
> <!--RP1End-->，通过[Canvas]{@link ./canvas}组件实现了图案密码锁功能，开发者可在此基础上自行进行功能扩展。

## 子组件

无

## PatternLock

```TypeScript
PatternLock(controller?: PatternLockController)
```

创建图案密码锁组件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PatternLockInterface-(controller?: PatternLockController): PatternLockAttribute--><!--Device-PatternLockInterface-(controller?: PatternLockController): PatternLockAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [PatternLockController](../arkts-apis/arkts-arkui-patternlock-patternlockcontroller-c.md) | No | 设置PatternLock组件控制器，用于重置组件状态和设置图案密码状态。当需要程序化控制组件状态（如重置密码锁、设置密码验证结果）时 传入此参数；不传入时无法通过控制器手动操作组件状态（即无法调用reset()、setChallengeResult()等方法）。 |

## Summary

- [CircleStyleOptions](arkts-arkui-patternlock-circlestyleoptions-i.md)
- [PatternLockChallengeResult](arkts-arkui-patternlock-patternlockchallengeresult-e.md)
