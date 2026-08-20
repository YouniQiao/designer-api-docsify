# MultiNavigation

*MultiNavigation** is a component designed for multi-column display and routing navigation on large-screen devices.

> **NOTE：**

> Due to the nested stack structure of **MultiNavigation**, calling APIs explicitly stated as unsupported in this &gt; document or APIs not listed in the supported API list (such as **getParent**, **setInterception**, and &gt; **pushDestination**) may lead to unpredictable issues.

> In scenarios with deep nesting, **MultiNavigation** may encounter routing animation issues.

@struct { MultiNavigation }

**Since:** 14

<!--Device-unnamed-export declare struct MultiNavigation--><!--Device-unnamed-export declare struct MultiNavigation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SplitPolicy, MultiNavigation, MultiNavPathStack } from '@kit.ArkUI';
```

## multiStack

```TypeScript
@State
  multiStack: MultiNavPathStack
```

Navigation stack.

**Type:** [MultiNavPathStack](arkts-arkui-arkui-advanced-multinavigation-multinavpathstack-c.md)

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MultiNavigation-@State  multiStack: MultiNavPathStack--><!--Device-MultiNavigation-@State  multiStack: MultiNavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navDestination

```TypeScript
@BuilderParam
  navDestination: NavDestinationBuildFunction
```

Routing rules for loading the target page.

**Type:** [NavDestinationBuildFunction](arkts-arkui-navdestinationbuildfunction-t.md)

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MultiNavigation-@BuilderParam  navDestination: NavDestinationBuildFunction--><!--Device-MultiNavigation-@BuilderParam  navDestination: NavDestinationBuildFunction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHomeShowOnTop

```TypeScript
onHomeShowOnTop?: OnHomeShowOnTopCallback
```

Callback invoked when the home page is on the top of the navigation stack.

**Type:** [OnHomeShowOnTopCallback](arkts-arkui-onhomeshowontopcallback-t.md)

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MultiNavigation-onHomeShowOnTop?: OnHomeShowOnTopCallback--><!--Device-MultiNavigation-onHomeShowOnTop?: OnHomeShowOnTopCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onNavigationModeChange

```TypeScript
onNavigationModeChange?: OnNavigationModeChangeCallback
```

Callback invoked when the mode of the **MultiNavigation** component changes.

**Type:** [OnNavigationModeChangeCallback](arkts-arkui-onnavigationmodechangecallback-t.md)

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MultiNavigation-onNavigationModeChange?: OnNavigationModeChangeCallback--><!--Device-MultiNavigation-onNavigationModeChange?: OnNavigationModeChangeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

