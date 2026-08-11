# ProgressObserver

```TypeScript
type ProgressObserver = (sessionId: string, progress: int) => void
```

Defines an observer for obtaining the transfer progress.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-distributedDataObject-type ProgressObserver = (sessionId: string, progress: int) => void--><!--Device-distributedDataObject-type ProgressObserver = (sessionId: string, progress: int) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | Session ID of the distributed data object, with a maximum length of 128 bytes. The value can contain only letters, digits, and underscores (_). |
| progress | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Asset transfer progress. The value is an integer ranging from -1 to 100. The value **-1** indicates that the progress fails to be obtained, and the value **100** indicates that the transfer is complete. |

