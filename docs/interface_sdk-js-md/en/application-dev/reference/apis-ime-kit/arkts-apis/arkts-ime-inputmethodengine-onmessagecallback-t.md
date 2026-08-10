# OnMessageCallback

```TypeScript
type OnMessageCallback = (msgId: string, msgParam?: ArrayBuffer) => void
```

当输入法框架需要显示预览文本时触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputMethodEngine-type OnMessageCallback = (msgId: string, msgParam?: ArrayBuffer) => void--><!--Device-inputMethodEngine-type OnMessageCallback = (msgId: string, msgParam?: ArrayBuffer) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msgId | string | Yes | 接收到的自定义通信数据的标识符。 |
| msgParam | ArrayBuffer | No | 接收到的自定义通信数据的消息体。 |

