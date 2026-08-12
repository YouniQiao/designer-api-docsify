# NavDestinationAttribute

The attribute function of NavDestination

**Inheritance/Implementation:** NavDestinationAttribute extends [CommonMethod](CommonMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavDestinationAttribute extends CommonMethod--><!--Device-unnamed-export declare interface NavDestinationAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<NavDestinationAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of navDestination.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default attributeModifier(modifier: AttributeModifier<NavDestinationAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-NavDestinationAttribute-default attributeModifier(modifier: AttributeModifier<NavDestinationAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes | The attribute modifier of navDestination. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backButtonIcon

```TypeScript
default backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this
```

Set back button icon and accessibility broadcast content.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this--><!--Device-NavDestinationAttribute-default backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier | undefined, accessibilityText?: ResourceStr | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md) \| undefined | Yes | Indicates icon of back button. |
| accessibilityText | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | No | Indicates content needs to broadcast. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindToNestedScrollable

```TypeScript
default bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo> | undefined): this
```

Bind NavDestination to nested scrollable container components to automatically hide titlebar and toolbar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo> | undefined): this--><!--Device-NavDestinationAttribute-default bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scrollInfos | Array&lt;[NestedScrollInfo](arkts-arkui-navdestination-nestedscrollinfo-i.md)&gt; \| undefined | Yes | The controllers of the nested scrollable container components. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## bindToScrollable

```TypeScript
default bindToScrollable(scrollers: Array<Scroller> | undefined): this
```

Bind NavDestination to scrollable container components to automatically hide titlebar and toolbar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default bindToScrollable(scrollers: Array<Scroller> | undefined): this--><!--Device-NavDestinationAttribute-default bindToScrollable(scrollers: Array<Scroller> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scrollers | Array&lt;[Scroller](../arkts-components/arkts-arkui-scroller-c.md)&gt; \| undefined | Yes | The controllers of the scrollable container components. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## customTransition

```TypeScript
default customTransition(delegate: NavDestinationTransitionDelegate | undefined): this
```

Set NavDestination custom animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default customTransition(delegate: NavDestinationTransitionDelegate | undefined): this--><!--Device-NavDestinationAttribute-default customTransition(delegate: NavDestinationTransitionDelegate | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delegate | [NavDestinationTransitionDelegate](arkts-arkui-navdestinationtransitiondelegate-t.md) \| undefined | Yes | The delegate of NavDestination custom animation. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## enableNavigationIndicator

```TypeScript
default enableNavigationIndicator(enabled: boolean | undefined): this
```

Set navigationIndicator to visible or invisible.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default enableNavigationIndicator(enabled: boolean | undefined): this--><!--Device-NavDestinationAttribute-default enableNavigationIndicator(enabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | Show navigationIndicator if true, or hide navigationIndicator if false. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## enableStatusBar

```TypeScript
default enableStatusBar(enabled: boolean | undefined, animated?: boolean | undefined): this
```

Set statusBar to visible or invisible.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default enableStatusBar(enabled: boolean | undefined, animated?: boolean | undefined): this--><!--Device-NavDestinationAttribute-default enableStatusBar(enabled: boolean | undefined, animated?: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | Show statusBar if true, or hide statusBar if false. |
| animated | boolean \| undefined | No | Whether using animation during hiding or showing statusBar, using animation if true or not using animation if false &lt;br&gt;If this parameter is set to undefined, the default value is used. Default value: false. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## fullScreenOverlay

```TypeScript
default fullScreenOverlay(fullScreenOverlay: boolean | undefined): this
```

Sets whether the NavDestination should cover the entire navigation container.

When set to true, in split navigation mode, the page covers both the NavBar and content area, displaying in full screen overlay mode. This setting applies to all instances of this NavDestination whenever it is pushed onto the stack, unless overridden by the fullScreen option in the push operation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default fullScreenOverlay(fullScreenOverlay: boolean | undefined): this--><!--Device-NavDestinationAttribute-default fullScreenOverlay(fullScreenOverlay: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fullScreenOverlay | boolean \| undefined | Yes | Whether to display as full screen overlay. &lt;br&gt;**true**: Full screen overlay mode, covers entire navigation container. &lt;br&gt;**false**: Normal display mode, follows navigation split rules(Except for DIALOG mode). &lt;br&gt;**undefined**: Follow the fullscreen inheritance rules. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hideBackButton

```TypeScript
default hideBackButton(hide: boolean | undefined): this
```

Hide navDestination back button

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default hideBackButton(hide: boolean | undefined): this--><!--Device-NavDestinationAttribute-default hideBackButton(hide: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

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
default hideTitleBar(value: boolean | undefined): this
```

Hide navigation title bar

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default hideTitleBar(value: boolean | undefined): this--><!--Device-NavDestinationAttribute-default hideTitleBar(value: boolean | undefined): this-End-->

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

<!--Device-NavDestinationAttribute-default hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this--><!--Device-NavDestinationAttribute-default hideTitleBar(hide: boolean | undefined, animated: boolean | undefined): this-End-->

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
default hideToolBar(hide: boolean | undefined, animated?: boolean | undefined): this
```

Hide tool bar

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default hideToolBar(hide: boolean | undefined, animated?: boolean | undefined): this--><!--Device-NavDestinationAttribute-default hideToolBar(hide: boolean | undefined, animated?: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

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
default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this
```

Set navDestination content expand types and edges.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this--><!--Device-NavDestinationAttribute-default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this-End-->

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

NavDestination title bar's menus

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this--><!--Device-NavDestinationAttribute-default menus(items: Array<NavigationMenuItem> | CustomBuilder | undefined, options?: NavigationMenuOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | Array&lt;[NavigationMenuItem](../arkts-components/arkts-arkui-navigationmenuitem-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | Yes |  |
| options | [NavigationMenuOptions](../arkts-components/arkts-arkui-navigationmenuoptions-i.md) \| undefined | No | Indicates the options of menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## mode

```TypeScript
default mode(value: NavDestinationMode | undefined): this
```

Sets the different mode of NavDestination.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default mode(value: NavDestinationMode | undefined): this--><!--Device-NavDestinationAttribute-default mode(value: NavDestinationMode | undefined): this-End-->

**System capability:** 
- API version 23 and later: SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NavDestinationMode](arkts-arkui-navdestination-navdestinationmode-e.md) \| undefined | Yes | NavDestinationMode<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onActive

```TypeScript
default onActive(callback: Callback<NavDestinationActiveReason> | undefined): this
```

Invoked when destination is active.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onActive(callback: Callback<NavDestinationActiveReason> | undefined): this--><!--Device-NavDestinationAttribute-default onActive(callback: Callback<NavDestinationActiveReason> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[NavDestinationActiveReason](arkts-arkui-navdestination-navdestinationactivereason-e.md)&gt; \| undefined | Yes | Indicates callback when destination is active. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onBackPressed

```TypeScript
default onBackPressed(callback: (() => boolean) | undefined): this
```

Invoked when the backButton is pressed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onBackPressed(callback: (() => boolean) | undefined): this--><!--Device-NavDestinationAttribute-default onBackPressed(callback: (() => boolean) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; boolean) \| undefined | Yes | Indicates callback when the backButton is pressed. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onHidden

```TypeScript
default onHidden(callback: Callback<VisibilityChangeReason> | undefined): this
```

Invoked when the navDestination is hidden.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onHidden(callback: Callback<VisibilityChangeReason> | undefined): this--><!--Device-NavDestinationAttribute-default onHidden(callback: Callback<VisibilityChangeReason> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[VisibilityChangeReason](arkts-arkui-navdestination-visibilitychangereason-e.md)&gt; \| undefined | Yes | Indicates callback when the navDestination is hidden. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onInactive

```TypeScript
default onInactive(callback: Callback<NavDestinationActiveReason> | undefined): this
```

Invoked when destination is inactive.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onInactive(callback: Callback<NavDestinationActiveReason> | undefined): this--><!--Device-NavDestinationAttribute-default onInactive(callback: Callback<NavDestinationActiveReason> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[NavDestinationActiveReason](arkts-arkui-navdestination-navdestinationactivereason-e.md)&gt; \| undefined | Yes | Indicates callback when destination is inactive. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onNewParam

```TypeScript
default onNewParam(callback: Callback<Object | null | undefined> | undefined): this
```

Invoked when destination be pushed with singleton mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onNewParam(callback: Callback<Object | null | undefined> | undefined): this--><!--Device-NavDestinationAttribute-default onNewParam(callback: Callback<Object | null | undefined> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;Object \| null \| undefined&gt; \| undefined | Yes | Indicates callback when destination be pushed with singleton mode. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onReady

```TypeScript
default onReady(callback: Callback<NavDestinationContext> | undefined): this
```

Invoked before sub-components of NavDestination are created.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onReady(callback: Callback<NavDestinationContext> | undefined): this--><!--Device-NavDestinationAttribute-default onReady(callback: Callback<NavDestinationContext> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[NavDestinationContext](arkts-arkui-navdestination-navdestinationcontext-i.md)&gt; \| undefined | Yes | Indicates callback that invoked before sub- components of NavDestination are created. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onRestoreState

```TypeScript
default onRestoreState(callback: RestoreStateCallback | undefined): this
```

Sets custom page state restore callback.

Triggered when page is reconstructed. The custom state saved by onSaveState is passed to this callback.Null is passed if no custom state was saved.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onRestoreState(callback: RestoreStateCallback | undefined): this--><!--Device-NavDestinationAttribute-default onRestoreState(callback: RestoreStateCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [RestoreStateCallback](arkts-arkui-restorestatecallback-t.md) \| undefined | Yes | Custom state restore callback. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## onResult

```TypeScript
default onResult(callback: Callback<Object | null | undefined> | undefined): this
```

Invoked when pop to the navDestination with result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onResult(callback: Callback<Object | null | undefined> | undefined): this--><!--Device-NavDestinationAttribute-default onResult(callback: Callback<Object | null | undefined> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;Object \| null \| undefined&gt; \| undefined | Yes | Indicates callback when pop to the navDestination with result. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onSaveState

```TypeScript
default onSaveState(callback: SaveStateCallback | undefined): this
```

Sets custom page state save callback.

Triggered when page becomes hidden. Save custom page state for potential restoration.The initial param used to create the page is preserved by Navigation separately.State object must be serializable.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onSaveState(callback: SaveStateCallback | undefined): this--><!--Device-NavDestinationAttribute-default onSaveState(callback: SaveStateCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SaveStateCallback](arkts-arkui-savestatecallback-t.md) \| undefined | Yes | Custom state save callback. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## onShown

```TypeScript
default onShown(callback: Callback<VisibilityChangeReason> | undefined): this
```

Invoked when the navDestination page is displayed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onShown(callback: Callback<VisibilityChangeReason> | undefined): this--><!--Device-NavDestinationAttribute-default onShown(callback: Callback<VisibilityChangeReason> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[VisibilityChangeReason](arkts-arkui-navdestination-visibilitychangereason-e.md)&gt; \| undefined | Yes | Indicates callback when the navDestination page is displayed. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onWillAppear

```TypeScript
default onWillAppear(callback: VoidCallback | undefined): this
```

Invoked before the navDestination is appeared.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onWillAppear(callback: VoidCallback | undefined): this--><!--Device-NavDestinationAttribute-default onWillAppear(callback: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes | Indicates callback before the navDestination is appeared. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onWillDisappear

```TypeScript
default onWillDisappear(callback: VoidCallback | undefined): this
```

Invoked before the navDestination is disappeared.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onWillDisappear(callback: VoidCallback | undefined): this--><!--Device-NavDestinationAttribute-default onWillDisappear(callback: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes | Indicates callback before the navDestination is disappeared. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onWillHide

```TypeScript
default onWillHide(callback: VoidCallback | undefined): this
```

Invoked before the navDestination is hidden.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onWillHide(callback: VoidCallback | undefined): this--><!--Device-NavDestinationAttribute-default onWillHide(callback: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes | Indicates callback before the navDestination is hidden. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onWillShow

```TypeScript
default onWillShow(callback: VoidCallback | undefined): this
```

Invoked before the navDestination is displayed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default onWillShow(callback: VoidCallback | undefined): this--><!--Device-NavDestinationAttribute-default onWillShow(callback: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes | Indicates callback before the navDestination is displayed. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## preferredOrientation

```TypeScript
default preferredOrientation(orientation: Orientation | undefined): this
```

Set NavDestination's preferred Orientation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default preferredOrientation(orientation: Orientation | undefined): this--><!--Device-NavDestinationAttribute-default preferredOrientation(orientation: Orientation | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| orientation | [Orientation](arkts-arkui-orientation-t.md) \| undefined | Yes | The preferred Orientation of NavDestination. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## recoverable

```TypeScript
default recoverable(recoverable: boolean | undefined): this
```

Set the NavDestination can be restored after the application is terminated.To enable this attribute, recoverable and id of Navigation must be set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default recoverable(recoverable: boolean | undefined): this--><!--Device-NavDestinationAttribute-default recoverable(recoverable: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recoverable | boolean \| undefined | Yes | set navdestination can be recovered. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setNavDestinationOptions

```TypeScript
default setNavDestinationOptions(moduleInfo?: NavDestinationModuleInfo): this
```

Set navDestination options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default setNavDestinationOptions(moduleInfo?: NavDestinationModuleInfo): this--><!--Device-NavDestinationAttribute-default setNavDestinationOptions(moduleInfo?: NavDestinationModuleInfo): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleInfo | [NavDestinationModuleInfo](arkts-arkui-navdestination-navdestinationmoduleinfo-i.md) | No | The NavDestination module info |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the NavDestinationAttribute. |

## systemBarStyle

```TypeScript
default systemBarStyle(style: SystemBarStyle | undefined): this
```

Set the style of system bar

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default systemBarStyle(style: SystemBarStyle | undefined): this--><!--Device-NavDestinationAttribute-default systemBarStyle(style: SystemBarStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [SystemBarStyle](../arkts-components/arkts-arkui-systembarstyle-t.md) \| undefined | Yes | The properties of system bar |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## systemTransition

```TypeScript
default systemTransition(type: NavigationSystemTransitionType | undefined): this
```

Configuration of system transition

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default systemTransition(type: NavigationSystemTransitionType | undefined): this--><!--Device-NavDestinationAttribute-default systemTransition(type: NavigationSystemTransitionType | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [NavigationSystemTransitionType](arkts-arkui-navdestination-navigationsystemtransitiontype-e.md) \| undefined | Yes | Types of system Transition |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## title

```TypeScript
default title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource | undefined, options?: NavigationTitleOptions | undefined): this
```

NavDestination title bar

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource | undefined, options?: NavigationTitleOptions | undefined): this--><!--Device-NavDestinationAttribute-default title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource | undefined, options?: NavigationTitleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [NavDestinationCommonTitle](arkts-arkui-navdestination-navdestinationcommontitle-i.md) \| [NavDestinationCustomTitle](arkts-arkui-navdestination-navdestinationcustomtitle-i.md) \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes | NavDestination title. |
| options | [NavigationTitleOptions](../arkts-components/arkts-arkui-navigationtitleoptions-i.md) \| undefined | No | Indicates the options of titlebar. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## toolbarConfiguration

```TypeScript
default toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this
```

Configure toolbar with default style parameter or custom parameter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationAttribute-default toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this--><!--Device-NavDestinationAttribute-default toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder | undefined, options?: NavigationToolbarOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| toolbarParam | Array&lt;[ToolbarItem](../arkts-components/arkts-arkui-toolbaritem-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | Yes | Toolbar configuration parameters. |
| options | [NavigationToolbarOptions](../arkts-components/arkts-arkui-navigationtoolbaroptions-i.md) \| undefined | No | Indicates the options of toolbar. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

