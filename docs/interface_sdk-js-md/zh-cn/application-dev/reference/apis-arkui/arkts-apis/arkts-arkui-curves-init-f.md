# init

## 导入模块

```TypeScript
import { curves } from '@kit.ArkUI';
```

## init

```TypeScript
function init(curve?: Curve): string
```

插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用[Curves.initCurve](arkts-arkui-curves-initcurve-f.md)替代。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [initCurve](arkts-arkui-curves-initcurve-f.md)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| curve | [Curve](arkts-arkui-curve-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string |
