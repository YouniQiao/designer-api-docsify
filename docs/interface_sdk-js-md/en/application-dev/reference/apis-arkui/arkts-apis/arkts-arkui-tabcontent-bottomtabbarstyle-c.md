# BottomTabBarStyle

底部页签和侧边页签样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class BottomTabBarStyle--><!--Device-unnamed-export declare class BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr)
```

BottomTabBarStyle的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr)--><!--Device-BottomTabBarStyle-constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | [ResourceStr](arkts-arkui-resourcestr-t.md) \| TabBarSymbol | Yes | 页签内的图片内容。 |
| text | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes | 页签内的文字内容。 |

## iconStyle

```TypeScript
iconStyle(style: TabBarIconStyle): BottomTabBarStyle
```

设置底部页签的label图标的样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-iconStyle(style: TabBarIconStyle): BottomTabBarStyle--><!--Device-BottomTabBarStyle-iconStyle(style: TabBarIconStyle): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [TabBarIconStyle](../arkts-components/arkts-arkui-tabbariconstyle-i.md) | Yes | 底部页签的label图标的样式。 |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) | 返回BottomTabBarStyle对象本身。 |

## id

```TypeScript
id(value: string): BottomTabBarStyle
```

设置底部页签的id。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-id(value: string): BottomTabBarStyle--><!--Device-BottomTabBarStyle-id(value: string): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | 设置底部页签的id。 |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) | 返回BottomTabBarStyle对象本身。 |

## labelStyle

```TypeScript
labelStyle(style: TabBarLabelStyle): BottomTabBarStyle
```

设置底部页签的label文本和字体的样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-labelStyle(style: TabBarLabelStyle): BottomTabBarStyle--><!--Device-BottomTabBarStyle-labelStyle(style: TabBarLabelStyle): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [TabBarLabelStyle](arkts-arkui-tabcontent-tabbarlabelstyle-i.md) | Yes | 底部页签的label文本和字体的样式。 |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) | 返回BottomTabBarStyle对象本身。 |

## layoutMode

```TypeScript
layoutMode(value: LayoutMode): BottomTabBarStyle
```

设置底部页签的图片、文字排布的方式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-layoutMode(value: LayoutMode): BottomTabBarStyle--><!--Device-BottomTabBarStyle-layoutMode(value: LayoutMode): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LayoutMode](arkts-arkui-tabcontent-layoutmode-e.md) | Yes | 底部页签的图片、文字排布的方式，具体参照LayoutMode枚举。&lt;br/&gt;默认值：LayoutMode.VERTICAL |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) | 返回BottomTabBarStyle对象本身。 |

## of

```TypeScript
static of(icon: ResourceStr | TabBarSymbol, text: ResourceStr): BottomTabBarStyle
```

BottomTabBarStyle的静态构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-static of(icon: ResourceStr | TabBarSymbol, text: ResourceStr): BottomTabBarStyle--><!--Device-BottomTabBarStyle-static of(icon: ResourceStr | TabBarSymbol, text: ResourceStr): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | [ResourceStr](arkts-arkui-resourcestr-t.md) \| TabBarSymbol | Yes | 页签内的图片内容。 |
| text | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes | 页签内的文字内容。 |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) | 返回创建的BottomTabBarStyle对象。 |

## padding

```TypeScript
padding(value: Padding | Dimension | LocalizedPadding): BottomTabBarStyle
```

设置底部页签的内边距属性（不支持百分比设置）。使用Dimension时，四个方向内边距同时生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-padding(value: Padding | Dimension | LocalizedPadding): BottomTabBarStyle--><!--Device-BottomTabBarStyle-padding(value: Padding | Dimension | LocalizedPadding): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Padding](arkts-arkui-units-padding-i.md) \| Dimension \| LocalizedPadding | Yes | 底部页签的内边距。&lt;br/&gt;取值范围：[0, +∞]&lt;br/&gt;默认值：{left:4.0vp,right:4.0 vp,top:0.0vp,bottom:0.0vp}&lt;br/&gt;使用LocalizedPadding时，支持镜像能力。&lt;br /&gt;默认值：{start:LengthMetrics.vp(4),end: LengthMetrics.vp(4),&lt;br/&gt;top:LengthMetrics.vp(0),bottom:LengthMetrics.vp(0)} |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) | 返回BottomTabBarStyle对象本身。 |

## symmetricExtensible

```TypeScript
symmetricExtensible(value: boolean): BottomTabBarStyle
```

设置底部页签的图片、文字是否可以对称借用左右底部页签的空余位置中的最小值，仅fixed水平模式下在底部页签之间有效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-symmetricExtensible(value: boolean): BottomTabBarStyle--><!--Device-BottomTabBarStyle-symmetricExtensible(value: boolean): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | 底部页签的图片、文字是否可以对称借用左右底部页签的空余位置中的最小值。&lt;br/&gt;true：可以对称借用；false：不可以对称借用。&lt;br/&gt;默认值：false，底部页签的图片 、文字不可以对称借用左右底部页签的空余位置中的最小值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) | 返回BottomTabBarStyle对象本身。 |

## verticalAlign

```TypeScript
verticalAlign(value: VerticalAlign): BottomTabBarStyle
```

设置底部页签的图片、文字在垂直方向上的对齐格式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-verticalAlign(value: VerticalAlign): BottomTabBarStyle--><!--Device-BottomTabBarStyle-verticalAlign(value: VerticalAlign): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [VerticalAlign](arkts-arkui-verticalalign-e.md) | Yes | 底部页签的图片、文字在垂直方向上的对齐格式。&lt;br/&gt;默认值：VerticalAlign.Center |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) | 返回BottomTabBarStyle对象本身。 |

