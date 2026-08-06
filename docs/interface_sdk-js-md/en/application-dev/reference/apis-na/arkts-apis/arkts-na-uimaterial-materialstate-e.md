# MaterialState

Enumerates the material enabling states, indicating the states of the application-level immersive system material configuration.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-uiMaterial-export enum MaterialState--><!--Device-uiMaterial-export enum MaterialState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 0
```

Default state. The immersive system material is enabled by default for the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_, \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, and [AlphabetIndexer]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ components if the background color, blur, and shadow are not set for the components. The immersive system material is enabled by default for the text menu triggered by long-pressing or double-clicking after [copyOption]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ is set in the [Text]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ component. For other components, whether the immersive system material is enabled is set by the application.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialState-DEFAULT = 0--><!--Device-MaterialState-DEFAULT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ENABLE

```TypeScript
ENABLE = 1
```

Enabled state. The immersive system material is enabled by default for the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_, \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, [AlphabetIndexer]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, [ChipGroup]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_, [Chip]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_, [Select]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_, [Menu Control]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_, [Toggle]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_, [SegmentButton]\_\_\_JSDOC\_LINK\_DESC\_USD\_8\_\_\_, [SegmentButtonV2]\_\_\_JSDOC\_LINK\_DESC\_USD\_9\_\_\_, [Slider]\_\_\_JSDOC\_LINK\_DESC\_USD\_10\_\_\_, [bindSheet]\_\_\_JSDOC\_LINK\_DESC\_USD\_11\_\_\_, and [SelectionMenu]\_\_\_JSDOC\_LINK\_DESC\_USD\_12\_\_\_. After [copyOption]\_\_\_JSDOC\_LINK\_DESC\_USD\_13\_\_\_ is set for the [Text]\_\_\_JSDOC\_LINK\_DESC\_USD\_14\_\_\_ component, the immersive system material is enabled by default for the text menu triggered by long-pressing or double-clicking. In this state, the immersive system material style takes precedence over the background color, blur, shadow, and border style set for the components. You need to set whether to enable the immersive system material for other components.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialState-ENABLE = 1--><!--Device-MaterialState-ENABLE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DISABLE

```TypeScript
DISABLE = 2
```

Disabled state. The immersive system material cannot be enabled for any component. Even if you set the immersive system material parameters for a component, the settings will not take effect.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialState-DISABLE = 2--><!--Device-MaterialState-DISABLE = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

