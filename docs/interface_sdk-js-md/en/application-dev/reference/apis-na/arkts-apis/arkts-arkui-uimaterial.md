# @ohos.arkui.uiMaterial

This module provides APIs for system materials. Different system materials correspond to different UI effects, including the background color, border color, border width, shadow, and material layer filter. The performance of a material object varies on devices with different computing power. The high, medium, and low levels of device computing power are determined by device vendors. For details about the level-based effect, see the description of [ImmersiveMaterial](../../apis-arkui/arkts-apis/arkts-arkui-uimaterial-immersivematerial-c.md#immersivematerial).

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

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
| [getGlobalMaterialLevel](arkts-na-uimaterial-getglobalmateriallevel-f.md#getglobalmateriallevel) | Obtains the global material level, which is related to the device computing power. This configuration item is defined by the device and cannot be modified. |
| [getMaterialInfo](arkts-na-uimaterial-getmaterialinfo-f.md#getmaterialinfo) | Obtains the material configuration information of this application. The returned configuration information comes from the metadata configured in the [module.json5](../../../quick-start/module-configuration-file.md) file of the application. |
| [isImmersiveMaterialSupported](arkts-na-uimaterial-isimmersivematerialsupported-f.md#isimmersivematerialsupported) | Check whether [ImmersiveMaterial](../../apis-arkui/arkts-apis/arkts-arkui-uimaterial-immersivematerial-c.md#immersivematerial) is supported on the current device. If it is true, the ImmersiveMaterial object can be used in the systemMaterial attribute. If it is false, setting the ImmersiveMaterial object in the systemMaterial attribute will not take effect. It is defined by the device and cannot be modified. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [convertToECMaterial](arkts-na-uimaterial-converttoecmaterial-f-sys.md#converttoecmaterial-system-api) | Convert from ImmersiveMaterial to another ImmersiveMaterial set on EffectComponent. |
| [convertToECSubMaterial](arkts-na-uimaterial-converttoecsubmaterial-f-sys.md#converttoecsubmaterial-system-api) | Convert from ImmersiveMaterial to another ImmersiveMaterial set on sub component of EffectComponent. |
<!--DelEnd-->

### Classes

| Name | Description |
| --- | --- |
| [ImmersiveMaterial](arkts-na-uimaterial-immersivematerial-c.md) | Immersive material class, which inherits from [Material](../../apis-arkui/arkts-apis/arkts-arkui-uimaterial-materialtype-e.md#materialtype-system-api). The performance of an immersive material varies based on device computing power. The high, medium, and low levels of device computing power are determined by device vendors and defined in the system configuration files. On devices with high- and mid-level computing power, the filter and shadow effects of the material layer are affected. On devices with low-level computing power, the background color, border color, border width, and shadow effects are affected. In addition, the effect of the same material is affected by the immersive light configuration in the application. The material parameters and effects vary depending on the immersive light configuration. |

<!--Del-->
### Classes（系统接口）

| Name | Description |
| --- | --- |
| [Material](arkts-na-uimaterial-material-c-sys.md) | Base class of the system material object on the UI. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [ImmersiveOptions](arkts-na-uimaterial-immersiveoptions-i.md) | Immersive material parameters. |
| [LightEffectOptions](arkts-na-uimaterial-lighteffectoptions-i.md) | Provides the light sensing interaction feedback configuration for immersive materials. The configuration is used to customize the color of the light sensing feedback. |
| [MaterialInfo](arkts-na-uimaterial-materialinfo-i.md) | Provides material configuration information, including the material enabling state and material type. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [MaterialOptions](arkts-na-uimaterial-materialoptions-i-sys.md) | Define the interface containing various material parameters. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ImmersiveStyle](arkts-na-uimaterial-immersivestyle-e.md) | Enumerates immersive material styles. Different material styles correspond to different material parameters, including the blur degree and brightness. |
| [MaterialLevel](arkts-na-uimaterial-materiallevel-e.md) | Enumerates the material levels, which indicate the computing power level of the device. Use [getGlobalMaterialLevel](../../apis-arkui/arkts-apis/arkts-arkui-uimaterial-getglobalmateriallevel-f.md#getglobalmateriallevel) to obtain the material level of the current device. |
| [MaterialState](arkts-na-uimaterial-materialstate-e.md) | Enumerates the material enabling states, indicating the states of the application-level immersive system material configuration. |
| [MaterialType](arkts-na-uimaterial-materialtype-e.md) | Enumerates system material types. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [ImmersiveStyle](arkts-na-uimaterial-immersivestyle-e-sys.md) | Enumerates immersive material styles. Different material styles correspond to different material parameters, including the blur degree and brightness. |
| [MaterialType](arkts-na-uimaterial-materialtype-e-sys.md) | Enumerates system material types. |
<!--DelEnd-->

