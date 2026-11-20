# VirtualFileOnStat

```TypeScript
type VirtualFileOnStat = (id: string) => Promise<VirtualFileItem>
```

Used to query the metadata of a specified virtual file.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-pasteboard-type VirtualFileOnStat = (id: string) => Promise<VirtualFileItem>--><!--Device-pasteboard-type VirtualFileOnStat = (id: string) => Promise<VirtualFileItem>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | Unique identifier of the virtual file to query. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[VirtualFileItem](arkts-basicservices-pasteboard-virtualfileitem-c.md)&gt; | Promise used to return the metadata object of the virtual file. |
