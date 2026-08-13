# OnExecuteAIAction

```TypeScript
type OnExecuteAIAction = (id: string, params: string, result: OnAISessionCallback) => void
```

AI会话执行操作回调函数类型。用于自定义实现AI模型执行。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-type OnExecuteAIAction = (id: string, params: string, result: OnAISessionCallback) => void--><!--Device-unnamed-type OnExecuteAIAction = (id: string, params: string, result: OnAISessionCallback) => void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| params | string | 是 |
| result | [OnAISessionCallback](arkts-arkweb-onaisessioncallback-t.md) | 是 |
