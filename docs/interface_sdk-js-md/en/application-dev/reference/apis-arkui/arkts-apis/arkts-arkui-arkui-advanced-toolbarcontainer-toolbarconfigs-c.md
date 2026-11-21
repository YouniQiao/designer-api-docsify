# ToolBarConfigs

```TypeScript
export class ToolBarConfigs
```

Observable configuration store for the toolbar, corresponding to [ToolBarParams](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarparams-i.md).

**Since:** 26.1.0

**Decorator:** @ObservedV2

<!--Device-unnamed-export class ToolBarConfigs--><!--Device-unnamed-export class ToolBarConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(params: ToolBarParams)
```

Constructor of the toolbar configuration class ToolBarConfigs.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarConfigs-constructor(params: ToolBarParams)--><!--Device-ToolBarConfigs-constructor(params: ToolBarParams)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [ToolBarParams](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarparams-i.md) | Yes | Parameters for constructing the toolbar. |

## advancedToolBarModifier

```TypeScript
advancedToolBarModifier: AdvancedToolBarV2Modifier
```

Modifier of the advanced toolbar.

**Type:** [AdvancedToolBarV2Modifier](arkts-arkui-arkui-advanced-toolbarv2-advancedtoolbarv2modifier-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarConfigs-advancedToolBarModifier: AdvancedToolBarV2Modifier--><!--Device-ToolBarConfigs-advancedToolBarModifier: AdvancedToolBarV2Modifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## callbacks

```TypeScript
callbacks?: ToolBarCallbacks
```

Collection of toolbar callbacks.

**Type:** [ToolBarCallbacks](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcallbacks-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarConfigs-callbacks?: ToolBarCallbacks--><!--Device-ToolBarConfigs-callbacks?: ToolBarCallbacks-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: ToolBarController
```

Toolbar controller.

**Type:** [ToolBarController](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontroller-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarConfigs-controller?: ToolBarController--><!--Device-ToolBarConfigs-controller?: ToolBarController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## floatingConfigs

```TypeScript
floatingConfigs?: ToolBarFloatingConfigs
```

Floating configuration of the advanced toolbar.

**Type:** [ToolBarFloatingConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingconfigs-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarConfigs-floatingConfigs?: ToolBarFloatingConfigs--><!--Device-ToolBarConfigs-floatingConfigs?: ToolBarFloatingConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialParams

```TypeScript
initialParams: ToolBarInitialParams
```

Initial position of the advanced toolbar.

**Type:** [ToolBarInitialParams](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarinitialparams-i.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarConfigs-initialParams: ToolBarInitialParams--><!--Device-ToolBarConfigs-initialParams: ToolBarInitialParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toolBarList

```TypeScript
toolBarList: AdvancedToolBarV2Item[]
```

List of advanced toolbar items to display.

**Type:** [AdvancedToolBarV2Item](arkts-arkui-arkui-advanced-toolbarv2-advancedtoolbarv2item-c.md)[]

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarConfigs-toolBarList: AdvancedToolBarV2Item[]--><!--Device-ToolBarConfigs-toolBarList: AdvancedToolBarV2Item[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
