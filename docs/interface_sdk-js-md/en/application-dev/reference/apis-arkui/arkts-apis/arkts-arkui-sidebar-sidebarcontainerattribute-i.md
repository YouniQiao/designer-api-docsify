# SideBarContainerAttribute

除支持[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)外，还支持以下属性：

**Inheritance/Implementation:** SideBarContainerAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SideBarContainerAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SideBarContainerAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SideBarContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置SideBarContainer组件的属性方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default attributeModifier(modifier: AttributeModifier<SideBarContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-SideBarContainerAttribute-default attributeModifier(modifier: AttributeModifier<SideBarContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;SideBarContainerAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | 在当 前组件上，动态设置属性方法，支持使用if/else语法。&lt;br/&gt;CommonMethod：通用属性和事件。&lt;br/&gt;取值为undefined时，按当前组件的属性方法默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## autoHide

```TypeScript
default autoHide(value: boolean | undefined): this
```

设置当侧边栏拖拽到小于最小宽度后，是否自动隐藏。受minSideBarWidth属性方法影响，minSideBarWidth属性方法未设置值使用默认值。

拖拽过程中判断是否要自动隐藏。小于最小宽度时需要阻尼效果触发隐藏（越界一段距离）。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default autoHide(value: boolean | undefined): this--><!--Device-SideBarContainerAttribute-default autoHide(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## controlButton

```TypeScript
default controlButton(value: ButtonStyle | undefined): this
```

设置侧边栏控制按钮的属性。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default controlButton(value: ButtonStyle | undefined): this--><!--Device-SideBarContainerAttribute-default controlButton(value: ButtonStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ButtonStyle](../arkts-components/arkts-arkui-buttonstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## divider

```TypeScript
default divider(value: DividerStyle | null | undefined): this
```

设置分割线的样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default divider(value: DividerStyle | null | undefined): this--><!--Device-SideBarContainerAttribute-default divider(value: DividerStyle | null | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [DividerStyle](../arkts-components/arkts-arkui-dividerstyle-i.md) \| null \| undefined | Yes | 分割线的样式。&lt;br/&gt;默认为DividerStyle：显示分割线。&lt;br/&gt;- null或undefined：行为不做处理，分 割线样式与默认值保持一致。&lt;br/&gt;**说明：** &lt;br/&gt;API version 11及以下版本，null效果为不显示分割线。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## maxSideBarWidth

```TypeScript
default maxSideBarWidth(value: Length | undefined): this
```

设置侧边栏最大宽度。设置为小于0的值时按默认值显示。值不能超过侧边栏容器本身宽度，超过使用侧边栏容器本身宽度。

maxSideBarWidth优先于侧边栏子组件maxWidth，maxSideBarWidth未设置时默认值优先级高于侧边栏子组件maxWidth。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default maxSideBarWidth(value: Length | undefined): this--><!--Device-SideBarContainerAttribute-default maxSideBarWidth(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## minContentWidth

```TypeScript
default minContentWidth(value: Dimension | undefined): this
```

设置SideBarContainer组件内容区可显示的最小宽度。

设置为小于0，内容区显示的最小宽度为360vp，未设置该属性时，组件内容区的可缩小到0。

Embed场景下，增大组件尺寸时仅增大内容区的尺寸。

缩小组件尺寸时，先缩小内容区的尺寸至minContentWidth。继续缩小组件尺寸时，保持内容区宽度minContentWidth不变，优先缩小侧边栏的尺寸。

当缩小侧边栏的尺寸至minSideBarWidth后，继续缩小组件尺寸时，

- 如果[autoHide](SideBarContainerAttribute.autoHide)属性为false，则会保持侧边栏宽度  
[minSideBarWidth](SideBarContainerAttribute.minSideBarWidth)和内容区宽度minContentWidth不变，但内容区会被截断显示；  
- 如果autoHide属性为true，则会优先隐藏侧边栏，然后继续缩小至内容区宽度minContentWidth后，内容区宽度保持不变，但内容区会被截断显示。

minContentWidth优先于侧边栏的[maxSideBarWidth](SideBarContainerAttribute.maxSideBarWidth)与sideBarWidth属性，minContentWidth未设置时默认值优先级低于设置的minSideBarWidth与maxSideBarWidth属性。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default minContentWidth(value: Dimension | undefined): this--><!--Device-SideBarContainerAttribute-default minContentWidth(value: Dimension | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes | SideBarContainer组件内容区可显示的最小宽度。&lt;br/&gt;默认值：360vp&lt;br/&gt;单位：vp&lt;br/&gt;取值为undefined时，按 默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## minSideBarWidth

```TypeScript
default minSideBarWidth(value: Length | undefined): this
```

设置侧边栏最小宽度。设置为小于0的值时按默认值显示。值不能超过侧边栏容器本身宽度，超过使用侧边栏容器本身宽度。

minSideBarWidth优先于侧边栏子组件minWidth，minSideBarWidth未设置时默认值优先级高于侧边栏子组件minWidth。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default minSideBarWidth(value: Length | undefined): this--><!--Device-SideBarContainerAttribute-default minSideBarWidth(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: ((value: boolean) => void) | undefined): this
```

当侧边栏的状态在显示和隐藏之间切换时触发回调。取值为undefined时，不使用回调函数。

触发该事件的条件：

1. showSideBar属性值变换时。2. showSideBar属性自适应行为变化时。3. 分割线拖拽触发[autoHide](SideBarContainerAttribute.autoHide)时。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default onChange(callback: ((value: boolean) => void) | undefined): this--><!--Device-SideBarContainerAttribute-default onChange(callback: ((value: boolean) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((value: boolean) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setSideBarContainerOptions

```TypeScript
default setSideBarContainerOptions(type?: SideBarContainerType): this
```

设置SideBarContainer选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default setSideBarContainerOptions(type?: SideBarContainerType): this--><!--Device-SideBarContainerAttribute-default setSideBarContainerOptions(type?: SideBarContainerType): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [SideBarContainerType](arkts-arkui-sidebar-sidebarcontainertype-e.md) | No | 设置侧边栏的显示类型。 &lt;br&gt;默认值:SideBarContainerType.Embed |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回SideBarContainerAttribute的实例。 |

## showControlButton

```TypeScript
default showControlButton(value: boolean | undefined): this
```

设置是否显示控制按钮。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default showControlButton(value: boolean | undefined): this--><!--Device-SideBarContainerAttribute-default showControlButton(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## showSideBar

```TypeScript
default showSideBar(value: boolean | Bindable<boolean> | undefined): this
```

设置是否显示侧边栏。

该属性支持双向绑定变量。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default showSideBar(value: boolean | Bindable<boolean> | undefined): this--><!--Device-SideBarContainerAttribute-default showSideBar(value: boolean | Bindable<boolean> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| Bindable&lt;boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## showSideBarWithGesture

```TypeScript
default showSideBarWithGesture(value: boolean | undefined): this
```

设置sideBar侧边栏是否可以通过手势显示或者隐藏。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default showSideBarWithGesture(value: boolean | undefined): this--><!--Device-SideBarContainerAttribute-default showSideBarWithGesture(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | 指示侧边栏是否可以通过手势显示或隐藏。 &lt;br&gt;默认值：**false**。 **true**：侧边栏可以通过手势来显示或隐藏。 **false**：侧边栏不能通过手势显示或隐藏。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## sideBarPosition

```TypeScript
default sideBarPosition(value: SideBarPosition | undefined): this
```

设置侧边栏显示位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default sideBarPosition(value: SideBarPosition | undefined): this--><!--Device-SideBarContainerAttribute-default sideBarPosition(value: SideBarPosition | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SideBarPosition](../arkts-components/arkts-arkui-sidebarposition-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## sideBarWidth

```TypeScript
default sideBarWidth(value: Length | Bindable<Length> | undefined): this
```

设置侧边栏的宽度。设置为小于0的值时按默认值显示。受最小宽度和最大宽度限制，不在限制区域内取最近的点。

该属性支持双向绑定变量。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default sideBarWidth(value: Length | Bindable<Length> | undefined): this--><!--Device-SideBarContainerAttribute-default sideBarWidth(value: Length | Bindable<Length> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| Bindable&lt;[Length](arkts-arkui-length-t.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

