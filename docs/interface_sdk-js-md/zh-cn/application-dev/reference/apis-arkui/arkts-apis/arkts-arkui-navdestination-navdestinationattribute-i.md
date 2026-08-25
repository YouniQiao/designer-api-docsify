# NavDestinationAttribute

支持通用属性。

**继承/实现关系：** NavDestinationAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<NavDestinationAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置NavDestination组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## backButtonIcon

```TypeScript
default backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this
```


> **说明：**&gt;
> 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。
设置标题栏返回键图标和无障碍播报内容。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| icon | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md) \| undefined | 是 |
| accessibilityText | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## bindToNestedScrollable

```TypeScript
default bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo> | undefined): this
```

绑定NavDestination组件和嵌套的可滚动容器组件（支持List、 Scroll、Grid、 WaterFlow），当滑动父组件或子组件时，会触发所有与其绑定的NavDestination组件的标题栏和工具栏的显示和隐藏 动效，上滑隐藏，下滑显示。一个NavDestination可与多个嵌套的可滚动容器组件绑定，嵌套的可滚动容器组件也可与多个NavDestination绑定。使用示例参见 示例1。

> **说明：**&gt;
> - 只有NavDestination的标题栏或工具栏设置为可见时，联动效果才会生效。&gt;
> - 当多个可滚动容器组件绑定了同一个NavDestination组件时，滚动任何一个容器都会触发标题栏和工具栏的显示或隐藏效果。且当任何一个可滚动容器组件滑动到底部或顶部位置时，会立即触发标题栏和工具栏的显示动效。因此，为了获
> 得最佳用户体验，不建议同时触发多个可滚动容器组件的滚动事件。&gt;
> - 从API version 22开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scrollInfos | Array&lt;[NestedScrollInfo](arkts-arkui-navdestination-nestedscrollinfo-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## bindToScrollable

```TypeScript
default bindToScrollable(scrollers: Array<Scroller> | undefined): this
```

绑定NavDestination组件和可滚动容器组件（支持List、 Scroll、Grid、 WaterFlow），当滑动可滚动容器组件时，会触发所有与其绑定的NavDestination组件的标题栏和工具栏的显示和隐藏 动效，上滑隐藏，下滑显示。一个NavDestination可与多个可滚动容器组件绑定，一个可滚动容器组件也可与多个NavDestination绑定。使用示例参见 示例1。

> **说明：**&gt;
> - 只有NavDestination的标题栏或工具栏设置为可见时，联动效果才会生效。&gt;
> - 当多个可滚动容器组件绑定了同一个NavDestination组件时，滚动任何一个容器都会触发标题栏和工具栏的显示或隐藏效果。且当任何一个可滚动容器组件滑动到底部或顶部位置时，会立即触发标题栏和工具栏的显示动效。因此，为了获
> 得最佳用户体验，不建议同时触发多个可滚动容器组件的滚动事件。&gt;
> - 从API version 22开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scrollers | Array&lt;[Scroller](../arkts-components/arkts-arkui-scroller-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## customTransition

```TypeScript
default customTransition(delegate: NavDestinationTransitionDelegate | undefined): this
```

设置NavDestination自定义转场动画。

> **说明：**&gt;
> - 该接口不支持在
> attributeModifier
> 中调用。&gt;
> - 该属性与[systemTransition](#systemtransition)同时设置时，后设置的属性生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| delegate | [NavDestinationTransitionDelegate](arkts-arkui-navdestinationtransitiondelegate-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## enableNavigationIndicator

```TypeScript
default enableNavigationIndicator(enabled: boolean | undefined): this
```

设置进入该NavDestination后，显示或者隐藏系统的导航条。

> **说明：**&gt;
> 该属性满足如下全部条件时才生效：&gt;>
> 设置系统导航条的实际效果依赖于具体的设备支持情况，具体参考窗口的
> [setSpecificSystemBarEnabled](arkts-arkui-window-window-i.md#setspecificsystembarenabled)
> 接口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## enableStatusBar

```TypeScript
default enableStatusBar(enabled: boolean | undefined, animated?: boolean | undefined): this
```

设置进入该NavDestination后，显示或者隐藏系统的状态栏。

> **说明：**&gt;
> - 该属性满足如下全部条件时才生效：
> 
> 1. NavDestination属于应用主窗口页面，并且主窗口为全屏窗口；
> 
> 2. NavDestination所属的Navigation的大小占满整个页面；
> 
> 3. NavDestination的大小占满整个Navigation组件；
> 
> 4. NavDestination类型为[NavDestinationMode](arkts-arkui-navdestination-navdestinationmode-e.md).STANDARD。&gt;
> - 设置系统状态栏的实际效果依赖于具体的设备支持情况，具体参考窗口的
> [setSpecificSystemBarEnabled](arkts-arkui-window-window-i.md#setspecificsystembarenabled)
> 接口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |
| animated | boolean \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## fullScreenOverlay

```TypeScript
default fullScreenOverlay(fullScreenOverlay: boolean | undefined): this
```

设置NavDestination是否以全屏覆盖模式显示。当参数设置为true时，在Navigation分栏模式下，当前页面会覆盖整个Navigation容器，包括NavBar和内容区。该配置作用于当前NavDestination的所有实例；当路由栈中已有页面以全屏覆盖模式显示时，其后入 栈的[DIALOG](arkts-arkui-navdestination-navdestinationmode-e.md)页面与未设置fullScreenOverlay为false的[STANDARD](arkts-arkui-navdestination-navdestinationmode-e.md)页面也会继承为全屏覆盖显示 。未通过该接口设置时，NavDestination默认是普通显示模式，遵循Navigation分栏显示规则。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fullScreenOverlay](#fullscreenoverlay) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## hideBackButton

```TypeScript
default hideBackButton(hide: boolean | undefined): this
```

设置是否隐藏标题栏中的返回键。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hide | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## hideTitleBar

```TypeScript
default hideTitleBar(value: boolean | undefined): this
```

设置是否隐藏标题栏。

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
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## hideTitleBar

```TypeScript
default hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this
```

设置是否隐藏标题栏。与hideTitleBar相比，新增标题栏显隐 时是否使用动画。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hide | boolean \| undefined | 是 |
| animated | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## hideToolBar

```TypeScript
default hideToolBar(hide: boolean | undefined, animated?: boolean | undefined): this
```

设置是否隐藏工具栏。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hide | boolean \| undefined | 是 |
| animated | boolean \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## ignoreLayoutSafeArea

```TypeScript
default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this
```

控制组件的布局，使其扩展到非安全区域。

> **说明：**&gt;
> - 组件设置ignoreLayoutSafeArea之后生效的条件为：
> 
> 设置LayoutSafeAreaType.SYSTEM时，组件的边界与非安全区域重合时组件能够延伸到非安全区域下。&gt;
> - 若组件扩展到非安全区域内，此时在非安全区域里触发的事件（例如：点击事件）等可能会被系统拦截，优先响应状态栏等系统组件。&gt;
> - 组件想要扩展到非安全区域内，需隐藏或者设置标题栏和工具栏为[STACK](../arkts-components/arkts-arkui-barstyle-e.md)模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array&lt;[LayoutSafeAreaType](../arkts-components/arkts-arkui-layoutsafeareatype-e.md)&gt; \| undefined | 否 |
| edges | Array&lt;[LayoutSafeAreaEdge](../arkts-components/arkts-arkui-layoutsafeareaedge-e.md)&gt; \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## menus

```TypeScript
default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this
```


> **说明：**&gt;
> 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。
设置页面右上角菜单。不设置时不显示菜单项。使用 Array&lt;[NavigationMenuItem](../arkts-components/arkts-arkui-navigationmenuitem-i.md)&gt; 写法时，竖屏最多支持显示3个图 标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | Array&lt;[NavigationMenuItem](../arkts-components/arkts-arkui-navigationmenuitem-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| options | [NavigationMenuOptions](../arkts-components/arkts-arkui-navigationmenuoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## mode

```TypeScript
default mode(value: NavDestinationMode | undefined): this
```

设置NavDestination类型，不支持动态修改。

> **说明：**&gt;
> 从API version 12开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- API版本23+：SystemCapability.ArkUI.ArkUI.Full
- API版本23+：SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full *

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [NavDestinationMode](arkts-arkui-navdestination-navdestinationmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## onActive

```TypeScript
default onActive(callback: Callback<NavDestinationActiveReason> | undefined): this
```

NavDestination处于激活态（处于栈顶可操作，且上层无特殊组件遮挡）时，触发该回调。使用示例参见 示例5 。

> **说明：**&gt;
> 从API version 22开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[NavDestinationActiveReason](arkts-arkui-navdestination-navdestinationactivereason-e.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## onBackPressed

```TypeScript
default onBackPressed(callback: (() => boolean) | undefined): this
```

当与Navigation绑定的导航控制器中存在内容时，此回调生效。当点击返回键时，触发该回调。返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (() = & gt; boolean) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## onHidden

```TypeScript
default onHidden(callback: Callback<VisibilityChangeReason> | undefined): this
```

当该NavDestination页面隐藏时触发此回调。从API version 21开始，支持通过VisibilityChangeReason说明onHidden触发的原因。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[VisibilityChangeReason](arkts-arkui-navdestination-visibilitychangereason-e.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## onInactive

```TypeScript
default onInactive(callback: Callback<NavDestinationActiveReason> | undefined): this
```

NavDestination处于非激活态（处于非栈顶不可操作，或处于栈顶时上层有特殊组件遮挡）时，触发该回调。使用示例参见 示例5 。

> **说明：**&gt;
> 从API version 22开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[NavDestinationActiveReason](arkts-arkui-navdestination-navdestinationactivereason-e.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## onNewParam

```TypeScript
default onNewParam(callback: Callback<Object | null | undefined> | undefined): this
```

当之前存在于栈中的NavDestination页面通过 [launchMode.MOVE_TO_TOP_SINGLETON](../arkts-components/arkts-arkui-launchmode-e.md)或 [launchMode.POP_TO_SINGLETON](../arkts-components/arkts-arkui-launchmode-e.md)移动到栈顶时，触发该回调。

> **说明：**&gt;
> -
> [replacePath](../arkts-components/arkts-arkui-navpathstack-c.md#replacepath)
> 、[replaceDestination](../arkts-components/arkts-arkui-navpathstack-c.md#replacedestination)不会触发该回调。&gt;
> - 从API version 22开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;Object \| null \| undefined & gt; \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## onReady

```TypeScript
default onReady(callback: Callback<NavDestinationContext> | undefined): this
```

当NavDestination即将构建子组件之前会触发此回调。

> **说明：**&gt;
> 从API version 20开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[NavDestinationContext](arkts-arkui-navdestination-navdestinationcontext-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## onResult

```TypeScript
default onResult(callback: Callback<Object | null | undefined> | undefined): this
```

NavDestination返回时触发该回调。

> **说明：**&gt;
> 从API version 22开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;Object \| null \| undefined & gt; \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## onShown

```TypeScript
default onShown(callback: Callback<VisibilityChangeReason> | undefined): this
```

当该NavDestination页面显示时触发此回调。从API version 21开始，支持通过VisibilityChangeReason说明onShown触发的原因。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[VisibilityChangeReason](arkts-arkui-navdestination-visibilitychangereason-e.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## onWillAppear

```TypeScript
default onWillAppear(callback: VoidCallback | undefined): this
```

当该NavDestination挂载之前触发此回调。在该回调中允许修改路由栈，当前帧生效。

> **说明：**&gt;
> 从API version 20开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## onWillDisappear

```TypeScript
default onWillDisappear(callback: VoidCallback | undefined): this
```

当该NavDestination卸载之前触发的生命周期(有转场动画时，在转场动画开始之前触发)。

> **说明：**&gt;
> 从API version 20开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## onWillHide

```TypeScript
default onWillHide(callback: VoidCallback | undefined): this
```

当该NavDestination隐藏之前触发此回调。

> **说明：**&gt;
> 从API version 20开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## onWillShow

```TypeScript
default onWillShow(callback: VoidCallback | undefined): this
```

当该NavDestination显示之前触发此回调。

> **说明：**&gt;
> 从API version 20开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## preferredOrientation

```TypeScript
default preferredOrientation(orientation: Orientation | undefined): this
```

设置NavDestination对应的显示方向。转场到该NavDestination后，系统也会将应用主窗口切到该显示方向。

> **说明：**&gt;
> - 该属性满足如下全部条件时才有效：
> 
> 1. NavDestination属于应用主窗口页面，并且主窗口为全屏窗口；
> 
> 2. NavDestination所属的Navigation的大小占满整个应用页面；
> 
> 3. NavDestination类型为[NavDestinationMode](arkts-arkui-navdestination-navdestinationmode-e.md).STANDARD。&gt;
> - 设置显示方向的实际效果依赖于具体的设备支持情况，具体参考窗口的
> [setPreferredOrientation](arkts-arkui-window-window-i.md#setpreferredorientation)接
> 口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| orientation | [Orientation](arkts-arkui-orientation-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## recoverable

```TypeScript
default recoverable(recoverable: boolean | undefined): this
```

配置NavDestination是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建该NavDestination。该功能需NavDestination对应的Navigation也配置了 [可恢复属性](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#recoverable14)。

> **说明：**&gt;
> 该接口需要配合Navigation的
> [recoverable](#recoverable)接口使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [recoverable](#recoverable) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## setNavDestinationOptions

```TypeScript
default setNavDestinationOptions(moduleInfo?: NavDestinationModuleInfo): this
```

设置navDestination选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleInfo | [NavDestinationModuleInfo](arkts-arkui-navdestination-navdestinationmoduleinfo-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## systemBarStyle

```TypeScript
default systemBarStyle(style: SystemBarStyle | undefined): this
```

当Navigation中显示当前NavDestination时，设置对应系统状态栏的样式。

> **说明：**&gt;
> - 必须配合Navigation使用，作为其Navigation目的页面的根节点时才能生效。&gt;
> - 其他使用限制请参考Navigation对应的
> [systemBarStyle](#systembarstyle)属性说明。&gt;>
> - 从API version 20开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [SystemBarStyle](../arkts-components/arkts-arkui-systembarstyle-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## systemTransition

```TypeScript
default systemTransition(type: NavigationSystemTransitionType | undefined): this
```

设置NavDestination系统转场动画，支持分别设置系统标题栏动画和内容动画。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [NavigationSystemTransitionType](arkts-arkui-navdestination-navigationsystemtransitiontype-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## title

```TypeScript
default title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource | undefined, options?: NavigationTitleOptions | undefined): this
```

设置页面标题。字符串超长时，如果不设置副标题，先缩小再换行2行后以"..."截断。如果设置副标题，先缩小后以"..."截断。

> **说明：**&gt;
> 从API version 12开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [NavDestinationCommonTitle](arkts-arkui-navdestination-navdestinationcommontitle-i.md) \| [NavDestinationCustomTitle](arkts-arkui-navdestination-navdestinationcustomtitle-i.md) \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |
| options | [NavigationTitleOptions](../arkts-components/arkts-arkui-navigationtitleoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |

## toolbarConfiguration

```TypeScript
default toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this
```

设置工具栏内容。未调用本接口时不显示工具栏。

> **说明：**&gt;
> - 从API version 20开始，该接口支持在
> attributeModifier
> 中调用。&gt;
> - 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| toolbarParam | Array&lt;[ToolbarItem](../arkts-components/arkts-arkui-toolbaritem-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| options | [NavigationToolbarOptions](../arkts-components/arkts-arkui-navigationtoolbaroptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |
