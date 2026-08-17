# NavDestinationAttribute

The attribute function of NavDestination

**Inheritance/Implementation:** NavDestinationAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface NavDestinationAttribute--><!--Device-unnamed-export declare interface NavDestinationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<NavDestinationAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-attributeModifier(modifier: AttributeModifier<NavDestinationAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-NavDestinationAttribute-attributeModifier(modifier: AttributeModifier<NavDestinationAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[NavDestinationAttribute](arkts-na-navdestination-navdestinationattribute-i.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backButtonIcon

```TypeScript
backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this--><!--Device-NavDestinationAttribute-backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| SymbolGlyphModifier \| undefined | Yes |  |
| accessibilityText | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindToNestedScrollable

```TypeScript
bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo> | undefined): this--><!--Device-NavDestinationAttribute-bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scrollInfos | Array&lt;[NestedScrollInfo](arkts-na-navdestination-nestedscrollinfo-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindToScrollable

```TypeScript
bindToScrollable(scrollers: Array<Scroller> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-bindToScrollable(scrollers: Array<Scroller> | undefined): this--><!--Device-NavDestinationAttribute-bindToScrollable(scrollers: Array<Scroller> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scrollers | Array&lt;[Scroller](../../apis-arkui/arkts-components/arkts-arkui-scroller-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## customTransition

```TypeScript
customTransition(delegate: NavDestinationTransitionDelegate | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-customTransition(delegate: NavDestinationTransitionDelegate | undefined): this--><!--Device-NavDestinationAttribute-customTransition(delegate: NavDestinationTransitionDelegate | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delegate | [NavDestinationTransitionDelegate](arkts-na-navdestinationtransitiondelegate-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableNavigationIndicator

```TypeScript
enableNavigationIndicator(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-enableNavigationIndicator(enabled: boolean | undefined): this--><!--Device-NavDestinationAttribute-enableNavigationIndicator(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableStatusBar

```TypeScript
enableStatusBar(enabled: boolean | undefined, animated?: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-enableStatusBar(enabled: boolean | undefined, animated?: boolean | undefined): this--><!--Device-NavDestinationAttribute-enableStatusBar(enabled: boolean | undefined, animated?: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |
| animated | boolean \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## fullScreenOverlay

```TypeScript
fullScreenOverlay(fullScreenOverlay: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-fullScreenOverlay(fullScreenOverlay: boolean | undefined): this--><!--Device-NavDestinationAttribute-fullScreenOverlay(fullScreenOverlay: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fullScreenOverlay | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hideBackButton

```TypeScript
hideBackButton(hide: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-hideBackButton(hide: boolean | undefined): this--><!--Device-NavDestinationAttribute-hideBackButton(hide: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hide | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hideTitleBar

```TypeScript
hideTitleBar(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-hideTitleBar(value: boolean | undefined): this--><!--Device-NavDestinationAttribute-hideTitleBar(value: boolean | undefined): this-End-->

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
hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this--><!--Device-NavDestinationAttribute-hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this-End-->

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
hideToolBar(hide: boolean | undefined, animated?: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-hideToolBar(hide: boolean | undefined, animated?: boolean | undefined): this--><!--Device-NavDestinationAttribute-hideToolBar(hide: boolean | undefined, animated?: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hide | boolean \| undefined | Yes |  |
| animated | boolean \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## ignoreLayoutSafeArea

```TypeScript
ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this--><!--Device-NavDestinationAttribute-ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;[LayoutSafeAreaType](../../apis-arkui/arkts-components/arkts-arkui-layoutsafeareatype-e.md)&gt; \| undefined | No |  |
| edges | Array&lt;[LayoutSafeAreaEdge](../../apis-arkui/arkts-components/arkts-arkui-layoutsafeareaedge-e.md)&gt; \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## menus

```TypeScript
menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this--><!--Device-NavDestinationAttribute-menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | Array&lt;NavigationMenuItem&gt; \| CustomBuilder \| undefined | Yes |  |
| options | [NavigationMenuOptions](../../apis-arkui/arkts-components/arkts-arkui-navigationmenuoptions-i.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## mode

```TypeScript
mode(value: NavDestinationMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-mode(value: NavDestinationMode | undefined): this--><!--Device-NavDestinationAttribute-mode(value: NavDestinationMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NavDestinationMode](arkts-na-navdestination-navdestinationmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onActive

```TypeScript
onActive(callback: Callback<NavDestinationActiveReason> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onActive(callback: Callback<NavDestinationActiveReason> | undefined): this--><!--Device-NavDestinationAttribute-onActive(callback: Callback<NavDestinationActiveReason> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[NavDestinationActiveReason](arkts-na-navdestination-navdestinationactivereason-e.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onBackPressed

```TypeScript
onBackPressed(callback: (() => boolean) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onBackPressed(callback: (() => boolean) | undefined): this--><!--Device-NavDestinationAttribute-onBackPressed(callback: (() => boolean) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; boolean) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onHidden

```TypeScript
onHidden(callback: Callback<VisibilityChangeReason> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onHidden(callback: Callback<VisibilityChangeReason> | undefined): this--><!--Device-NavDestinationAttribute-onHidden(callback: Callback<VisibilityChangeReason> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[VisibilityChangeReason](arkts-na-navdestination-visibilitychangereason-e.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onInactive

```TypeScript
onInactive(callback: Callback<NavDestinationActiveReason> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onInactive(callback: Callback<NavDestinationActiveReason> | undefined): this--><!--Device-NavDestinationAttribute-onInactive(callback: Callback<NavDestinationActiveReason> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[NavDestinationActiveReason](arkts-na-navdestination-navdestinationactivereason-e.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onNewParam

```TypeScript
onNewParam(callback: Callback<Object | null | undefined> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onNewParam(callback: Callback<Object | null | undefined> | undefined): this--><!--Device-NavDestinationAttribute-onNewParam(callback: Callback<Object | null | undefined> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;Object \| null \| undefined&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onReady

```TypeScript
onReady(callback: Callback<NavDestinationContext> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onReady(callback: Callback<NavDestinationContext> | undefined): this--><!--Device-NavDestinationAttribute-onReady(callback: Callback<NavDestinationContext> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[NavDestinationContext](arkts-na-navdestination-navdestinationcontext-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onRestoreState

```TypeScript
onRestoreState(callback: RestoreStateCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onRestoreState(callback: RestoreStateCallback | undefined): this--><!--Device-NavDestinationAttribute-onRestoreState(callback: RestoreStateCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [RestoreStateCallback](arkts-na-restorestatecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onResult

```TypeScript
onResult(callback: Callback<Object | null | undefined> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onResult(callback: Callback<Object | null | undefined> | undefined): this--><!--Device-NavDestinationAttribute-onResult(callback: Callback<Object | null | undefined> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;Object \| null \| undefined&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onSaveState

```TypeScript
onSaveState(callback: SaveStateCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onSaveState(callback: SaveStateCallback | undefined): this--><!--Device-NavDestinationAttribute-onSaveState(callback: SaveStateCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SaveStateCallback](arkts-na-savestatecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onShown

```TypeScript
onShown(callback: Callback<VisibilityChangeReason> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onShown(callback: Callback<VisibilityChangeReason> | undefined): this--><!--Device-NavDestinationAttribute-onShown(callback: Callback<VisibilityChangeReason> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[VisibilityChangeReason](arkts-na-navdestination-visibilitychangereason-e.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onWillAppear

```TypeScript
onWillAppear(callback: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onWillAppear(callback: VoidCallback | undefined): this--><!--Device-NavDestinationAttribute-onWillAppear(callback: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onWillDisappear

```TypeScript
onWillDisappear(callback: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onWillDisappear(callback: VoidCallback | undefined): this--><!--Device-NavDestinationAttribute-onWillDisappear(callback: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onWillHide

```TypeScript
onWillHide(callback: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onWillHide(callback: VoidCallback | undefined): this--><!--Device-NavDestinationAttribute-onWillHide(callback: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onWillShow

```TypeScript
onWillShow(callback: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-onWillShow(callback: VoidCallback | undefined): this--><!--Device-NavDestinationAttribute-onWillShow(callback: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## preferredOrientation

```TypeScript
preferredOrientation(orientation: Orientation | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-preferredOrientation(orientation: Orientation | undefined): this--><!--Device-NavDestinationAttribute-preferredOrientation(orientation: Orientation | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| orientation | [Orientation](arkts-na-orientation-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## recoverable

```TypeScript
recoverable(recoverable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-recoverable(recoverable: boolean | undefined): this--><!--Device-NavDestinationAttribute-recoverable(recoverable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recoverable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setNavDestinationOptions

```TypeScript
setNavDestinationOptions(moduleInfo?: NavDestinationModuleInfo): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-setNavDestinationOptions(moduleInfo?: NavDestinationModuleInfo): this--><!--Device-NavDestinationAttribute-setNavDestinationOptions(moduleInfo?: NavDestinationModuleInfo): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleInfo | [NavDestinationModuleInfo](arkts-na-navdestination-navdestinationmoduleinfo-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## systemBarStyle

```TypeScript
systemBarStyle(style: SystemBarStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-systemBarStyle(style: SystemBarStyle | undefined): this--><!--Device-NavDestinationAttribute-systemBarStyle(style: SystemBarStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [SystemBarStyle](../../apis-arkui/arkts-components/arkts-arkui-systembarstyle-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## systemTransition

```TypeScript
systemTransition(type: NavigationSystemTransitionType | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-systemTransition(type: NavigationSystemTransitionType | undefined): this--><!--Device-NavDestinationAttribute-systemTransition(type: NavigationSystemTransitionType | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [NavigationSystemTransitionType](arkts-na-navdestination-navigationsystemtransitiontype-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## title

```TypeScript
title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource | undefined, options?: NavigationTitleOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource | undefined, options?: NavigationTitleOptions | undefined): this--><!--Device-NavDestinationAttribute-title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource | undefined, options?: NavigationTitleOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| CustomBuilder \| [NavDestinationCommonTitle](arkts-na-navdestination-navdestinationcommontitle-i.md) \| [NavDestinationCustomTitle](arkts-na-navdestination-navdestinationcustomtitle-i.md) \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |  |
| options | NavigationTitleOptions \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## toolbarConfiguration

```TypeScript
toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-NavDestinationAttribute-toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this--><!--Device-NavDestinationAttribute-toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| toolbarParam | Array&lt;ToolbarItem&gt; \| CustomBuilder \| undefined | Yes |  |
| options | [NavigationToolbarOptions](../../apis-arkui/arkts-components/arkts-arkui-navigationtoolbaroptions-i.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## default

```TypeScript
default
```

Set navDestination options.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default--><!--Device-NavDestinationAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

