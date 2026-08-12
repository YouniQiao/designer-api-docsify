# stepsCurve

## stepsCurve

```TypeScript
function stepsCurve(count: number, end: boolean): ICurve
```

构造阶梯曲线对象。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-curves-function stepsCurve(count: number, end: boolean): ICurve--><!--Device-curves-function stepsCurve(count: number, end: boolean): ICurve-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | number | 是 |
| end | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [ICurve](arkts-arkui-icurve-t.md) |

## 示例

```TypeScript
import { curves } from '@kit.ArkUI';
curves.stepsCurve(9, true);  // 创建一个阶梯曲线
```
