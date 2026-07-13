# request（系统接口）

## request

```TypeScript
function request(param: RequestParameterForStage, callback: AsyncCallback<RequestCallbackParameters>): void
```

插件组件request方法，用于发送其所需模板信息的请求。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | RequestParameterForStage | 是 | stage模型的插件组件request参数。 |
| callback | AsyncCallback&lt;RequestCallbackParameters&gt; | 是 | 插件组件request事件回调。 |

