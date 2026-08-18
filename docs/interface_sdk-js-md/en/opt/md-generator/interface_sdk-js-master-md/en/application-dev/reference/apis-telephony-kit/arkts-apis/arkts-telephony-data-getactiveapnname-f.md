# getActiveApnName

## Modules to Import

```TypeScript
```

## getActiveApnName

```TypeScript
function getActiveApnName(): Promise<string>
```

Get Active APN's Name.

**Since:** 23

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-data-function getActiveApnName(): Promise<string>--><!--Device-data-function getActiveApnName(): Promise<string>-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getActiveApnName().then((apn: string) => {
    console.info(`getActiveApnName success, apn: ${apn}`);
}).catch((err: BusinessError) => {
    console.error(`getActiveApnName failed. code: ${err.code}, message: ${err.message}`);
});
```
