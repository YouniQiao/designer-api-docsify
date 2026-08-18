# enableCellularData (System API)

## Modules to Import

```TypeScript
```

## enableCellularData

```TypeScript
function enableCellularData(callback: AsyncCallback<void>): void
```

Enable cellular data services.

**Since:** 23

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-data-function enableCellularData(callback: AsyncCallback<void>): void--><!--Device-data-function enableCellularData(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CellularData

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

**Examples**

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.enableCellularData((err: BusinessError) => {
    if(err) {
        console.error(`enableCellularData fail. code: ${err.code}, message: ${err.message}`);
    } else {
        console.info(`enableCellularData success`);
    }
});
```


## enableCellularData

```TypeScript
function enableCellularData(): Promise<void>
```

Enable cellular data services.

**Since:** 23

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-data-function enableCellularData(): Promise<void>--><!--Device-data-function enableCellularData(): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CellularData

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |

**Examples**

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.enableCellularData().then(() => {
    console.info(`enableCellularData success.`);
}).catch((err: BusinessError) => {
    console.error(`enableCellularData fail. code: ${err.code}, message: ${err.message}`);
});
```
