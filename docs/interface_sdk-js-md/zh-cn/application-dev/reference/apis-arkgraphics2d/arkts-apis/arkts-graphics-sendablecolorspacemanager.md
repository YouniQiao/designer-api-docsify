# @ohos.graphics.sendableColorSpaceManager(可共享的色彩管理)

本模块提供管理抽象化色域对象的基础能力，包括可共享的色彩管理的创建与可共享的色域基础属性的获取等。适用于需要在多线程间传递色域信息的场景，能够解决跨线程色彩管理对象无法共享的问题，提高色彩处理的效率和一致性。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

## 导入模块

```TypeScript
import { sendableColorSpaceManager } from '@kit.ArkGraphics2D';
```

## 汇总

### 函数

| 名称 |
| --- |
| [create(可共享的色彩管理)](arkts-arkgraphics2d-sendablecolorspacemanager-create-f.md) |
| [create(可共享的色彩管理)](arkts-arkgraphics2d-sendablecolorspacemanager-create-f.md) |

### 接口

| 名称 |
| --- |
| [ColorSpaceManager(可共享的色彩管理)](arkts-arkgraphics2d-sendablecolorspacemanager-colorspacemanager-i.md) |

### 类型

| 名称 |
| --- |
| [ISendable(可共享的色彩管理)](arkts-arkgraphics2d-sendablecolorspacemanager-isendable-t.md) |
