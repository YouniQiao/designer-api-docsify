# DataObserver

```TypeScript
type DataObserver = (sessionId: string, fields: Array<string>) => void
```

Defines an observer for obtaining the data change of a distributed object.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-distributedDataObject-type DataObserver = (sessionId: string, fields: Array<string>) => void--><!--Device-distributedDataObject-type DataObserver = (sessionId: string, fields: Array<string>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | Session ID of the distributed data object, with a maximum length of 128 bytes. The value can contain only letters, digits, and underscores (_). |
| fields | Array&lt;string&gt; | Yes | Changed properties of the distributed data object, with a maximum length of 128 bytes. The value can be customized and must be a non-empty string. |

