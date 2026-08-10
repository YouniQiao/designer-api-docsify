# init

## Modules to Import

```TypeScript
import { matrix4 } from 'kits/@kit.ArkUI';
```

## init

```TypeScript
function init(options: [
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double
    ]): Matrix4Transit
```

Matrix的构造函数，可以通过传入的参数创建一个四阶矩阵，矩阵为列优先。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-matrix4-function init(options: [        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double    ]): Matrix4Transit--><!--Device-matrix4-function init(options: [        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double    ]): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [         double,         double,         double,         double,         double,         double,         double,         double,         double,         double,         double,         double,         double,         double,         double,         double     ] | Yes | 参数为长度为16（4*4）的number数组, 详情见四阶矩阵说明。&lt;br/&gt;各number取值范围：(-∞, +∞)&lt;br/&gt;默认值：&lt;br/&gt; [1, 0, 0, 0,&lt;br/&gt;0, 1, 0, 0,&lt;br/&gt;0, 0, 1, 0,&lt;br/&gt;0, 0, 0, 1] |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) | 根据入参创建的四阶矩阵对象。 |

