# MultiNavigation

MultiNavigation({navDestination: PageMapBuilder | undefined, multiStack: MultiNavPathStack, onNavigationModeChange?: OnNavigationModeChangeCallback, onHomeShowOnTop?: OnHomeShowOnTopCallback})

创建并初始化MultiNavigation组件。

MultiNavigation组件遵循默认的左起右清栈规则，这意味着从左侧主页点击时，会触发详情页的加载并同时清除右侧所有其他详情页，确保右侧仅展示最新加载的详情页。然而，若在右侧的详情页上再次执行详情页加载操作，系统将不会执行清栈动作。效果可参见[主页跳转详情页效果演示](../../../reference/apis-arkui/arkui-ts/ohos-arkui-advanced-MultiNavigation copy.md#示例)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Component

<!--Device-unnamed-export declare struct MultiNavigation--><!--Device-unnamed-export declare struct MultiNavigation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { MultiNavPathStack, MultiNavigation, SplitPolicy } from 'kits/@kit.ArkUI';
```

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

## onHomeShowOnTop

```TypeScript
onHomeShowOnTop?: OnHomeShowOnTopCallback
```

设置主页处于栈顶时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-onHomeShowOnTop?: OnHomeShowOnTopCallback--><!--Device-MultiNavigation-onHomeShowOnTop?: OnHomeShowOnTopCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onNavigationModeChange

```TypeScript
onNavigationModeChange?: OnNavigationModeChangeCallback
```

设置MultiNavigation模式变更时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-onNavigationModeChange?: OnNavigationModeChangeCallback--><!--Device-MultiNavigation-onNavigationModeChange?: OnNavigationModeChangeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## multiStack

```TypeScript
multiStack: MultiNavPathStack
```

设置路由栈。

**Type:** [MultiNavPathStack](arkts-arkui-arkui-advanced-multinavigation-multinavpathstack-c.md)

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

设置加载目标页面的路由规则。

取值为undefined时，不会加载。

**Type:** [PageMapBuilder](arkts-arkui-pagemapbuilder-t.md) \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @BuilderParam

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavigation-navDestination: PageMapBuilder | undefined--><!--Device-MultiNavigation-navDestination: PageMapBuilder | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

