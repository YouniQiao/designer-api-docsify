# MultiNavigation

Declaration struct MultiNavigation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare struct MultiNavigation--><!--Device-unnamed-export declare struct MultiNavigation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## build

```TypeScript
@Builder
  build(): void
```

The method to build multiNavigation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-@Builder  build(): void--><!--Device-MultiNavigation-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## multiStack

```TypeScript
@State
  multiStack: MultiNavPathStack
```

MultiNavigation path stack of the MultiNavigation.

**Type:** [MultiNavPathStack](arkts-na-arkui-advanced-multinavigation-multinavpathstack-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-@State  multiStack: MultiNavPathStack--><!--Device-MultiNavigation-@State  multiStack: MultiNavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navDestination

```TypeScript
@BuilderParam
  navDestination: PageMapBuilder | undefined
```

build function of NavDestination.

**Type:** PageMapBuilder \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-@BuilderParam  navDestination: PageMapBuilder | undefined--><!--Device-MultiNavigation-@BuilderParam  navDestination: PageMapBuilder | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHomeShowOnTop

```TypeScript
onHomeShowOnTop?: OnHomeShowOnTopCallback
```

This callback is triggered when the HomePage at the top of the stack.

**Type:** [OnHomeShowOnTopCallback](arkts-na-onhomeshowontopcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-onHomeShowOnTop?: OnHomeShowOnTopCallback--><!--Device-MultiNavigation-onHomeShowOnTop?: OnHomeShowOnTopCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onNavigationModeChange

```TypeScript
onNavigationModeChange?: OnNavigationModeChangeCallback
```

callback when the MultiNavigationMode change.

**Type:** [OnNavigationModeChangeCallback](arkts-na-onnavigationmodechangecallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-onNavigationModeChange?: OnNavigationModeChangeCallback--><!--Device-MultiNavigation-onNavigationModeChange?: OnNavigationModeChangeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

