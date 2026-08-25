# @ohos.matrix4

用于对组件进行图形变换的各种操作，为组件提供矩阵变换能力，支持对图形进行平移、旋转和缩放等。Matrix4的使用场景包括：  
图形变换中的transform接口通过使用图形变换矩阵Matrix4对象显示二维 变换时的矩阵变换，transform3D接口通过使用图形变换矩阵Matrix4对象设置组件的三维变换矩阵。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { matrix4 } from '@kit.ArkUI';
```

## 汇总

### 函数

| 名称 |
| --- |
| [combine](arkts-arkui-matrix4-combine-f.md) |
| [copy](arkts-arkui-matrix4-copy-f.md) |
| [identity](arkts-arkui-matrix4-identity-f.md) |
| [init](arkts-arkui-matrix4-init-f.md) |
| [invert](arkts-arkui-matrix4-invert-f.md) |
| [rotate](arkts-arkui-matrix4-rotate-f.md) |
| [scale](arkts-arkui-matrix4-scale-f.md) |
| [transformPoint](arkts-arkui-matrix4-transformpoint-f.md) |
| [translate](arkts-arkui-matrix4-translate-f.md) |

### 接口

| 名称 |
| --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) |
| [Point](arkts-arkui-matrix4-point-i.md) |
| [PolyToPolyOptions](arkts-arkui-matrix4-polytopolyoptions-i.md) |
| [RotateOption](arkts-arkui-matrix4-rotateoption-i.md) |
| [ScaleOption](arkts-arkui-matrix4-scaleoption-i.md) |
| [TranslateOption](arkts-arkui-matrix4-translateoption-i.md) |
