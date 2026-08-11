# Filter

Filter效果类，用于将模糊、边缘像素扩展、水波纹等效果添加到组件上。在调用Filter的方法前，需要先通过[createFilter](arkts-arkgraphics2d-uieffect-createfilter-f.md#createfilter)创建一个Filter实例。

**起始版本：** 12

<!--Device-uiEffect-interface Filter--><!--Device-uiEffect-interface Filter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## blur

```TypeScript
blur(blurRadius: number): Filter
```

将模糊效果添加至组件上。

**起始版本：** 12

<!--Device-Filter-blur(blurRadius: double): Filter--><!--Device-Filter-blur(blurRadius: double): Filter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| blurRadius | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## 示例

```TypeScript
// xxx.ts
import { uiEffect } from '@kit.ArkGraphics2D';

// 创建Filter实例
let filter: uiEffect.Filter = uiEffect.createFilter();
// 设置模糊半径为10px
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
                // 将Filter效果应用到组件背景
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

为组件内容添加HDR（高动态范围成像）提亮效果。不建议嵌套使用，强行嵌套使用可能造成过曝现象。

提亮效果需要开启HDR渲染管线才能生效，某些场景下即使尝试触发HDR渲染管线也无法开启HDR，例如：设备硬件规格不支持HDR。

设备当前支持最大提亮倍数为设备当前的最大亮度除以设备SDR参考白亮度得到的值。

> **说明：**
> 
> 使用HDR提亮效果会带来一定的性能功耗开销，建议在已有HDR图片或视频的场景使用。

**起始版本：** 24

**需要权限：** 
- API版本24+：ohos.permission.HDR_BRIGHTNESS

<!--Device-Filter-hdrBrightnessRatio(ratio: double): Filter--><!--Device-Filter-hdrBrightnessRatio(ratio: double): Filter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ratio | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
// 创建Filter实例
let filter: uiEffect.Filter = uiEffect.createFilter();
// 设置HDR提亮倍数为2.0
filter.hdrBrightnessRatio(2.0);
```
