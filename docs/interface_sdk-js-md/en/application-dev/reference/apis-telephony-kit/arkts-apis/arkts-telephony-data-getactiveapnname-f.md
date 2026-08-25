# getActiveApnName

## Modules to Import

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## getActiveApnName

```TypeScript
function getActiveApnName(): Promise<string>
```

Obtains the access point name (APN) of the default SIM card used for mobile data. This API returns the result asynchronously.  
**Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 20

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**System capability:** SystemCapability.Telephony.CellularData

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
