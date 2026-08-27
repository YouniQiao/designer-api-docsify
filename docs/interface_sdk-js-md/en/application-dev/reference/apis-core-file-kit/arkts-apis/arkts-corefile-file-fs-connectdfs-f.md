# connectDfs

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
```

## connectDfs

```TypeScript
declare function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>
```

Triggers connection. If the peer device is abnormal, [onStatus](arkts-corefile-file-fs-dfslisteners-i.md#onstatus) in **DfsListeners** will be called to notify the application.

**Since:** 12

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | string | Yes | Network ID of the device. The device network ID can be obtained from [DeviceBasicInfo](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md) using the related [distributedDeviceManager](../../apis-distributed-service-kit/arkts-apis/arkts-distributeddevicemanager.md) API. |
| listeners | [DfsListeners](arkts-corefile-file-fs-dfslisteners-i.md) | Yes | Listeners for distributed file system status. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed.Possible causes: 1.Mandatory parameters are left unspecified;  2.Incorrect parameter types. |
| 13900045 | Connection failed. |
| 13900046 | Software caused connection abort. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';

let dmInstance = distributedDeviceManager.createDeviceManager("com.example.filesync");
let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
if (deviceInfoList && deviceInfoList.length > 0) {
  console.info(`Succeeded in getting available device list.`);
  let networkId = deviceInfoList[0].networkId;
  let listeners: fileIo.DfsListeners = {
    onStatus(networkId, status) {
      console.info('onStatus');
    }
  };
  fileIo.connectDfs(networkId, listeners).then(() => {
    console.info("Succeeded in connecting dfs.");
  }).catch((err: BusinessError) => {
    console.error(`Failed to connectDfs. Code: ${err.code}, message: ${err.message}`);
  });
}
```
