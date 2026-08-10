# connectDfs

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## connectDfs

```TypeScript
function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>
```

业务调用connectDfs接口，触发建链。如果对端设备出现异常，业务执行回调DfsListeners内  
[onStatus](../../../reference/apis-core-file-kit/js-apis-file-fs.md#onstatus12)通知应用。可参考  
[跨设备文件共享和访问](../../../file-management/file-access-across-devices.md)文档进行开发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-fileIo-function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>--><!--Device-fileIo-function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | string | Yes | 设备的网络Id。通过 [distributedDeviceManager](../../apis-distributed-service-kit/arkts-apis/arkts-distributeddevicemanager.md/arkts-distributeddevicemanager.md)接口调用 [DeviceBasicInfo](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md/arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)获得。 |
| listeners | [DfsListeners](arkts-corefile-file-fs-dfslisteners-i.md) | Yes | 分布式文件系统状态监听器。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 201 | Permission denied. |
| 13900045 | Connection failed. |
| 13900046 | Software caused connection abort. |

