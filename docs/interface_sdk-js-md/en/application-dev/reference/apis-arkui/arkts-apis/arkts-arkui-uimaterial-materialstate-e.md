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

Default state. The immersive system material is enabled by default for the   
[Dialog](../../../ui/arkts-base-dialog-overview.md), [Toast](../../../ui/arkts-create-toast.md), and   
[AlphabetIndexer](alphabet_indexer) components if the background color, blur, and shadow are not set for the components. The immersive system material is enabled by default for the text menu triggered by long-pressing or double-clicking after [copyOption](arkts-arkui-text-textattribute-i.md#copyoption) is set in the [Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md) component.For other components, whether the immersive system material is enabled is set by the application.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialState-DEFAULT = 0--><!--Device-MaterialState-DEFAULT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ENABLE

```TypeScript
ENABLE = 1
```

Enabled state. The immersive system material is enabled by default for the   
[Dialog](../../../ui/arkts-base-dialog-overview.md), [Toast](../../../ui/arkts-create-toast.md),   
[AlphabetIndexer](alphabet_indexer), [ChipGroup](arkts-arkui-advanced-chipgroup.md),   
[Chip](arkts-arkui-advanced-chip.md), [Select](arkts-arkui-select-select-f.md#select), [Menu Control](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md),   
[Toggle](arkts-arkui-toggle-toggle-f.md#toggle), [SegmentButton](arkts-arkui-advanced-segmentbutton.md),   
[SegmentButtonV2](arkts-arkui-advanced-segmentbuttonv2.md), [Slider](arkts-arkui-slider-slider-f.md#slider),   
[bindSheet](arkts-arkui-common-commonmethod-i.md#bindsheet), and [SelectionMenu](arkts-arkui-advanced-selectionmenu.md). After   
[copyOption](arkts-arkui-text-textattribute-i.md#copyoption) is set for the [Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md) component, the immersive system material is enabled by default for the text menu triggered by long-pressing or double-clicking. In this state, the immersive system material style takes precedence over the background color, blur, shadow, and border style set for the components. You need to set whether to enable the immersive system material for other components.

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

