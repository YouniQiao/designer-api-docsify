# SideBarContainerAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** SideBarContainerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SideBarContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置SideBarContainer组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## autoHide

```TypeScript
default autoHide(value: boolean | undefined): this
```

设置当侧边栏拖拽到小于最小宽度后，是否自动隐藏。受minSideBarWidth属性方法影响，minSideBarWidth属性方法未设置值使用默认值。拖拽过程中判断是否要自动隐藏。小于最小宽度时需要阻尼效果触发隐藏（越界一段距离）。

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
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## controlButton

```TypeScript
default controlButton(value: ButtonStyle | undefined): this
```

设置侧边栏控制按钮的属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ButtonStyle](arkts-arkui-sidebar-buttonstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## divider

```TypeScript
default divider(value: DividerStyle | null | undefined): this
```

设置分割线的样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | DividerStyle \| null \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## maxSideBarWidth

```TypeScript
default maxSideBarWidth(value: Length | undefined): this
```

设置侧边栏最大宽度。设置为小于0的值时按默认值显示。值不能超过侧边栏容器本身宽度，超过使用侧边栏容器本身宽度。maxSideBarWidth优先于侧边栏子组件maxWidth，maxSideBarWidth未设置时默认值优先级高于侧边栏子组件maxWidth。

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
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## minContentWidth

```TypeScript
default minContentWidth(value: Dimension | undefined): this
```

设置SideBarContainer组件内容区可显示的最小宽度。设置为小于0，内容区显示的最小宽度为360vp，未设置该属性时，组件内容区的可缩小到0。Embed场景下，增大组件尺寸时仅增大内容区的尺寸。缩小组件尺寸时，先缩小内容区的尺寸至minContentWidth。继续缩小组件尺寸时，保持内容区宽度minContentWidth不变，优先缩小侧边栏的尺寸。当缩小侧边栏的尺寸至minSideBarWidth后，继续缩小组件尺寸时，  
- 如果[autoHide](#autohide)属性为false，则会保持侧边栏宽度 [minSideBarWidth](#minsidebarwidth)和内容区宽度minContentWidth不变，但内容区会被截断显示； - 如果autoHide属性为true，则会优先隐藏侧边栏，然后继续缩小至内容区宽度minContentWidth后，内容区宽度保持不变，但内容区会被截断显示。  
minContentWidth优先于侧边栏的[maxSideBarWidth](#maxsidebarwidth)与sideBarWidth属性， minContentWidth未设置时默认值优先级低于设置的minSideBarWidth与maxSideBarWidth属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## minSideBarWidth

```TypeScript
default minSideBarWidth(value: Length | undefined): this
```

设置侧边栏最小宽度。设置为小于0的值时按默认值显示。值不能超过侧边栏容器本身宽度，超过使用侧边栏容器本身宽度。minSideBarWidth优先于侧边栏子组件minWidth，minSideBarWidth未设置时默认值优先级高于侧边栏子组件minWidth。

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
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: ((value: boolean) => void) | undefined): this
```

当侧边栏的状态在显示和隐藏之间切换时触发回调。取值为undefined时，不使用回调函数。触发该事件的条件：
1. showSideBar属性值变换时。
2. showSideBar属性自适应行为变化时。
3. 分割线拖拽触发[autoHide](#autohide)时。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((value: boolean) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## setSideBarContainerOptions

```TypeScript
default setSideBarContainerOptions(type?: SideBarContainerType): this
```

设置SideBarContainer选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SideBarContainerType](arkts-arkui-sidebar-sidebarcontainertype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## showControlButton

```TypeScript
default showControlButton(value: boolean | undefined): this
```

设置是否显示控制按钮。

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
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## showSideBar

```TypeScript
default showSideBar(value: boolean | Bindable<boolean> | undefined): this
```

设置是否显示侧边栏。该属性支持双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## showSideBarWithGesture

```TypeScript
default showSideBarWithGesture(value: boolean | undefined): this
```

设置sideBar侧边栏是否可以通过手势显示或者隐藏。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## sideBarPosition

```TypeScript
default sideBarPosition(value: SideBarPosition | undefined): this
```

设置侧边栏显示位置。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SideBarPosition](arkts-arkui-sidebar-sidebarposition-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |

## sideBarWidth

```TypeScript
default sideBarWidth(value: Length | Bindable<Length> | undefined): this
```

设置侧边栏的宽度。设置为小于0的值时按默认值显示。受最小宽度和最大宽度限制，不在限制区域内取最近的点。该属性支持双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;[Length](arkts-arkui-length-t.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md) |
