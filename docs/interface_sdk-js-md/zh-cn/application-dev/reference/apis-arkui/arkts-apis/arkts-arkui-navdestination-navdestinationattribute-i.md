# NavDestinationAttribute

支持[通用属性](./../../@internal/component/ets/common)。

**继承/实现关系：** NavDestinationAttribute extends [CommonMethod](CommonMethod)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface NavDestinationAttribute extends CommonMethod--><!--Device-unnamed-export declare interface NavDestinationAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<NavDestinationAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置NavDestination组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default attributeModifier(modifier: AttributeModifier<NavDestinationAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-NavDestinationAttribute-default attributeModifier(modifier: AttributeModifier<NavDestinationAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 | 在当前组 件上，动态设置属性方法，支持使用if/else语法。取值为undefined时，按当前组件的属性方法默认值处理。&lt;br/&gt;CommonMethod：通用属性和事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## backButtonIcon

```TypeScript
default backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this
```

> **说明：**
> 
> 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

设置标题栏返回键图标和无障碍播报内容。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this--><!--Device-NavDestinationAttribute-default backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| icon | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md) \| undefined | 是 | 标题栏返回键图标。&lt;br/&gt;取值为undefined时，显示返回图标。 |
| accessibilityText | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 否 | 返回键无障碍播报内容。&lt;br/&gt;取值为undefined时，按默认值处理。&lt;/br&gt;默认值：系统语言是中文时为“返回 ”，系统语言是英文时为“back”。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## bindToNestedScrollable

```TypeScript
default bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo> | undefined): this
```

绑定NavDestination组件和嵌套的可滚动容器组件（支持[List](./../../@internal/component/ets/list)、  
[Scroll](./../../@internal/component/ets/scroll)、[Grid](./../../@internal/component/ets/grid)、  
[WaterFlow](./../../@internal/component/ets/water_flow)），当滑动父组件或子组件时，会触发所有与其绑定的NavDestination组件的标题栏和工具栏的显示和隐藏动效，上滑隐藏，下滑显示。一个NavDestination可与多个嵌套的可滚动容器组件绑定，嵌套的可滚动容器组件也可与多个NavDestination绑定。使用示例参见  
[示例1](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination copy.md#示例1标题栏工具栏与可滚动类组件联动)。

> **说明：**
> 
> - 只有NavDestination的标题栏或工具栏设置为可见时，联动效果才会生效。
> 
> - 当多个可滚动容器组件绑定了同一个NavDestination组件时，滚动任何一个容器都会触发标题栏和工具栏的显示或隐藏效果。且当任何一个可滚动容器组件滑动到底部或顶部位置时，会立即触发标题栏和工具栏的显示动效。因此，为了获
> 得最佳用户体验，不建议同时触发多个可滚动容器组件的滚动事件。
> 
> - 从API version 22开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo> | undefined): this--><!--Device-NavDestinationAttribute-default bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollInfos | Array&lt;[NestedScrollInfo](arkts-arkui-navdestination-nestedscrollinfo-i.md)&gt; \| undefined | 是 | 嵌套的可滚动容器组件的控制器。&lt;br/&gt;取值为undefined时，无控制器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## bindToScrollable

```TypeScript
default bindToScrollable(scrollers: Array<Scroller> | undefined): this
```

绑定NavDestination组件和可滚动容器组件（支持[List](./../../@internal/component/ets/list)、  
[Scroll](./../../@internal/component/ets/scroll)、[Grid](./../../@internal/component/ets/grid)、  
[WaterFlow](./../../@internal/component/ets/water_flow)），当滑动可滚动容器组件时，会触发所有与其绑定的NavDestination组件的标题栏和工具栏的显示和隐藏动效，上滑隐藏，下滑显示。一个NavDestination可与多个可滚动容器组件绑定，一个可滚动容器组件也可与多个NavDestination绑定。使用示例参见  
[示例1](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination copy.md#示例1标题栏工具栏与可滚动类组件联动)。

> **说明：**
> 
> - 只有NavDestination的标题栏或工具栏设置为可见时，联动效果才会生效。
> 
> - 当多个可滚动容器组件绑定了同一个NavDestination组件时，滚动任何一个容器都会触发标题栏和工具栏的显示或隐藏效果。且当任何一个可滚动容器组件滑动到底部或顶部位置时，会立即触发标题栏和工具栏的显示动效。因此，为了获
> 得最佳用户体验，不建议同时触发多个可滚动容器组件的滚动事件。
> 
> - 从API version 22开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default bindToScrollable(scrollers: Array<Scroller> | undefined): this--><!--Device-NavDestinationAttribute-default bindToScrollable(scrollers: Array<Scroller> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollers | Array&lt;[Scroller](../arkts-components/arkts-arkui-scroller-c.md)&gt; \| undefined | 是 | 可滚动容器组件的控制器。&lt;br/&gt;取值为undefined时，无控制器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## customTransition

```TypeScript
default customTransition(delegate: NavDestinationTransitionDelegate | undefined): this
```

设置NavDestination自定义转场动画。

> **说明：**
> 
> - 该接口不支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。
> 
> - 该属性与[systemTransition](#systemTransition)同时设置时，后设置的属性生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default customTransition(delegate: NavDestinationTransitionDelegate | undefined): this--><!--Device-NavDestinationAttribute-default customTransition(delegate: NavDestinationTransitionDelegate | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate | [NavDestinationTransitionDelegate](arkts-arkui-navdestinationtransitiondelegate-t.md) \| undefined | 是 | NavDestination自定义动画的代理函数。&lt;br/&gt;取值为undefined时，不使用回 调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## enableNavigationIndicator

```TypeScript
default enableNavigationIndicator(enabled: boolean | undefined): this
```

设置进入该NavDestination后，显示或者隐藏系统的导航条。

> **说明：**
> 
> 该属性满足如下全部条件时才生效：
> 
> 
> 设置系统导航条的实际效果依赖于具体的设备支持情况，具体参考窗口的
> [setSpecificSystemBarEnabled](../../../reference/apis-arkui/arkts-apis-window-Window.md#setspecificsystembarenabled11)
> 接口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default enableNavigationIndicator(enabled: boolean | undefined): this--><!--Device-NavDestinationAttribute-default enableNavigationIndicator(enabled: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 | 进入该NavDestination后，系统导航条的显示/隐藏状态。&lt;br/&gt;取值为undefined时，按默认值处理。&lt;br/&gt;true：显示导航条 。&lt;br/&gt;false：隐藏导航条。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## enableStatusBar

```TypeScript
default enableStatusBar(enabled: boolean | undefined, animated?: boolean | undefined): this
```

设置进入该NavDestination后，显示或者隐藏系统的状态栏。

> **说明：**
> 
> - 该属性满足如下全部条件时才生效：
> > 1. NavDestination属于应用主窗口页面，并且主窗口为全屏窗口；
> > 2. NavDestination所属的Navigation的大小占满整个页面；
> > 3. NavDestination的大小占满整个Navigation组件；
> > 4. NavDestination类型为[NavDestinationMode](arkts-arkui-navdestination-navdestinationmode-e.md#NavDestinationMode).STANDARD。
> 
> - 设置系统状态栏的实际效果依赖于具体的设备支持情况，具体参考窗口的
> [setSpecificSystemBarEnabled](../../../reference/apis-arkui/arkts-apis-window-Window.md#setspecificsystembarenabled11)
> 接口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default enableStatusBar(enabled: boolean | undefined, animated?: boolean | undefined): this--><!--Device-NavDestinationAttribute-default enableStatusBar(enabled: boolean | undefined, animated?: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 | 进入该NavDestination后，系统状态栏的显示/隐藏状态。&lt;br/&gt;取值为undefined时，按默认值处理。&lt;br/&gt;true：显示状态栏 。&lt;br/&gt;false：隐藏状态栏。 |
| animated | boolean \| undefined | 否 | 进入该NavDestination后，系统状态栏的显示/隐藏状态。 &lt;br&gt;取值为undefined时，按默认值处理。 默认值： false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 返回Navigation属性对象。 |

## fullScreenOverlay

```TypeScript
default fullScreenOverlay(fullScreenOverlay: boolean | undefined): this
```

设置NavDestination是否以全屏覆盖模式显示。

当参数设置为true时，在Navigation分栏模式下，当前页面会覆盖整个Navigation容器，包括NavBar和内容区。该配置作用于当前NavDestination的所有实例；当路由栈中已有页面以全屏覆盖模式显示时，其后入栈的[DIALOG](arkts-arkui-navdestination-navdestinationmode-e.md#NavDestinationMode)页面与未设置fullScreenOverlay为false的[STANDARD](arkts-arkui-navdestination-navdestinationmode-e.md#NavDestinationMode)页面也会继承为全屏覆盖显示。未通过该接口设置时，NavDestination默认是普通显示模式，遵循Navigation分栏显示规则。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default fullScreenOverlay(fullScreenOverlay: boolean | undefined): this--><!--Device-NavDestinationAttribute-default fullScreenOverlay(fullScreenOverlay: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fullScreenOverlay | boolean \| undefined | 是 | 是否以全屏覆盖模式显示。&lt;br/&gt;true：全屏覆盖模式，覆盖整个Navigation容器。&lt;br/&gt;false：普通显示模式， 遵循Navigation分栏显示规则。指定为false的STANDARD类型页面不会继承全屏显示。&lt;br/&gt;undefined：普通显示模式，遵循Navigation分栏显示规则。指定为undefined的页面会继承全屏显 示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## hideBackButton

```TypeScript
default hideBackButton(hide: boolean | undefined): this
```

设置是否隐藏标题栏中的返回键。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default hideBackButton(hide: boolean | undefined): this--><!--Device-NavDestinationAttribute-default hideBackButton(hide: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## hideTitleBar

```TypeScript
default hideTitleBar(value: boolean | undefined): this
```

设置是否隐藏标题栏。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default hideTitleBar(value: boolean | undefined): this--><!--Device-NavDestinationAttribute-default hideTitleBar(value: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## hideTitleBar

```TypeScript
default hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this
```

设置是否隐藏标题栏。与[hideTitleBar](NavDestinationAttribute.default hideTitleBar(value: boolean | undefined))相比，新增标题栏显隐时是否使用动画。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this--><!--Device-NavDestinationAttribute-default hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean \| undefined | 是 |  |
| animated | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## hideToolBar

```TypeScript
default hideToolBar(hide: boolean | undefined, animated?: boolean | undefined): this
```

设置是否隐藏工具栏。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default hideToolBar(hide: boolean | undefined, animated?: boolean | undefined): this--><!--Device-NavDestinationAttribute-default hideToolBar(hide: boolean | undefined, animated?: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean \| undefined | 是 |  |
| animated | boolean \| undefined | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## ignoreLayoutSafeArea

```TypeScript
default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this
```

控制组件的布局，使其扩展到非安全区域。

> **说明：**
> 
> - 组件设置ignoreLayoutSafeArea之后生效的条件为：
> > 设置LayoutSafeAreaType.SYSTEM时，组件的边界与非安全区域重合时组件能够延伸到非安全区域下。
> 
> - 若组件扩展到非安全区域内，此时在非安全区域里触发的事件（例如：点击事件）等可能会被系统拦截，优先响应状态栏等系统组件。
> 
> - 组件想要扩展到非安全区域内，需隐藏或者设置标题栏和工具栏为[STACK](../arkts-components/arkts-arkui-barstyle-e.md#BarStyle)模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this--><!--Device-NavDestinationAttribute-default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | Array&lt;[LayoutSafeAreaType](../arkts-components/arkts-arkui-layoutsafeareatype-e.md)&gt; \| undefined | 否 | 配置扩展安全区域的类型。&lt;br /&gt;取值为undefined时，按照默认值处理。&lt;br /&gt;默认值：&lt;br /&gt; [LayoutSafeAreaType.SYSTEM] |
| edges | Array&lt;[LayoutSafeAreaEdge](../arkts-components/arkts-arkui-layoutsafeareaedge-e.md)&gt; \| undefined | 否 | 配置扩展安全区域的方向。&lt;br /&gt;取值为undefined时，按照默认值处理。&lt;br /&gt; 默认值：&lt;br / &gt;[LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## menus

```TypeScript
default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this
```

> **说明：**
> 
> 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

设置页面右上角菜单。不设置时不显示菜单项。与  
[menus](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination copy.md#menus12)相比，新增菜单选项。使用Array<[NavigationMenuItem](../arkts-components/arkts-arkui-navigationmenuitem-i.md#NavigationMenuItem)&gt; 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this--><!--Device-NavDestinationAttribute-default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array&lt;[NavigationMenuItem](../arkts-components/arkts-arkui-navigationmenuitem-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |  |
| options | [NavigationMenuOptions](../arkts-components/arkts-arkui-navigationmenuoptions-i.md) \| undefined | 否 | 页面右上角菜单选项。&lt;br/&gt;取值为undefined时，按NavigationMenuOptions中的默认值处理 。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## mode

```TypeScript
default mode(value: NavDestinationMode | undefined): this
```

设置NavDestination类型，不支持动态修改。

> **说明：**
> 
> 从API version 12开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default mode(value: NavDestinationMode | undefined): this--><!--Device-NavDestinationAttribute-default mode(value: NavDestinationMode | undefined): this-End-->

**系统能力：** 
- API版本23+：SystemCapability.ArkUI.ArkUI.Full
- API版本23+：SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NavDestinationMode](arkts-arkui-navdestination-navdestinationmode-e.md) \| undefined | 是 | NavDestination类型。&lt;br/&gt;取值为undefined时，按默认值处理。&lt;br/&gt;默认值： NavDestinationMode.STANDARD<br>**起始版本：** 23 - 24 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onActive

```TypeScript
default onActive(callback: Callback<NavDestinationActiveReason> | undefined): this
```

NavDestination处于激活态（处于栈顶可操作，且上层无特殊组件遮挡）时，触发该回调。使用示例参见  
[示例5](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination copy.md#示例5navdestination的onactive与oninactive生命周期)。

> **说明：**
> 
> 从API version 22开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default onActive(callback: Callback<NavDestinationActiveReason> | undefined): this--><!--Device-NavDestinationAttribute-default onActive(callback: Callback<NavDestinationActiveReason> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[NavDestinationActiveReason](arkts-arkui-navdestination-navdestinationactivereason-e.md)&gt; \| undefined | 是 | NavDestination由非激活态变为激活态的原因。&lt;br/&gt;取值为 undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onBackPressed

```TypeScript
default onBackPressed(callback: (() => boolean) | undefined): this
```

当与Navigation绑定的导航控制器中存在内容时，此回调生效。当点击返回键时，触发该回调。

返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default onBackPressed(callback: (() => boolean) | undefined): this--><!--Device-NavDestinationAttribute-default onBackPressed(callback: (() => boolean) | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (() =&gt; boolean) \| undefined | 是 | 当与Navigation绑定的导航控制器中存在内容时，此回调生效。当点击返回键时，触发该回调。&lt;br/&gt;取值为undefined时，不使用回调函 数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onHidden

```TypeScript
default onHidden(callback: Callback<VisibilityChangeReason> | undefined): this
```

当该NavDestination页面隐藏时触发此回调。从API version 21开始，支持通过VisibilityChangeReason说明onHidden触发的原因。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default onHidden(callback: Callback<VisibilityChangeReason> | undefined): this--><!--Device-NavDestinationAttribute-default onHidden(callback: Callback<VisibilityChangeReason> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[VisibilityChangeReason](arkts-arkui-navdestination-visibilitychangereason-e.md)&gt; \| undefined | 是 | 当该NavDestination页面隐藏时触发此回调。&lt;br/&gt;取值为undefined时，不使 用回调函数。&lt;br/&gt;在API version 21之前，当NavDestination页面隐藏时触发回调。&lt;br/&gt;从API version 21开始，该回调会提供入参VisibilityChangeReason以说明 onHidden触发的原因。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onInactive

```TypeScript
default onInactive(callback: Callback<NavDestinationActiveReason> | undefined): this
```

NavDestination处于非激活态（处于非栈顶不可操作，或处于栈顶时上层有特殊组件遮挡）时，触发该回调。使用示例参见  
[示例5](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination copy.md#示例5navdestination的onactive与oninactive生命周期)。

> **说明：**
> 
> 从API version 22开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default onInactive(callback: Callback<NavDestinationActiveReason> | undefined): this--><!--Device-NavDestinationAttribute-default onInactive(callback: Callback<NavDestinationActiveReason> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[NavDestinationActiveReason](arkts-arkui-navdestination-navdestinationactivereason-e.md)&gt; \| undefined | 是 | NavDestination由激活态变为非激活态的原因。&lt;br/&gt;取值为 undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onNewParam

```TypeScript
default onNewParam(callback: Callback<Object | null | undefined> | undefined): this
```

当之前存在于栈中的NavDestination页面通过  
[launchMode.MOVE_TO_TOP_SINGLETON](../arkts-components/arkts-arkui-launchmode-e.md#LaunchMode)或  
[launchMode.POP_TO_SINGLETON](../arkts-components/arkts-arkui-launchmode-e.md#LaunchMode)移动到栈顶时，触发该回调。

> **说明：**
> 
> -
> [replacePath](../arkts-components/arkts-arkui-navpathstack-c.md#replacePath)
> 、[replaceDestination](../arkts-components/arkts-arkui-navpathstack-c.md#replaceDestination)不会触发该回调。
> 
> - 从API version 22开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default onNewParam(callback: Callback<Object | null | undefined> | undefined): this--><!--Device-NavDestinationAttribute-default onNewParam(callback: Callback<Object | null | undefined> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;Object \| null \| undefined&gt; \| undefined | 是 | Indicates callback when destination be pushed with singleton mode. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onReady

```TypeScript
default onReady(callback: Callback<NavDestinationContext> | undefined): this
```

当NavDestination即将构建子组件之前会触发此回调。

> **说明：**
> 
> 从API version 20开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default onReady(callback: Callback<NavDestinationContext> | undefined): this--><!--Device-NavDestinationAttribute-default onReady(callback: Callback<NavDestinationContext> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[NavDestinationContext](arkts-arkui-navdestination-navdestinationcontext-i.md)&gt; \| undefined | 是 | 当NavDestination即将构建子组件之前会触发此回调。&lt;br/&gt;取值为undefined时 ，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onResult

```TypeScript
default onResult(callback: Callback<Object | null | undefined> | undefined): this
```

NavDestination返回时触发该回调。

> **说明：**
> 
> 从API version 22开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default onResult(callback: Callback<Object | null | undefined> | undefined): this--><!--Device-NavDestinationAttribute-default onResult(callback: Callback<Object | null | undefined> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;Object \| null \| undefined&gt; \| undefined | 是 | 页面返回回调，入参为 [pop](../arkts-components/arkts-arkui-navpathstack-c.md#pop-1)、 [popToName](../arkts-components/arkts-arkui-navpathstack-c.md#popToName-1) 、 [popToIndex](../arkts-components/arkts-arkui-navpathstack-c.md#popToIndex-1) 接口传入的result参数。如果不传该参数，入参为undefined。&lt;br/&gt;取值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onShown

```TypeScript
default onShown(callback: Callback<VisibilityChangeReason> | undefined): this
```

当该NavDestination页面显示时触发此回调。从API version 21开始，支持通过VisibilityChangeReason说明onShown触发的原因。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default onShown(callback: Callback<VisibilityChangeReason> | undefined): this--><!--Device-NavDestinationAttribute-default onShown(callback: Callback<VisibilityChangeReason> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[VisibilityChangeReason](arkts-arkui-navdestination-visibilitychangereason-e.md)&gt; \| undefined | 是 | 当该NavDestination页面显示时触发此回调。&lt;br/&gt;取值为undefined时，不使 用回调函数。&lt;br/&gt;在API version 21之前，当NavDestination页面显示时触发回调。&lt;br/&gt;从API version 21开始，回调会提供入参VisibilityChangeReason以说明 onShown触发的原因。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onWillAppear

```TypeScript
default onWillAppear(callback: VoidCallback | undefined): this
```

当该NavDestination挂载之前触发此回调。在该回调中允许修改路由栈，当前帧生效。

> **说明：**
> 
> 从API version 20开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default onWillAppear(callback: VoidCallback | undefined): this--><!--Device-NavDestinationAttribute-default onWillAppear(callback: VoidCallback | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 | 当该NavDestination挂载之前触发此回调。在该回调中允许修改路由栈，当前帧生效。&lt;br/&gt;取值为undefined时，不使用回 调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onWillDisappear

```TypeScript
default onWillDisappear(callback: VoidCallback | undefined): this
```

当该NavDestination卸载之前触发的生命周期(有转场动画时，在转场动画开始之前触发)。

> **说明：**
> 
> 从API version 20开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default onWillDisappear(callback: VoidCallback | undefined): this--><!--Device-NavDestinationAttribute-default onWillDisappear(callback: VoidCallback | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 | 当该NavDestination卸载之前触发的生命周期(有转场动画时，在转场动画开始之前触发)。&lt;br/&gt;取值为undefined时，不 使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onWillHide

```TypeScript
default onWillHide(callback: VoidCallback | undefined): this
```

当该NavDestination隐藏之前触发此回调。

> **说明：**
> 
> 从API version 20开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default onWillHide(callback: VoidCallback | undefined): this--><!--Device-NavDestinationAttribute-default onWillHide(callback: VoidCallback | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 | 当该NavDestination隐藏之前触发此回调。&lt;br/&gt;取值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onWillShow

```TypeScript
default onWillShow(callback: VoidCallback | undefined): this
```

当该NavDestination显示之前触发此回调。

> **说明：**
> 
> 从API version 20开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default onWillShow(callback: VoidCallback | undefined): this--><!--Device-NavDestinationAttribute-default onWillShow(callback: VoidCallback | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 | 当该NavDestination显示之前触发此回调。&lt;br/&gt;取值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## preferredOrientation

```TypeScript
default preferredOrientation(orientation: Orientation | undefined): this
```

设置NavDestination对应的显示方向。转场到该NavDestination后，系统也会将应用主窗口切到该显示方向。

> **说明：**
> 
> - 该属性满足如下全部条件时才有效：
> > 1. NavDestination属于应用主窗口页面，并且主窗口为全屏窗口；
> > 2. NavDestination所属的Navigation的大小占满整个应用页面；
> > 3. NavDestination类型为[NavDestinationMode](arkts-arkui-navdestination-navdestinationmode-e.md#NavDestinationMode).STANDARD。
> 
> - 设置显示方向的实际效果依赖于具体的设备支持情况，具体参考窗口的
> [setPreferredOrientation](../../../reference/apis-arkui/arkts-apis-window-Window.md#setpreferredorientation9-1)接
> 口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default preferredOrientation(orientation: Orientation | undefined): this--><!--Device-NavDestinationAttribute-default preferredOrientation(orientation: Orientation | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | [Orientation](arkts-arkui-orientation-t.md) \| undefined | 是 | NavDestination页面对应的Orientation。&lt;br/&gt;取值为undefined时，按当前设备的显示方向处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## recoverable

```TypeScript
default recoverable(recoverable: boolean | undefined): this
```

配置NavDestination是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建该NavDestination。该功能需NavDestination对应的Navigation也配置了  
[可恢复属性](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#recoverable14)。

> **说明：**
> 
> 该接口需要配合Navigation的
> [recoverable](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#recoverable14)接口使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default recoverable(recoverable: boolean | undefined): this--><!--Device-NavDestinationAttribute-default recoverable(recoverable: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recoverable | boolean \| undefined | 是 | NavDestination是否可恢复。&lt;br/&gt;取值为undefined时，按默认值处理。&lt;br/&gt;默认值：false&lt;br/&gt;true： 路由栈可恢复。&lt;br/&gt;false：路由栈不可恢复。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setNavDestinationOptions

```TypeScript
default setNavDestinationOptions(moduleInfo?: NavDestinationModuleInfo): this
```

设置navDestination选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default setNavDestinationOptions(moduleInfo?: NavDestinationModuleInfo): this--><!--Device-NavDestinationAttribute-default setNavDestinationOptions(moduleInfo?: NavDestinationModuleInfo): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleInfo | [NavDestinationModuleInfo](arkts-arkui-navdestination-navdestinationmoduleinfo-i.md) | 否 | NavDestination模块信息 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 返回NavDestinationAttribute的实例。 |

## systemBarStyle

```TypeScript
default systemBarStyle(style: SystemBarStyle | undefined): this
```

当Navigation中显示当前NavDestination时，设置对应系统状态栏的样式。

> **说明：**
> 
> - 必须配合Navigation使用，作为其Navigation目的页面的根节点时才能生效。
> 
> - 其他使用限制请参考Navigation对应的
> [systemBarStyle](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#systembarstyle12)属性说明。
> 
> 
> - 从API version 20开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default systemBarStyle(style: SystemBarStyle | undefined): this--><!--Device-NavDestinationAttribute-default systemBarStyle(style: SystemBarStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [SystemBarStyle](../arkts-components/arkts-arkui-systembarstyle-t.md) \| undefined | 是 | 系统状态栏样式。&lt;br/&gt;取值为undefined时，无样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## systemTransition

```TypeScript
default systemTransition(type: NavigationSystemTransitionType | undefined): this
```

设置NavDestination系统转场动画，支持分别设置系统标题栏动画和内容动画。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default systemTransition(type: NavigationSystemTransitionType | undefined): this--><!--Device-NavDestinationAttribute-default systemTransition(type: NavigationSystemTransitionType | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [NavigationSystemTransitionType](arkts-arkui-navdestination-navigationsystemtransitiontype-e.md) \| undefined | 是 | 系统转场动画类型。&lt;br/&gt;取值为undefined时，按默认值处理。&lt;br/&gt;默认值： NavigationSystemTransitionType.DEFAULT |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## title

```TypeScript
default title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource | undefined, options?: NavigationTitleOptions | undefined): this
```

设置页面标题。字符串超长时，如果不设置副标题，先缩小再换行2行后以"..."截断。如果设置副标题，先缩小后以"..."截断。

> **说明：**
> 
> 从API version 12开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource | undefined, options?: NavigationTitleOptions | undefined): this--><!--Device-NavDestinationAttribute-default title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource | undefined, options?: NavigationTitleOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [NavDestinationCommonTitle](arkts-arkui-navdestination-navdestinationcommontitle-i.md) \| [NavDestinationCustomTitle](arkts-arkui-navdestination-navdestinationcustomtitle-i.md) \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 | NavDestination title. |
| options | [NavigationTitleOptions](../arkts-components/arkts-arkui-navigationtitleoptions-i.md) \| undefined | 否 | 标题栏选项。&lt;br/&gt;取值为undefined时，按NavigationTitleOptions中的默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## toolbarConfiguration

```TypeScript
default toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this
```

设置工具栏内容。未调用本接口时不显示工具栏。

> **说明：**
> 
> - 从API version 20开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。
> 
> - 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NavDestinationAttribute-default toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this--><!--Device-NavDestinationAttribute-default toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| toolbarParam | Array&lt;[ToolbarItem](../arkts-components/arkts-arkui-toolbaritem-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 | 工具栏内容。&lt;br/&gt;使用Array&lt; [ToolbarItem](../arkts-components/arkts-arkui-toolbaritem-i.md#ToolbarItem)&gt;写法设置的工具栏有如下特性：&lt;br/&gt;-工具栏所有选项均分底部工具栏， 在每个均分内容区布局文本和图标。&lt;br/&gt;-竖屏模式最多支持显示5个图标，多余的图标会被放入自动生成的更多图标中，点击更多图标，可以展示剩余内容。横屏模式时，如果为 [Split](../arkts-components/arkts-arkui-navigationmode-e.md#NavigationMode)模式，仍按照竖屏模式显示，如果为 [Stack](../arkts-components/arkts-arkui-navigationmode-e.md#NavigationMode)模式需配合 [menus](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination copy.md#menus12)属性的Array&lt; [NavigationMenuItem](../arkts-components/arkts-arkui-navigationmenuitem-i.md#NavigationMenuItem)&gt;使用，底部工具栏会自动隐藏，同时底部工具栏 所有选项移动至页面右上角菜单。&lt;br/&gt;使用[CustomBuilder](../../../reference/apis-arkui/arkui-ts/ts-types.md#custombuilder8)写法为用户自 定义工具栏选项，不具备以上功能。&lt;br/&gt;取值为undefined时，无内容。 |
| options | [NavigationToolbarOptions](../arkts-components/arkts-arkui-navigationtoolbaroptions-i.md) \| undefined | 否 | 工具栏选项。包含工具栏背景颜色、工具栏背景模糊样式及模糊选项、工具栏背景属性、工具栏布局方式、是否隐藏工具栏的 文本、工具栏更多图标的菜单选项。&lt;br/&gt;取值为undefined时，按NavigationToolbarOptions的默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

