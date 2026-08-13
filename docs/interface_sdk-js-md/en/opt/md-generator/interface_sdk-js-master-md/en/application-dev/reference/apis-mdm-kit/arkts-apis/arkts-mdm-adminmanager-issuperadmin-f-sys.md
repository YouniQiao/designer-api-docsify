# isSuperAdmin (System API)

## Modules to Import

```TypeScript
import { adminManager } from '@kit.MDMKit';
```

## isSuperAdmin

```TypeScript
function isSuperAdmin(bundleName: String, callback: AsyncCallback<boolean>): void
```

Checks whether the super device administrator application of the first user (u100) is enabled based on **bundleName**. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-adminManager-function isSuperAdmin(bundleName: String, callback: AsyncCallback<boolean>): void--><!--Device-adminManager-function isSuperAdmin(bundleName: String, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | String | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

// Replace with actual values.
let bundleName: string = 'com.example.myapplication';

adminManager.isSuperAdmin(bundleName, (err, result) => {
  if (err) {
    console.error(`Failed to query admin is super admin or not. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying admin is super admin or not, result : ${result}`);
});
```


## isSuperAdmin

```TypeScript
function isSuperAdmin(bundleName: String): Promise<boolean>
```

Checks whether the super device administrator application of the first user (u100) is enabled based on **bundleName**. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-adminManager-function isSuperAdmin(bundleName: String): Promise<boolean>--><!--Device-adminManager-function isSuperAdmin(bundleName: String): Promise<boolean>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | String | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Replace with actual values.
let bundleName: string = 'com.example.myapplication';

adminManager.isSuperAdmin(bundleName).then((result) => {
  console.info(`Succeeded in querying admin is super admin or not, result : ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query admin is super admin or not. Code: ${err.code}, message: ${err.message}`);
});
```
