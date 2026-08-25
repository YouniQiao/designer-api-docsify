# showActionMenu

## 导入模块

```TypeScript
import { promptAction, LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## showActionMenu

```TypeScript
function showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>): void
```

创建并显示操作菜单，菜单响应结果使用callback异步回调返回。

> **说明：**&gt;
> - 从API version 9开始支持，从API version 18开始废弃，建议使用showActionMenu替代。 showActionMenu需先通过UIContext中的 [getPromptAction](arkts-arkui-arkui-uicontext-uicontext-c.md#getpromptaction)方法获取 [PromptAction](arkts-arkui-arkui-uicontext-promptaction-c.md)对象，然后通过该对象进行调用。且直接使用showActionMenu可能导致 [UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的问题。&gt;
> - 从API version 11开始，可以通过使用UIContext中的 [getPromptAction](arkts-arkui-arkui-uicontext-uicontext-c.md#getpromptaction)方法获取当前UI上下文关联的 [PromptAction](arkts-arkui-arkui-uicontext-promptaction-c.md)对象。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** showActionMenu

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ActionMenuOptions](arkts-arkui-prompt-actionmenuoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ActionMenuSuccessResponse&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |


## showActionMenu

```TypeScript
function showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>
```

创建并显示操作菜单，菜单响应后通过Promise返回结果。

> **说明：**&gt;
> - 从API version 9开始支持，从API version 18开始废弃，建议使用showActionMenu替代。 showActionMenu需先通过UIContext中的 [getPromptAction](arkts-arkui-arkui-uicontext-uicontext-c.md#getpromptaction)方法获取 [PromptAction](arkts-arkui-arkui-uicontext-promptaction-c.md)对象，然后通过该对象进行调用。且直接使用showActionMenu可能导致 [UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的问题。&gt;
> - 从API version 10开始，可以通过使用UIContext中的 [getPromptAction](arkts-arkui-arkui-uicontext-uicontext-c.md#getpromptaction)方法获取当前UI上下文关联的 [PromptAction](arkts-arkui-arkui-uicontext-promptaction-c.md)对象。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** showActionMenu

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ActionMenuOptions](arkts-arkui-prompt-actionmenuoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ActionMenuSuccessResponse & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
