# NavigationAttribute

Declare Navigation view properties.

**Inheritance/Implementation:** NavigationAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavigationAttribute extends CommonMethod--><!--Device-unnamed-export declare interface NavigationAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<NavigationAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of navigation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default attributeModifier(modifier: AttributeModifier<NavigationAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-NavigationAttribute-default attributeModifier(modifier: AttributeModifier<NavigationAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;NavigationAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | The attribute modifier of navigation. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backButtonIcon

```TypeScript
default backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this
```

Sets the back button icon and accessibility broadcast content.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this--><!--Device-NavigationAttribute-default backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | string \| PixelMap \| Resource \| SymbolGlyphModifier \| undefined | Yes | Indicates icon of back button |
| accessibilityText | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | No | Indicates content needs to broadcast. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## configuration

```TypeScript
default configuration(config: NavigationConfiguration | undefined): this
```

Sets Navigation configuration.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default configuration(config: NavigationConfiguration | undefined): this--><!--Device-NavigationAttribute-default configuration(config: NavigationConfiguration | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [NavigationConfiguration](../arkts-components/arkts-arkui-navigationconfiguration-i.md) \| undefined | Yes | Navigation configuration options. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns instance of NavigationAttribute. |

## customNavContentTransition

```TypeScript
default customNavContentTransition(delegate: ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined) | undefined): this
```

Set custom navigation content transition animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default customNavContentTransition(delegate: ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined) | undefined): this--><!--Device-NavigationAttribute-default customNavContentTransition(delegate: ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delegate | ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) =&gt; NavigationAnimatedTransition \| undefined) \| undefined | Yes | Custom transition delegate. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## divider

```TypeScript
default divider(style: NavigationDividerStyle | null | undefined): this
```

Set the navigation divider style in split mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default divider(style: NavigationDividerStyle | null | undefined): this--><!--Device-NavigationAttribute-default divider(style: NavigationDividerStyle | null | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [NavigationDividerStyle](arkts-arkui-navigation-navigationdividerstyle-i.md) \| null \| undefined | Yes | navigation divider style in split mode. null indicates that the divider is hidden. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## enableDragBar

```TypeScript
default enableDragBar(isEnabled: boolean | undefined): this
```

Enable dragbar

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default enableDragBar(isEnabled: boolean | undefined): this--><!--Device-NavigationAttribute-default enableDragBar(isEnabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes | enable dragbar or disable dragbar. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## enableModeChangeAnimation

```TypeScript
default enableModeChangeAnimation(isEnabled: boolean | undefined): this
```

whether to enable modeChangeAnimation

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default enableModeChangeAnimation(isEnabled: boolean | undefined): this--><!--Device-NavigationAttribute-default enableModeChangeAnimation(isEnabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes | enableModeChangeAnimation. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## enableToolBarAdaptation

```TypeScript
default enableToolBarAdaptation(enable: boolean | undefined): this
```

Enable tool bar adaptation

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default enableToolBarAdaptation(enable: boolean | undefined): this--><!--Device-NavigationAttribute-default enableToolBarAdaptation(enable: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes | Enable or disable tool bar adaptation. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableVisibilityLifecycleWithContentCover

```TypeScript
default enableVisibilityLifecycleWithContentCover(isEnabled: boolean | undefined): this
```

Whether to enable the show or hide lifecycle with bindContentCover.The true means that bindContentCover can affect the show or hide lifecycle of Navigation, and the false not.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default enableVisibilityLifecycleWithContentCover(isEnabled: boolean | undefined): this--><!--Device-NavigationAttribute-default enableVisibilityLifecycleWithContentCover(isEnabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes | enable the show or hide lifecycle with bindContentCover. Default value: **true**. **true**: The bindContentCover can affect the show or hide lifecycle of Navigation. **false**: The bindContentCover can not affect the show or hide lifecycle of Navigation. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## hideBackButton

```TypeScript
default hideBackButton(value: boolean | undefined): this
```

Hide navigation back button

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

Hide the NavBar, which includes title bar, the child of Navigation and tool bar. Supported in all mode.It will show top page in the NavPathStack directly or empty if there is no page in the NavPathStack.

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

Hide navigation title bar

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

Hide tool bar

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

Set navigation content expand types and edges.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this--><!--Device-NavigationAttribute-default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;[LayoutSafeAreaType](../arkts-components/arkts-arkui-layoutsafeareatype-e.md)&gt; \| undefined | No | Indicates the types of the safe area. |
| edges | Array&lt;[LayoutSafeAreaEdge](../arkts-components/arkts-arkui-layoutsafeareaedge-e.md)&gt; \| undefined | No | Indicates the edges of the safe area. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## menus

```TypeScript
default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this
```

Navigation title bar's menus

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this--><!--Device-NavigationAttribute-default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | Array&lt;NavigationMenuItem&gt; \| CustomBuilder \| undefined | Yes |  |
| options | [NavigationMenuOptions](../arkts-components/arkts-arkui-navigationmenuoptions-i.md) \| undefined | No | Indicates the options of menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## minContentWidth

```TypeScript
default minContentWidth(value: Dimension | undefined): this
```

Sets the minimum width of content.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default minContentWidth(value: Dimension | undefined): this--><!--Device-NavigationAttribute-default minContentWidth(value: Dimension | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes | The minimum width of content. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## mode

```TypeScript
default mode(value: NavigationMode | undefined): this
```

Sets the mode of navigation.

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

Sets the position of navigation bar.

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

Sets the width of navigation bar.

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

Sets the minimum width and the maximum width of navigation bar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default navBarWidthRange(value: [        Dimension,        Dimension    ] | undefined): this--><!--Device-NavigationAttribute-default navBarWidthRange(value: [        Dimension,        Dimension    ] | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [         Dimension,         Dimension     ] \| undefined | Yes | The minimum and the maximum width of navigation bar. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## navDestination

```TypeScript
default navDestination(builder: PageMapBuilder | undefined): this
```

Set builder for user-defined NavDestination component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default navDestination(builder: PageMapBuilder | undefined): this--><!--Device-NavigationAttribute-default navDestination(builder: PageMapBuilder | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [PageMapBuilder](arkts-arkui-pagemapbuilder-t.md) \| undefined | Yes | The builder function of NavDestination component. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## onNavBarStateChange

```TypeScript
default onNavBarStateChange(callback: ((isVisible: boolean) => void) | undefined): this
```

Trigger callback when the visibility of navigation bar change.

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

Trigger callback when navigation mode changes.

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

Trigger callback when title mode change finished at free mode.

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

Set the Navigation can be restored after the application is terminated.To enable this attribute, a navigation id must be set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default recoverable(recoverable: boolean | undefined): this--><!--Device-NavigationAttribute-default recoverable(recoverable: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recoverable | boolean \| undefined | Yes | navigation can be recovered. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## setNavigationOptions

```TypeScript
default setNavigationOptions(pathInfos?: NavPathStack, homeDestination?: HomePathInfo, moduleInfo?: NavigationModuleInfo): this
```

Sets Navigation options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default setNavigationOptions(pathInfos?: NavPathStack, homeDestination?: HomePathInfo, moduleInfo?: NavigationModuleInfo): this--><!--Device-NavigationAttribute-default setNavigationOptions(pathInfos?: NavPathStack, homeDestination?: HomePathInfo, moduleInfo?: NavigationModuleInfo): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | No | the stack of navigation |
| homeDestination | [HomePathInfo](arkts-arkui-navigation-homepathinfo-i.md) | No | the custom home destination info. |
| moduleInfo | [NavigationModuleInfo](arkts-arkui-navigation-navigationmoduleinfo-i.md) | No | the pageInfo and module info of navigation |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns instance of NavigationAttribute. |

## setNavigationOptions

```TypeScript
default setNavigationOptions(pathInfos?: NavPathStack,  moduleInfo?: NavigationModuleInfo): this
```

Sets Navigation options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default setNavigationOptions(pathInfos?: NavPathStack,  moduleInfo?: NavigationModuleInfo): this--><!--Device-NavigationAttribute-default setNavigationOptions(pathInfos?: NavPathStack,  moduleInfo?: NavigationModuleInfo): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | No | the stack of navigation |
| moduleInfo | [NavigationModuleInfo](arkts-arkui-navigation-navigationmoduleinfo-i.md) | No | the pageInfo and module info of navigation |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns instance of NavigationAttribute. |

## splitPlaceholder

```TypeScript
default splitPlaceholder(placeholder: ComponentContent<Object> | undefined): this
```

Set placeholder in split mode.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default splitPlaceholder(placeholder: ComponentContent<Object> | undefined): this--><!--Device-NavigationAttribute-default splitPlaceholder(placeholder: ComponentContent<Object> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| placeholder | [ComponentContent](../arkts-components/arkts-arkui-componentcontent-t.md)&lt;Object&gt; \| undefined | Yes | Set placeholder in split mode. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavigationAttribute. |

## systemBarStyle

```TypeScript
default systemBarStyle(style: SystemBarStyle | undefined): this
```

Set the style of system bar

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default systemBarStyle(style: SystemBarStyle | undefined): this--><!--Device-NavigationAttribute-default systemBarStyle(style: SystemBarStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [SystemBarStyle](../arkts-components/arkts-arkui-systembarstyle-t.md) \| undefined | Yes | The properties of system bar |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## title

```TypeScript
default title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle | undefined, options?: NavigationTitleOptions | undefined): this
```

Navigation title

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle | undefined, options?: NavigationTitleOptions | undefined): this--><!--Device-NavigationAttribute-default title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle | undefined, options?: NavigationTitleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| CustomBuilder \| NavigationCommonTitle \| NavigationCustomTitle \| undefined | Yes |  |
| options | [NavigationTitleOptions](arkts-arkui-navigation-navigationtitleoptions-i.md) \| undefined | No | Indicates the options of titlebar. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## titleMode

```TypeScript
default titleMode(value: NavigationTitleMode | undefined): this
```

Navigation title mode

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

Configure toolbar with default style parameter or custom parameter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this--><!--Device-NavigationAttribute-default toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;ToolbarItem&gt; \| CustomBuilder \| undefined | Yes | Toolbar configuration parameters. |
| options | [NavigationToolbarOptions](arkts-arkui-navigation-navigationtoolbaroptions-i.md) \| undefined | No | Indicates the options of toolbar. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

