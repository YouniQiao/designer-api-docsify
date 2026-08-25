# createEffect

## Modules to Import

```TypeScript
import { effectKit } from 'kits/@kit.ArkGraphics2D';
```

## createEffect

```TypeScript
function createEffect(source: image.PixelMap): Filter
```

Creates a Filter instance based on the input PixelMap. You can then add various image effects through chained calls, and finally obtain the processed image via getEffectPixelMap.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | image.PixelMap | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |
