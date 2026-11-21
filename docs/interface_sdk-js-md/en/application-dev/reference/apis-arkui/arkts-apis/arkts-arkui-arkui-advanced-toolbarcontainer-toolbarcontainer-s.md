# ToolBarContainer

```TypeScript
export struct ToolBarContainer
```

The ToolBarContainer component hosts one or more floating toolbars, and supports docking, safe area avoidance, and handedness adaptation.

**Since:** 26.1.0

**Decorator:** @ComponentV2

<!--Device-unnamed-export struct ToolBarContainer--><!--Device-unnamed-export struct ToolBarContainer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## containerConfigs

```TypeScript
containerConfigs?: ToolBarContainerConfigs
```

Container-level configuration, including docking offsets, safe area avoidance, and handedness adaptation.

**Type:** [ToolBarContainerConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontainerconfigs-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarContainer-containerConfigs?: ToolBarContainerConfigs--><!--Device-ToolBarContainer-containerConfigs?: ToolBarContainerConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content: Callback<void>
```

Content displayed in the component.

**Type:** Callback&lt;void&gt;

**Since:** 26.1.0

**Decorator:** @BuilderParam

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarContainer-content: Callback<void>--><!--Device-ToolBarContainer-content: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toolbars

```TypeScript
toolbars: ToolBarConfigs[]
```

List of toolbar configurations. A maximum of four toolbars is supported; any additional toolbars do not take effect.

**Type:** [ToolBarConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarconfigs-c.md)[]

**Since:** 26.1.0

**Decorator:** @Require

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarContainer-toolbars: ToolBarConfigs[]--><!--Device-ToolBarContainer-toolbars: ToolBarConfigs[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
