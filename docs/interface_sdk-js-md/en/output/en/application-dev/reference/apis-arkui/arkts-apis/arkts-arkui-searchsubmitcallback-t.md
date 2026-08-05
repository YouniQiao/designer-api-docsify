# SearchSubmitCallback

```TypeScript
export type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void
```

Declare the event listener callback of the enter key.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void--><!--Device-unnamed-export type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchContent | string | Yes | The submitted content of search.  |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Provides the method of keeping Search editable state when submitted.  |

