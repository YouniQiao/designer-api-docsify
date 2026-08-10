# combine

## Modules to Import

```TypeScript
import { matrix4 } from 'kits/@kit.ArkUI';
```

## combine

```TypeScript
function combine(options: Matrix4Transit): Matrix4Transit
```

Matrix的叠加函数，可以将两个矩阵的效果叠加起来生成一个新的矩阵对象。

> **说明：**

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [matrix4.Matrix4Transit.combine](arkts-arkui-matrix4-matrix4transit-i.md#combine)

<!--Device-matrix4-function combine(options: Matrix4Transit): Matrix4Transit--><!--Device-matrix4-function combine(options: Matrix4Transit): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) | Yes | 待叠加的矩阵对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) | 叠加后的矩阵对象。 |

