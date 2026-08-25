# createServer

## Modules to Import

```TypeScript
import { linkEnhance } from 'kits/@kit.DistributedServiceKit';
```

## createServer

```TypeScript
function createServer(name: string): Server
```

Creates a **Server** object. After **start()** is called, the device can be connected to other devices as a server. After using the object, call **close()** to destroy the **Server** object to release resources. To use the object again, you need to create another **Server** object.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [32390206](../errorcode-link-enhance.md#32390206-invalid-parameter) |
| [32390203](../errorcode-link-enhance.md#32390203-duplicate-service-name) |
