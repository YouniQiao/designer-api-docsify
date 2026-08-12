# hibernate (System API)

## Modules to Import

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## hibernate

```TypeScript
function hibernate(clearMemory: boolean): void
```

Hibernates a device.

**Since:** 12

**Required permissions:** 
- API version 19+: ohos.permission.POWER_MANAGER

<!--Device-power-function hibernate(clearMemory: boolean): void--><!--Device-power-function hibernate(clearMemory: boolean): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| clearMemory | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [4900101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-power.md#4900101-service-connection-failure) |

## Examples

```TypeScript
try {
    power.hibernate(true);
} catch(err) {
    console.error('hibernate failed, err: ' + err);
}
```
