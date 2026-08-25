# @ohos.graphics.colorSpaceManager(色彩管理)

本模块提供管理抽象化色域对象的基础能力，包括创建标准色域对象（如SRGB、DCI-P3、BT2020等）和自定义色域对象，获取色域类型、白点值、gamma值等属性。适用于需要保证色彩一致性的场景，如图像处理、视频渲染、跨设备色彩显示 等，帮助开发者实现准确的色彩管理和转换，提升应用在色彩显示方面的用户体验。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

## 导入模块

```TypeScript
import { colorSpaceManager } from '@kit.ArkGraphics2D';
```

## 汇总

### 函数

| 名称 |
| --- |
| [create(色彩管理)](arkts-arkgraphics2d-colorspacemanager-create-f.md) |
| [create(色彩管理)](arkts-arkgraphics2d-colorspacemanager-create-f.md) |

### 接口

| 名称 |
| --- |
| [ColorSpaceManager(色彩管理)](arkts-arkgraphics2d-colorspacemanager-colorspacemanager-i.md) |
| [ColorSpacePrimaries(色彩管理)](arkts-arkgraphics2d-colorspacemanager-colorspaceprimaries-i.md) |

### 枚举

| 名称 |
| --- |
| [ColorSpace(色彩管理)](arkts-arkgraphics2d-colorspacemanager-colorspace-e.md) |
