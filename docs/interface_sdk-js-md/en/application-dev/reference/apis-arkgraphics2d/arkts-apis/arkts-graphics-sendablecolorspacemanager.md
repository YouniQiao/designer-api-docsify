# @ohos.graphics.sendableColorSpaceManager(可共享的色彩管理)

本模块提供管理抽象化色域对象的基础能力，包括可共享的色彩管理的创建与可共享的色域基础属性的获取等。适用于需要在多线程间传递色域信息的场景，能够解决跨线程色彩管理对象无法共享的问题，提高色彩处理的效率和一致性。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare namespace sendableColorSpaceManager--><!--Device-unnamed-declare namespace sendableColorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

## Modules to Import

```TypeScript
import { sendableColorSpaceManager } from 'kits/@kit.ArkGraphics2D';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [create](arkts-arkgraphics2d-sendablecolorspacemanager-create-f.md#create) | 创建标准可共享的色彩管理实例。 |
| [create](arkts-arkgraphics2d-sendablecolorspacemanager-create-f.md#create-1) | 创建用户自定义可共享的色彩管理实例。 |

### Interfaces

| Name | Description |
| --- | --- |
| [ColorSpaceManager](arkts-arkgraphics2d-sendablecolorspacemanager-colorspacemanager-i.md) | 当前可共享的色彩管理实例。ColorSpaceManager是用于管理和操作色域对象的核心类，提供了获取色域类型、白点值、gamma值等功能，并支持在ArkTS并发实例间传递。  下列API示例中都需先使用[create()](arkts-arkgraphics2d-sendablecolorspacemanager-create-f.md#create)获取到ColorSpaceManager实例，再通过此实例调用对应方法。 |

### Types

| Name | Description |
| --- | --- |
| [ISendable](arkts-arkgraphics2d-sendablecolorspacemanager-isendable-t.md) | 为与当前模块的接口规范保持一致，定义了ISendable类型别名。 |

