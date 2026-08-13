# ImmersiveMaterial

Immersive material class, which inherits from [Material](arkts-arkui-uimaterial-materialtype-e.md#MaterialType-(System-API)). The performance of an immersive material varies based on device computing power. The high, medium, and low levels of device computing power are determined by device vendors and defined in the system configuration files. On devices with high- and mid-level computing power, the filter and shadow effects of the material layer are affected. On devices with low-level computing power, the background color, border color, border width, and shadow effects are affected. In addition, the effect of the same material is affected by the immersive light configuration in the application. The material parameters and effects vary depending on the immersive light configuration.

**Inheritance/Implementation:** ImmersiveMaterial extends [Material](arkts-arkui-uimaterial-material-c-sys.md#Material-(System-API))

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-uiMaterial-class ImmersiveMaterial--><!--Device-uiMaterial-class ImmersiveMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiMaterial } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ImmersiveOptions)
```

Constructs **ImmersiveMaterial**.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ImmersiveMaterial-constructor(options?: ImmersiveOptions)--><!--Device-ImmersiveMaterial-constructor(options?: ImmersiveOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ImmersiveOptions](arkts-arkui-uimaterial-immersiveoptions-i.md) | No |
