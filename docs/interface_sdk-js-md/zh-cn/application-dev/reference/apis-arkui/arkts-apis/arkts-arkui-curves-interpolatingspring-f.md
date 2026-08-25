# interpolatingSpring

## 导入模块

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## interpolatingSpring

```TypeScript
function interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve
```

构造插值器弹簧曲线对象，生成一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。动画时间由曲线参数决定，不受animation、animateTo中的duration参数控制。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| velocity | number | 是 |
| mass | number | 是 |
| [stiffness](../arkts-components/arkts-arkui-chainanimationoptions-i-sys.md) | number | 是 |
| [damping](../arkts-components/arkts-arkui-chainanimationoptions-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ICurve](../arkts-components/arkts-arkui-icurve-i.md) |
