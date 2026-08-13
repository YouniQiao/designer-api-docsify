# createServer

## Modules to Import

```TypeScript
import { linkEnhance } from '@kit.DistributedServiceKit';
```

## createServer

```TypeScript
function createServer(name: string): Server
```

Creates a **Server** object. After **start()** is called, the device can be connected to other devices as a server.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-linkEnhance-function createServer(name: string): Server--><!--Device-linkEnhance-function createServer(name: string): Server-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Server** object name. The value is a string of up to 255 bytes. It cannot be empty. |

**Return value:**

| Type | Description |
| --- | --- |
| Server | Server** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [32390206](../../apis-distributedservice-kit/errorcode-link-enhance.md#32390206-invalid-parameter) | Invalid parameter. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the linkEnhance function has been trimmed.<br>**Applicable version:** 26.0.0 and later |
| [32390203](../../apis-distributedservice-kit/errorcode-link-enhance.md#32390203-duplicate-service-name) | Duplicate server name. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

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

