# DataPanel属性/事件

除支持[通用属性](arkts-arkui-commonmethod-c.md)外，还支持以下属性：支持[通用事件](arkts-arkui-commonmethod-c.md)。@extends CommonMethod [since 7 - 10] @extends CommonMethod&lt;DataPanelAttribute&gt; [since 11]

**继承/实现关系：** DataPanelAttribute extends CommonMethod<DataPanelAttribute>

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## closeEffect

```TypeScript
closeEffect(value: boolean)
```

设置是否关闭数据占比图表旋转动效和投影效果。若未设置[trackShadow](#trackshadow)属性，则由该属性控制投影效果，当closeEffect为false（投影开启 ）时，投影为默认效果。若已设置trackShadow属性，则由trackShadow属性值控制投影效果。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<DataPanelConfiguration>)
```

定制DataPanel内容区的方法。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](arkts-arkui-contentmodifier-i.md)&lt;[DataPanelConfiguration](arkts-arkui-datapanelconfiguration-i.md)&gt; | 是 |

## strokeWidth

```TypeScript
strokeWidth(value: Length)
```

设置圆环粗细。数据面板的类型为DataPanelType.Line时该属性不生效。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## trackBackgroundColor

```TypeScript
trackBackgroundColor(value: ResourceColor)
```

设置底板颜色。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## trackShadow

```TypeScript
trackShadow(value: DataPanelShadowOptions)
```

设置投影样式。若设置了本属性，则投影效果由本属性控制，closeEffect对投影效果的控制不再生效（closeEffect对旋转动效的控制不受影响）。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [DataPanelShadowOptions](arkts-arkui-datapanelshadowoptions-i.md) | 是 |

## valueColors

```TypeScript
valueColors(value: Array<ResourceColor | LinearGradient>)
```

设置各数据段颜色。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-arkui-lineargradient-c.md)&gt; | 是 |
