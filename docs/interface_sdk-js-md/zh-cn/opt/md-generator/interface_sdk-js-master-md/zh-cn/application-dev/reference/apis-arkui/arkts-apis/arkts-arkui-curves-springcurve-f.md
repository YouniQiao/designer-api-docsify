# springCurve

## 导入模块

```TypeScript
```

## springCurve

```TypeScript
function springCurve(velocity: number, mass: number, stiffness: number, damping: number): ICurve
```

构造弹簧曲线对象，曲线形状由弹簧参数决定，动画时长受animation、animateTo中的duration参数控制。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-curves-function springCurve(velocity: number, mass: number, stiffness: number, damping: number): ICurve--><!--Device-curves-function springCurve(velocity: number, mass: number, stiffness: number, damping: number): ICurve-End-->

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
| [ICurve](../../apis-na/arkts-apis/arkts-na-icurve-t.md) |

**示例**

```TypeScript
import { curves } from '@kit.ArkUI';
curves.springCurve(10, 1, 228, 30); // 创建一个弹簧插值曲线
```
