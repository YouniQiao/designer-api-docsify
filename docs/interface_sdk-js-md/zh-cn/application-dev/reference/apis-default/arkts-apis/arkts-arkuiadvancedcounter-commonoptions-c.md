# CommonOptions

Defines the common options.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-declare class CommonOptions--><!--Device-unnamed-declare class CommonOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## focusable

```TypeScript
focusable?: boolean
```

设置Counter是否可以获焦。 **说明：** 该属性对列表型和紧凑型Counter生效。 默认值：true。

**类型：** boolean

**默认值：** true

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonOptions-focusable?: boolean--><!--Device-CommonOptions-focusable?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onHoverDecrease

```TypeScript
onHoverDecrease?: OnCounterHoverCallback
```

鼠标进入或退出Counter组件的减小按钮触时发该回调。 isHover：表示鼠标是否悬浮在组件上，进入时为true，离开时为false。 默认值：不触发鼠标进入或退出Counter组件的减小按钮时的回调。

**类型：** [OnCounterHoverCallback](arkts-oncounterhovercallback-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonOptions-onHoverDecrease?: OnCounterHoverCallback--><!--Device-CommonOptions-onHoverDecrease?: OnCounterHoverCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onHoverIncrease

```TypeScript
onHoverIncrease?: OnCounterHoverCallback
```

鼠标进入或退出Counter组件的增加按钮时触发该回调。 isHover：表示鼠标是否悬浮在增加按钮组件上，鼠标进入时为true，退出时为false。 默认值：不触发鼠标进入或退出Counter组件的增加按钮时的回调。

**类型：** [OnCounterHoverCallback](arkts-oncounterhovercallback-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonOptions-onHoverIncrease?: OnCounterHoverCallback--><!--Device-CommonOptions-onHoverIncrease?: OnCounterHoverCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## step

```TypeScript
step?: int
```

设置Counter的步长。 取值范围：大于等于1的整数。 取值限定为整数。默认值：1。

**类型：** int

**默认值：** 1

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonOptions-step?: int--><!--Device-CommonOptions-step?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

