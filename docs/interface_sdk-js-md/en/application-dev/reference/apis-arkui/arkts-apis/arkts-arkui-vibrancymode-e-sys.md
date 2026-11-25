# VibrancyMode (System API)

```TypeScript
declare enum VibrancyMode
```

Defines the vibrancy modes, which specify whether to apply a brighten or darken effect to the content to improve readability against translucent material backgrounds.

**Since:** 26.1.0

<!--Device-unnamed-declare enum VibrancyMode--><!--Device-unnamed-declare enum VibrancyMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## AUTO

```TypeScript
AUTO = 1
```

Auto mode. When the system material of the component itself or an ancestor component can auto color-invert, the vibrancy effect follows the material's color-invert result (brighten when the material samples a dark color, darken when it samples a light color); otherwise follows the control's dark/light color mode (brighten in dark mode, darken in light mode).

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-VibrancyMode-AUTO = 1--><!--Device-VibrancyMode-AUTO = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## BRIGHTEN

```TypeScript
BRIGHTEN = 2
```

Brighten mode. Fixedly brightens the content to improve readability against dark backgrounds.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-VibrancyMode-BRIGHTEN = 2--><!--Device-VibrancyMode-BRIGHTEN = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## DARKEN

```TypeScript
DARKEN = 3
```

Darken mode. Fixedly darkens the content to improve readability against light backgrounds.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-VibrancyMode-DARKEN = 3--><!--Device-VibrancyMode-DARKEN = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## DISABLED

```TypeScript
DISABLED = 0
```

Vibrancy effect is disabled, the content has no vibrancy effect.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-VibrancyMode-DISABLED = 0--><!--Device-VibrancyMode-DISABLED = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.
