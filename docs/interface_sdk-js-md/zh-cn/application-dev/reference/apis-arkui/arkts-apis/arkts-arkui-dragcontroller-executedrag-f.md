# executeDrag

## 导入模块

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## executeDrag

```TypeScript
function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo,
    callback: AsyncCallback<DragEventParam>): void
```

Execute a drag event.

**起始版本：** 10

**废弃版本：** 18

**替代接口：** executeDrag

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| custom | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| [DragItemInfo](../arkts-components/arkts-arkui-dragiteminfo-i.md) | 是 |
| dragInfo | [DragInfo](arkts-arkui-dragcontroller-draginfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DragEventParam](arkts-arkui-dragcontroller-drageventparam-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |


## executeDrag

```TypeScript
function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo): Promise<DragEventParam>
```

主动发起拖拽能力，传入拖拽发起后跟手效果所拖拽的对象以及携带拖拽信息。使用Promise异步回调。

> **说明：**&gt;
> 从API version 11开始，可以通过使用[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)中的
> [getDragController](arkts-arkui-arkui-uicontext-uicontext-c.md#getdragcontroller)方法获取当前UI
> 上下文关联的[DragController](arkts-arkui-arkui-uicontext-dragcontroller-c.md)对象。

**起始版本：** 10

**废弃版本：** 18

**替代接口：** executeDrag

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| custom | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| [DragItemInfo](../arkts-components/arkts-arkui-dragiteminfo-i.md) | 是 |
| dragInfo | [DragInfo](arkts-arkui-dragcontroller-draginfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;{ event: DragEvent, extraParams: string |
| Promise&lt;[DragEventParam](arkts-arkui-dragcontroller-drageventparam-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
