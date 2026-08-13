# isWearDetectionSupported (System API)

## Modules to Import

```TypeScript
import { wearDetection } from '@kit.ConnectivityKit';
```

## isWearDetectionSupported

```TypeScript
function isWearDetectionSupported(deviceId: string, callback: AsyncCallback<boolean>): void
```

Checks whether the device supports wear detection.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

<!--Device-wearDetection-function isWearDetectionSupported(deviceId: string, callback: AsyncCallback<boolean>): void--><!--Device-wearDetection-function isWearDetectionSupported(deviceId: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
try {
    wearDetection.isWearDetectionSupported('XX:XX:XX:XX:XX:XX', (err, supported) => {
        console.info('device support wear detection ' + supported);
    });
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```


## isWearDetectionSupported

```TypeScript
function isWearDetectionSupported(deviceId: string): Promise<boolean>
```

Checks whether the device supports wear detection.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

<!--Device-wearDetection-function isWearDetectionSupported(deviceId: string): Promise<boolean>--><!--Device-wearDetection-function isWearDetectionSupported(deviceId: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
try {
    wearDetection.isWearDetectionSupported('XX:XX:XX:XX:XX:XX').then((supported) => {
        console.info('device support wear detection ' + supported);
    });
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```
