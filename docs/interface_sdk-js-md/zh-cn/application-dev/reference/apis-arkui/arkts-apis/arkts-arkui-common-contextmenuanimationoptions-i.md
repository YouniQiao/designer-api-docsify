# ContextMenuAnimationOptions

Defines the ContextMenu's preview animator options.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## hoverScale

```TypeScript
hoverScale?: AnimationNumberRange
```

Sets the scale start and end animator of the image displayed before the custom builder preview is displayed.

**类型：** [AnimationNumberRange](arkts-arkui-animationnumberrange-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## hoverScaleInterruption

```TypeScript
hoverScaleInterruption?: boolean
```

Sets whether support to interrupt the process of hover scale.

**类型：** boolean

**默认值：** false

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale?: AnimationNumberRange
```

Sets the start animator scale and end animator scale.

**类型：** [AnimationNumberRange](arkts-arkui-animationnumberrange-t.md)

**默认值：** -

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition?: TransitionEffect
```

Defines the transition effect of menu preview opening and closing.

**类型：** [TransitionEffect](arkts-arkui-common-transitioneffect-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
