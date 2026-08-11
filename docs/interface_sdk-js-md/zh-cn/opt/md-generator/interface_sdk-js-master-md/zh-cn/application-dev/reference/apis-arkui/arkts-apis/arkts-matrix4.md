# @ohos.matrix4

用于对组件进行[图形变换](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)的各种操作，为组件提供矩阵变换能力，支持对图形进行平移、旋转和缩放等。

Matrix4的使用场景包括：

[图形变换](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)中的[transform](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#transform)接口通过使用图形变换矩阵Matrix4对象显示二维变换时的矩阵变换，[transform3D](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#transform3d)接口通过使用图形变换矩阵Matrix4对象设置组件的三维变换矩阵。

**起始版本：** 7

<!--Device-unnamed-declare namespace matrix4--><!--Device-unnamed-declare namespace matrix4-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 汇总

### 函数

| 名称 |
| --- |
| [combine](arkts-arkui-matrix4-combine-f.md#combine) |
| [copy](arkts-arkui-matrix4-copy-f.md#copy) |
| [identity](arkts-arkui-matrix4-identity-f.md#identity) |
| [init](arkts-arkui-matrix4-init-f.md#init) |
| [invert](arkts-arkui-matrix4-invert-f.md#invert) |
| [rotate](arkts-arkui-matrix4-rotate-f.md#rotate) |
| [scale](arkts-arkui-matrix4-scale-f.md#scale) |
| [transformPoint](arkts-arkui-matrix4-transformpoint-f.md#transformpoint) |
| [translate](arkts-arkui-matrix4-translate-f.md#translate) |

### 接口

| 名称 |
| --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) |
| [Point](arkts-arkui-matrix4-point-i.md) |
| [PolyToPolyOptions](arkts-arkui-matrix4-polytopolyoptions-i.md) |
| [RotateOption](arkts-arkui-matrix4-rotateoption-i.md) |
| [ScaleOption](arkts-arkui-matrix4-scaleoption-i.md) |
| [TranslateOption](arkts-arkui-matrix4-translateoption-i.md) |
