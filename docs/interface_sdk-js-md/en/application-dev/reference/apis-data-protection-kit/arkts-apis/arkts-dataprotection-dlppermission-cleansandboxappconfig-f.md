# cleanSandboxAppConfig

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## cleanSandboxAppConfig

```TypeScript
function cleanSandboxAppConfig(): Promise<void>
```

清理沙箱应用配置信息。调用成功后，沙箱应用配置将被清除，恢复默认状态。使用Promise异步回调。

该接口用于清理沙箱应用的配置信息，恢复默认状态以防止配置残留影响后续使用。仅支持在非DLP沙箱应用中调用。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-dlpPermission-function cleanSandboxAppConfig(): Promise<void>--><!--Device-dlpPermission-function cleanSandboxAppConfig(): Promise<void>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19100018 | The application is not authorized. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.cleanSandboxAppConfig().then(() => { // Clear sandbox application configuration.
  console.info('cleanSandboxAppConfig success');
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```

