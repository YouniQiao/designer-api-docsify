# TapGestureEvent

继承自[BaseGestureEvent](arkts-arkui-basegestureevent-i.md)。可将该对象作为[onGestureJudgeBegin](arkts-arkui-common-commonmethod-i.md#ongesturejudgebegin)的event参数来传递。

**继承/实现关系：** TapGestureEvent extends [BaseGestureEvent](arkts-arkui-basegestureevent-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export interface TapGestureEvent extends BaseGestureEvent--><!--Device-unnamed-export interface TapGestureEvent extends BaseGestureEvent-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## tapLocation

```TypeScript
tapLocation?: EventLocationInfo
```

获取点击手势的坐标信息。

**类型：** [EventLocationInfo](arkts-arkui-eventlocationinfo-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TapGestureEvent-tapLocation?: EventLocationInfo--><!--Device-TapGestureEvent-tapLocation?: EventLocationInfo-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

