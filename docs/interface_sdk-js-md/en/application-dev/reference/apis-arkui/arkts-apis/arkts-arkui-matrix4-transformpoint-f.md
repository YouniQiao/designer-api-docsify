# transformPoint

## Modules to Import

```TypeScript
import { matrix4 } from 'kits/@kit.ArkUI';
```

## transformPoint

```TypeScript
function transformPoint(options: [number, number]): [number, number]
```

Matrix的坐标点转换函数，可以将当前的变换效果作用到一个坐标点上。

> **说明：**

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [matrix4.Matrix4Transit.transformPoint](arkts-arkui-matrix4-matrix4transit-i.md#transformpoint)

<!--Device-matrix4-function transformPoint(options: [number, number]): [number, number]--><!--Device-matrix4-function transformPoint(options: [number, number]): [number, number]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [number, number] | Yes | 需要转换的坐标点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [number, number] | 返回矩阵变换后的Point对象。 |

