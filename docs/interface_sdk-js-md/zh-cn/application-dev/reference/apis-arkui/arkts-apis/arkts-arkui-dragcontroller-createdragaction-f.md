# createDragAction

## 导入模块

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## createDragAction

```TypeScript
function createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: DragInfo): DragAction
```

创建拖拽的Action对象，需要显式指定拖拽背板图（可多个），以及拖拽的数据，跟手点等信息；当通过一个已创建的 Action 对象发起的拖拽未结束时，无法再次创建新的 Action 对象，接口会抛出异常； 当Action对象的生命周期结束后，注册在该对象上的回调函数会失效，因此需要在一个尽量长的作用域下持有该对象，并在每次发起拖拽前通过createDragAction返回新的对象覆盖旧值。

> **说明：**&gt;
> - 从API version 11开始，可以通过使用[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)中的
> [getDragController](arkts-arkui-arkui-uicontext-uicontext-c.md#getdragcontroller)方法获取当前UI
> 上下文关联的[DragController](arkts-arkui-arkui-uicontext-dragcontroller-c.md)对象。&gt;
> - 建议控制传递的拖拽背板数量，传递过多容易导致拖起的效率问题。

**起始版本：** 11

**废弃版本：** 18

**替代接口：** createDragAction

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| customArray | Array&lt;[CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| [DragItemInfo](../arkts-components/arkts-arkui-dragiteminfo-i.md)&gt; | 是 |
| dragInfo | [DragInfo](arkts-arkui-dragcontroller-draginfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DragAction](arkts-arkui-dragcontroller-dragaction-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
