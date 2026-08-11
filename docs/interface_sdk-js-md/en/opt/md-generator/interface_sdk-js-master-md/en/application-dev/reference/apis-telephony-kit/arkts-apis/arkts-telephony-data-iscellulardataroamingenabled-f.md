# isCellularDataRoamingEnabled

## Modules to Import

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## isCellularDataRoamingEnabled

```TypeScript
function isCellularDataRoamingEnabled(slotId: number, callback: AsyncCallback<boolean>): void
```

Check whether roaming is enabled for cellular data services.

**Since:** 7

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-data-function isCellularDataRoamingEnabled(slotId: int, callback: AsyncCallback<boolean>): void--><!--Device-data-function isCellularDataRoamingEnabled(slotId: int, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.isCellularDataRoamingEnabled(0, (err: BusinessError, contextData: boolean) => {
    if(err) {
        console.error(`isCellularDataRoamingEnabled fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
    } else {
        console.info(`isCellularDataRoamingEnabled success`);
    }
});
```


## isCellularDataRoamingEnabled

```TypeScript
function isCellularDataRoamingEnabled(slotId: number): Promise<boolean>
```

Check whether roaming is enabled for cellular data services.

**Since:** 7

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-data-function isCellularDataRoamingEnabled(slotId: int): Promise<boolean>--><!--Device-data-function isCellularDataRoamingEnabled(slotId: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.isCellularDataRoamingEnabled(0).then((contextData: boolean) => {
    console.info(`isCellularDataRoamingEnabled success, contextData: ${contextData}`);
}).catch((err: BusinessError) => {
    console.error(`isCellularDataRoamingEnabled fail. code: ${err.code}, message: ${err.message}`);
});
```
