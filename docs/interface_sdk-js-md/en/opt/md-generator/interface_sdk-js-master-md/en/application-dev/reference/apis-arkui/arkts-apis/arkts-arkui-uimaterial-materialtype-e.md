# MaterialType

Enumerates system material types.

**Since:** 26.0.0

<!--Device-uiMaterial-enum MaterialType--><!--Device-uiMaterial-enum MaterialType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

No system material effect. The corresponding effects are:   
[backgroundColor](CommonMethod#backgroundColor(value: ResourceColor)) and   
[borderColor](CommonMethod#borderColor) are transparent, [borderWidth](CommonMethod#borderWidth) is 0, and there is no [shadow](CommonMethod#shadow(value: ShadowOptions | ShadowStyle)).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-MaterialType-NONE = 0--><!--Device-MaterialType-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SEMI_TRANSPARENT

```TypeScript
SEMI_TRANSPARENT = 1
```

Semi-transparent system material effect. The corresponding effect is as follows:

[backgroundColor](CommonMethod#backgroundColor(value: ResourceColor)):  
#f2f1f3f5 in light mode and #f2303131 in dark mode.

[borderColor](CommonMethod#borderColor):   
[token](../../../ui/theme_skinning.md#system-default-token-color-values) value of   
**theme.colors.compForegroundPrimary** with 10% transparency. 

[borderWidth](CommonMethod#borderWidth): 1 vp.

[shadow](CommonMethod#shadow(value: ShadowOptions | ShadowStyle)): ShadowStyle.OUTER_DEFAULT_SM.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-MaterialType-SEMI_TRANSPARENT = 1--><!--Device-MaterialType-SEMI_TRANSPARENT = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## IMMERSIVE

```TypeScript
IMMERSIVE = 2
```

Immersive material type. It is used only by the **type** attribute of the   
[MaterialInfo](arkts-arkui-uimaterial-materialinfo-i.md#MaterialInfo) API to identify the current material type and does not map to underlying features. The actual material effect is implemented by the   
[ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md#ImmersiveMaterial) class.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MaterialType-IMMERSIVE = 2--><!--Device-MaterialType-IMMERSIVE = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
