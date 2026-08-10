# NavigationAttribute

除支持[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)外，还支持以下属性：

**Inheritance/Implementation:** NavigationAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavigationAttribute extends CommonMethod--><!--Device-unnamed-export declare interface NavigationAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<NavigationAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置Navigation组件的属性方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default attributeModifier(modifier: AttributeModifier<NavigationAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-NavigationAttribute-default attributeModifier(modifier: AttributeModifier<NavigationAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;NavigationAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | 在当前组件上 ，动态设置属性方法，支持使用if/else语法。&lt;br/&gt;CommonMethod：通用属性和事件。&lt;br/&gt;取值为undefined时，按当前组件的属性方法默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backButtonIcon

```TypeScript
default backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this
```

设置标题栏中返回键图标和无障碍播报内容。

> **说明：**
> 
> 不支持通过[SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md/arkts-arkui-symbolglyphmodifier-t.md)对象的
> [fontSize](../../../reference/apis-arkui/arkui-ts/ts-basic-components-symbolGlyph.md#fontsize)属性修改图标大小、
> [effectStrategy](../../../reference/apis-arkui/arkui-ts/ts-basic-components-symbolGlyph.md#effectstrategy)属性修改
> 动效、[symbolEffect](../../../reference/apis-arkui/arkui-ts/ts-basic-components-symbolGlyph.md#symboleffect12)属性修
> 改动效类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this--><!--Device-NavigationAttribute-default backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | string \| PixelMap \| Resource \| SymbolGlyphModifier \| undefined | Yes | 标题栏中返回键图标。&lt;br/&gt;取值为undefined时，显示返回键图标。 |
| accessibilityText | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | No | 需要播报的内容。&lt;br/&gt;取值为undefined时，无播报内容。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## customNavContentTransition

```TypeScript
default customNavContentTransition(delegate: ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined) | undefined): this
```

自定义转场动画回调。取值为undefined时，不使用回调函数。

> **说明：**
> 
> 从API version 20开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default customNavContentTransition(delegate: ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined) | undefined): this--><!--Device-NavigationAttribute-default customNavContentTransition(delegate: ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delegate | ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) =&gt; NavigationAnimatedTransition \| undefined) \| undefined | Yes | 自定义转场动画的回调函数。&lt;br/&gt;from：退场Destination的页面信息。&lt;br/&gt;to：进场Destination的页面信息。&lt; br/&gt;operation：当前页面转场的类型。&lt;br/&gt;当回调函数返回[NavigationAnimatedTransition](../arkts-components/arkts-arkui-navigationanimatedtransition-i.md/arkts-arkui-navigationanimatedtransition-i.md)时，表示自定义 转场动画协议；返回undefined时表示未定义，执行默认转场动效。 &lt;br/&gt;取值为undefined时，不使用自定义转场动画回调函数，执行默认转场动效。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## divider

```TypeScript
default divider(style: NavigationDividerStyle | null): this
```

设置Navigation双栏模式下的分割线样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default divider(style: NavigationDividerStyle | null): this--><!--Device-NavigationAttribute-default divider(style: NavigationDividerStyle | null): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [NavigationDividerStyle](arkts-arkui-navigation-navigationdividerstyle-i.md) \| null | Yes | navigation divider style in split mode.<br>**Since:** 23 - 24 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回Navigation属性对象 |

## enableDragBar

```TypeScript
default enableDragBar(isEnabled: boolean | undefined): this
```

控制分栏场景下是否显示拖拽条。该属性在PC/2in1设备上不生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default enableDragBar(isEnabled: boolean | undefined): this--><!--Device-NavigationAttribute-default enableDragBar(isEnabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes | 是否开启拖拽条，默认为无拖拽条样式。&lt;br/&gt;true：有拖拽条样式；false：无拖拽条样式。&lt;br/&gt;参数非法或为undefined时， 按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## enableModeChangeAnimation

```TypeScript
default enableModeChangeAnimation(isEnabled: boolean | undefined): this
```

控制是否开启单双栏切换时的动效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default enableModeChangeAnimation(isEnabled: boolean | undefined): this--><!--Device-NavigationAttribute-default enableModeChangeAnimation(isEnabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes | 是否开启单双栏切换动效。&lt;br/&gt;默认值：true&lt;br/&gt;true：开启单双栏切换动效；false：关闭单双栏切换动效。&lt;br/&gt;参数非法 或为undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## enableToolBarAdaptation

```TypeScript
default enableToolBarAdaptation(enable: boolean | undefined): this
```

设置是否启用Navigation和NavDestination的工具栏[toolbarConfiguration](NavigationAttribute.toolbarConfiguration)自适应能力。关闭此能力后，底部工具栏[toolbarConfiguration](NavigationAttribute.toolbarConfiguration)将不会再移动至页面右上角的菜单中。该接口不适配于自定义菜单，使用该接口需采用[NavigationMenuItem](../arkts-components/arkts-arkui-navigationmenuitem-i.md/arkts-arkui-navigationmenuitem-i.md)接口来定义[菜单](NavigationAttribute.menus)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default enableToolBarAdaptation(enable: boolean | undefined): this--><!--Device-NavigationAttribute-default enableToolBarAdaptation(enable: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes | 是否启用Navigation和NavDestination的工具栏自适应能力。&lt;br/&gt;默认值：true&lt;br/&gt;true：启用 Navigation和NavDestination的工具栏自适应能力。&lt;br/&gt;false：不启用Navigation和NavDestination的工具栏自适应能力。&lt;br/&gt;参数非法或为undefined时，按默认 值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableVisibilityLifecycleWithContentCover

```TypeScript
default enableVisibilityLifecycleWithContentCover(isEnabled: boolean | undefined): this
```

设置是否启用[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面  
[onHidden](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#onhidden10)、  
[onShown](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#onshown10)生命周期与全模态的联动触发。

> **说明：**
> 
> 从API version 23开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default enableVisibilityLifecycleWithContentCover(isEnabled: boolean | undefined): this--><!--Device-NavigationAttribute-default enableVisibilityLifecycleWithContentCover(isEnabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes | 是否启用NavDestination页面onShown、onHidden生命周期与全模态的联动触发。&lt;br/&gt;默认值：true&lt;br/&gt; true：全模态拉起时，会触发当前NavDestination页面的onHidden生命周期；全模态关闭时会触发当前NavDestination页面的onShown生命周期&lt;br/&gt;false： NavDestination页面onHidden、onShown生命周期不会因为全模态的拉起、关闭而触发。&lt;br/&gt;取值为undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## hideBackButton

```TypeScript
default hideBackButton(value: boolean | undefined): this
```

设置是否隐藏标题栏中的返回键。返回键仅在[titleMode](NavigationAttribute.titleMode)设置为NavigationTitleMode.Mini时才生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default hideBackButton(value: boolean | undefined): this--><!--Device-NavigationAttribute-default hideBackButton(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hideNavBar

```TypeScript
default hideNavBar(value: boolean | undefined): this
```

设置是否隐藏导航页。设置为true时，隐藏Navigation的导航页，包括标题栏、内容区和工具栏。如果此时路由栈中存在NavDestination页面，则直接显示栈顶NavDestination页面，反之显示空白。

从API version 9开始到API version 10仅在双栏模式下生效。从API version 11开始在单栏、双栏与自适应模式均生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default hideNavBar(value: boolean | undefined): this--><!--Device-NavigationAttribute-default hideNavBar(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hideTitleBar

```TypeScript
default hideTitleBar(value: boolean | undefined): this
```

Hide navigation title bar

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default hideTitleBar(value: boolean | undefined): this--><!--Device-NavigationAttribute-default hideTitleBar(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hideTitleBar

```TypeScript
default hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this
```

设置是否隐藏标题栏。与  
[hideTitleBar](NavigationAttribute.default hideTitleBar(hide: boolean | undefined, animated: boolean | undefined))相比，新增标题栏显隐时是否使用动画。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this--><!--Device-NavigationAttribute-default hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hide | boolean \| undefined | Yes |  |
| animated | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hideToolBar

```TypeScript
default hideToolBar(value: boolean | undefined): this
```

Hide tool bar

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default hideToolBar(value: boolean | undefined): this--><!--Device-NavigationAttribute-default hideToolBar(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hideToolBar

```TypeScript
default hideToolBar(hide: boolean | undefined, animated: boolean | undefined): this
```

设置是否隐藏工具栏。与  
[hideToolBar](NavigationAttribute.default hideToolBar(hide: boolean | undefined, animated: boolean | undefined))相比，新增工具栏显隐时是否使用动画。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default hideToolBar(hide: boolean | undefined, animated: boolean | undefined): this--><!--Device-NavigationAttribute-default hideToolBar(hide: boolean | undefined, animated: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hide | boolean \| undefined | Yes |  |
| animated | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
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
> - 组件想要扩展到非安全区域内，需隐藏或者设置标题栏和工具栏为[STACK](../arkts-components/arkts-arkui-barstyle-e.md/arkts-arkui-barstyle-e.md)模式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this--><!--Device-NavigationAttribute-default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;[LayoutSafeAreaType](../arkts-components/arkts-arkui-layoutsafeareatype-e.md)&gt; \| undefined | No | 配置扩展安全区域的类型。&lt;br/&gt;取值为undefined时，按默认值处理。&lt;br /&gt;默认值：&lt;br /&gt; [LayoutSafeAreaType.SYSTEM] |
| edges | Array&lt;[LayoutSafeAreaEdge](../arkts-components/arkts-arkui-layoutsafeareaedge-e.md)&gt; \| undefined | No | 配置扩展安全区域的方向。&lt;br/&gt;取值为undefined时，按默认值处理。&lt;br /&gt; 默认值：&lt;br / &gt;[LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM]。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## menus

```TypeScript
default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this
```

设置页面右上角菜单。不设置时不显示菜单项。使用Array&lt;[NavigationMenuItem](../arkts-components/arkts-arkui-navigationmenuitem-i.md/arkts-arkui-navigationmenuitem-i.md)&gt; 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

&gt; **说明：**
> 
> 不支持通过[SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md/arkts-arkui-symbolglyphmodifier-t.md)对象的
> [fontSize](../../../reference/apis-arkui/arkui-ts/ts-basic-components-symbolGlyph.md#fontsize)属性修改图标大小、
> [effectStrategy](../../../reference/apis-arkui/arkui-ts/ts-basic-components-symbolGlyph.md#effectstrategy)属性修改
> 动效、[symbolEffect](../../../reference/apis-arkui/arkui-ts/ts-basic-components-symbolGlyph.md#symboleffect12)属性修
> 改动效类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this--><!--Device-NavigationAttribute-default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | Array&lt;NavigationMenuItem&gt; \| CustomBuilder \| undefined | Yes |  |
| options | [NavigationMenuOptions](../arkts-components/arkts-arkui-navigationmenuoptions-i.md) \| undefined | No | 菜单选项。&lt;br/&gt;取值为undefined时，按NavigationMenuOptions中的默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## minContentWidth

```TypeScript
default minContentWidth(value: Dimension | undefined): this
```

设置导航页内容区最小宽度（双栏模式下生效）。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default minContentWidth(value: Dimension | undefined): this--><!--Device-NavigationAttribute-default minContentWidth(value: Dimension | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes | 导航页内容区最小宽度。&lt;br/&gt;默认值：360&lt;br/&gt;单位：vp&lt;br/&gt;取值为undefined时，按默认值处理。&lt;br/&gt;Auto模式断点 计算：默认600vp，minNavBarWidth(240vp) + minContentWidth (360vp) |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## mode

```TypeScript
default mode(value: NavigationMode | undefined): this
```

设置导航页的显示模式，支持单栏（Stack）、分栏（Split）和自适应（Auto）。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default mode(value: NavigationMode | undefined): this--><!--Device-NavigationAttribute-default mode(value: NavigationMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NavigationMode](arkts-arkui-navigation-navigationmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## navBarPosition

```TypeScript
default navBarPosition(value: NavBarPosition | undefined): this
```

设置导航页位置。仅在[mode](NavigationAttribute.mode)设置为NavigationMode.Auto或NavigationMode.Split时生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default navBarPosition(value: NavBarPosition | undefined): this--><!--Device-NavigationAttribute-default navBarPosition(value: NavBarPosition | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NavBarPosition](arkts-arkui-navigation-navbarposition-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## navBarWidth

```TypeScript
default navBarWidth(value: Length | Bindable<Length> | undefined): this
```

设置导航页宽度。仅在[mode](NavigationAttribute.mode)设置为NavigationMode.Auto或NavigationMode.Split时生效。

从API version 18开始，该参数支持[!!](../../../ui/state-management/arkts-new-binding.md)双向绑定变量。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default navBarWidth(value: Length | Bindable<Length> | undefined): this--><!--Device-NavigationAttribute-default navBarWidth(value: Length | Bindable<Length> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| Bindable&lt;[Length](arkts-arkui-length-t.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## navBarWidthRange

```TypeScript
default navBarWidthRange(value: [
        Dimension,
        Dimension
    ] | undefined): this
```

设置导航页最小和最大宽度（双栏模式下生效）。未设置该接口时，最小宽度默认为240vp，最大宽度默认为组件宽度的40%，且不大于432vp，即导航页和内容区之间的分割线可以在此范围内进行拖拽。拖拽分割线使导航页宽度变化时，内容区的内容会被压缩。

分割线的拖拽范围：

| 条件| 拖拽范围 |  
| ----| ----------- |  
|navBarWidthRange和minContentWidth同时设置 | 满足minContentWidth所设置的值后，在navBarWidthRange所设置的范围内进行拖拽 |  
|navBarWidthRange和minContentWidth均不设置 | 在navBarWidthRange默认的最小和最大范围内进行拖拽 |  
|仅设置navBarWidthRange属性 | 在navBarWidthRange所设置的范围内进行拖拽，最大拖拽范围不能超过minContentWidth的默认值 |  
|仅设置minContentWidth属性 | 在navBarWidthRange默认的最小和最大范围内进行拖拽 |  
|仅设置navBarWidth属性 | 不支持拖拽 |

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default navBarWidthRange(value: [        Dimension,        Dimension    ] | undefined): this--><!--Device-NavigationAttribute-default navBarWidthRange(value: [        Dimension,        Dimension    ] | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [         Dimension,         Dimension     ] \| undefined | Yes | 导航页最小和最大宽度。&lt;br/&gt;参数非法或为undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## navDestination

```TypeScript
default navDestination(builder: PageMapBuilder | undefined): this
```

创建NavDestination组件。使用builder函数，基于name和param构造NavDestination组件。builder下只能有一个根节点。builder中允许在NavDestination组件外包含一层自定义组件， 但自定义组件不允许设置属性和事件，否则仅显示空白。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default navDestination(builder: PageMapBuilder | undefined): this--><!--Device-NavigationAttribute-default navDestination(builder: PageMapBuilder | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [PageMapBuilder](arkts-arkui-pagemapbuilder-t.md) \| undefined | Yes | 创建NavDestination组件。name：NavDestination页面名称。param：开发者设置的 NavDestination页面详细参数，unknown可以是用户自定义的类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## onNavBarStateChange

```TypeScript
default onNavBarStateChange(callback: ((isVisible: boolean) => void) | undefined): this
```

导航页显示状态切换时触发该回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default onNavBarStateChange(callback: ((isVisible: boolean) => void) | undefined): this--><!--Device-NavigationAttribute-default onNavBarStateChange(callback: ((isVisible: boolean) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((isVisible: boolean) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onNavigationModeChange

```TypeScript
default onNavigationModeChange(callback: ((mode: NavigationMode) => void) | undefined): this
```

当Navigation首次显示或者单双栏状态发生变化时触发该回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default onNavigationModeChange(callback: ((mode: NavigationMode) => void) | undefined): this--><!--Device-NavigationAttribute-default onNavigationModeChange(callback: ((mode: NavigationMode) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((mode: NavigationMode) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onTitleModeChange

```TypeScript
default onTitleModeChange(callback: ((titleMode: NavigationTitleMode) => void) | undefined): this
```

当[titleMode](NavigationAttribute.titleMode)为NavigationTitleMode.Free时，随着可滚动组件的滑动标题栏模式发生变化时触发此回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default onTitleModeChange(callback: ((titleMode: NavigationTitleMode) => void) | undefined): this--><!--Device-NavigationAttribute-default onTitleModeChange(callback: ((titleMode: NavigationTitleMode) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((titleMode: NavigationTitleMode) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## recoverable

```TypeScript
default recoverable(recoverable: boolean | undefined): this
```

配置Navigation是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建该Navigation，并恢复至异常退出时的路由栈。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default recoverable(recoverable: boolean | undefined): this--><!--Device-NavigationAttribute-default recoverable(recoverable: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recoverable | boolean \| undefined | Yes | Navigation是否可恢复，默认为不可恢复。&lt;br/&gt;true：路由栈可恢复；false：路由栈不可恢复。&lt;br/&gt;参数非法或为 undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## setNavigationOptions

```TypeScript
default setNavigationOptions(pathInfos?: NavPathStack, homeDestination?: HomePathInfo, moduleInfo?: NavigationModuleInfo): this
```

设置Navigation配置项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default setNavigationOptions(pathInfos?: NavPathStack, homeDestination?: HomePathInfo, moduleInfo?: NavigationModuleInfo): this--><!--Device-NavigationAttribute-default setNavigationOptions(pathInfos?: NavPathStack, homeDestination?: HomePathInfo, moduleInfo?: NavigationModuleInfo): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | No | Navigation页面栈。 |
| homeDestination | [HomePathInfo](arkts-arkui-navigation-homepathinfo-i.md) | No | 自定义Navigation首页信息。 |
| moduleInfo | [NavigationModuleInfo](arkts-arkui-navigation-navigationmoduleinfo-i.md) | No | 导航的页面路径和模块信息 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回导航属性的实例。 |

## setNavigationOptions

```TypeScript
default setNavigationOptions(pathInfos?: NavPathStack,  moduleInfo?: NavigationModuleInfo): this
```

设置导航选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default setNavigationOptions(pathInfos?: NavPathStack,  moduleInfo?: NavigationModuleInfo): this--><!--Device-NavigationAttribute-default setNavigationOptions(pathInfos?: NavPathStack,  moduleInfo?: NavigationModuleInfo): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | No | 导航栈 |
| moduleInfo | [NavigationModuleInfo](arkts-arkui-navigation-navigationmoduleinfo-i.md) | No | 导航的pageInfo和模块信息 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回导航属性的实例。 |

## splitPlaceholder

```TypeScript
default splitPlaceholder<T extends Object>(placeholder: ComponentContent<T>): this
```

Navigation双栏模式下，支持设置右侧页面显示默认占位页，占位页仅作为UI展示页，不可获焦和响应事件。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default splitPlaceholder<T extends Object>(placeholder: ComponentContent<T>): this--><!--Device-NavigationAttribute-default splitPlaceholder<T extends Object>(placeholder: ComponentContent<T>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| placeholder | [ComponentContent](../arkts-components/arkts-arkui-componentcontent-t.md)&lt;T&gt; | Yes | 设置Navigation双栏模式下右侧的默认占位页。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## systemBarStyle

```TypeScript
default systemBarStyle(style: SystemBarStyle | undefined): this
```

当Navigation中显示Navigation首页时，设置对应系统状态栏的样式。

> **说明：**
> 
> 
> 从API version 20开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default systemBarStyle(style: SystemBarStyle | undefined): this--><!--Device-NavigationAttribute-default systemBarStyle(style: SystemBarStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [SystemBarStyle](../arkts-components/arkts-arkui-systembarstyle-t.md) \| undefined | Yes | 系统状态栏样式。&lt;br/&gt;取值为undefined时，无样式。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## title

```TypeScript
default title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle | undefined, options?: NavigationTitleOptions | undefined): this
```

设置页面标题。

> **说明：**
> 
> 从API version 12开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle | undefined, options?: NavigationTitleOptions | undefined): this--><!--Device-NavigationAttribute-default title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle | undefined, options?: NavigationTitleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| CustomBuilder \| NavigationCommonTitle \| NavigationCustomTitle \| undefined | Yes |  |
| options | [NavigationTitleOptions](arkts-arkui-navigation-navigationtitleoptions-i.md) \| undefined | No | 标题栏选项。 包含标题栏背景颜色、标题栏背景模糊样式及模糊选项、标题栏背景属性、标题栏布局方式、标题栏起始端内 间距、标题栏结束端内间距、主标题属性修改器、子标题属性修改器、是否响应悬停态。&lt;br/&gt;取值为undefined时，按NavigationTitleOptions中的默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## titleMode

```TypeScript
default titleMode(value: NavigationTitleMode | undefined): this
```

设置页面标题栏显示模式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default titleMode(value: NavigationTitleMode | undefined): this--><!--Device-NavigationAttribute-default titleMode(value: NavigationTitleMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NavigationTitleMode](arkts-arkui-navigation-navigationtitlemode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## toolbarConfiguration

```TypeScript
default toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this
```

设置工具栏内容。不设置时不显示工具栏。

> **说明：**
> 
> 从API version 20开始，该接口支持在
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> 中调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this--><!--Device-NavigationAttribute-default toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;ToolbarItem&gt; \| CustomBuilder \| undefined | Yes | 工具栏内容，使用Array&lt;[ToolbarItem](../arkts-components/arkts-arkui-toolbaritem-i.md/arkts-arkui-toolbaritem-i.md)&gt; 设置的工具栏有如下特性：&lt;br/&gt;工具栏所有选项均分底部工具栏，在每个均分内容区布局文本和图标。&lt;br/&gt;竖屏模式最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。横屏模式时，如果为 [Split](../arkts-components/arkts-arkui-navigationmode-e.md/arkts-arkui-navigationmode-e.md)模式，仍按照竖屏模式显示，如果为[Stack](../arkts-components/arkts-arkui-navigationmode-e.md/arkts-arkui-navigationmode-e.md)模式需配合menus属性的Array&lt; [NavigationMenuItem](../arkts-components/arkts-arkui-navigationmenuitem-i.md/arkts-arkui-navigationmenuitem-i.md)&gt;使用，底部工具栏会自动隐藏，同时底部工具栏所有选项移动至页面右上角菜单。&lt;br/&gt;使用 [CustomBuilder](../../../reference/apis-arkui/arkui-ts/ts-types.md#custombuilder8)写法为用户自定义工具栏选项，不具备以上功能。&lt;br/ &gt;取值为undefined时，无工具栏。 |
| options | [NavigationToolbarOptions](arkts-arkui-navigation-navigationtoolbaroptions-i.md) \| undefined | No | 工具栏选项。 包含工具栏背景颜色、工具栏背景模糊样式及模糊选项、工具栏背景属性、工具栏布局方式、是否隐藏工 具栏的文本、工具栏更多图标的菜单选项。&lt;br/&gt;取值为undefined时，按NavigationToolbarOptions中的默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

