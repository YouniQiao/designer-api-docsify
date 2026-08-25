# DataPanelAttribute

除支持通用属性外，还支持以下属性。支持通用事件。

**继承/实现关系：** DataPanelAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<DataPanelAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[DataPanelAttribute](arkts-arkui-datapanel-datapanelattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [BadgeAttribute](../arkts-components/arkts-arkui-badge-attribute.md) |

## closeEffect

```TypeScript
default closeEffect(value: boolean | undefined): this
```

设置是否关闭数据占比图表旋转动效和投影效果。若未设置[trackShadow](#trackshadow)属性，则由该属性控制投影效果的开关，开启投影的效果为投影的默认效果。若设置了trackShadow属性，则由 trackShadow属性值控制投影效果的开关。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DataPanelAttribute](arkts-arkui-datapanel-datapanelattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<DataPanelConfiguration> | undefined): this
```

定制DataPanel内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[DataPanelConfiguration](arkts-arkui-datapanel-datapanelconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DataPanelAttribute](arkts-arkui-datapanel-datapanelattribute-i.md) |

## setDataPanelOptions

```TypeScript
default setDataPanelOptions(options: DataPanelOptions): this
```

设置DataPanel选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DataPanelOptions](arkts-arkui-datapanel-datapaneloptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataPanelAttribute](arkts-arkui-datapanel-datapanelattribute-i.md) |

## strokeWidth

```TypeScript
default strokeWidth(value: Length | undefined): this
```

设置圆环粗细。数据面板的类型为DataPanelType.Line时该属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DataPanelAttribute](arkts-arkui-datapanel-datapanelattribute-i.md) |

## trackBackgroundColor

```TypeScript
default trackBackgroundColor(value: ResourceColor | undefined): this
```

设置底板颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DataPanelAttribute](arkts-arkui-datapanel-datapanelattribute-i.md) |

## trackShadow

```TypeScript
default trackShadow(value: DataPanelShadowOptions | undefined | null): this
```

设置投影样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [DataPanelShadowOptions](arkts-arkui-datapanel-datapanelshadowoptions-i.md) \| undefined \| null | 是 |

**返回值：**

| 类型 |
| --- |
| [DataPanelAttribute](arkts-arkui-datapanel-datapanelattribute-i.md) |

## valueColors

```TypeScript
default valueColors(value: Array<ResourceColor | LinearGradient> | undefined): this
```

设置各数据段颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-arkui-datapanel-lineargradient-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DataPanelAttribute](arkts-arkui-datapanel-datapanelattribute-i.md) |
