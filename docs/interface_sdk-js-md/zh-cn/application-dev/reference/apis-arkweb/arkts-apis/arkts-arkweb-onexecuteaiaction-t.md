# OnExecuteAIAction

```TypeScript
export type OnExecuteAIAction = (id: string, params: string, result: OnAISessionCallback) => void
```

Triggered when executing an AI session action. Enables custom implementation of AI model execution.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| params | string | 是 |
| result | [OnAISessionCallback](arkts-arkweb-onaisessioncallback-t.md) | 是 |
