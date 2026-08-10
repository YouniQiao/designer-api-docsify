# initCurve

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## initCurve

```TypeScript
export function initCurve(curve?: Curve): ICurve
```

插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function initCurve(curve?: Curve): ICurve--><!--Device-curves-export function initCurve(curve?: Curve): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| curve | [Curve](arkts-arkui-curve-e.md) | No | 曲线类型。&lt;br/&gt;默认值：Curve.Linear |

**Return value:**

| Type | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) | 曲线的插值对象。 |

