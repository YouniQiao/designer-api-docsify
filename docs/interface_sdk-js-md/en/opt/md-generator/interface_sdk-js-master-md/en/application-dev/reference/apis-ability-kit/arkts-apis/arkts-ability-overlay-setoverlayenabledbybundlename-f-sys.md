# setOverlayEnabledByBundleName (System API)

## Modules to Import

```TypeScript
import { overlay } from '@kit.AbilityKit';
```

## setOverlayEnabledByBundleName

```TypeScript
function setOverlayEnabledByBundleName(bundleName:string, moduleName:string, isEnabled: boolean, callback: AsyncCallback<void>): void
```

Enables or disables a module with the overlay feature in another application. This API uses an asynchronous callback to return the result. No permission is required when the specified application is the caller itself.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CHANGE_OVERLAY_ENABLED_STATE

<!--Device-overlay-function setOverlayEnabledByBundleName(bundleName:string, moduleName:string, isEnabled: boolean, callback: AsyncCallback<void>): void--><!--Device-overlay-function setOverlayEnabledByBundleName(bundleName:string, moduleName:string, isEnabled: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Overlay

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | Yes |
| isEnabled | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700032](../errorcode-bundle.md#17700032-application-does-not-contain-a-module-with-the-overlay-feature) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700033](../errorcode-bundle.md#17700033-module-is-not-configured-with-the-overlay-feature) |

## Examples

```TypeScript
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = "com.example.myapplication_xxxxx";
let moduleName = "feature";
let isEnabled = false;

try {
  overlay.setOverlayEnabledByBundleName(bundleName, moduleName, isEnabled, (err, data) => {
    if (err) {
      console.error('setOverlayEnabledByBundleName failed due to err code: ' + err.code + ' ' + 'message:' +
      err.message);
      return;
    }
    console.info('setOverlayEnabledByBundleName successfully');
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('setOverlayEnabledByBundleName failed due to err code: ' + code + ' ' + 'message:' + message);
}
```


## setOverlayEnabledByBundleName

```TypeScript
function setOverlayEnabledByBundleName(bundleName:string, moduleName:string, isEnabled: boolean): Promise<void>
```

Enables or disables a module with the overlay feature in another application. This API uses a promise to return the result. No permission is required when the specified application is the caller itself.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CHANGE_OVERLAY_ENABLED_STATE

<!--Device-overlay-function setOverlayEnabledByBundleName(bundleName:string, moduleName:string, isEnabled: boolean): Promise<void>--><!--Device-overlay-function setOverlayEnabledByBundleName(bundleName:string, moduleName:string, isEnabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Overlay

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | Yes |
| isEnabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700032](../errorcode-bundle.md#17700032-application-does-not-contain-a-module-with-the-overlay-feature) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700033](../errorcode-bundle.md#17700033-module-is-not-configured-with-the-overlay-feature) |

## Examples

```TypeScript
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = "com.example.myapplication_xxxxx";
let moduleName = "feature";
let isEnabled = false;

try {

  overlay.setOverlayEnabledByBundleName(bundleName, moduleName, isEnabled)
    .then((data) => {
      console.info('setOverlayEnabledByBundleName successfully');
    }).catch((err: BusinessError) => {
    console.error('setOverlayEnabledByBundleName failed due to err code: ' + err.code + ' ' + 'message:' + err.message);
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('setOverlayEnabledByBundleName failed due to err code: ' + code + ' ' + 'message:' + message);
}
```
