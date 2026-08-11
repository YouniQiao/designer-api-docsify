# SideBarContainerAttribute

除支持[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)外，还支持以下属性：

**继承/实现关系：** SideBarContainerAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface SideBarContainerAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SideBarContainerAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SideBarContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置SideBarContainer组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default attributeModifier(modifier: AttributeModifier<SideBarContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-SideBarContainerAttribute-default attributeModifier(modifier: AttributeModifier<SideBarContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;SideBarContainerAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 | 在当 前组件上，动态设置属性方法，支持使用if/else语法。&lt;br/&gt;CommonMethod：通用属性和事件。&lt;br/&gt;取值为undefined时，按当前组件的属性方法默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## autoHide

```TypeScript
default autoHide(value: boolean | undefined): this
```

设置当侧边栏拖拽到小于最小宽度后，是否自动隐藏。受minSideBarWidth属性方法影响，minSideBarWidth属性方法未设置值使用默认值。

拖拽过程中判断是否要自动隐藏。小于最小宽度时需要阻尼效果触发隐藏（越界一段距离）。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default autoHide(value: boolean | undefined): this--><!--Device-SideBarContainerAttribute-default autoHide(value: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## controlButton

```TypeScript
default controlButton(value: ButtonStyle | undefined): this
```

设置侧边栏控制按钮的属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default controlButton(value: ButtonStyle | undefined): this--><!--Device-SideBarContainerAttribute-default controlButton(value: ButtonStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonStyle](arkts-arkui-sidebar-buttonstyle-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## divider

```TypeScript
default divider(value: DividerStyle | null | undefined): this
```

设置分割线的样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default divider(value: DividerStyle | null | undefined): this--><!--Device-SideBarContainerAttribute-default divider(value: DividerStyle | null | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DividerStyle](../arkts-components/arkts-arkui-dividerstyle-i.md) \| null \| undefined | 是 | 分割线的样式。&lt;br/&gt;默认为DividerStyle：显示分割线。&lt;br/&gt;- null或undefined：行为不做处理，分 割线样式与默认值保持一致。&lt;br/&gt;**说明：** &lt;br/&gt;API version 11及以下版本，null效果为不显示分割线。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## maxSideBarWidth

```TypeScript
default maxSideBarWidth(value: Length | undefined): this
```

设置侧边栏最大宽度。设置为小于0的值时按默认值显示。值不能超过侧边栏容器本身宽度，超过使用侧边栏容器本身宽度。

maxSideBarWidth优先于侧边栏子组件maxWidth，maxSideBarWidth未设置时默认值优先级高于侧边栏子组件maxWidth。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default maxSideBarWidth(value: Length | undefined): this--><!--Device-SideBarContainerAttribute-default maxSideBarWidth(value: Length | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
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

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default minContentWidth(value: Dimension | undefined): this--><!--Device-SideBarContainerAttribute-default minContentWidth(value: Dimension | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 | SideBarContainer组件内容区可显示的最小宽度。&lt;br/&gt;默认值：360vp&lt;br/&gt;单位：vp&lt;br/&gt;取值为undefined时，按 默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## minSideBarWidth

```TypeScript
default minSideBarWidth(value: Length | undefined): this
```

设置侧边栏最小宽度。设置为小于0的值时按默认值显示。值不能超过侧边栏容器本身宽度，超过使用侧边栏容器本身宽度。

minSideBarWidth优先于侧边栏子组件minWidth，minSideBarWidth未设置时默认值优先级高于侧边栏子组件minWidth。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default minSideBarWidth(value: Length | undefined): this--><!--Device-SideBarContainerAttribute-default minSideBarWidth(value: Length | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: ((value: boolean) => void) | undefined): this
```

当侧边栏的状态在显示和隐藏之间切换时触发回调。取值为undefined时，不使用回调函数。

触发该事件的条件：

1. showSideBar属性值变换时。2. showSideBar属性自适应行为变化时。3. 分割线拖拽触发[autoHide](SideBarContainerAttribute.autoHide)时。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default onChange(callback: ((value: boolean) => void) | undefined): this--><!--Device-SideBarContainerAttribute-default onChange(callback: ((value: boolean) => void) | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | ((value: boolean) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setSideBarContainerOptions

```TypeScript
default setSideBarContainerOptions(type?: SideBarContainerType): this
```

设置SideBarContainer选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default setSideBarContainerOptions(type?: SideBarContainerType): this--><!--Device-SideBarContainerAttribute-default setSideBarContainerOptions(type?: SideBarContainerType): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SideBarContainerType](arkts-arkui-sidebar-sidebarcontainertype-e.md) | 否 | 设置侧边栏的显示类型。 &lt;br&gt;默认值:SideBarContainerType.Embed |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 返回SideBarContainerAttribute的实例。 |

## showControlButton

```TypeScript
default showControlButton(value: boolean | undefined): this
```

设置是否显示控制按钮。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default showControlButton(value: boolean | undefined): this--><!--Device-SideBarContainerAttribute-default showControlButton(value: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## showSideBar

```TypeScript
default showSideBar(value: boolean | Bindable<boolean> | undefined): this
```

设置是否显示侧边栏。

该属性支持双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default showSideBar(value: boolean | Bindable<boolean> | undefined): this--><!--Device-SideBarContainerAttribute-default showSideBar(value: boolean | Bindable<boolean> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| Bindable&lt;boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## showSideBarWithGesture

```TypeScript
default showSideBarWithGesture(value: boolean | undefined): this
```

设置sideBar侧边栏是否可以通过手势显示或者隐藏。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default showSideBarWithGesture(value: boolean | undefined): this--><!--Device-SideBarContainerAttribute-default showSideBarWithGesture(value: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 | 指示侧边栏是否可以通过手势显示或隐藏。 &lt;br&gt;默认值：**false**。 **true**：侧边栏可以通过手势来显示或隐藏。 **false**：侧边栏不能通过手势显示或隐藏。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## sideBarPosition

```TypeScript
default sideBarPosition(value: SideBarPosition | undefined): this
```

设置侧边栏显示位置。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default sideBarPosition(value: SideBarPosition | undefined): this--><!--Device-SideBarContainerAttribute-default sideBarPosition(value: SideBarPosition | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SideBarPosition](arkts-arkui-sidebar-sidebarposition-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## sideBarWidth

```TypeScript
default sideBarWidth(value: Length | Bindable<Length> | undefined): this
```

设置侧边栏的宽度。设置为小于0的值时按默认值显示。受最小宽度和最大宽度限制，不在限制区域内取最近的点。

该属性支持双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SideBarContainerAttribute-default sideBarWidth(value: Length | Bindable<Length> | undefined): this--><!--Device-SideBarContainerAttribute-default sideBarWidth(value: Length | Bindable<Length> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| Bindable&lt;[Length](arkts-arkui-length-t.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

