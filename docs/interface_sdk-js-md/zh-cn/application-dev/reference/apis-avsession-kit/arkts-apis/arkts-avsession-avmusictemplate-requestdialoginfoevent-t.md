# RequestDialogInfoEvent

```TypeScript
type RequestDialogInfoEvent = (actionType: DialogActionType, actionInfo?: DialogActionInfo) => Promise<DialogInfo>
```

对话框信息请求事件。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| actionType | [DialogActionType](arkts-avsession-avmusictemplate-dialogactiontype-t.md) | 是 |
| actionInfo | [DialogActionInfo](arkts-avsession-avmusictemplate-dialogactioninfo-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DialogInfo](arkts-avsession-avmusictemplate-dialoginfo-i.md)&gt; |
