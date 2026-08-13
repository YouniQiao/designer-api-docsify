# cleanSandboxAppConfig

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## cleanSandboxAppConfig

```TypeScript
function cleanSandboxAppConfig(): Promise<void>
```

Clears the sandbox application configuration. After the API is successfully called, the sandbox application configuration is cleared and the default state is restored. This API uses a promise to return the result. This API clears the sandbox application configuration and restores the default state to prevent residual configurations from affecting subsequent use. This API can be called only in non-sandbox applications.

**Since:** 11

**Deprecated since:** -1

<!--Device-dlpPermission-function cleanSandboxAppConfig(): Promise<void>--><!--Device-dlpPermission-function cleanSandboxAppConfig(): Promise<void>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100018](../errorcode-dlp.md#19100018-application-unauthorized) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100007](../errorcode-dlp.md#19100007-access-denied-for-a-dlp-sandbox-application) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.cleanSandboxAppConfig().then(() => { // Clear sandbox application configuration.
  console.info('cleanSandboxAppConfig success');
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```
