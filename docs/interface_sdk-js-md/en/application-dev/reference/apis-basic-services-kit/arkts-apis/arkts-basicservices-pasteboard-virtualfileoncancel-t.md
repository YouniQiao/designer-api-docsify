# VirtualFileOnCancel

```TypeScript
type VirtualFileOnCancel = (idList: Array<string>) => Promise<void>
```

Used to cancel the operation for specified virtual files.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-pasteboard-type VirtualFileOnCancel = (idList: Array<string>) => Promise<void>--><!--Device-pasteboard-type VirtualFileOnCancel = (idList: Array<string>) => Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| idList | Array&lt;string&gt; | Yes | List of unique identifiers of the virtual files to be cancelled. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |
