# VirtualFileOnRead

```TypeScript
type VirtualFileOnRead = (id: string, offset: number, length: number) => Promise<Uint8Array>
```

Used to query the content of a specified virtual file.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-pasteboard-type VirtualFileOnRead = (id: string, offset: long, length: int) => Promise<Uint8Array>--><!--Device-pasteboard-type VirtualFileOnRead = (id: string, offset: long, length: int) => Promise<Uint8Array>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | Unique identifier of the virtual file to query. |
| offset | number | Yes | Start position of the virtual file content to query (unit: bytes). |
| length | number | Yes | Length of the virtual file content to query (unit: bytes). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Uint8Array&gt; | Promise used to return the virtual file data starting from **offset** with the specified **length**. |
