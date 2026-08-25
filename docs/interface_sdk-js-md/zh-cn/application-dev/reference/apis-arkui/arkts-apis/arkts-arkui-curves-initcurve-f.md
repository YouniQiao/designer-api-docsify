# initCurve

## 导入模块

```TypeScript
import { curves } from '@kit.ArkUI';
```

## initCurve

```TypeScript
function initCurve(curve?: Curve): ICurve
```

插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| curve | [Curve](arkts-arkui-curve-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |
