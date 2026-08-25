# ComponentV2

Defining ComponentV2 Annotation ComponentV2 is an Annotation to define a custom component using state management V2.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## poolAccepts

```TypeScript
poolAccepts: string[] = []
```

要重用的自定义组件的集合。

**类型：** string[]

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## reusePool

```TypeScript
reusePool: ReusePoolOwnership = ReusePoolOwnership.OFF
```

自定义组件的重用类型。默认值为OFF。

**类型：** [ReusePoolOwnership](arkts-arkui-customcomponent-reusepoolownership-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
