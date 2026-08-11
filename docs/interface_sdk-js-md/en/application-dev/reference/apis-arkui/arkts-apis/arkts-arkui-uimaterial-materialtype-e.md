# MaterialType

Enumerates system material types.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-uiMaterial-export enum MaterialType--><!--Device-uiMaterial-export enum MaterialType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

Material type with no effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialType-NONE = 0--><!--Device-MaterialType-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SEMI_TRANSPARENT

```TypeScript
SEMI_TRANSPARENT = 1
```

Material type for semitransparent style. It includes predefined backgroundColor, border, and shadow effects.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialType-SEMI_TRANSPARENT = 1--><!--Device-MaterialType-SEMI_TRANSPARENT = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## IMMERSIVE

```TypeScript
IMMERSIVE = 2
```

Immersive material type. It is used only by the **type** attribute of the   
[MaterialInfo](arkts-arkui-uimaterial-materialinfo-i.md) API to identify the current material type and does not map to underlying features. The actual material effect is implemented by the   
[ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md) class.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialType-IMMERSIVE = 2--><!--Device-MaterialType-IMMERSIVE = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

