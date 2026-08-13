# cubicBezierCurve

## cubicBezierCurve

```TypeScript
function cubicBezierCurve(x1: number, y1: number, x2: number, y2: number): ICurve
```

构造三阶贝塞尔曲线对象，确保曲线的值在0到1之间。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-curves-function cubicBezierCurve(x1: number, y1: number, x2: number, y2: number): ICurve--><!--Device-curves-function cubicBezierCurve(x1: number, y1: number, x2: number, y2: number): ICurve-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x1 | number | 是 |
| y1 | number | 是 |
| x2 | number | 是 |
| y2 | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ICurve](../../apis-na/arkts-apis/arkts-na-icurve-t.md) |

## 示例

```TypeScript
import { curves } from '@kit.ArkUI';
curves.cubicBezierCurve(0.1, 0.0, 0.1, 1.0); // 创建一个三阶贝塞尔曲线
```
