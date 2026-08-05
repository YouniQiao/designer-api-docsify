# MaterialType

Enumerates system material types.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-uiMaterial-enum MaterialType--><!--Device-uiMaterial-enum MaterialType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

No system material effect. The corresponding effects are: [backgroundColor]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and [borderColor]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ are transparent, [borderWidth]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ is 0, and there is no [shadow]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-MaterialType-NONE = 0--><!--Device-MaterialType-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SEMI_TRANSPARENT

```TypeScript
SEMI_TRANSPARENT = 1
```

Semi-transparent system material effect. The corresponding effect is as follows: [backgroundColor]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_: #f2f1f3f5 in light mode and #f2303131 in dark mode. [borderColor]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_: \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ value of **theme.colors.compForegroundPrimary** with 10% transparency. [borderWidth]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_: 1 vp. [shadow]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_: ShadowStyle.OUTER\_DEFAULT\_SM.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-MaterialType-SEMI_TRANSPARENT = 1--><!--Device-MaterialType-SEMI_TRANSPARENT = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## IMMERSIVE

```TypeScript
IMMERSIVE = 2
```

Immersive material type. It is used only by the **type** attribute of the [MaterialInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ API to identify the current material type and does not map to underlying features. The actual material effect is implemented by the [ImmersiveMaterial]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ class.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MaterialType-IMMERSIVE = 2--><!--Device-MaterialType-IMMERSIVE = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

