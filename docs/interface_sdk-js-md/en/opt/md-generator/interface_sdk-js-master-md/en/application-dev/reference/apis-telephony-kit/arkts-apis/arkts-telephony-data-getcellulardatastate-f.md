# getCellularDataState

## Modules to Import

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## getCellularDataState

```TypeScript
function getCellularDataState(callback: AsyncCallback<DataConnectState>): void
```

Obtain the connection state of the PS domain.

**Since:** 22

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-data-function getCellularDataState(callback: AsyncCallback<DataConnectState>): void--><!--Device-data-function getCellularDataState(callback: AsyncCallback<DataConnectState>): void-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataConnectState&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getCellularDataState((err: BusinessError, contextData: data.DataConnectState) => {
    if(err) {
        console.error(`getCellularDataState fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
    } else {
        console.info(`getCellularDataState success`);
    }
});
```


## getCellularDataState

```TypeScript
function getCellularDataState(): Promise<DataConnectState>
```

Obtain the connection state of the PS domain.

**Since:** 22

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-data-function getCellularDataState(): Promise<DataConnectState>--><!--Device-data-function getCellularDataState(): Promise<DataConnectState>-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;DataConnectState&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getCellularDataState().then((contextData: data.DataConnectState) => {
    console.info(`getCellularDataState success, contextData: ${contextData}`);
}).catch((err: BusinessError) => {
    console.error(`getCellularDataState fail. code: ${err.code}, message: ${err.message}`);
});
```
