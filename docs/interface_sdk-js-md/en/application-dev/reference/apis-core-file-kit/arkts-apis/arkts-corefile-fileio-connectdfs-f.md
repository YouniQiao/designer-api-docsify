# connectDfs

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## connectDfs

```TypeScript
function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>
```

Triggers connection. If the peer device is abnormal, [onStatus](arkts-corefile-fileio-dfslisteners-i.md#onstatus)in DfsListeners will be called to notify the application.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-fileIo-function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>--><!--Device-fileIo-function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | string | Yes | Network ID of the device. The device network ID can be obtained from [DeviceBasicInfo](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md/arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md) using the related [distributedDeviceManager](../../apis-distributed-service-kit/arkts-apis/arkts-distributeddevicemanager.md/arkts-distributeddevicemanager.md) API. |
| listeners | [DfsListeners](arkts-corefile-file-fs-dfslisteners-i.md) | Yes | Listeners for distributed file system status. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 13900045 | Connection failed. |
| 13900046 | Software caused connection abort. |

