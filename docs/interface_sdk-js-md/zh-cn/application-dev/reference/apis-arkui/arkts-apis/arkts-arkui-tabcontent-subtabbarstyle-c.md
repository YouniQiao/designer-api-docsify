# SubTabBarStyle

子页签样式。打开后在切换页签时会播放跳转动画。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## board

```TypeScript
board(value: BoardStyle): SubTabBarStyle
```

设置选中子页签的背板风格。子页签的背板风格仅在水平模式下有效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BoardStyle](arkts-arkui-tabcontent-boardstyle-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-tabcontent-subtabbarstyle-c.md) |

## constructor

```TypeScript
constructor(content: ResourceStr | ComponentContentBase)
```

SubTabBarStyle的构造函数。支持ComponentContent设置自定义内容。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md) | 是 |

## id

```TypeScript
id(value: string): SubTabBarStyle
```

设置子页签的id。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-tabcontent-subtabbarstyle-c.md) |

## indicator

```TypeScript
indicator(style: SubTabBarIndicatorStyle): SubTabBarStyle
```

设置选中子页签的下划线风格。子页签的下划线风格仅在水平模式下有效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [SubTabBarIndicatorStyle](arkts-arkui-tabcontent-subtabbarindicatorstyle-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-tabcontent-subtabbarstyle-c.md) |

## indicator

```TypeScript
indicator(value: SubTabBarIndicatorStyle | DrawableTabBarIndicator): SubTabBarStyle
```

设置选中子页签的下划线风格。子页签的下划线风格仅在水平模式下有效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SubTabBarIndicatorStyle](arkts-arkui-tabcontent-subtabbarindicatorstyle-i.md) \| [DrawableTabBarIndicator](arkts-arkui-tabcontent-drawabletabbarindicator-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-tabcontent-subtabbarstyle-c.md) |

## labelStyle

```TypeScript
labelStyle(style: TabBarLabelStyle): SubTabBarStyle
```

设置子页签的label文本和字体的样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [TabBarLabelStyle](arkts-arkui-tabcontent-tabbarlabelstyle-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-tabcontent-subtabbarstyle-c.md) |

## of

```TypeScript
static of(content: ResourceStr | ComponentContentBase): SubTabBarStyle
```

SubTabBarStyle的静态构造函数。支持ComponentContent设置自定义内容。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-tabcontent-subtabbarstyle-c.md) |

## padding

```TypeScript
padding(value: Padding | Dimension): SubTabBarStyle
```

设置子页签的内边距属性（不支持百分比设置）。使用Dimension时，四个方向内边距同时生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Padding](arkts-arkui-units-padding-i.md) \| [Dimension](arkts-arkui-dimension-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-tabcontent-subtabbarstyle-c.md) |

## padding

```TypeScript
padding(padding: LocalizedPadding): SubTabBarStyle
```

设置子页签的内边距属性，支持镜像能力（不支持百分比设置）。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [padding](#padding) | [LocalizedPadding](arkts-arkui-localizedpadding-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-tabcontent-subtabbarstyle-c.md) |

## selectedMode

```TypeScript
selectedMode(value: SelectedMode): SubTabBarStyle
```

设置选中子页签的显示方式。子页签的显示方式仅在水平模式下有效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SelectedMode](arkts-arkui-tabcontent-selectedmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SubTabBarStyle](arkts-arkui-tabcontent-subtabbarstyle-c.md) |
