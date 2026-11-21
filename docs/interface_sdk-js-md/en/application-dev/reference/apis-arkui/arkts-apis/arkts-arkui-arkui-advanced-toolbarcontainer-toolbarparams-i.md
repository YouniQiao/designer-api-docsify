# ToolBarParams

```TypeScript
export interface ToolBarParams
```

Parameters for constructing a toolbar, including the item list, modifier, floating configuration, and callbacks.

**Since:** 26.1.0

<!--Device-unnamed-export interface ToolBarParams--><!--Device-unnamed-export interface ToolBarParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## advancedToolBarModifier

```TypeScript
advancedToolBarModifier?: AdvancedToolBarV2Modifier
```

Modifier of the advanced toolbar.

**Type:** [AdvancedToolBarV2Modifier](arkts-arkui-arkui-advanced-toolbarv2-advancedtoolbarv2modifier-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarParams-advancedToolBarModifier?: AdvancedToolBarV2Modifier--><!--Device-ToolBarParams-advancedToolBarModifier?: AdvancedToolBarV2Modifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## callbacks

```TypeScript
callbacks?: ToolBarCallbacks
```

Collection of toolbar callbacks.

**Type:** [ToolBarCallbacks](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcallbacks-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarParams-callbacks?: ToolBarCallbacks--><!--Device-ToolBarParams-callbacks?: ToolBarCallbacks-End-->

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

<!--Device-ToolBarParams-controller?: ToolBarController--><!--Device-ToolBarParams-controller?: ToolBarController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## floatingConfigs

```TypeScript
floatingConfigs?: ToolBarFloatingConfigs
```

Floating behavior configuration of the toolbar. Default value: the respective default values of the fields in [ToolBarFloatingConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingconfigs-c.md).

**Type:** [ToolBarFloatingConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingconfigs-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarParams-floatingConfigs?: ToolBarFloatingConfigs--><!--Device-ToolBarParams-floatingConfigs?: ToolBarFloatingConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialParams

```TypeScript
initialParams: ToolBarInitialParams
```

Initial position.

**Type:** [ToolBarInitialParams](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarinitialparams-i.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarParams-initialParams: ToolBarInitialParams--><!--Device-ToolBarParams-initialParams: ToolBarInitialParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toolBarList

```TypeScript
toolBarList: AdvancedToolBarV2Item[]
```

List of advanced toolbar items to display.

**Type:** [AdvancedToolBarV2Item](arkts-arkui-arkui-advanced-toolbarv2-advancedtoolbarv2item-c.md)[]

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarParams-toolBarList: AdvancedToolBarV2Item[]--><!--Device-ToolBarParams-toolBarList: AdvancedToolBarV2Item[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
