# OnMessageCallback

```TypeScript
type OnMessageCallback = (msgId: string, msgParam?: ArrayBuffer) => void
```

Callback function on receiving a custom message.

**Since:** 23

<!--Device-inputMethodEngine-type OnMessageCallback = (msgId: string, msgParam?: ArrayBuffer) => void--><!--Device-inputMethodEngine-type OnMessageCallback = (msgId: string, msgParam?: ArrayBuffer) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msgId | string | Yes | the identifier of the message. |
| msgParam | ArrayBuffer | No | the parameter of the custom message. |

