# createCloudServiceStub (System API)

## Modules to Import

```TypeScript
import { cloudExtension } from '@kit.ArkData';
```

## createCloudServiceStub

```TypeScript
function createCloudServiceStub(instance: CloudService): Promise<rpc.RemoteObject>
```

Creates a RemoteObject instance based on a CloudService instance. The system uses this object to call the APIs of the CloudService instance. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-cloudExtension-function createCloudServiceStub(instance: CloudService): Promise<rpc.RemoteObject>--><!--Device-cloudExtension-function createCloudServiceStub(instance: CloudService): Promise<rpc.RemoteObject>-End-->

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

## Examples

```TypeScript
import { Want, ServiceExtensionAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

class MyCloudService implements cloudExtension.CloudService {
  constructor() {}
  async connectShareCenter(userId: number, bundleName: string): Promise<rpc.RemoteObject> {
    // ...
  }
}

export default class MyServiceExtension extends ServiceExtensionAbility {
  onCreate(want: Want) {
    console.info(`onCreate: ${want}`);
  }
  onRequest(want: Want, startId: number) {
    console.info(`onRequest: ${want} ${startId}`);
  }
  onConnect(want: Want): rpc.RemoteObject | Promise<rpc.RemoteObject> {
    console.info(`onConnect: ${want}`);
    return cloudExtension.createCloudServiceStub(new MyCloudService());
  }
  onDisconnect(want: Want) {
    console.info(`onDisconnect: ${want}`);
  }
  onDestroy() {
    console.info('onDestroy');
  }
}
```
