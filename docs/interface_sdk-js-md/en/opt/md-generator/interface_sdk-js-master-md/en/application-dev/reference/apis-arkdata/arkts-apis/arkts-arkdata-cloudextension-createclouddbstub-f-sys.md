# createCloudDBStub (System API)

## Modules to Import

```TypeScript
import { cloudExtension } from '@kit.ArkData';
```

## createCloudDBStub

```TypeScript
function createCloudDBStub(instance: CloudDB): Promise<rpc.RemoteObject>
```

Creates a RemoteObject instance based on a CloudDB instance. The system uses this object to call the APIs of the CloudDB instance. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-cloudExtension-function createCloudDBStub(instance: CloudDB): Promise<rpc.RemoteObject>--><!--Device-cloudExtension-function createCloudDBStub(instance: CloudDB): Promise<rpc.RemoteObject>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| instance | [CloudDB](arkts-arkdata-cloudextension-clouddb-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;rpc.RemoteObject & gt; |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';

class MyCloudDB implements cloudExtension.CloudDB {
  // ...
}

class MyCloudService implements cloudExtension.CloudService {
  constructor() {}
  // ...
  async connectDB(bundleName: string, database: cloudExtension.Database): Promise<rpc.RemoteObject> {
    console.info(`connect DB, bundleName: ${bundleName}`);
    return cloudExtension.createCloudDBStub(new MyCloudDB());
  }
}
```
