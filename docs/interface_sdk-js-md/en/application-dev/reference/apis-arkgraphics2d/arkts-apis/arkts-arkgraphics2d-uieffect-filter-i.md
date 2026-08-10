# Filter

Filter效果类，用于将模糊、边缘像素扩展、水波纹等效果添加到组件上。在调用Filter的方法前，需要先通过[createFilter](arkts-arkgraphics2d-uieffect-createfilter-f.md#createfilter)创建一个Filter实例。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-uiEffect-interface Filter--><!--Device-uiEffect-interface Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## blur

ArkTS-Dyn:
```TypeScript
blur(blurRadius: number): Filter
```

ArkTS-Sta:
```TypeScript
blur(blurRadius: double): Filter
```

将模糊效果添加至组件上。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Filter-blur(blurRadius: double): Filter--><!--Device-Filter-blur(blurRadius: double): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blurRadius | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 模糊半径，单位为px。 取值需大于等于0，模糊半径越大，模糊效果越强。 模糊半径为0时无模糊效果。传入负数时自动修正为0。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 返回挂载了模糊效果的Filter，支持链式调用继续添加其他效果。 |

## Examples

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

ArkTS-Dyn:
```TypeScript
hdrBrightnessRatio(ratio: number): Filter
```

ArkTS-Sta:
```TypeScript
hdrBrightnessRatio(ratio: double): Filter
```

为组件内容添加HDR（高动态范围成像）提亮效果。不建议嵌套使用，强行嵌套使用可能造成过曝现象。

提亮效果需要开启HDR渲染管线才能生效，某些场景下即使尝试触发HDR渲染管线也无法开启HDR，例如：设备硬件规格不支持HDR。

设备当前支持最大提亮倍数为设备当前的最大亮度除以设备SDR参考白亮度得到的值。

> **说明：**
> 
> 使用HDR提亮效果会带来一定的性能功耗开销，建议在已有HDR图片或视频的场景使用。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 24+: ohos.permission.HDR_BRIGHTNESS

<!--Device-Filter-hdrBrightnessRatio(ratio: double): Filter--><!--Device-Filter-hdrBrightnessRatio(ratio: double): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ratio | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 提亮倍数，取值范围为[1.0, 设备当前支持的最大提亮倍数]。 小于1.0按1.0处理；等于1.0不做处理；大于1.0尝试触发HDR渲染管线； 超过最大倍数按最大倍数处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 返回挂载了HDR提亮效果的Filter，支持链式调用继续添加其他效果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | 权限校验失败，应用无权限使用该API，需要申请权限。<br>**Applicable version:** 24 and later |
| 202 | 权限校验失败，非系统应用调用系统接口。<br>**Applicable version:** 20 - 23 |

## Examples

```TypeScript
// Create a Filter instance
let filter: uiEffect.Filter = uiEffect.createFilter();
// Set the HDR brightness ratio to 2.0
filter.hdrBrightnessRatio(2.0);
```

