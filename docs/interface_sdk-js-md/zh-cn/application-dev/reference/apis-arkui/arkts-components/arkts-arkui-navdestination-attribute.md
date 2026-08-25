# NavDestination属性/事件

支持通用属性。除支持通用事件外，还支持如下事件：

**继承/实现关系：** NavDestinationAttribute extends CommonMethod<NavDestinationAttribute>

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## backButtonIcon

```TypeScript
backButtonIcon(value: ResourceStr | PixelMap | SymbolGlyphModifier)
```

设置标题栏返回键图标。

> **说明：**

> - 从API version 12开始，该接口支持在attributeModifier中调用。&gt;
> - 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ResourceStr \| PixelMap \| [SymbolGlyphModifier](../arkts-apis/arkts-arkui-symbolglyphmodifier-c.md) | 是 |

## backButtonIcon

```TypeScript
backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier, accessibilityText?: ResourceStr)
```

设置标题栏返回键图标和无障碍播报内容。

> **说明：**

> - 该接口不支持在attributeModifier中调用。&gt;
> - 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| icon | ResourceStr \| PixelMap \| [SymbolGlyphModifier](../arkts-apis/arkts-arkui-symbolglyphmodifier-c.md) | 是 |
| accessibilityText | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | 否 |

## bindToNestedScrollable

```TypeScript
bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo>)
```

绑定NavDestination组件和嵌套的可滚动容器组件（支持List、Scroll、Grid、 WaterFlow），当滑动父组件或子组件时，会触发所有与其绑定的NavDestination组件的标题栏和工具栏的显示和隐藏动效，上滑隐藏，下滑显示。一个NavDestination可与多 个嵌套的可滚动容器组件绑定，嵌套的可滚动容器组件也可与多个NavDestination绑定。使用示例参见 [示例1](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#示例1标题栏工具栏与可滚动类组件联动)。

> **说明：**

> - 只有NavDestination的标题栏或工具栏设置为可见时，联动效果才会生效。&gt;
> - 当多个可滚动容器组件绑定了同一个NavDestination组件时，滚动任何一个容器都会触发标题栏和工具栏的显示或隐藏效果。且当任何一个可滚动容器组件滑动到底部或顶部位置时，会立即触发标题栏和工具栏的显示动效。因此，为了获
> 得最佳用户体验，不建议同时触发多个可滚动容器组件的滚动事件。&gt;
> - 从API version 22开始，该接口支持在attributeModifier中调用。

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为14。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scrollInfos | Array&lt;[NestedScrollInfo](arkts-arkui-nestedscrollinfo-i.md)&gt; | 是 |

## bindToScrollable

```TypeScript
bindToScrollable(scrollers: Array<Scroller>)
```

绑定NavDestination组件和可滚动容器组件（支持List、Scroll、Grid、 WaterFlow），当滑动可滚动容器组件时，会触发所有与其绑定的NavDestination组件的标题栏和工具栏的显示和隐藏动效，上滑隐藏，下滑显示。一个NavDestination可与多 个可滚动容器组件绑定，一个可滚动容器组件也可与多个NavDestination绑定。使用示例参见 [示例1](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#示例1标题栏工具栏与可滚动类组件联动)。

> **说明：**

> - 只有NavDestination的标题栏或工具栏设置为可见时，联动效果才会生效。&gt;
> - 当多个可滚动容器组件绑定了同一个NavDestination组件时，滚动任何一个容器都会触发标题栏和工具栏的显示或隐藏效果。且当任何一个可滚动容器组件滑动到底部或顶部位置时，会立即触发标题栏和工具栏的显示动效。因此，为了获
> 得最佳用户体验，不建议同时触发多个可滚动容器组件的滚动事件。&gt;
> - 从API version 22开始，该接口支持在attributeModifier中调用。

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为14。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scrollers | Array & lt;Scroller & gt; | 是 |

## customTransition

```TypeScript
customTransition(delegate: NavDestinationTransitionDelegate)
```

设置NavDestination自定义转场动画。

> **说明：**

> - 该接口不支持在attributeModifier中调用。&gt;
> - 该属性与[systemTransition](#systemtransition)同时设置时，后设置的属性生效。

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为15。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| delegate | [NavDestinationTransitionDelegate](arkts-arkui-navdestinationtransitiondelegate-t.md) | 是 |

## enableNavigationIndicator

```TypeScript
enableNavigationIndicator(enabled: Optional<boolean>)
```

设置进入该NavDestination后，显示或者隐藏系统的导航条。

> **说明：**

> 该属性满足如下全部条件时才生效：

> 设置系统导航条的实际效果依赖于具体的设备支持情况，具体参考窗口的
> [setSpecificSystemBarEnabled](../arkts-apis/arkts-arkui-window-window-i.md#setspecificsystembarenabled)
> 接口。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | Optional & lt;boolean & gt; | 是 |

## enableStatusBar

```TypeScript
enableStatusBar(enabled: Optional<boolean>, animated?: boolean)
```

设置进入该NavDestination后，显示或者隐藏系统的状态栏。

> **说明：**

> - 该属性满足如下全部条件时才生效：
> 
> 1. NavDestination属于应用主窗口页面，并且主窗口为全屏窗口；
> 
> 2. NavDestination所属的Navigation的大小占满整个页面；
> 
> 3. NavDestination的大小占满整个Navigation组件；
> 
> 4. NavDestination类型为[NavDestinationMode](arkts-arkui-navdestinationmode-e.md).STANDARD。&gt;
> - 设置系统状态栏的实际效果依赖于具体的设备支持情况，具体参考窗口的
> [setSpecificSystemBarEnabled](../arkts-apis/arkts-arkui-window-window-i.md#setspecificsystembarenabled)
> 接口。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | Optional & lt;boolean & gt; | 是 |
| animated | boolean | 否 |

## fullScreenOverlay

```TypeScript
fullScreenOverlay(fullScreenOverlay: Optional<boolean>)
```

设置NavDestination是否以全屏覆盖模式显示。当参数设置为true时，在Navigation分栏模式下，当前页面会覆盖整个Navigation容器，包括NavBar和内容区。该配置作用于当前NavDestination的所有实例；当路由栈中已有页面以全屏覆盖模式显示时，其后入 栈的[DIALOG](arkts-arkui-navdestinationmode-e.md)页面与未将fullScreenOverlay为false的[STANDARD](arkts-arkui-navdestinationmode-e.md)页面也会继承为全屏覆盖显 示。未通过该接口设置时，NavDestination默认是普通显示模式，遵循Navigation分栏显示规则。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fullScreenOverlay](#fullscreenoverlay) | Optional & lt;boolean & gt; | 是 |

## hideBackButton

```TypeScript
hideBackButton(hide: Optional<boolean>)
```

设置是否隐藏标题栏中的返回键。隐藏返回键后，用户可通过系统返回手势、[onBackPressed](#onbackpressed)回调或自定义导航按钮返回上一页面。适用于首页或不希望用户通过标准返回键返回的场景。

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为15。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hide | Optional & lt;boolean & gt; | 是 |

## hideTitleBar

```TypeScript
hideTitleBar(value: boolean)
```

设置是否隐藏标题栏。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## hideTitleBar

```TypeScript
hideTitleBar(hide: boolean, animated: boolean)
```

设置是否隐藏标题栏。与[hideTitleBar](#hidetitlebar)相比，新增标题栏显隐时是否使用动画。

**起始版本：** 13

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为13。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hide | boolean | 是 |
| animated | boolean | 是 |

## hideToolBar

```TypeScript
hideToolBar(hide: boolean, animated?: boolean)
```

设置是否隐藏工具栏。

**起始版本：** 13

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为13。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hide | boolean | 是 |
| animated | boolean | 否 |

## ignoreLayoutSafeArea

```TypeScript
ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>)
```

控制组件的布局，使其扩展到非安全区域。

> **说明：**

> - 组件设置ignoreLayoutSafeArea生效条件：设置LayoutSafeAreaType.SYSTEM时，若组件边界与非安全区域重合，组件可延伸到非安全区域内。&gt;
> - 若组件扩展到非安全区域内，此时在非安全区域里触发的事件（例如：点击事件）等可能会被系统拦截，优先响应状态栏等系统组件。&gt;
> - 组件想要扩展到非安全区域内，需隐藏或者设置标题栏和工具栏为STACK模式。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array & lt;LayoutSafeAreaType & gt; | 否 |
| edges | Array & lt;LayoutSafeAreaEdge & gt; | 否 |

## menus

```TypeScript
menus(value: Array<NavigationMenuItem> | CustomBuilder)
```

设置页面右上角菜单。不设置时不显示菜单项。使用Array&lt;NavigationMenuItem&gt; 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标 会被放入自动生成的更多图标。

&gt; **说明：**

> - 从API version 14开始，该接口支持在attributeModifier中调用。&gt;
> - 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array & lt;NavigationMenuItem & gt; \ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |

## menus

```TypeScript
menus(items: Array<NavigationMenuItem> | CustomBuilder, options?: NavigationMenuOptions)
```

设置页面右上角菜单。不设置时不显示菜单项。与 [menus](#menus)相比，新增菜单选项。使用Array&lt;NavigationMenuItem&gt; 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

&gt; **说明：**

> - 该接口不支持在attributeModifier中调用。&gt;
> - 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | Array & lt;NavigationMenuItem & gt; \ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |
| options | [NavigationMenuOptions](arkts-arkui-navigationmenuoptions-i.md) | 否 |

## mode

```TypeScript
mode(value: NavDestinationMode)
```

设置NavDestination类型，不支持动态修改。

> **说明：**

> 从API version 12开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [NavDestinationMode](arkts-arkui-navdestinationmode-e.md) | 是 |

## onActive

```TypeScript
onActive(callback: Optional<Callback<NavDestinationActiveReason>>)
```

NavDestination处于激活态（处于栈顶可操作，且上层无特殊组件遮挡）时，触发该回调。使用示例参见 [示例5](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#示例5navdestination的onactive与oninactive生命周期)。

> **说明：**

> 从API version 22开始，该接口支持在attributeModifier中调用。

**起始版本：** 17

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为17。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本17开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Optional&lt;Callback&lt;[NavDestinationActiveReason](arkts-arkui-navdestinationactivereason-e.md)&gt;&gt; | 是 |

## onBackPressed

```TypeScript
onBackPressed(callback: () => boolean)
```

当与Navigation绑定的导航控制器中存在内容时，此回调生效。当点击返回键时，触发该回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | () = & gt; boolean | 是 |

## onHidden

```TypeScript
onHidden(callback: Callback<VisibilityChangeReason>)
```

当该NavDestination页面隐藏时触发此回调。从API version 21开始，支持通过VisibilityChangeReason说明onHidden触发的原因。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback&lt;[VisibilityChangeReason](arkts-arkui-visibilitychangereason-e.md)&gt; | 是 |

## onInactive

```TypeScript
onInactive(callback: Optional<Callback<NavDestinationActiveReason>>)
```

NavDestination处于非激活态（处于非栈顶不可操作，或处于栈顶时上层有特殊组件遮挡）时，触发该回调。使用示例参见 [示例5](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#示例5navdestination的onactive与oninactive生命周期)。

> **说明：**

> 从API version 22开始，该接口支持在attributeModifier中调用。

**起始版本：** 17

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为17。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本17开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Optional&lt;Callback&lt;[NavDestinationActiveReason](arkts-arkui-navdestinationactivereason-e.md)&gt;&gt; | 是 |

## onNewParam

```TypeScript
onNewParam(callback: Optional<Callback<ESObject>>)
```

当之前存在于栈中的NavDestination页面通过launchMode.MOVE_TO_TOP_SINGLETON或 launchMode.POP_TO_SINGLETON移动到栈顶时，触发该回调。

> **说明：**

> - replacePath、
> replaceDestination不会触发该回调。&gt;
> - 从API version 22开始，该接口支持在attributeModifier中调用。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Optional & lt;Callback & lt;ESObject & gt; & gt; | 是 |

## onReady

```TypeScript
onReady(callback: import('../api/@ohos.base').Callback<NavDestinationContext>)
```

当NavDestination即将构建子组件之前会触发此回调。

> **说明：**

> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | import('../api/@ohos.base').Callback&lt;[NavDestinationContext](arkts-arkui-navdestinationcontext-i.md)&gt; | 是 |

## onRestoreState

```TypeScript
onRestoreState(callback: Optional<RestoreStateCallback>)
```

设置自定义页面状态恢复回调。当页面重构时触发。由onSaveState保存的自定义状态将传递给此回调。 如果没有保存自定义状态，则传递Null。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Optional&lt;[RestoreStateCallback](arkts-arkui-restorestatecallback-t.md)&gt; | 是 |

## onResult

```TypeScript
onResult(callback: Optional<Callback<ESObject>>)
```

NavDestination返回时触发该回调。

> **说明：**

> 从API version 22开始，该接口支持在attributeModifier中调用。

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为15。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Optional & lt;Callback & lt;ESObject & gt; & gt; | 是 |

## onSaveState

```TypeScript
onSaveState(callback: Optional<SaveStateCallback>)
```

设置自定义页面状态保存回调。当页面被隐藏时触发。保存自定义页面状态以备恢复。 用于创建页面的初始参数由导航单独保留。 状态对象必须是可序列化的。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Optional&lt;[SaveStateCallback](arkts-arkui-savestatecallback-t.md)&gt; | 是 |

## onShown

```TypeScript
onShown(callback: Callback<VisibilityChangeReason>)
```

当该NavDestination页面显示时触发此回调。从API version 21开始，支持通过VisibilityChangeReason说明onShown触发的原因。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback&lt;[VisibilityChangeReason](arkts-arkui-visibilitychangereason-e.md)&gt; | 是 |

## onWillAppear

```TypeScript
onWillAppear(callback: Callback<void>)
```

当该NavDestination挂载之前触发此回调。在该回调中允许修改路由栈，当前帧生效。

> **说明：**

> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback & lt;void & gt; | 是 |

## onWillDisappear

```TypeScript
onWillDisappear(callback: Callback<void>)
```

当该NavDestination卸载之前触发的生命周期(有转场动画时，在转场动画开始之前触发)。

> **说明：**

> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback & lt;void & gt; | 是 |

## onWillHide

```TypeScript
onWillHide(callback: Callback<void>)
```

当该NavDestination隐藏之前触发此回调。

> **说明：**

> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback & lt;void & gt; | 是 |

## onWillShow

```TypeScript
onWillShow(callback: Callback<void>)
```

当该NavDestination显示之前触发此回调。

> **说明：**

> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback & lt;void & gt; | 是 |

## preferredOrientation

```TypeScript
preferredOrientation(orientation: Optional<Orientation>)
```

设置NavDestination对应的显示方向。转场到该NavDestination后，系统也会将应用主窗口切到该显示方向。

> **说明：**

> - 该属性满足如下全部条件时才有效：
> 
> 1. NavDestination属于应用主窗口页面，并且主窗口为全屏窗口；
> 
> 2. NavDestination所属的Navigation的大小占满整个应用页面；
> 
> 3. NavDestination类型为[NavDestinationMode](arkts-arkui-navdestinationmode-e.md).STANDARD。&gt;
> - 设置显示方向的实际效果依赖于具体的设备支持情况，具体参考窗口的
> [setPreferredOrientation](../arkts-apis/arkts-arkui-window-window-i.md#setpreferredorientation)接
> 口。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| orientation | Optional&lt;[Orientation](arkts-arkui-orientation-t.md)&gt; | 是 |

## recoverable

```TypeScript
recoverable(recoverable: Optional<boolean>)
```

配置NavDestination是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建该NavDestination。该功能需NavDestination对应的Navigation也配置了 可恢复属性。

> **说明：**

> 该接口需要配合Navigation的recoverable接口使用。

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为14。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [recoverable](#recoverable) | Optional & lt;boolean & gt; | 是 |

## systemBarStyle

```TypeScript
systemBarStyle(style: Optional<SystemBarStyle>)
```

当Navigation中显示当前NavDestination时，设置对应系统状态栏的样式。

> **说明：**

> - 必须配合Navigation使用，作为其Navigation目的页面的根节点时才能生效。&gt;
> - 其他使用限制请参考Navigation对应的systemBarStyle属性说明。&gt;
> - 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | Optional & lt;SystemBarStyle & gt; | 是 |

## systemTransition

```TypeScript
systemTransition(type: NavigationSystemTransitionType)
```

设置NavDestination系统转场动画，支持分别设置系统标题栏动画和内容动画。该属性与customTransition同时设置时，后设置的属性生效。

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为14。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [NavigationSystemTransitionType](arkts-arkui-navigationsystemtransitiontype-e.md) | 是 |

## title

```TypeScript
title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource,
          options?: NavigationTitleOptions)
```

设置页面标题。字符串超长时，如果不设置副标题，先缩小再换行2行后以"..."截断。如果设置副标题，先缩小后以"..."截断。

> **说明：**

> 从API version 12开始，该接口支持在attributeModifier中调用。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| CustomBuilder \| [NavDestinationCommonTitle](arkts-arkui-navdestinationcommontitle-i.md) \| [NavDestinationCustomTitle](arkts-arkui-navdestinationcustomtitle-i.md) \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
| options | [NavigationTitleOptions](../arkts-apis/arkts-arkui-navigation-navigationtitleoptions-i.md) | 否 |

## toolbarConfiguration

```TypeScript
toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)
```

设置工具栏内容。未调用本接口时不显示工具栏。

> **说明：**

> - 从API version 20开始，该接口支持在attributeModifier中调用。&gt;
> - 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**起始版本：** 13

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为13。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| toolbarParam | Array & lt;ToolbarItem & gt; \ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |
| options | [NavigationToolbarOptions](../arkts-apis/arkts-arkui-navigation-navigationtoolbaroptions-i.md) | 否 |
