# isCellularDataEnabledSync

## Modules to Import

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## isCellularDataEnabledSync

```TypeScript
function isCellularDataEnabledSync(): boolean
```

Checks whether the cellular data service is enabled. This API returns the result synchronously.  
**Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 12

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**System capability:** SystemCapability.Telephony.CellularData

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
