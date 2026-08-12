# createHdrBrightnessBlender（系统接口）

## createHdrBrightnessBlender

```TypeScript
function createHdrBrightnessBlender(param: BrightnessBlenderParam): HdrBrightnessBlender
```

创建HdrBrightnessBlender实例用于给组件添加支持HDR的提亮效果。

**起始版本：** 20

<!--Device-uiEffect-function createHdrBrightnessBlender(param: BrightnessBlenderParam): HdrBrightnessBlender--><!--Device-uiEffect-function createHdrBrightnessBlender(param: BrightnessBlenderParam): HdrBrightnessBlender-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | [BrightnessBlenderParam](arkts-arkgraphics2d-graphics-uieffect-brightnessblenderparam-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [HdrBrightnessBlender](arkts-arkgraphics2d-uieffect-hdrbrightnessblender-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';

// 创建支持HDR的BrightnessBlender实例
let blender: uiEffect.HdrBrightnessBlender =
  uiEffect.createHdrBrightnessBlender({cubicRate:1.0, quadraticRate:1.0, linearRate:1.0, degree:1.0, saturation:1.0,
    positiveCoefficient:[2.3, 4.5, 2.0], negativeCoefficient:[0.5, 2.0, 0.5], fraction:0.0});

@Entry
@Component
struct Example {
  build() {
    RelativeContainer() {
      Image($r('app.media.screenshot'))
        .width('100%')
        .height('100%')
        .advancedBlendMode(blender)
    }
  }
}
```
