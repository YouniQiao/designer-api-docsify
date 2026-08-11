# responsiveSpringMotion

## responsiveSpringMotion

```TypeScript
function responsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve
```

构造弹性跟手动画曲线对象，是[springMotion](arkts-arkui-curves-springmotion-f.md#springmotion)的一种特例，仅默认参数不同，可与springMotion混合使用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-curves-function responsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve--><!--Device-curves-function responsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| response | number | 否 |
| dampingFraction | number | 否 |
| overlapDuration | number | 否 |

**返回值：**

| 类型 |
| --- |
| [ICurve](../arkts-components/arkts-arkui-icurve-i.md) |

## 示例

```TypeScript
import { curves } from '@kit.ArkUI';
curves.responsiveSpringMotion(); // 创建一个默认弹性跟手动画曲线
```
