# customCurve

## 导入模块

```TypeScript
import { curves } from '@kit.ArkUI';
```

## customCurve

```TypeScript
function customCurve(interpolate: (fraction: number) => number): ICurve
```

构造自定义曲线对象。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| interpolate | (fraction: number) = & gt; number | 是 |

**返回值：**

| 类型 |
| --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |

**示例**

```TypeScript
import { curves } from '@kit.ArkUI'
let interpolate = (fraction:number):number => {
  return Math.sqrt(fraction)
}
let curve = curves.customCurve(interpolate) // 创建一个用户自定义插值曲线
```
