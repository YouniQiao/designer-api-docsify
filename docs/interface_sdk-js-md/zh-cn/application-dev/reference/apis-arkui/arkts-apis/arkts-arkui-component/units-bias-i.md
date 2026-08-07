# Bias

设置组件在锚点约束下的偏移参数。

以水平方向Bias为例，其值为组件到左锚点的距离 D\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_start\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_与组件到水平方向锚点间总距离 D\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_start\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_ + D\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_end\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_的比值。镜像语言下，D\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_start\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_为组件到右锚点的距离。下图中D\_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_width\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_表示组件宽度。

!\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_

竖直方向同理，其值为组件到上锚点的距离D\_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_top\_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_与组件到竖直方向锚点间总距离D\_\_\_HTML\_TAG\_DESC\_USD\_14\_\_\_top\_\_\_HTML\_TAG\_DESC\_USD\_15\_\_\_ + D\_\_\_HTML\_TAG\_DESC\_USD\_16\_\_\_bottom\_\_\_HTML\_TAG\_DESC\_USD\_17\_\_\_的比值。下图中D\_\_\_HTML\_TAG\_DESC\_USD\_18\_\_\_height\_\_\_HTML\_TAG\_DESC\_USD\_19\_\_\_表示组件高度。

!\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface Bias--><!--Device-unnamed-export declare interface Bias-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## horizontal

```TypeScript
horizontal?: double
```

水平方向上的bias值。

当子组件的width属性有正确值并且有2个水平方向的锚点时生效，设置的值必须大于等于0。

默认值： 0.5

**类型：** double

**默认值：** 0.5

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Bias-horizontal?: double--><!--Device-Bias-horizontal?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## vertical

```TypeScript
vertical?: double
```

垂直方向上的bias值。

当子组件的height属性有正确值并且有2个垂直方向的锚点时生效，设置的值必须大于等于0。

默认值： 0.5

**类型：** double

**默认值：** 0.5

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Bias-vertical?: double--><!--Device-Bias-vertical?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

