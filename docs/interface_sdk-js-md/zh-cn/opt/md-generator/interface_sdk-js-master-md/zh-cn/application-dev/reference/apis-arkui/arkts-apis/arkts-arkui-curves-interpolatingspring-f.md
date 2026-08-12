# interpolatingSpring

## interpolatingSpring

```TypeScript
function interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve
```

构造插值器弹簧曲线对象，生成一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。动画时间由曲线参数决定，不受animation、animateTo中的duration参数控制。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-curves-function interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve--><!--Device-curves-function interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| velocity | number | 是 |
| mass | number | 是 |
| stiffness | number | 是 |
| damping | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ICurve](arkts-arkui-icurve-t.md) |

## 示例

```TypeScript
import { curves } from '@kit.ArkUI';
curves.interpolatingSpring(10, 1, 228, 30); // 创建一个时长由弹簧参数决定的弹簧插值曲线
```
