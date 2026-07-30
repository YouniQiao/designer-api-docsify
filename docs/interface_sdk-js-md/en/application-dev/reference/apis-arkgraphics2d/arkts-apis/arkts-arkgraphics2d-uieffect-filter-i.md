# Filter

The Filter for Component.

**Since:** 12

<!--Device-uiEffect-interface Filter--><!--Device-uiEffect-interface Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## blur

```TypeScript
blur(blurRadius: number): Filter
```

Set blur effect of the Component.

**Since:** 12

<!--Device-Filter-blur(blurRadius: double): Filter--><!--Device-Filter-blur(blurRadius: double): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blurRadius | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | @syscap SystemCapability.Graphics.Drawing |

**Example**

```TypeScript
// xxx.ts
import { uiEffect } from '@kit.ArkGraphics2D';

// Create a Filter instance
let filter: uiEffect.Filter = uiEffect.createFilter();
// Set the blur radius to 10px
filter.blur(10);

@Entry
@Component
struct UIEffectFilterExample {
    build() {
        Column({ space: 15 }) {
            Text('UIEffectFilter').fontSize(20).width('75%').fontColor('#DCDCDC')
            Image($r('app.media.foreground'))
                .width(100)
                .height(100)
                .backgroundImage($r('app.media.background'))
                .backgroundImagePosition(Alignment.Center)
                .backgroundImageSize({ width: 90, height: 90 })
                // Apply the Filter effect to the component background
                .backgroundFilter(filter)
        }
        .height('100%')
        .width('100%')
    }
}

```

## hdrBrightnessRatio

```TypeScript
hdrBrightnessRatio(ratio: number): Filter
```

Applies a high dynamic range (HDR) brightness enhancement filter to the component.

**Since:** 24

**Required permissions:** 
- API version 24+: ohos.permission.HDR_BRIGHTNESS

<!--Device-Filter-hdrBrightnessRatio(ratio: double): Filter--><!--Device-Filter-hdrBrightnessRatio(ratio: double): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ratio | number | Yes | The brightness multiplier ratio (1.0 = original, >1.0 = brighter). |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | - Returns hdr brightness Filter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 20 - 23 |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API.<br>**Applicable version:** 24 and later |

**Example**

```TypeScript
// Create a Filter instance
let filter: uiEffect.Filter = uiEffect.createFilter();
// Set the HDR brightness ratio to 2.0
filter.hdrBrightnessRatio(2.0);

```

