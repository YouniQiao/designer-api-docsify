# rotate

## Modules to Import

```TypeScript
import { matrix4 } from 'kits/@kit.ArkUI';
```

## rotate

```TypeScript
function rotate(options: RotateOption): Matrix4Transit
```

Matrix的旋转函数，可以为当前矩阵增加x轴/y轴/z轴旋转效果。

> **说明：**

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [matrix4.Matrix4Transit.rotate](arkts-arkui-matrix4-matrix4transit-i.md#rotate)

<!--Device-matrix4-function rotate(options: RotateOption): Matrix4Transit--><!--Device-matrix4-function rotate(options: RotateOption): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RotateOption](arkts-arkui-matrix4-rotateoption-i.md) | Yes | 设置旋转参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) | 旋转后的矩阵对象。 |

