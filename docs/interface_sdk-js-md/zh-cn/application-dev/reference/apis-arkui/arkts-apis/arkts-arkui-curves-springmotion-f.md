# springMotion

## 导入模块

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## springMotion

```TypeScript
function springMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve
```

构造弹性动画曲线对象。如果对同一对象的同一属性进行多个弹性动画，每个动画会替换掉前一个动画，并继承之前的速度。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
