# showActionMenu

## 导入模块

```TypeScript
import { prompt } from 'kits/@kit.ArkUI';
```

## showActionMenu

```TypeScript
function showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>): void
```

创建并显示操作菜单，菜单响应结果异步返回。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** showActionMenu

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ActionMenuOptions](arkts-arkui-prompt-actionmenuoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ActionMenuSuccessResponse&gt; | 是 |


## showActionMenu

```TypeScript
function showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>
```

创建并显示操作菜单，菜单响应后同步返回结果。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** showActionMenu

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ActionMenuOptions](arkts-arkui-prompt-actionmenuoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ActionMenuSuccessResponse & gt; |
