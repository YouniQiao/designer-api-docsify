# createServer

## Modules to Import

```TypeScript
```

## createServer

```TypeScript
function createServer(name: string): Server
```

Creates a **Server** object. After **start()** is called, the device can be connected to other devices as a server. After using the object, call **close()** to destroy the **Server** object to release resources. To use the object again, you need to create another **Server** object.

**Since:** 23

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-linkEnhance-function createServer(name: string): Server--><!--Device-linkEnhance-function createServer(name: string): Server-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Server](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-server-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [32390206](../../apis-distributedservice-kit/errorcode-link-enhance.md#32390206-invalid-parameter) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [32390203](../../apis-distributedservice-kit/errorcode-link-enhance.md#32390203-duplicate-service-name) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start server name = ' + name);
  // Construct a Server object using the specified name.
  let server: linkEnhance.Server = linkEnhance.createServer(name);
} catch (err) {
  hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```
