# ContainerReaderInterface

Defines the ContainerReader Component. Used for reading and analyzing container layout information based on size breakpoints in dynamic scenarios. Provides container dimension analysis and breakpoint detection capabilities.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-unnamed-export interface ContainerReaderInterface--><!--Device-unnamed-export interface ContainerReaderInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { BreakpointOptions, ContainerReader, ContainerReaderAttribute } from '@kit.ArkUI';
```

## constructor

```TypeScript
(value: ContainerReaderInfo): ContainerReaderAttribute
```

Sets the container reading configuration for ContainerReader component. Configures the size parameters and breakpoint rules for container layout analysis.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ContainerReaderInterface-(value: ContainerReaderInfo): ContainerReaderAttribute--><!--Device-ContainerReaderInterface-(value: ContainerReaderInfo): ContainerReaderAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ContainerReaderInfo](arkts-arkui-arkui-components-containerreader-containerreaderinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ContainerReaderAttribute](arkts-arkui-arkui-components-containerreader-containerreaderattribute-c.md) |
