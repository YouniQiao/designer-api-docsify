# DragPreview

Provides the functions of setting color or updating animation.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-dragController-export class DragPreview--><!--Device-dragController-export class DragPreview-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## animate

```TypeScript
animate(options: AnimationOptions, handler: () => void): void
```

update preview style with animation

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragPreview-animate(options: AnimationOptions, handler: () => void): void--><!--Device-DragPreview-animate(options: AnimationOptions, handler: () => void): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AnimationOptions](arkts-arkui-arkui-drawabledescriptor-animationoptions-i.md) | 是 | animation options |
| handler | () =&gt; void | 是 | change style functions |

## setForegroundColor

```TypeScript
setForegroundColor(color: ResourceColor): void
```

change foreground color of preview

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragPreview-setForegroundColor(color: ResourceColor): void--><!--Device-DragPreview-setForegroundColor(color: ResourceColor): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) | 是 | color value |

