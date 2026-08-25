# DynamicLayout

## Modules to Import

```TypeScript
import { DynamicLayout, DynamicLayoutAttribute } from '@kit.ArkUI';
```

## DynamicLayout

```TypeScript
export declare function DynamicLayout (
    algorithm: LayoutAlgorithm, 
    content_: CustomBuilder,
): DynamicLayoutAttribute
```

Defines DynamicLayout Component.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md) | Yes |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DynamicLayoutAttribute](arkts-arkui-arkui-components-arkdynamiclayout-dynamiclayoutattribute-c.md) |
