# init

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## init

```TypeScript
function init(curve?: Curve): string
```

插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。建议使用[Curves.initCurve](arkts-arkui-curves-initcurve-f.md#initcurve)替代。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [curves.initCurve](arkts-arkui-curves-initcurve-f.md#initcurve)

<!--Device-curves-function init(curve?: Curve): string--><!--Device-curves-function init(curve?: Curve): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| curve | [Curve](arkts-arkui-curve-e.md) | No | 曲线类型。&lt;br/&gt;默认值：Curve.Linear |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回插值曲线对象。 |

