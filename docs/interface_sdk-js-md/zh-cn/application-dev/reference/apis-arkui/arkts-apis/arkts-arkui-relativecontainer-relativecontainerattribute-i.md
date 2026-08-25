# RelativeContainerAttribute

相对布局组件，用于复杂场景中元素对齐的布局。@extends CommonMethod @interface RelativeContainerAttribute

**继承/实现关系：** RelativeContainerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RelativeContainerAttribute> | AttributeModifier<CommonMethod>
        | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md) |

## barrier

```TypeScript
default barrier(barrierStyle: Array<BarrierStyle> | Array<LocalizedBarrierStyle> | undefined): this
```

设置RelativeContainer容器内的屏障，Array中每个项目即为一条barrier， 支持定义镜像模式的屏障线。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| barrierStyle | Array&lt;[BarrierStyle](arkts-arkui-relativecontainer-barrierstyle-i.md)&gt; \| Array&lt;[LocalizedBarrierStyle](arkts-arkui-relativecontainer-localizedbarrierstyle-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md) |

## guideLine

```TypeScript
default guideLine(value: Array<GuideLineStyle> | undefined): this
```

设置RelativeContainer容器内的辅助线，Array中每个项目即为一条guideLine。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[GuideLineStyle](arkts-arkui-relativecontainer-guidelinestyle-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md) |

## setRelativeContainerOptions

```TypeScript
default setRelativeContainerOptions(): this
```

设置RelativeContainer选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md) |
