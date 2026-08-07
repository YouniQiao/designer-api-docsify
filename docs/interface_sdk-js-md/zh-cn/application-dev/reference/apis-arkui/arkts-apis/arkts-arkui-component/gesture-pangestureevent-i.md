# PanGestureEvent

继承自[BaseGestureEvent]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_。可将该对象作为[onGestureJudgeBegin]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_的event参数来传递。

**继承/实现关系：** PanGestureEvent extends [BaseGestureEvent](gesture-basegestureevent-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export interface PanGestureEvent extends BaseGestureEvent--><!--Device-unnamed-export interface PanGestureEvent extends BaseGestureEvent-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## offsetX

```TypeScript
offsetX: double
```

手势事件x轴相对当前组件元素原始区域的偏移量，单位为vp，从左向右滑动offsetX为正，反之为负。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PanGestureEvent-offsetX: double--><!--Device-PanGestureEvent-offsetX: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## offsetY

```TypeScript
offsetY: double
```

手势事件y轴相对当前组件元素原始区域的偏移量，单位为vp，从上向下滑动offsetY为正，反之为负。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PanGestureEvent-offsetY: double--><!--Device-PanGestureEvent-offsetY: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## velocity

```TypeScript
velocity: double
```

获取当前的主方向速度。为xy轴方向速度的平方和的算术平方根。单位为vp/s。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PanGestureEvent-velocity: double--><!--Device-PanGestureEvent-velocity: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## velocityX

```TypeScript
velocityX: double
```

获取当前手势的x轴方向速度。坐标轴原点为屏幕左上角，分正负方向速度，从左往右为正，反之为负。单位为vp/s。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PanGestureEvent-velocityX: double--><!--Device-PanGestureEvent-velocityX: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## velocityY

```TypeScript
velocityY: double
```

获取当前手势的y轴方向速度。坐标轴原点为屏幕左上角，分正负方向速度，从上往下为正，反之为负。单位为vp/s。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PanGestureEvent-velocityY: double--><!--Device-PanGestureEvent-velocityY: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

