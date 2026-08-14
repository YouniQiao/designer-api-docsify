# createCloudDBStub (System API)

## Modules to Import

```TypeScript
import { cloudExtension } from 'cloudExtension';
```

## createCloudDBStub

```TypeScript
function createCloudDBStub(instance: CloudDB): Promise<rpc.RemoteObject>
```

Creates a RemoteObject instance based on a CloudDB instance. The system uses this object to call the APIs of the CloudDB instance. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-cloudExtension-function createCloudDBStub(instance: CloudDB): Promise<rpc.RemoteObject>--><!--Device-cloudExtension-function createCloudDBStub(instance: CloudDB): Promise<rpc.RemoteObject>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | [CloudDB](arkts-arkdata-cloudextension-clouddb-i-sys.md) | Yes | CloudDB instance. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;rpc.RemoteObject&gt; | Promise used to return the rpc.RemoteObject instance of CloudDB. |

