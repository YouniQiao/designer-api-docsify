# translate

## Modules to Import

```TypeScript
import { matrix4 } from 'kits/@kit.ArkUI';
```

## translate

```TypeScript
function translate(options: TranslateOption): Matrix4Transit
```

Matrix的平移函数，可以为当前矩阵增加x轴/y轴/z轴平移效果。

> **说明：**

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [matrix4.Matrix4Transit.translate](arkts-arkui-matrix4-matrix4transit-i.md#translate)

<!--Device-matrix4-function translate(options: TranslateOption): Matrix4Transit--><!--Device-matrix4-function translate(options: TranslateOption): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TranslateOption](arkts-arkui-matrix4-translateoption-i.md) | Yes | 设置平移参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) | 平移后的矩阵对象。 |

