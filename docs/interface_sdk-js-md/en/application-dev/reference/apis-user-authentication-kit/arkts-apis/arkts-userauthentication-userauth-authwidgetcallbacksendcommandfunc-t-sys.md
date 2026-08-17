# AuthWidgetCallbackSendCommandFunc (System API)

```TypeScript
type AuthWidgetCallbackSendCommandFunc = (cmdData: string) => void
```

Called to return the command sent from the user authentication framework to the user authentication widget.

**Since:** 23

<!--Device-userAuth-type AuthWidgetCallbackSendCommandFunc = (cmdData: string) => void--><!--Device-userAuth-type AuthWidgetCallbackSendCommandFunc = (cmdData: string) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cmdData | string | Yes | Command sent from the user authentication framework to the user authentication widget. |

