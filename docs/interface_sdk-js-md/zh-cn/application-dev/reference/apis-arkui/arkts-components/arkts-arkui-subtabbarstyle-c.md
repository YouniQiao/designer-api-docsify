# SubTabBarStyle

子页签样式。打开后在切换页签时会播放跳转动画。

**起始版本：** 9

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## board

```TypeScript
board(value: BoardStyle): SubTabBarStyle
```

设置选中子页签的背板风格。子页签的背板风格仅在水平模式下有效。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BoardStyle](arkts-arkui-boardstyle-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## constructor

```TypeScript
constructor(content: ResourceStr)
```

SubTabBarStyle的构造函数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | 是 |

## constructor

```TypeScript
constructor(content: ResourceStr | ComponentContent)
```

SubTabBarStyle的构造函数。支持ComponentContent设置自定义内容。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md) | 是 |

## id

```TypeScript
id(value: string): SubTabBarStyle
```

设置子页签的id。可用于通过TabsController查找或控制指定页签，以及在状态管理和事件处理中标识不同的页签。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## indicator

```TypeScript
indicator(value: IndicatorStyle): SubTabBarStyle
```

设置选中子页签的下划线风格。子页签的下划线风格仅在水平模式下有效。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [IndicatorStyle](arkts-arkui-indicatorstyle-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## indicator

```TypeScript
indicator(value: IndicatorStyle | DrawableTabBarIndicator): SubTabBarStyle
```

设置选中子页签的下划线风格。与[indicator](#indicator)相比，新增了图片格式的下划线风格，图片的显示效果参照 [ImageFit.Cover](../arkts-apis/arkts-arkui-imagefit-e.md)。子页签的下划线风格仅在水平模式下有效。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [IndicatorStyle](arkts-arkui-indicatorstyle-i.md) \| [DrawableTabBarIndicator](arkts-arkui-drawabletabbarindicator-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## labelStyle

```TypeScript
labelStyle(value: LabelStyle): SubTabBarStyle
```

设置子页签的label文本和字体的样式。子页签的label文本和字体的样式仅在水平模式下有效。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LabelStyle](arkts-arkui-labelstyle-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## of

```TypeScript
static of(content: ResourceStr): SubTabBarStyle
```

SubTabBarStyle的静态构造函数。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## of

```TypeScript
static of(content: ResourceStr | ComponentContent): SubTabBarStyle
```

SubTabBarStyle的静态构造函数。支持ComponentContent设置自定义内容。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## padding

```TypeScript
padding(value: Padding | Dimension): SubTabBarStyle
```

设置子页签的内边距属性（不支持百分比设置）。使用Dimension时，四个方向内边距同时生效。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Padding \| [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## padding

```TypeScript
padding(padding: LocalizedPadding): SubTabBarStyle
```

设置子页签的内边距属性，支持镜像能力（不支持百分比设置）。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [padding](#padding) | [LocalizedPadding](../arkts-apis/arkts-arkui-localizedpadding-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## selectedMode

```TypeScript
selectedMode(value: SelectedMode): SubTabBarStyle
```

设置选中子页签的显示方式。子页签的显示方式仅在水平模式下有效。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SelectedMode](arkts-arkui-selectedmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |
