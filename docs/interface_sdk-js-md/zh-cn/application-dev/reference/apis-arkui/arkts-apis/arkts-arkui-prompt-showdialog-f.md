# showDialog

## 导入模块

```TypeScript
import { prompt } from 'kits/@kit.ArkUI';
```

## showDialog

```TypeScript
function showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>): void
```

创建并显示对话框，对话框响应结果异步返回。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** showDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ShowDialogSuccessResponse&gt; | 是 |


## showDialog

```TypeScript
function showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>
```

创建并显示对话框，对话框响应后同步返回结果。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** showDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ShowDialogSuccessResponse & gt; |
