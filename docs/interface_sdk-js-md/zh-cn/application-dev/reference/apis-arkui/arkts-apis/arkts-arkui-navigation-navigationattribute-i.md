# NavigationAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** NavigationAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<NavigationAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置Navigation组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## backButtonIcon

```TypeScript
default backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this
```

设置标题栏中返回键图标和无障碍播报内容。

> **说明：**&gt;
> 不支持通过[SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md)对象的
> fontSize属性修改图标大小、
> effectStrategy属性修改
> 动效、symbolEffect属性修
> 改动效类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| icon | string \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| [SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md) \| undefined | 是 |
| accessibilityText | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## customNavContentTransition

```TypeScript
default customNavContentTransition(delegate: ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined) | undefined): this
```

自定义转场动画回调。取值为undefined时，不使用回调函数。

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
| delegate | ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) = & gt; NavigationAnimatedTransition \ | undefined) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## divider

```TypeScript
default divider(style: NavigationDividerStyle | null): this
```

设置Navigation双栏模式下的分割线样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [NavigationDividerStyle](arkts-arkui-navigation-navigationdividerstyle-i.md) \| null | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## enableDragBar

```TypeScript
default enableDragBar(isEnabled: boolean | undefined): this
```

控制分栏场景下是否显示拖拽条。该属性在PC/2in1设备上不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## enableModeChangeAnimation

```TypeScript
default enableModeChangeAnimation(isEnabled: boolean | undefined): this
```

控制是否开启单双栏切换时的动效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## enableToolBarAdaptation

```TypeScript
default enableToolBarAdaptation(enable: boolean | undefined): this
```

设置是否启用Navigation和NavDestination的工具栏[toolbarConfiguration](#toolbarconfiguration)自适应能力。关闭 此能力后，底部工具栏[toolbarConfiguration](#toolbarconfiguration)将不会再移动至页面右上角的菜单中。该接口不适配于自定义菜单，使用该 接口需采用[NavigationMenuItem](arkts-arkui-navigation-navigationmenuitem-i.md)接口来定义[菜单](#menus)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## enableVisibilityLifecycleWithContentCover

```TypeScript
default enableVisibilityLifecycleWithContentCover(isEnabled: boolean | undefined): this
```

设置是否启用NavDestination页面 onHidden、 onShown生命周期与全模态的联动触发。

> **说明：**&gt;
> 从API version 23开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## hideBackButton

```TypeScript
default hideBackButton(value: boolean | undefined): this
```

设置是否隐藏标题栏中的返回键。返回键仅在[titleMode](#titlemode)设置为NavigationTitleMode.Mini时才生效。

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
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## hideNavBar

```TypeScript
default hideNavBar(value: boolean | undefined): this
```

设置是否隐藏导航页。设置为true时，隐藏Navigation的导航页，包括标题栏、内容区和工具栏。如果此时路由栈中存在NavDestination页面，则直接显示栈顶NavDestination页面，反之显示空白。从API version 9开始到API version 10仅在双栏模式下生效。从API version 11开始在单栏、双栏与自适应模式均生效。

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
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## hideTitleBar

```TypeScript
default hideTitleBar(value: boolean | undefined): this
```

Hide navigation title bar

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
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## hideTitleBar

```TypeScript
default hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this
```

设置是否隐藏标题栏。与 hideTitleBar 相比，新增标题栏显隐时是否使用动画。

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
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## hideToolBar

```TypeScript
default hideToolBar(value: boolean | undefined): this
```

Hide tool bar

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
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## hideToolBar

```TypeScript
default hideToolBar(hide: boolean | undefined, animated: boolean | undefined): this
```

设置是否隐藏工具栏。与 hideToolBar 相比，新增工具栏显隐时是否使用动画。

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
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

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
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## menus

```TypeScript
default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this
```

设置页面右上角菜单。不设置时不显示菜单项。使用Array&lt;[NavigationMenuItem](arkts-arkui-navigation-navigationmenuitem-i.md)&gt; 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的 图标会被放入自动生成的更多图标。

&gt; **说明：**&gt;
> 不支持通过[SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md)对象的
> fontSize属性修改图标大小、
> effectStrategy属性修改
> 动效、symbolEffect属性修
> 改动效类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | Array&lt;[NavigationMenuItem](arkts-arkui-navigation-navigationmenuitem-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| options | [NavigationMenuOptions](arkts-arkui-navigation-navigationmenuoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## minContentWidth

```TypeScript
default minContentWidth(value: Dimension | undefined): this
```

设置导航页内容区最小宽度（双栏模式下生效）。

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
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## mode

```TypeScript
default mode(value: NavigationMode | undefined): this
```

设置导航页的显示模式，支持单栏（Stack）、分栏（Split）和自适应（Auto）。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [NavigationMode](arkts-arkui-navigation-navigationmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## navBarPosition

```TypeScript
default navBarPosition(value: NavBarPosition | undefined): this
```

设置导航页位置。仅在[mode](#mode)设置为NavigationMode.Auto或NavigationMode.Split时生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [NavBarPosition](arkts-arkui-navigation-navbarposition-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## navBarWidth

```TypeScript
default navBarWidth(value: Length | Bindable<Length> | undefined): this
```

设置导航页宽度。仅在[mode](#mode)设置为NavigationMode.Auto或NavigationMode.Split时生效。从API version 18开始，该参数支持[!!](../../../ui/state-management/arkts-new-binding.md)双向绑定变量。

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
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## navBarWidthRange

```TypeScript
default navBarWidthRange(value: [
        Dimension,
        Dimension
    ] | undefined): this
```

设置导航页最小和最大宽度（双栏模式下生效）。未设置该接口时，最小宽度默认为240vp，最大宽度默认为组件宽度的40%，且不大于432vp，即导航页和内容区之间的分割线可以在此范围内进行拖拽。拖拽分割线使导航页宽度变化时，内容区 的内容会被压缩。分割线的拖拽范围：  
| 条件| 拖拽范围 | | ----| ----------- | |navBarWidthRange和minContentWidth同时设置 | 满足minContentWidth所设置的值后，在navBarWidthRange所设置的范围内进行拖拽 | |navBarWidthRange和minContentWidth均不设置 | 在navBarWidthRange默认的最小和最大范围内进行拖拽 | |仅设置navBarWidthRange属性 | 在navBarWidthRange所设置的范围内进行拖拽，最大拖拽范围不能超过minContentWidth的默认值 | |仅设置minContentWidth属性 | 在navBarWidthRange默认的最小和最大范围内进行拖拽 | |仅设置navBarWidth属性 |

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [         Dimension,         Dimension     ] \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## navDestination

```TypeScript
default navDestination(builder: PageMapBuilder | undefined): this
```

创建NavDestination组件。使用builder函数，基于name和param构造NavDestination组件。builder下只能有一个根节点。builder中允许在NavDestination组件外包含一层自定 义组件， 但自定义组件不允许设置属性和事件，否则仅显示空白。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [PageMapBuilder](arkts-arkui-pagemapbuilder-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## onNavBarStateChange

```TypeScript
default onNavBarStateChange(callback: ((isVisible: boolean) => void) | undefined): this
```

导航页显示状态切换时触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((isVisible: boolean) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## onNavigationModeChange

```TypeScript
default onNavigationModeChange(callback: ((mode: NavigationMode) => void) | undefined): this
```

当Navigation首次显示或者单双栏状态发生变化时触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((mode: NavigationMode) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## onTitleModeChange

```TypeScript
default onTitleModeChange(callback: ((titleMode: NavigationTitleMode) => void) | undefined): this
```

当[titleMode](#titlemode)为NavigationTitleMode.Free时，随着可滚动组件的滑动标题栏模式发生变化时触发此回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((titleMode: NavigationTitleMode) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## recoverable

```TypeScript
default recoverable(recoverable: boolean | undefined): this
```

配置Navigation是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建该Navigation，并恢复至异常退出时的路由栈。

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
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## setNavigationOptions

```TypeScript
default setNavigationOptions(pathInfos?: NavPathStack, homeDestination?: HomePathInfo, moduleInfo?: NavigationModuleInfo): this
```

设置Navigation配置项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | 否 |
| homeDestination | [HomePathInfo](arkts-arkui-navigation-homepathinfo-i.md) | 否 |
| moduleInfo | [NavigationModuleInfo](arkts-arkui-navigation-navigationmoduleinfo-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## setNavigationOptions

```TypeScript
default setNavigationOptions(pathInfos?: NavPathStack,  moduleInfo?: NavigationModuleInfo): this
```

设置导航选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | 否 |
| moduleInfo | [NavigationModuleInfo](arkts-arkui-navigation-navigationmoduleinfo-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## splitPlaceholder

```TypeScript
default splitPlaceholder<T extends Object>(placeholder: ComponentContent<T>): this
```

Navigation双栏模式下，支持设置右侧页面显示默认占位页，占位页仅作为UI展示页，不可获焦和响应事件。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| placeholder | ComponentContent & lt;T & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## systemBarStyle

```TypeScript
default systemBarStyle(style: SystemBarStyle | undefined): this
```

当Navigation中显示Navigation首页时，设置对应系统状态栏的样式。

> **说明：**&gt;>
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
| style | [SystemBarStyle](arkts-arkui-systembarstyle-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## title

```TypeScript
default title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle | undefined, options?: NavigationTitleOptions | undefined): this
```

设置页面标题。

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
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [NavigationCommonTitle](arkts-arkui-navigation-navigationcommontitle-i.md) \| [NavigationCustomTitle](arkts-arkui-navigation-navigationcustomtitle-i.md) \| undefined | 是 |
| options | [NavigationTitleOptions](arkts-arkui-navigation-navigationtitleoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## titleMode

```TypeScript
default titleMode(value: NavigationTitleMode | undefined): this
```

设置页面标题栏显示模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [NavigationTitleMode](arkts-arkui-navigation-navigationtitlemode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |

## toolbarConfiguration

```TypeScript
default toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this
```

设置工具栏内容。不设置时不显示工具栏。

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
| value | Array&lt;[ToolbarItem](arkts-arkui-navigation-toolbaritem-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| options | [NavigationToolbarOptions](arkts-arkui-navigation-navigationtoolbaroptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) |
