# createCloudServiceStub (System API)

## Modules to Import

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## createCloudServiceStub

```TypeScript
function createCloudServiceStub(instance: CloudService): Promise<rpc.RemoteObject>
```

Creates a RemoteObject instance based on a CloudService instance. The system uses this object to call the APIs of the CloudService instance. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| instance | [CloudService](arkts-arkdata-cloudextension-cloudservice-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;rpc.RemoteObject & gt; |
