# sendEventByKey

## Modules to Import

```TypeScript
```

## sendEventByKey

```TypeScript
function sendEventByKey(id: string, action: int, params: string): boolean
```

Sends an event to the component with the specified ID.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-inspector-function sendEventByKey(id: string, action: int, params: string): boolean--><!--Device-inspector-function sendEventByKey(id: string, action: int, params: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | ID of the component for which the event is to be sent. |
| action | int | Yes | Type of the event to be sent. The options are as follows: Click event: 10 LongClick: 11. |
| params | string | Yes | Event parameters. If there is no parameter, pass an empty string "". |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

