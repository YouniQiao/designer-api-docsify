# disconnectAllowedProfiles (System API)

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## disconnectAllowedProfiles

```TypeScript
function disconnectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void
```

Disconnects all allowed bluetooth profiles between the local and remote device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function disconnectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void--><!--Device-connection-function disconnectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void-End-->

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
import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.disconnectAllowedProfiles('68:13:24:79:4C:8C', (err: BusinessError) => {
        if (err) {
            console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
            return;
        }
        console.info('disconnectAllowedProfiles, err: ' + JSON.stringify(err));
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```


## disconnectAllowedProfiles

```TypeScript
function disconnectAllowedProfiles(deviceId: string): Promise<void>
```

Disconnects all allowed bluetooth profiles between the local and remote device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ACCESS_BLUETOOTH
- API version 11 - 24: ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function disconnectAllowedProfiles(deviceId: string): Promise<void>--><!--Device-connection-function disconnectAllowedProfiles(deviceId: string): Promise<void>-End-->

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
import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.disconnectAllowedProfiles('68:13:24:79:4C:8C').then(() => {
        console.info('disconnectAllowedProfiles');
    }, (err: BusinessError) => {
        console.error('disconnectAllowedProfiles:errCode' + err.code + ', errMessage: ' + err.message);
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

```TypeScript
try {
  await connection.disconnectAllowedProfiles('68:13:24:79:4C:8C');
} catch (err) {
  console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
