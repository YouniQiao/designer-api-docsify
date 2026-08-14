# connectDfs

## Modules to Import

```TypeScript
import { ConflictFiles } from 'ConflictFiles';
import { FileFilter } from 'FileFilter';
import { Filter } from 'Filter';
import { Options } from 'Options';
import { ReaderIteratorResult } from 'ReaderIteratorResult';
import { WatchEvent } from 'WatchEvent';
import { WatchEventListener } from 'WatchEventListener';
import { Watcher } from 'Watcher';
import { ReadOptions } from 'ReadOptions';
import { ReadTextOptions } from 'ReadTextOptions';
import { WriteOptions } from 'WriteOptions';
import { ListFileExtOptions } from 'ListFileExtOptions';
import { ListFileOptions } from 'ListFileOptions';
import { DfsListeners } from 'DfsListeners';
import { TaskSignal } from 'TaskSignal';
```

## connectDfs

```TypeScript
declare function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>
```

Triggers connection. If the peer device is abnormal, [onStatus](arkts-corefile-file-fs-dfslisteners-i.md#onStatus) in **DfsListeners** will be called to notify the application.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-unnamed-declare function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>--><!--Device-unnamed-declare function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | string | Yes | Network ID of the device. The device network ID can be obtained from [DeviceBasicInfo](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md#DeviceBasicInfo) using the related [distributedDeviceManager](../../apis-distributed-service-kit/arkts-apis/arkts-distributeddevicemanager.md#@ohos.distributedDeviceManager) API. |
| listeners | [DfsListeners](arkts-corefile-file-fs-dfslisteners-i.md) | Yes | Listeners for distributed file system status. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed.Possible causes: 1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 13900045 | Connection failed. |
| 13900046 | Software caused connection abort. |

