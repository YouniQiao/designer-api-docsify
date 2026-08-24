# ImmersiveMaterial

Immersive material class, which inherits from [Material](../../apis-arkui/arkts-apis/arkts-arkui-uimaterial-materialtype-e.md).The performance of an immersive material varies based on device computing power. The high, medium, and low levels of device computing power are determined by device vendors and defined in the system configuration files. On devices with high- and mid-level computing power, the filter and shadow effects of the material layer are affected. On devices with low-level computing power, the background color, border color, border width, and shadow effects are affected. In addition, the effect of the same material is affected by the immersive light configuration in the application. The material parameters and effects vary depending on the immersive light configuration.

**Inheritance/Implementation:** ImmersiveMaterial extends [Material](../../apis-arkui/arkts-apis/arkts-arkui-uimaterial-material-c-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-uiMaterial-export class ImmersiveMaterial--><!--Device-uiMaterial-export class ImmersiveMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options?: ImmersiveOptions)
```

Constructs **ImmersiveMaterial**.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImmersiveMaterial-constructor(options?: ImmersiveOptions)--><!--Device-ImmersiveMaterial-constructor(options?: ImmersiveOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ImmersiveOptions](../../apis-arkui/arkts-apis/arkts-arkui-uimaterial-immersiveoptions-i.md) | No | System material configuration options, including the material style and material layer coloring.<br>For details about the default values, see the default values of the parameters in the **ImmersiveOptions** API, that is, **{style:ImmersiveStyle.REGULAR, materialColor:Color.Transparent, colorInvert:false, applyShadow:true, interactive:false, lightEffect:undefined}**. |

