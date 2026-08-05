# ImmersiveMaterial

Immersive material class, which inherits from [Material]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. The performance of an immersive material varies based on device computing power. The high, medium, and low levels of device computing power are determined by device vendors and defined in the system configuration files. On devices with high- and mid-level computing power, the filter and [shadow]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ effects of the material layer are affected. On devices with low-level computing power, the [background color]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, [border color]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_, [border width]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_, and [shadow]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ effects are affected. In addition, the effect of the same material is affected by the immersive light configuration in the application. The material parameters and effects vary depending on the immersive light configuration.

**Inheritance/Implementation:** ImmersiveMaterial extends [Material](arkts-na-uimaterial-material-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-uiMaterial-export class ImmersiveMaterial extends Material--><!--Device-uiMaterial-export class ImmersiveMaterial extends Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: ImmersiveOptions)
```

Constructs **ImmersiveMaterial**.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImmersiveMaterial-constructor(options?: ImmersiveOptions)--><!--Device-ImmersiveMaterial-constructor(options?: ImmersiveOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | System material configuration options, including the material style and material layer coloring.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_For details about the default values, see the default values of the parameters in the **ImmersiveOptions** API, that is,**{style:ImmersiveStyle.REGULAR, materialColor:Color.Transparent, colorInvert:false, applyShadow:true, interactive:false, lightEffect:undefined}**. |

