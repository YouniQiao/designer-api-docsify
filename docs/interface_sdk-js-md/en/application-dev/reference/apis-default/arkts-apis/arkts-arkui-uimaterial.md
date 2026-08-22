# @ohos.arkui.uiMaterial

This module provides APIs for system materials. Different system materials correspond to different UI effects, including the background color, border color, border width, shadow, and material layer filter. The performance of a material object varies on devices with different computing power. The high, medium, and low levels of device computing power are determined by device vendors. For details about the level-based effect, see the description of [ImmersiveMaterial](arkts-uimaterial-immersivematerial-c.md).

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace uiMaterial--><!--Device-unnamed-declare namespace uiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getGlobalMaterialLevel](arkts-uimaterial-getglobalmateriallevel-f.md) | Obtains the global material level, which is related to the device computing power. This configuration item is defined by the device and cannot be modified. |
| [getMaterialInfo](arkts-uimaterial-getmaterialinfo-f.md) | Obtains the material configuration information of this application. The returned configuration information comes from the metadata configured in the [module.json5](../../../quick-start/module-configuration-file.md) file of the application. |
| [isImmersiveMaterialSupported](arkts-uimaterial-isimmersivematerialsupported-f.md) | Check whether [ImmersiveMaterial](arkts-uimaterial-immersivematerial-c.md) is supported on the current device. If it is true, the ImmersiveMaterial object can be used in the systemMaterial attribute. If it is false, setting the ImmersiveMaterial object in the systemMaterial attribute will not take effect. It is defined by the device and cannot be modified. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [convertToECMaterial](arkts-uimaterial-converttoecmaterial-f-sys.md) | Convert from ImmersiveMaterial to another ImmersiveMaterial set on EffectComponent. |
| [convertToECSubMaterial](arkts-uimaterial-converttoecsubmaterial-f-sys.md) | Convert from ImmersiveMaterial to another ImmersiveMaterial set on sub component of EffectComponent. |
<!--DelEnd-->

### Classes

| Name | Description |
| --- | --- |
| [ImmersiveMaterial](arkts-uimaterial-immersivematerial-c.md) | Immersive material class, which inherits from [Material](arkts-uimaterial-materialtype-e.md). |

<!--Del-->
### Classes(System API)

| Name | Description |
| --- | --- |
| [Material](arkts-uimaterial-material-c-sys.md) | Base class of the system material object on the UI. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [ImmersiveOptions](arkts-uimaterial-immersiveoptions-i.md) | Immersive material parameters. |
| [LightEffectOptions](arkts-uimaterial-lighteffectoptions-i.md) | Provides the light sensing interaction feedback configuration for immersive materials. The configuration is used to customize the color of the light sensing feedback. |
| [MaterialInfo](arkts-uimaterial-materialinfo-i.md) | Provides material configuration information, including the material enabling state and material type. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [MaterialOptions](arkts-uimaterial-materialoptions-i-sys.md) | Define the interface containing various material parameters. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ImmersiveStyle](arkts-uimaterial-immersivestyle-e.md) | Enumerates immersive material styles. Different material styles correspond to different material parameters, including the blur degree and brightness. |
| [MaterialLevel](arkts-uimaterial-materiallevel-e.md) | Enumerates the material levels, which indicate the computing power level of the device. Use [getGlobalMaterialLevel](arkts-uimaterial-getglobalmateriallevel-f.md) to obtain the material level of the current device. |
| [MaterialState](arkts-uimaterial-materialstate-e.md) | Enumerates the material enabling states, indicating the states of the application-level immersive system material configuration. |
| [MaterialType](arkts-uimaterial-materialtype-e.md) | Enumerates system material types. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [ImmersiveStyle](arkts-uimaterial-immersivestyle-e-sys.md) | Enumerates immersive material styles. Different material styles correspond to different material parameters, including the blur degree and brightness. |
| [MaterialType](arkts-uimaterial-materialtype-e-sys.md) | Enumerates system material types. |
<!--DelEnd-->

