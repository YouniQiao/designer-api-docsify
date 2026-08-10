# scale

## Modules to Import

```TypeScript
import { matrix4 } from 'kits/@kit.ArkUI';
```

## scale

```TypeScript
function scale(options: ScaleOption): Matrix4Transit
```

Matrix的缩放函数，可以为当前矩阵增加x轴/y轴/z轴缩放效果。

> **说明：**

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [matrix4.Matrix4Transit.scale](arkts-arkui-matrix4-matrix4transit-i.md#scale)

<!--Device-matrix4-function scale(options: ScaleOption): Matrix4Transit--><!--Device-matrix4-function scale(options: ScaleOption): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ScaleOption](arkts-arkui-matrix4-scaleoption-i.md) | Yes | 设置缩放参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) | 缩放后的矩阵对象。 |

