# BottomTabBarStyle

底部页签和侧边页签样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr)
```

BottomTabBarStyle的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| icon | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [TabBarSymbol](arkts-arkui-tabcontent-tabbarsymbol-c.md) | 是 |
| text | [ResourceStr](arkts-arkui-resourcestr-t.md) | 是 |

## iconStyle

```TypeScript
iconStyle(style: TabBarIconStyle): BottomTabBarStyle
```

设置底部页签的label图标的样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [TabBarIconStyle](arkts-arkui-tabcontent-tabbariconstyle-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) |

## id

```TypeScript
id(value: string): BottomTabBarStyle
```

设置底部页签的id。

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
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) |

## labelStyle

```TypeScript
labelStyle(style: TabBarLabelStyle): BottomTabBarStyle
```

设置底部页签的label文本和字体的样式。

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
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) |

## layoutMode

```TypeScript
layoutMode(value: LayoutMode): BottomTabBarStyle
```

设置底部页签的图片、文字排布的方式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LayoutMode](arkts-arkui-tabcontent-layoutmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) |

## of

```TypeScript
static of(icon: ResourceStr | TabBarSymbol, text: ResourceStr): BottomTabBarStyle
```

BottomTabBarStyle的静态构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| icon | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [TabBarSymbol](arkts-arkui-tabcontent-tabbarsymbol-c.md) | 是 |
| text | [ResourceStr](arkts-arkui-resourcestr-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) |

## padding

```TypeScript
padding(value: Padding | Dimension | LocalizedPadding): BottomTabBarStyle
```

设置底部页签的内边距属性（不支持百分比设置）。使用Dimension时，四个方向内边距同时生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Padding](arkts-arkui-units-padding-i.md) \| [Dimension](arkts-arkui-dimension-t.md) \| [LocalizedPadding](arkts-arkui-localizedpadding-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) |

## symmetricExtensible

```TypeScript
symmetricExtensible(value: boolean): BottomTabBarStyle
```

设置底部页签的图片、文字是否可以对称借用左右底部页签的空余位置中的最小值，仅fixed水平模式下在底部页签之间有效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) |

## verticalAlign

```TypeScript
verticalAlign(value: VerticalAlign): BottomTabBarStyle
```

设置底部页签的图片、文字在垂直方向上的对齐格式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [VerticalAlign](arkts-arkui-verticalalign-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) |
