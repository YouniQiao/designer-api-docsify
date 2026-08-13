# showDialog

## showDialog

```TypeScript
function showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>): void
```

创建并显示对话框，对话框响应结果异步返回。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** showDialog

<!--Device-prompt-function showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>): void--><!--Device-prompt-function showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ShowDialogSuccessResponse&gt; | 是 |

## 示例

```TypeScript
import prompt from '@ohos.prompt'
prompt.showDialog({
  title: 'showDialog Title Info',
  message: 'Message Info',
  buttons: [
    {
      text: 'button1',
      color: '#000000'
    },
    {
      text: 'button2',
      color: '#000000'
    }
  ]
}, (err, data) => {
  if (err) {
    console.info('showDialog err: ' + err);
    return;
  }
  console.info('showDialog success callback, click button: ' + data.index);
});
```


## showDialog

```TypeScript
function showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>
```

创建并显示对话框，对话框响应后同步返回结果。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** showDialog

<!--Device-prompt-function showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>--><!--Device-prompt-function showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ShowDialogSuccessResponse & gt; |

## 示例

```TypeScript
import prompt from '@ohos.prompt'
prompt.showDialog({
  title: 'Title Info',
  message: 'Message Info',
  buttons: [
    {
      text: 'button1',
      color: '#000000'
    },
    {
      text: 'button2',
      color: '#000000'
    }
  ],
})
  .then(data => {
    console.info('showDialog success, click button: ' + data.index);
  })
  .catch((err:Error) => {
    console.info('showDialog error: ' + err);
  })
```
