# getCellularDataState

## Modules to Import

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## getCellularDataState

```TypeScript
function getCellularDataState(callback: AsyncCallback<DataConnectState>): void
```

Obtains the cellular data connection status. This API uses an asynchronous callback to return the result.  
**Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 7

**Required permissions:** 
- API version 22+: ohos.permission.GET_NETWORK_INFO

**System capability:** SystemCapability.Telephony.CellularData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataConnectState&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |


## getCellularDataState

```TypeScript
function getCellularDataState(): Promise<DataConnectState>
```

Obtains the cellular data connection status. This API uses a promise to return the result.  
**Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 7

**Required permissions:** 
- API version 22+: ohos.permission.GET_NETWORK_INFO

**System capability:** SystemCapability.Telephony.CellularData

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DataConnectState & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
