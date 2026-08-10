# createServer

## Modules to Import

```TypeScript
import { linkEnhance } from 'kits/@kit.DistributedServiceKit';
```

## createServer

```TypeScript
function createServer(name: string): Server
```

在服务端设备上，应用创建服务。通过start()开启后，该设备可作为服务端被其他设备连接。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-linkEnhance-function createServer(name: string): Server--><!--Device-linkEnhance-function createServer(name: string): Server-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 自定义的非空字符串，标识应用的服务名，最大长度255字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Server](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-server-i.md) | 创建成功的服务对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 32390206 | Invalid parameter. |
| 801 | Capability not supported because the linkEnhance function has been trimmed.<br>**Applicable version:** 26.0.0 and later |
| 32390203 | Duplicate server name. |
| 201 | Permission denied. |

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

