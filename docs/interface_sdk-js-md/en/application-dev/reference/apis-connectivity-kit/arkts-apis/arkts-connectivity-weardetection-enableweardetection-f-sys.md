# enableWearDetection (System API)

## Modules to Import

```TypeScript
import { wearDetection } from '@kit.ConnectivityKit';
```

## enableWearDetection

```TypeScript
function enableWearDetection(deviceId: string, callback: AsyncCallback<void>): void
```

Turn on the wearing detection switch.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

<!--Device-wearDetection-function enableWearDetection(deviceId: string, callback: AsyncCallback<void>): void--><!--Device-wearDetection-function enableWearDetection(deviceId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates device ID.For example, "11:22:33:AA:BB:FF", |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the Callback result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
try {
    wearDetection.enableWearDetection('XX:XX:XX:XX:XX:XX', (err) => {
        if (err) {
            console.error("enableWearDetection error");
        }
    });
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```


## enableWearDetection

```TypeScript
function enableWearDetection(deviceId: string): Promise<void>
```

Turn on the wearing detection switch.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

<!--Device-wearDetection-function enableWearDetection(deviceId: string): Promise<void>--><!--Device-wearDetection-function enableWearDetection(deviceId: string): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates device ID.For example, "11:22:33:AA:BB:FF", |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Returns the promise object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
try {
    wearDetection.enableWearDetection('XX:XX:XX:XX:XX:XX').then(() => {
        console.info("enableWearDetection");
    });
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

