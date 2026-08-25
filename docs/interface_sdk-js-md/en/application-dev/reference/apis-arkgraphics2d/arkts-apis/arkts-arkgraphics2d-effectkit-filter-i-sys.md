# Filter

An image effect class used to add a specified effect to the effect chain through chained calls. It is suitable for scenarios such as image filter processing, visual effect enhancement, and image beautification. Before calling the methods of Filter, you need to create a Filter instance via createEffect. After adding effects, you need to call getEffectPixelMap to obtain the processed image.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { effectKit } from 'kits/@kit.ArkGraphics2D';
```

## ellipticalGradientBlur

```TypeScript
ellipticalGradientBlur(blurRadius: number, center: EllipticalMaskCenter,
      maskRadius: EllipticalMaskRadius, fractionStops: FractionStop[]): Filter
```

Adds the elliptical gradient blur effect to the filter linked list, and returns the head node of the linked list.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | Yes |
| center | [EllipticalMaskCenter](arkts-arkgraphics2d-effectkit-ellipticalmaskcenter-t-sys.md) | Yes |
| maskRadius | [EllipticalMaskRadius](arkts-arkgraphics2d-effectkit-ellipticalmaskradius-t-sys.md) | Yes |
| [fractionStops](../../apis-arkui/arkts-components/arkts-arkui-lineargradientbluroptions-i.md) | [FractionStop](../../apis-arkui/arkts-components/arkts-arkui-fractionstop-t.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
