# ExecuteActionEvent

```TypeScript
type ExecuteActionEvent = (actionType: string, params: string) => Promise<string>
```

执行操作事件。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type ExecuteActionEvent = (actionType: string, params: string) => Promise<string>--><!--Device-avMusicTemplate-type ExecuteActionEvent = (actionType: string, params: string) => Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| actionType | string | Yes | 动作类型。 |
| params | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回执行操作的结果字符串。 |

