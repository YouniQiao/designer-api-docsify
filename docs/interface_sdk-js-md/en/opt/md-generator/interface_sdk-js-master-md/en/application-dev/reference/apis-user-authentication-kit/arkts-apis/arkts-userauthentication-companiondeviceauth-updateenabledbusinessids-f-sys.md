# updateEnabledBusinessIds (System API)

## Modules to Import

```TypeScript
import { companionDeviceAuth } from '@kit.UserAuthenticationKit';
```

## updateEnabledBusinessIds

```TypeScript
function updateEnabledBusinessIds(templateId: Uint8Array, enabledBusinessIds: number[]): Promise<void>
```

Updates the service scope supported by the specified companion device template. This API is used to modify the list of service IDs enabled for a registered template, thereby controlling the service scenarios in which the template can be used. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.USE_USER_IDM

**Model restriction:** This API can be used only in the stage model.

<!--Device-companionDeviceAuth-function updateEnabledBusinessIds(templateId: Uint8Array, enabledBusinessIds: int[]): Promise<void>--><!--Device-companionDeviceAuth-function updateEnabledBusinessIds(templateId: Uint8Array, enabledBusinessIds: int[]): Promise<void>-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| templateId | Uint8Array | Yes |
| [enabledBusinessIds](arkts-userauthentication-companiondeviceauth-templatestatus-i-sys.md) | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [32600001](../errorcode-useriam.md#32600001-system-service-not-working-properly) |
| [32600003](../errorcode-useriam.md#32600003-invalid-service-id) |
| [32600002](../errorcode-useriam.md#32600002-template-not-found) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const templateId = new Uint8Array([1, 2, 3]);
companionDeviceAuth.updateEnabledBusinessIds(templateId, [companionDeviceAuth.BusinessId.DEFAULT])
  .then(() => {
    console.info('business scope updated');
  })
  .catch((err: BusinessError) => {
    console.error(`error has been captured: code: ${err.code}, message: ${err.message}`);
  })
```
