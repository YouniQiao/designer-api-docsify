# spring

## 导入模块

```TypeScript
import { curves } from '@kit.ArkUI';
```

## spring

```TypeScript
function spring(velocity: number, mass: number, stiffness: number, damping: number): string
```

构造弹簧曲线对象。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用[Curves.springCurve](arkts-arkui-curves-springcurve-f.md)替代。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [springCurve](arkts-arkui-curves-springcurve-f.md)

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
| string |
