# NavigationAttribute

Declare Navigation view properties.

**Inheritance/Implementation:** NavigationAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface NavigationAttribute--><!--Device-unnamed-export declare interface NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<NavigationAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-attributeModifier(modifier: AttributeModifier<NavigationAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-NavigationAttribute-attributeModifier(modifier: AttributeModifier<NavigationAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[NavigationAttribute](arkts-na-navigation-navigationattribute-i.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## backButtonIcon

```TypeScript
backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this--><!--Device-NavigationAttribute-backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | string \| [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| SymbolGlyphModifier \| undefined | Yes |  |
| accessibilityText | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## configuration

```TypeScript
configuration(config: NavigationConfiguration | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-configuration(config: NavigationConfiguration | undefined): this--><!--Device-NavigationAttribute-configuration(config: NavigationConfiguration | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [NavigationConfiguration](arkts-na-navigation-navigationconfiguration-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## customNavContentTransition

```TypeScript
customNavContentTransition(delegate: ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-customNavContentTransition(delegate: ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined) | undefined): this--><!--Device-NavigationAttribute-customNavContentTransition(delegate: ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delegate | ((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) =&gt; NavigationAnimatedTransition \| undefined) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## divider

```TypeScript
divider(style: NavigationDividerStyle | null | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-divider(style: NavigationDividerStyle | null | undefined): this--><!--Device-NavigationAttribute-divider(style: NavigationDividerStyle | null | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [NavigationDividerStyle](arkts-na-navigation-navigationdividerstyle-i.md) \| null \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableDragBar

```TypeScript
enableDragBar(isEnabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-enableDragBar(isEnabled: boolean | undefined): this--><!--Device-NavigationAttribute-enableDragBar(isEnabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableModeChangeAnimation

```TypeScript
enableModeChangeAnimation(isEnabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-enableModeChangeAnimation(isEnabled: boolean | undefined): this--><!--Device-NavigationAttribute-enableModeChangeAnimation(isEnabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableToolBarAdaptation

```TypeScript
enableToolBarAdaptation(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-enableToolBarAdaptation(enable: boolean | undefined): this--><!--Device-NavigationAttribute-enableToolBarAdaptation(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableVisibilityLifecycleWithContentCover

```TypeScript
enableVisibilityLifecycleWithContentCover(isEnabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-enableVisibilityLifecycleWithContentCover(isEnabled: boolean | undefined): this--><!--Device-NavigationAttribute-enableVisibilityLifecycleWithContentCover(isEnabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## hideBackButton

```TypeScript
hideBackButton(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-hideBackButton(value: boolean | undefined): this--><!--Device-NavigationAttribute-hideBackButton(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## hideNavBar

```TypeScript
hideNavBar(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-hideNavBar(value: boolean | undefined): this--><!--Device-NavigationAttribute-hideNavBar(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## hideTitleBar

```TypeScript
hideTitleBar(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-hideTitleBar(value: boolean | undefined): this--><!--Device-NavigationAttribute-hideTitleBar(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## hideTitleBar

```TypeScript
hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this--><!--Device-NavigationAttribute-hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hide | boolean \| undefined | Yes |  |
| animated | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## hideToolBar

```TypeScript
hideToolBar(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-hideToolBar(value: boolean | undefined): this--><!--Device-NavigationAttribute-hideToolBar(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## hideToolBar

```TypeScript
hideToolBar(hide: boolean | undefined, animated: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-hideToolBar(hide: boolean | undefined, animated: boolean | undefined): this--><!--Device-NavigationAttribute-hideToolBar(hide: boolean | undefined, animated: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hide | boolean \| undefined | Yes |  |
| animated | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## ignoreLayoutSafeArea

```TypeScript
ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this--><!--Device-NavigationAttribute-ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;[LayoutSafeAreaType](../../apis-arkui/arkts-components/arkts-arkui-layoutsafeareatype-e.md)&gt; \| undefined | No |  |
| edges | Array&lt;[LayoutSafeAreaEdge](../../apis-arkui/arkts-components/arkts-arkui-layoutsafeareaedge-e.md)&gt; \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## menus

```TypeScript
menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this--><!--Device-NavigationAttribute-menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | Array&lt;[NavigationMenuItem](arkts-na-navigation-navigationmenuitem-i.md)&gt; \| CustomBuilder \| undefined | Yes |  |
| options | [NavigationMenuOptions](arkts-na-navigation-navigationmenuoptions-i.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## minContentWidth

```TypeScript
minContentWidth(value: Dimension | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-minContentWidth(value: Dimension | undefined): this--><!--Device-NavigationAttribute-minContentWidth(value: Dimension | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## mode

```TypeScript
mode(value: NavigationMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-mode(value: NavigationMode | undefined): this--><!--Device-NavigationAttribute-mode(value: NavigationMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NavigationMode](arkts-na-navigation-navigationmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## navBarPosition

```TypeScript
navBarPosition(value: NavBarPosition | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-navBarPosition(value: NavBarPosition | undefined): this--><!--Device-NavigationAttribute-navBarPosition(value: NavBarPosition | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NavBarPosition](arkts-na-navigation-navbarposition-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## navBarWidth

```TypeScript
navBarWidth(value: Length | Bindable<Length> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-navBarWidth(value: Length | Bindable<Length> | undefined): this--><!--Device-NavigationAttribute-navBarWidth(value: Length | Bindable<Length> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| [Bindable](arkts-na-common-bindable-i.md)&lt;[Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## navBarWidthRange

```TypeScript
navBarWidthRange(value: [
        Dimension,
        Dimension
    ] | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-navBarWidthRange(value: [        Dimension,        Dimension    ] | undefined): this--><!--Device-NavigationAttribute-navBarWidthRange(value: [        Dimension,        Dimension    ] | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [         Dimension,         Dimension     ] \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## navDestination

```TypeScript
navDestination(builder: PageMapBuilder | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-navDestination(builder: PageMapBuilder | undefined): this--><!--Device-NavigationAttribute-navDestination(builder: PageMapBuilder | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | PageMapBuilder \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onNavBarStateChange

```TypeScript
onNavBarStateChange(callback: ((isVisible: boolean) => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-onNavBarStateChange(callback: ((isVisible: boolean) => void) | undefined): this--><!--Device-NavigationAttribute-onNavBarStateChange(callback: ((isVisible: boolean) => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((isVisible: boolean) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onNavigationModeChange

```TypeScript
onNavigationModeChange(callback: ((mode: NavigationMode) => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-onNavigationModeChange(callback: ((mode: NavigationMode) => void) | undefined): this--><!--Device-NavigationAttribute-onNavigationModeChange(callback: ((mode: NavigationMode) => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((mode: NavigationMode) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onTitleModeChange

```TypeScript
onTitleModeChange(callback: ((titleMode: NavigationTitleMode) => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-onTitleModeChange(callback: ((titleMode: NavigationTitleMode) => void) | undefined): this--><!--Device-NavigationAttribute-onTitleModeChange(callback: ((titleMode: NavigationTitleMode) => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((titleMode: NavigationTitleMode) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## recoverable

```TypeScript
recoverable(recoverable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-recoverable(recoverable: boolean | undefined): this--><!--Device-NavigationAttribute-recoverable(recoverable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recoverable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setNavigationOptions

```TypeScript
setNavigationOptions(pathInfos?: NavPathStack, homeDestination?: HomePathInfo, moduleInfo?: NavigationModuleInfo): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-setNavigationOptions(pathInfos?: NavPathStack, homeDestination?: HomePathInfo, moduleInfo?: NavigationModuleInfo): this--><!--Device-NavigationAttribute-setNavigationOptions(pathInfos?: NavPathStack, homeDestination?: HomePathInfo, moduleInfo?: NavigationModuleInfo): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-na-navigation-navpathstack-c.md) | No |  |
| homeDestination | [HomePathInfo](arkts-na-navigation-homepathinfo-i.md) | No |  |
| moduleInfo | [NavigationModuleInfo](arkts-na-navigation-navigationmoduleinfo-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## setNavigationOptions

```TypeScript
setNavigationOptions(pathInfos?: NavPathStack,  moduleInfo?: NavigationModuleInfo): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-setNavigationOptions(pathInfos?: NavPathStack,  moduleInfo?: NavigationModuleInfo): this--><!--Device-NavigationAttribute-setNavigationOptions(pathInfos?: NavPathStack,  moduleInfo?: NavigationModuleInfo): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-na-navigation-navpathstack-c.md) | No |  |
| moduleInfo | [NavigationModuleInfo](arkts-na-navigation-navigationmoduleinfo-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## splitPlaceholder

```TypeScript
splitPlaceholder(placeholder: ComponentContent<Object> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-splitPlaceholder(placeholder: ComponentContent<Object> | undefined): this--><!--Device-NavigationAttribute-splitPlaceholder(placeholder: ComponentContent<Object> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| placeholder | ComponentContent&lt;Object&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## systemBarStyle

```TypeScript
systemBarStyle(style: SystemBarStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-systemBarStyle(style: SystemBarStyle | undefined): this--><!--Device-NavigationAttribute-systemBarStyle(style: SystemBarStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [SystemBarStyle](arkts-na-systembarstyle-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## title

```TypeScript
title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle | undefined, options?: NavigationTitleOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle | undefined, options?: NavigationTitleOptions | undefined): this--><!--Device-NavigationAttribute-title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle | undefined, options?: NavigationTitleOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| CustomBuilder \| [NavigationCommonTitle](arkts-na-navigation-navigationcommontitle-i.md) \| [NavigationCustomTitle](arkts-na-navigation-navigationcustomtitle-i.md) \| undefined | Yes |  |
| options | [NavigationTitleOptions](arkts-na-navigation-navigationtitleoptions-i.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## titleMode

```TypeScript
titleMode(value: NavigationTitleMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-titleMode(value: NavigationTitleMode | undefined): this--><!--Device-NavigationAttribute-titleMode(value: NavigationTitleMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NavigationTitleMode](arkts-na-navigation-navigationtitlemode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## toolbarConfiguration

```TypeScript
toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavigationAttribute-toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this--><!--Device-NavigationAttribute-toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[ToolbarItem](arkts-na-navigation-toolbaritem-i.md)&gt; \| CustomBuilder \| undefined | Yes |  |
| options | [NavigationToolbarOptions](arkts-na-navigation-navigationtoolbaroptions-i.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set placeholder in split mode.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAttribute-default--><!--Device-NavigationAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

