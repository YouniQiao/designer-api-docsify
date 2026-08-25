# OnCreateAISession

```TypeScript
type OnCreateAISession = (id: string, params: string, result: OnAISessionCallback) => boolean
```

AI会话创建回调函数类型。允许自定义模型初始化和结果处理。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| params | string | 是 |
| result | [OnAISessionCallback](arkts-arkweb-onaisessioncallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
