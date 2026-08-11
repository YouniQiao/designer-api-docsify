# @ohos.arkui.uiMaterial

This module provides APIs for system materials. Different system materials correspond to different UI effects, including the [background color](arkts-arkui-common-commonmethod-i.md#backgroundcolor),   
[border color](arkts-arkui-common-commonmethod-i.md#bordercolor), [border width](arkts-arkui-common-commonmethod-i.md#borderwidth),   
[shadow](arkts-arkui-common-commonmethod-i.md#shadow), and material layer filter. The performance of a material object varies on devices with different computing power. The high, medium, and low levels of device computing power are determined by device vendors. For details about the level-based effect, see the description of   
[ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace uiMaterial--><!--Device-unnamed-declare namespace uiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiMaterial } from 'kits/@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [convertToECMaterial](arkts-arkui-uimaterial-converttoecmaterial-f.md#converttoecmaterial) | Convert from ImmersiveMaterial to another ImmersiveMaterial set on EffectComponent. |
| [convertToECSubMaterial](arkts-arkui-uimaterial-converttoecsubmaterial-f.md#converttoecsubmaterial) | Convert from ImmersiveMaterial to another ImmersiveMaterial set on sub component of EffectComponent. |
| [getGlobalMaterialLevel](arkts-arkui-uimaterial-getglobalmateriallevel-f.md#getglobalmateriallevel) | Obtains the global material level, which is related to the device computing power. This configuration item is defined by the device and cannot be modified. |
| [getMaterialInfo](arkts-arkui-uimaterial-getmaterialinfo-f.md#getmaterialinfo) | Obtains the material configuration information of this application. The returned configuration information comes from the metadata configured in the [module.json5](../../../quick-start/module-configuration-file.md) file of the application. |
| [isImmersiveMaterialSupported](arkts-arkui-uimaterial-isimmersivematerialsupported-f.md#isimmersivematerialsupported) | Check whether [ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md) is supported on the current device.If it is true, the ImmersiveMaterial object can be used in the  [systemMaterial](arkts-arkui-common-commonmethod-i.md#systemmaterial) attribute.If it is false, setting the ImmersiveMaterial object in the systemMaterial attribute will not take effect.It is defined by the device and cannot be modified. |

### Classes

| Name | Description |
| --- | --- |
| [ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md) | Immersive material class, which inherits from [Material](arkts-arkui-uimaterial-materialtype-e.md).  The performance of an immersive material varies based on device computing power. The high, medium, and low levels of device computing power are determined by device vendors and defined in the system configuration files. On devices with high- and mid-level computing power, the filter and  [shadow](arkts-arkui-common-commonmethod-i.md#shadow) effects of the material layer are affected.On devices with low-level computing power, the  [background color](arkts-arkui-common-commonmethod-i.md#backgroundcolor),  [border color](arkts-arkui-common-commonmethod-i.md#bordercolor), [border width](arkts-arkui-common-commonmethod-i.md#borderwidth), and  [shadow](arkts-arkui-common-commonmethod-i.md#shadow) effects are affected. In addition, the effect of the same material is affected by the immersive light configuration in the application. The material parameters and effects vary depending on the immersive light configuration. |
| [Material](arkts-arkui-uimaterial-material-c.md) | Base class of the system material object on the UI. |

### Interfaces

| Name | Description |
| --- | --- |
| [ImmersiveOptions](arkts-arkui-uimaterial-immersiveoptions-i.md) | Immersive material parameters. |
| [LightEffectOptions](arkts-arkui-uimaterial-lighteffectoptions-i.md) | Provides the light sensing interaction feedback configuration for immersive materials. The configuration is used to customize the color of the light sensing feedback. |
| [MaterialInfo](arkts-arkui-uimaterial-materialinfo-i.md) | Provides material configuration information, including the material enabling state and material type. |
| [MaterialOptions](arkts-arkui-uimaterial-materialoptions-i.md) | Define the interface containing various material parameters. |

### Enums

| Name | Description |
| --- | --- |
| [ImmersiveStyle](arkts-arkui-uimaterial-immersivestyle-e.md) | Enumerates immersive material styles. Different material styles correspond to different material parameters, including the blur degree and brightness. |
| [MaterialLevel](arkts-arkui-uimaterial-materiallevel-e.md) | Enumerates the material levels, which indicate the computing power level of the device.Use [getGlobalMaterialLevel](arkts-arkui-uimaterial-getglobalmateriallevel-f.md#getglobalmateriallevel) to obtain the material level of the current device. |
| [MaterialState](arkts-arkui-uimaterial-materialstate-e.md) | Enumerates the material enabling states, indicating the states of the application-level immersive system material configuration. |
| [MaterialType](arkts-arkui-uimaterial-materialtype-e.md) | Enumerates system material types. |

