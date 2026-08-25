# DragPreview

拖拽背板的对象，在OnDrop和OnDragEnd回调中使用不生效。

**起始版本：** 11

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## animate

```TypeScript
animate(options: AnimationOptions, handler: () =>void): void
```

设置背板蒙版颜色变化动效，在OnDrop和OnDragEnd回调中使用不生效，仅支持通过 [getDragPreview()](arkts-arkui-arkui-uicontext-dragcontroller-c.md#getdragpreview)方法获取到的 对象上使用。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AnimationOptions](arkts-arkui-arkui-drawabledescriptor-animationoptions-i.md) | 是 |
| handler | () = & gt;void | 是 |

## setForegroundColor

```TypeScript
setForegroundColor(color: ResourceColor): void
```

设置背板蒙版颜色，在OnDrop和OnDragEnd回调中使用不生效，仅支持通过 [getDragPreview()](arkts-arkui-arkui-uicontext-dragcontroller-c.md#getdragpreview)方法获取到的 对象上使用。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) | 是 |
