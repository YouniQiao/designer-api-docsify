# createHdrBrightnessBlender（系统接口）

## 导入模块

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## createHdrBrightnessBlender

```TypeScript
function createHdrBrightnessBlender(param: BrightnessBlenderParam): HdrBrightnessBlender
```

创建HdrBrightnessBlender实例用于给组件添加支持HDR的提亮效果。

**起始版本：** 20

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
