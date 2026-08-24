# getBundleInstaller (System API)

## Modules to Import

```TypeScript
import { installer } from '@kit.AbilityKit';
```

## getBundleInstaller

```TypeScript
function getBundleInstaller(callback: AsyncCallback<BundleInstaller>): void
```

Obtains a BundleInstaller object. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-installer-function getBundleInstaller(callback: AsyncCallback<BundleInstaller>): void--><!--Device-installer-function getBundleInstaller(callback: AsyncCallback<BundleInstaller>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;BundleInstaller&gt; | Yes | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md) used to return the result. If the operation is successful, **err** is **null** and **data** is the BundleInstaller object obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    installer.getBundleInstaller((err: BusinessError, data: installer.BundleInstaller) => {
        if (err) {
            console.error('getBundleInstaller failed:' + err.message);
        } else {
            console.info('getBundleInstaller successfully');
        }
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed:' + message);
}
```

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        console.info('getBundleInstaller successfully.');
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```


## getBundleInstaller

```TypeScript
function getBundleInstaller(): Promise<BundleInstaller>
```

Obtains a BundleInstaller object. This API uses a promise to return the result.

**Since:** 23

<!--Device-installer-function getBundleInstaller(): Promise<BundleInstaller>--><!--Device-installer-function getBundleInstaller(): Promise<BundleInstaller>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;BundleInstaller&gt; | BundleInstaller object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

**Examples**

See [getBundleInstaller](#getbundleinstaller)

