# @ohos.matrix4

用于对组件进行[图形变换](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)的各种操作，为组件提供矩阵变换能力，支持对图形进行平移、旋转和缩放等。

Matrix4的使用场景包括：

[图形变换](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)中的[transform](arkts-arkui-common-commonmethod-i.md#transform)接口通过使用图形变换矩阵Matrix4对象显示二维变换时的矩阵变换，[transform3D](arkts-arkui-common-commonmethod-i.md#transform3d)接口通过使用图形变换矩阵Matrix4对象设置组件的三维变换矩阵。

> **说明：**
> 
> - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace matrix4--><!--Device-unnamed-declare namespace matrix4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { matrix4 } from 'kits/@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [identity](arkts-arkui-matrix4-identity-f.md#identity) | Matrix的初始化函数，可以返回一个单位矩阵对象。 |
| [init](arkts-arkui-matrix4-init-f.md#init) | Matrix的构造函数，可以通过传入的参数创建一个四阶矩阵，矩阵为列优先。 |

### Interfaces

| Name | Description |
| --- | --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) | 矩阵对象。 |
| [Point](arkts-arkui-matrix4-point-i.md) | 坐标点的数据结构。 |
| [PolyToPolyOptions](arkts-arkui-matrix4-polytopolyoptions-i.md) | 多边形到多边形的映射选项。 |
| [RotateOption](arkts-arkui-matrix4-rotateoption-i.md) | 旋转参数。 |
| [ScaleOption](arkts-arkui-matrix4-scaleoption-i.md) | 缩放参数。 |
| [TranslateOption](arkts-arkui-matrix4-translateoption-i.md) | 平移参数。 |

