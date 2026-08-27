# @ohos.arkui.uiMaterial

This module provides APIs for system materials. Different system materials correspond to different UI effects, including the background color (backgroundColor), border color (borderColor), border width (borderWidth), and shadow (shadow).

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiMaterial } from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getGlobalMaterialLevel](arkts-arkui-uimaterial-getglobalmateriallevel-f.md) | Obtains the global material level, which is related to the device computing power. This configuration item is defined by the device and cannot be modified. |
| [getMaterialInfo](arkts-arkui-uimaterial-getmaterialinfo-f.md) | Obtains the material configuration information of this application. The returned configuration information comes from the metadata configured in the [module.json5](../../../quick-start/module-configuration-file.md) file of the application. |
| [isImmersiveMaterialSupported](arkts-arkui-uimaterial-isimmersivematerialsupported-f.md) | Check whether [ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md) is supported on the current device. If it is true, the ImmersiveMaterial object can be used in the systemMaterial attribute. If it is false, setting the ImmersiveMaterial object in the systemMaterial attribute will not take effect. It is defined by the device and cannot be modified. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [convertToECMaterial](arkts-arkui-uimaterial-converttoecmaterial-f-sys.md) | Convert from ImmersiveMaterial to another ImmersiveMaterial set on EffectComponent. |
| [convertToECSubMaterial](arkts-arkui-uimaterial-converttoecsubmaterial-f-sys.md) | Convert from ImmersiveMaterial to another ImmersiveMaterial set on sub component of EffectComponent. |
<!--DelEnd-->

### Classes

| Name | Description |
| --- | --- |
| [ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md) | Immersive material class, which inherits from [Material](arkts-arkui-uimaterial-materialtype-e.md). |
| [Material](arkts-arkui-uimaterial-material-c.md) | System material object on the UI. |

<!--Del-->
### Classes(System API)

| Name | Description |
| --- | --- |
| [Material](arkts-arkui-uimaterial-material-c-sys.md) | System material object on the UI. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [ImmersiveOptions](arkts-arkui-uimaterial-immersiveoptions-i.md) | Immersive material parameters. |
| [LightEffectOptions](arkts-arkui-uimaterial-lighteffectoptions-i.md) | Provides the light sensing interaction feedback configuration for immersive materials. The configuration is used to customize the color of the light sensing feedback. |
| [MaterialInfo](arkts-arkui-uimaterial-materialinfo-i.md) | Provides material configuration information, including the material enabling state and material type. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [MaterialOptions](arkts-arkui-uimaterial-materialoptions-i-sys.md) | System material options. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ImmersiveStyle](arkts-arkui-uimaterial-immersivestyle-e.md) | Enumerates immersive material styles. Different material styles correspond to different material parameters, including the blur degree and brightness. |
| [MaterialLevel](arkts-arkui-uimaterial-materiallevel-e.md) | Enumerates the material levels, which indicate the computing power level of the device. Use [getGlobalMaterialLevel](arkts-arkui-uimaterial-getglobalmateriallevel-f.md) to obtain the material level of the current device. |
| [MaterialState](arkts-arkui-uimaterial-materialstate-e.md) | Enumerates the material enabling states, indicating the states of the application-level immersive system material configuration. |
| [MaterialType](arkts-arkui-uimaterial-materialtype-e.md) | Enumerates system material types. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [ImmersiveStyle](arkts-arkui-uimaterial-immersivestyle-e-sys.md) | Enumerates immersive material styles. Different material styles correspond to different material parameters, including the blur degree and brightness. |
| [MaterialType](arkts-arkui-uimaterial-materialtype-e-sys.md) | Enumerates system material types. |
<!--DelEnd-->

## Examples

This example shows how to apply the Material object of a semi-transparent material to a component using the [systemMaterial](../arkui-ts/ts-universal-attributes-image-effect-sys.md#systemmaterial23) attribute.

```TypeScript
import { uiMaterial } from '@kit.ArkUI';

@Entry
@Component
struct SystemMaterialPage {
  build() {
    Column() {
      Stack() {
        Image($r('app.media.bg1')) // Replace $r('app.media.bg1') with the image resource file you use.
          .width('100%')
          .height('100%')

        Column()
          .width(100)
          .height(50)
          .position({ x: 50, y: 350 })
          .systemMaterial(new uiMaterial.Material({ type: uiMaterial.MaterialType.SEMI_TRANSPARENT })) // Use the semi-transparent system material effect.
      }
      .height('90%')
      .width('90%')
    }
    .height('100%')
    .width('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```

Since API version 26.0.0, the uiMaterial.convertToECMaterial and uiMaterial.convertToECSubMaterial APIs are added.

```TypeScript
import { uiMaterial } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State myMaterialBase: uiMaterial.ImmersiveMaterial | undefined = new uiMaterial.ImmersiveMaterial({
    style: uiMaterial.ImmersiveStyle.ULTRA_THIN,
  });
  @State myMaterialEC: uiMaterial.ImmersiveMaterial | undefined = new uiMaterial.ImmersiveMaterial({
    style: uiMaterial.ImmersiveStyle.ULTRA_THIN_EC,
  });
  @State myMaterialECSub: uiMaterial.ImmersiveMaterial | undefined = new uiMaterial.ImmersiveMaterial({
    style: uiMaterial.ImmersiveStyle.ULTRA_THIN_EC_SUB,
  });

  build() {
    Stack() {
      // Replace $r('app.media.startIcon') with the actual resource file.
      Image($r('app.media.startIcon'))
      Row() {
        // It is recommended to use different styles to set materials for EffectComponent and its child components.
        EffectComponent() {
          Row() {
            Column()
              .width(100)
              .height(100)
              .systemMaterial(this.myMaterialECSub)
              .margin(5)
          }
        }
        .systemMaterial(this.myMaterialEC)

        EffectComponent() {
          Row() {
            Column()
              .width(100)
              .height(100)
              .systemMaterial(uiMaterial.convertToECSubMaterial(this.myMaterialBase))
              .margin(5)

            Column()
              .width(100)
              .height(100)
              .systemMaterial(uiMaterial.convertToECSubMaterial(this.myMaterialBase))
              .margin(5)
          }
        }
        .systemMaterial(uiMaterial.convertToECMaterial(this.myMaterialBase))
      }.height('100%').width('100%').justifyContent(FlexAlign.Center)
    }
  }
}
```
