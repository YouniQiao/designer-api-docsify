# customCurve

## 导入模块

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## customCurve

```TypeScript
function customCurve(interpolate: (fraction: number) => number): ICurve
```

构造自定义曲线对象。

**起始版本：** 10

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
| [ICurve](../arkts-components/arkts-arkui-icurve-i.md) |
