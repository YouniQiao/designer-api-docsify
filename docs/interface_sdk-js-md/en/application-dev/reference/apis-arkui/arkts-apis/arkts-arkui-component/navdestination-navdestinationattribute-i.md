# NavDestinationAttribute

The attribute function of NavDestination

**Inheritance/Implementation:** NavDestinationAttribute extends [CommonMethod](common-commonmethod-i.md)

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
| modifier | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | The attribute modifier of navDestination. |

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
| icon | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| PixelMap \| SymbolGlyphModifier \| undefined | Yes | Indicates icon of back button. |
| accessibilityText | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | No | Indicates content needs to broadcast. |

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
| scrollInfos | Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; \| undefined | Yes | The controllers of the nested scrollable container components. |

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
| scrollers | Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; \| undefined | Yes | The controllers of the scrollable container components. |

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
| delegate | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | The delegate of NavDestination custom animation. |

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
| animated | boolean \| undefined | No | Whether using animation during hiding or showing statusBar, using animation if true or not using animation if false \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_If this parameter is set to undefined, the default value is used. Default value: false. |

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
| fullScreenOverlay | boolean \| undefined | Yes | Whether to display as full screen overlay. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_**true**: Full screen overlay mode, covers entire navigation container. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_**false**: Normal display mode, follows navigation split rules(Except for DIALOG mode). \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_2\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_**undefined**: Follow the fullscreen inheritance rules. |

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
| types | Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; \| undefined | No | Indicates the types of the safe area. |
| edges | Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; \| undefined | No | Indicates the edges of the safe area. |

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
| items | Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; \| CustomBuilder \| undefined | Yes |  |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | No | Indicates the options of menu. |

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
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | NavDestinationMode\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 26.0.0 |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| undefined | Yes | Indicates callback when destination is active. |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| undefined | Yes | Indicates callback when the navDestination is hidden. |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| undefined | Yes | Indicates callback when destination is inactive. |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Object \| null \| undefined&gt; \| undefined | Yes | Indicates callback when destination be pushed with singleton mode. |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| undefined | Yes | Indicates callback that invoked before sub- components of NavDestination are created. |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Custom state restore callback. |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Object \| null \| undefined&gt; \| undefined | Yes | Indicates callback when pop to the navDestination with result. |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Custom state save callback. |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| undefined | Yes | Indicates callback when the navDestination page is displayed. |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Indicates callback before the navDestination is appeared. |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Indicates callback before the navDestination is disappeared. |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Indicates callback before the navDestination is hidden. |

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Indicates callback before the navDestination is displayed. |

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
| orientation | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | The preferred Orientation of NavDestination. |

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
| moduleInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | The NavDestination module info |

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
| style | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | The properties of system bar |

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
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Types of system Transition |

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
| value | string \| CustomBuilder \| NavDestinationCommonTitle \| NavDestinationCustomTitle \| Resource \| undefined | Yes | NavDestination title. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | No | Indicates the options of titlebar. |

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
| toolbarParam | Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; \| CustomBuilder \| undefined | Yes | Toolbar configuration parameters. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | No | Indicates the options of toolbar. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

