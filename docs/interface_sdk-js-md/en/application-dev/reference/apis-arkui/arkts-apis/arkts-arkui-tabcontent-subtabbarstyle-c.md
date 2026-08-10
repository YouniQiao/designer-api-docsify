# SubTabBarStyle

子页签样式。打开后在切换页签时会播放跳转动画。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class SubTabBarStyle--><!--Device-unnamed-export declare class SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## board

```TypeScript
board(value: BoardStyle): SubTabBarStyle
```

设置选中子页签的背板风格。子页签的背板风格仅在水平模式下有效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-board(value: BoardStyle): SubTabBarStyle--><!--Device-SubTabBarStyle-board(value: BoardStyle): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [BoardStyle](../arkts-components/arkts-arkui-boardstyle-i.md) | Yes | 选中子页签的背板风格对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](../arkts-components/arkts-arkui-subtabbarstyle-c.md) | 返回SubTabBarStyle对象本身。 |

## constructor

```TypeScript
constructor(content: ResourceStr | ComponentContentBase)
```

SubTabBarStyle的构造函数。支持ComponentContent设置自定义内容。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-constructor(content: ResourceStr | ComponentContentBase)--><!--Device-SubTabBarStyle-constructor(content: ResourceStr | ComponentContentBase)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ResourceStr](arkts-arkui-resourcestr-t.md) \| ComponentContentBase | Yes | 页签内的内容。&lt;br /&gt;**说明：**&lt;br /&gt;1.自定义内容不支持labelStyle属性。&lt;br /&gt;2.自定 义内容超出页签范围，则不显示超出部分。&lt;br /&gt;3.自定义内容小于页签范围，则会居中对齐。&lt;br /&gt;4.自定义内容异常或无可用显示组件，则显示空白。 |

## id

```TypeScript
id(value: string): SubTabBarStyle
```

设置子页签的id。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-id(value: string): SubTabBarStyle--><!--Device-SubTabBarStyle-id(value: string): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | 子页签的id。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](../arkts-components/arkts-arkui-subtabbarstyle-c.md) | 返回SubTabBarStyle对象本身。 |

## indicator

```TypeScript
indicator(style: SubTabBarIndicatorStyle): SubTabBarStyle
```

设置选中子页签的下划线风格。子页签的下划线风格仅在水平模式下有效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-indicator(style: SubTabBarIndicatorStyle): SubTabBarStyle--><!--Device-SubTabBarStyle-indicator(style: SubTabBarIndicatorStyle): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [SubTabBarIndicatorStyle](arkts-arkui-tabcontent-subtabbarindicatorstyle-i.md) | Yes | 选中子页签的下划线风格对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](../arkts-components/arkts-arkui-subtabbarstyle-c.md) | 返回SubTabBarStyle对象本身。 |

## indicator

```TypeScript
indicator(value: SubTabBarIndicatorStyle | DrawableTabBarIndicator): SubTabBarStyle
```

设置选中子页签的下划线风格。子页签的下划线风格仅在水平模式下有效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-indicator(value: SubTabBarIndicatorStyle | DrawableTabBarIndicator): SubTabBarStyle--><!--Device-SubTabBarStyle-indicator(value: SubTabBarIndicatorStyle | DrawableTabBarIndicator): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SubTabBarIndicatorStyle](arkts-arkui-tabcontent-subtabbarindicatorstyle-i.md) \| DrawableTabBarIndicator | Yes | 选中子页签的下划线风格对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](../arkts-components/arkts-arkui-subtabbarstyle-c.md) | 返回SubTabBarStyle对象本身。 |

## labelStyle

```TypeScript
labelStyle(style: TabBarLabelStyle): SubTabBarStyle
```

设置子页签的label文本和字体的样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-labelStyle(style: TabBarLabelStyle): SubTabBarStyle--><!--Device-SubTabBarStyle-labelStyle(style: TabBarLabelStyle): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [TabBarLabelStyle](arkts-arkui-tabcontent-tabbarlabelstyle-i.md) | Yes | 子页签的label文本和字体的样式对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](../arkts-components/arkts-arkui-subtabbarstyle-c.md) | 返回SubTabBarStyle对象本身。 |

## of

```TypeScript
static of(content: ResourceStr | ComponentContentBase): SubTabBarStyle
```

SubTabBarStyle的静态构造函数。支持ComponentContent设置自定义内容。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-static of(content: ResourceStr | ComponentContentBase): SubTabBarStyle--><!--Device-SubTabBarStyle-static of(content: ResourceStr | ComponentContentBase): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ResourceStr](arkts-arkui-resourcestr-t.md) \| ComponentContentBase | Yes | 页签内的内容。支持ComponentContentBase设置自定义内容。&lt;br /&gt;**说明：**&lt;br /&gt;1.自 定义内容不支持labelStyle属性。&lt;br /&gt;2.自定义内容超出页签范围，则不显示超出部分。&lt;br /&gt;3.自定义内容小于页签范围，则会居中对齐。&lt;br /&gt;4.自定义内容异常或无可用显示组件，则显示空白。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](../arkts-components/arkts-arkui-subtabbarstyle-c.md) | 返回创建的SubTabBarStyle对象。 |

## padding

```TypeScript
padding(value: Padding | Dimension): SubTabBarStyle
```

设置子页签的内边距属性（不支持百分比设置）。使用Dimension时，四个方向内边距同时生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-padding(value: Padding | Dimension): SubTabBarStyle--><!--Device-SubTabBarStyle-padding(value: Padding | Dimension): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Padding](arkts-arkui-units-padding-i.md) \| Dimension | Yes | 子页签的内边距属性。&lt;br/&gt;取值范围：[0, +∞]&lt;br/&gt;异常值时取默认值。&lt;br /&gt;默认值：{left:8.0vp,right:8.0vp, top:17.0vp,bottom:18.0vp} |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](../arkts-components/arkts-arkui-subtabbarstyle-c.md) | 返回SubTabBarStyle对象本身。 |

## padding

```TypeScript
padding(padding: LocalizedPadding): SubTabBarStyle
```

设置子页签的内边距属性，支持镜像能力（不支持百分比设置）。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-padding(padding: LocalizedPadding): SubTabBarStyle--><!--Device-SubTabBarStyle-padding(padding: LocalizedPadding): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| padding | [LocalizedPadding](arkts-arkui-localizedpadding-i.md) | Yes | 子页签的内边距属性。&lt;br/&gt;异常值时取默认值。&lt;br/&gt;取值范围：[0, +∞]&lt;br/&gt;异常值时取默认值。&lt;br /&gt;默认值：{start: LengthMetrics.vp(8),end:LengthMetrics.vp(8),&lt;br/&gt;top:LengthMetrics.vp(17),bottom:LengthMetrics.vp(18)} |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](../arkts-components/arkts-arkui-subtabbarstyle-c.md) | 返回SubTabBarStyle对象本身。 |

## selectedMode

```TypeScript
selectedMode(value: SelectedMode): SubTabBarStyle
```

设置选中子页签的显示方式。子页签的显示方式仅在水平模式下有效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-selectedMode(value: SelectedMode): SubTabBarStyle--><!--Device-SubTabBarStyle-selectedMode(value: SelectedMode): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SelectedMode](../arkts-components/arkts-arkui-selectedmode-e.md) | Yes | 选中子页签的显示方式。&lt;br /&gt;默认值：SelectedMode.INDICATOR |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](../arkts-components/arkts-arkui-subtabbarstyle-c.md) | 返回SubTabBarStyle对象本身。 |

