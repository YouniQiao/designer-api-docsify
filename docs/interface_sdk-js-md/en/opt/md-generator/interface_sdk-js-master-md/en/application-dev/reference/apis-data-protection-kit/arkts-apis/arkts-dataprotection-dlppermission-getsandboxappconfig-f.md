# getSandboxAppConfig

## Modules to Import

```TypeScript
```

## getSandboxAppConfig

```TypeScript
function getSandboxAppConfig(): Promise<string>
```

Obtains sandbox application configuration. This API uses a promise to return the result. This API obtains the sandbox application configuration, which can be used to read or verify the current configuration status.

**Since:** 11

<!--Device-dlpPermission-function getSandboxAppConfig(): Promise<string>--><!--Device-dlpPermission-function getSandboxAppConfig(): Promise<string>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100018](../errorcode-dlp.md#19100018-application-unauthorized) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getSandboxAppConfig().then((configInfo) => { // Obtain the sandbox application configuration.
  console.info('configInfo', configInfo);
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```
