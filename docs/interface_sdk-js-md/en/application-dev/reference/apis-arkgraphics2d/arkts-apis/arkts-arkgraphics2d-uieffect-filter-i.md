# Filter

Filter effect class, used to apply corresponding effects to specified components. Before calling Filter methods, you need to first create a Filter instance through createFilter.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## blur

```TypeScript
blur(blurRadius: number): Filter
```

Adds a blur effect to the component.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## hdrBrightnessRatio

```TypeScript
hdrBrightnessRatio(ratio: number): Filter
```

Adds an HDR (High Dynamic Range) brightening effect to the component content. Nesting is not recommended, as forced nesting may cause overexposure.The brightening effect requires the HDR rendering pipeline to be enabled to take effect. In some scenarios, HDR cannot be enabled even if an attempt is made to trigger the HDR rendering pipeline, for example, when the device hardware specifications do not support HDR.The maximum supported brightness boost multiple is calculated as the device's current maximum brightness divided by its SDR reference white luminance.

> **NOTE：**&gt;
> Using the HDR brightening effect incurs certain performance and power consumption overhead.
> It is recommended to use it in scenarios where HDR images or videos already exist.

**Since:** 24

**Required permissions:** 
- API version 24+: ohos.permission.HDR_BRIGHTNESS

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ratio](../../apis-arkui/arkts-apis/arkts-arkui-componentutils-getitemsinshapepathparams-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |
