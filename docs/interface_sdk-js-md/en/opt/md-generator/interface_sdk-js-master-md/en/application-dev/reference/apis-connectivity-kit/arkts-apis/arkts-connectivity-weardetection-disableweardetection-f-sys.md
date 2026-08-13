# disableWearDetection (System API)

## Modules to Import

```TypeScript
import { wearDetection } from '@kit.ConnectivityKit';
```

## disableWearDetection

```TypeScript
function disableWearDetection(deviceId: string, callback: AsyncCallback<void>): void
```

Turn off the wearing detection switch.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

<!--Device-wearDetection-function disableWearDetection(deviceId: string, callback: AsyncCallback<void>): void--><!--Device-wearDetection-function disableWearDetection(deviceId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

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
    wearDetection.disableWearDetection('XX:XX:XX:XX:XX:XX', (err) => {
        if (err) {
            console.error("disableWearDetection error");
        }
    });
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```


## disableWearDetection

```TypeScript
function disableWearDetection(deviceId: string): Promise<void>
```

Turn off the wearing detection switch.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

<!--Device-wearDetection-function disableWearDetection(deviceId: string): Promise<void>--><!--Device-wearDetection-function disableWearDetection(deviceId: string): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

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
    wearDetection.disableWearDetection('XX:XX:XX:XX:XX:XX').then(() => {
        console.info("disableWearDetection");
    });
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```
