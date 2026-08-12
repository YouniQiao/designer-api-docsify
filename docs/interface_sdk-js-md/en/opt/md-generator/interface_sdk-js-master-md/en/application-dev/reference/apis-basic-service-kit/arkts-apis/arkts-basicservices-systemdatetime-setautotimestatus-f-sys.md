# setAutoTimeStatus (System API)

## Modules to Import

```TypeScript
import { systemDateTime } from '@kit.BasicServicesKit';
```

## setAutoTimeStatus

```TypeScript
function setAutoTimeStatus(status: boolean): Promise<void>
```

Sets the status of the automatic time setting. This API uses a promise to return the result.

**Since:** 21

**Required permissions:** ohos.permission.SET_TIME

<!--Device-systemDateTime-function setAutoTimeStatus(status: boolean): Promise<void>--><!--Device-systemDateTime-function setAutoTimeStatus(status: boolean): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| status | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [13000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-time.md#13000001-network-or-os-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [204](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#204-access-denied-by-user-access-control-policy) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.setAutoTimeStatus(true).then(() => {
    console.info(`Succeeded in setting autotime.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to set autotime. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to set autotime. message: ${error.message}, code: ${error.code}`);
}
```
