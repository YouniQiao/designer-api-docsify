# DfsListenerCallback

```TypeScript
type DfsListenerCallback = (networkId: string, status: int) => void
```

DfsListener Callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileIo-type DfsListenerCallback = (networkId: string, status: int) => void--><!--Device-fileIo-type DfsListenerCallback = (networkId: string, status: int) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | string | Yes | The networkId of device.  |
| status | int | Yes | The status code of Distributed File System. The value should be an integer.  |

