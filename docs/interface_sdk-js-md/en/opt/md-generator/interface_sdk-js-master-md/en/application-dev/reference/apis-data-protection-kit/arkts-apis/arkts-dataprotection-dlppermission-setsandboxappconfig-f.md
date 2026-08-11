# setSandboxAppConfig

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## setSandboxAppConfig

```TypeScript
function setSandboxAppConfig(configInfo: string): Promise<void>
```

Sets the configuration information of the sandbox application. The configuration information is in JSON string format and can be set by the application. After the API is successfully called, the sandbox application runs based on the configuration information. This API uses a promise to return the result. This API can be called only in non-DLP sandbox applications.

This API sets the sandbox application configuration so that the application can pass custom parameters as required.

**Since:** 11

<!--Device-dlpPermission-function setSandboxAppConfig(configInfo: string): Promise<void>--><!--Device-dlpPermission-function setSandboxAppConfig(configInfo: string): Promise<void>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configInfo | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100018](../errorcode-dlp.md#19100018-application-unauthorized) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100007](../errorcode-dlp.md#19100007-access-denied-for-a-dlp-sandbox-application) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.setSandboxAppConfig('configInfo').then(() => { // Set sandbox application configuration.
  console.info('setSandboxAppConfig success');
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```
