# createHdrDarkenBlender（系统接口）

## createHdrDarkenBlender

```TypeScript
function createHdrDarkenBlender(hdrBrightnessRatio: number,
    grayscaleFactor?: [number, number, number]): HdrDarkenBlender
```

创建HdrDarkenBlender实例用于HDR图层的压暗混合效果。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-uiEffect-function createHdrDarkenBlender(hdrBrightnessRatio: double,    grayscaleFactor?: [double, double, double]): HdrDarkenBlender--><!--Device-uiEffect-function createHdrDarkenBlender(hdrBrightnessRatio: double,    grayscaleFactor?: [double, double, double]): HdrDarkenBlender-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hdrBrightnessRatio | number | 是 |
| grayscaleFactor | [number, number, number] | 否 |

**返回值：**

| 类型 |
| --- |
| [HdrDarkenBlender](arkts-arkgraphics2d-uieffect-hdrdarkenblender-i-sys.md) |

## 示例

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';

// 创建HDR压暗混合器实例
let blender: uiEffect.HdrDarkenBlender =
  uiEffect.createHdrDarkenBlender(1.3, [0.299, 0.587, 0.114]);

@Entry
@Component
struct Example {
  build() {
    RelativeContainer() {
      Stack(){
          Text('TextWord')
          Image($r('app.media.screenshot'))
            .width('100%')
            .height('100%')
            .advancedBlendMode(blender)
      }
    }
  }
}
```
