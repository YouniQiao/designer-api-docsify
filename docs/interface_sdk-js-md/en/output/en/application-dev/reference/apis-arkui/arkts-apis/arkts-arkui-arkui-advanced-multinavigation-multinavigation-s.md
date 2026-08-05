# MultiNavigation

Declaration struct MultiNavigation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Component

<!--Device-unnamed-export declare struct MultiNavigation--><!--Device-unnamed-export declare struct MultiNavigation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## build

```TypeScript
build(): void
```

The method to build multiNavigation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-build(): void--><!--Device-MultiNavigation-build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## multiStack

```TypeScript
multiStack: MultiNavPathStack
```

MultiNavigation path stack of the MultiNavigation.

**Type:** MultiNavPathStack

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @State

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-multiStack: MultiNavPathStack--><!--Device-MultiNavigation-multiStack: MultiNavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navDestination

```TypeScript
navDestination: PageMapBuilder | undefined
```

build function of NavDestination.

**Type:** PageMapBuilder \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @BuilderParam

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-navDestination: PageMapBuilder | undefined--><!--Device-MultiNavigation-navDestination: PageMapBuilder | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHomeShowOnTop

```TypeScript
onHomeShowOnTop?: OnHomeShowOnTopCallback
```

This callback is triggered when the HomePage at the top of the stack.

**Type:** OnHomeShowOnTopCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-onHomeShowOnTop?: OnHomeShowOnTopCallback--><!--Device-MultiNavigation-onHomeShowOnTop?: OnHomeShowOnTopCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onNavigationModeChange

```TypeScript
onNavigationModeChange?: OnNavigationModeChangeCallback
```

callback when the MultiNavigationMode change.

**Type:** OnNavigationModeChangeCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-onNavigationModeChange?: OnNavigationModeChangeCallback--><!--Device-MultiNavigation-onNavigationModeChange?: OnNavigationModeChangeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

