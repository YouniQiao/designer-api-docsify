# @ohos.arkui.uiMaterial

This module provides APIs for system materials. Different system materials correspond to different UI effects, including the background color ([backgroundColor](CommonMethod#backgroundColor(value: ResourceColor))), border color ([borderColor](CommonMethod#borderColor)), border width ([borderWidth](CommonMethod#borderWidth)), and shadow ([shadow](CommonMethod#shadow(value: ShadowOptions | ShadowStyle))).

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace uiMaterial--><!--Device-unnamed-declare namespace uiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiMaterial } from '@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [convertToECMaterial](arkts-arkui-uimaterial-converttoecmaterial-f.md#converttoecmaterial) |
| [convertToECSubMaterial](arkts-arkui-uimaterial-converttoecsubmaterial-f.md#converttoecsubmaterial) |
| [getGlobalMaterialLevel](arkts-arkui-uimaterial-getglobalmateriallevel-f.md#getglobalmateriallevel) |
| [getMaterialInfo](arkts-arkui-uimaterial-getmaterialinfo-f.md#getmaterialinfo) |
| [isImmersiveMaterialSupported](arkts-arkui-uimaterial-isimmersivematerialsupported-f.md#isimmersivematerialsupported) | Check whether [ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md#ImmersiveMaterial) is supported on the current device.If it is true, the ImmersiveMaterial object can be used in the  [systemMaterial](CommonMethod#systemMaterial(material: SystemUiMaterial \|

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md) | Immersive material class, which inherits from [Material](arkts-arkui-uimaterial-materialtype-e.md#MaterialType).  The performance of an immersive material varies based on device computing power. The high, medium, and low levels of device computing power are determined by device vendors and defined in the system configuration files. On devices with high- and mid-level computing power, the filter and  [shadow](CommonMethod#shadow(value: ShadowOptions \| ShadowStyle)) effects of the material layer are affected.On devices with low-level computing power, the  [background color](CommonMethod#backgroundColor(value: ResourceColor)),  [border color](CommonMethod#borderColor), [border width](CommonMethod#borderWidth), and  [shadow](CommonMethod#shadow(value: ShadowOptions \|
| [Material](arkts-arkui-uimaterial-material-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ImmersiveOptions](arkts-arkui-uimaterial-immersiveoptions-i.md) |
| [LightEffectOptions](arkts-arkui-uimaterial-lighteffectoptions-i.md) |
| [MaterialInfo](arkts-arkui-uimaterial-materialinfo-i.md) |
| [MaterialOptions](arkts-arkui-uimaterial-materialoptions-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ImmersiveStyle](arkts-arkui-uimaterial-immersivestyle-e.md) |
| [MaterialLevel](arkts-arkui-uimaterial-materiallevel-e.md) |
| [MaterialState](arkts-arkui-uimaterial-materialstate-e.md) |
| [MaterialType](arkts-arkui-uimaterial-materialtype-e.md) |
