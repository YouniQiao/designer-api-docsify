# FloatViewState

```TypeScript
enum FloatViewState
```

闪控窗状态的枚举。

**起始版本：** 26.0.0

<!--Device-floatView-enum FloatViewState--><!--Device-floatView-enum FloatViewState-End-->

**系统能力：** SystemCapability.Window.SessionManager

## ERROR

```TypeScript
ERROR = 6
```

闪控窗发生异常。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FloatViewState-ERROR = 6--><!--Device-FloatViewState-ERROR = 6-End-->

**系统能力：** SystemCapability.Window.SessionManager

## HIDDEN

```TypeScript
HIDDEN = 2
```

闪控窗已隐藏。上滑进入多任务界面时触发；或使用[setFloatViewVisibilityInApp](arkts-arkui-floatview-floatviewcontroller-i.md#setfloatviewvisibilityinapp)接口设置了应用在前台时隐藏闪控窗后，应用处于前台时触发。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FloatViewState-HIDDEN = 2--><!--Device-FloatViewState-HIDDEN = 2-End-->

**系统能力：** SystemCapability.Window.SessionManager

## IN_FLOATING_BALL

```TypeScript
IN_FLOATING_BALL = 5
```

闪控窗切换为闪控球。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FloatViewState-IN_FLOATING_BALL = 5--><!--Device-FloatViewState-IN_FLOATING_BALL = 5-End-->

**系统能力：** SystemCapability.Window.SessionManager

## IN_SIDEBAR

```TypeScript
IN_SIDEBAR = 4
```

闪控窗在侧边栏中。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FloatViewState-IN_SIDEBAR = 4--><!--Device-FloatViewState-IN_SIDEBAR = 4-End-->

**系统能力：** SystemCapability.Window.SessionManager

## STARTED

```TypeScript
STARTED = 1
```

闪控窗已启动并显示。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FloatViewState-STARTED = 1--><!--Device-FloatViewState-STARTED = 1-End-->

**系统能力：** SystemCapability.Window.SessionManager

## STOPPED

```TypeScript
STOPPED = 3
```

闪控窗已停止。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FloatViewState-STOPPED = 3--><!--Device-FloatViewState-STOPPED = 3-End-->

**系统能力：** SystemCapability.Window.SessionManager
