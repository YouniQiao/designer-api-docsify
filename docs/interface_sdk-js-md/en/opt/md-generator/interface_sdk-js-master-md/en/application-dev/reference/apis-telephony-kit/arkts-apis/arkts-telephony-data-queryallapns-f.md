# queryAllApns

## Modules to Import

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## queryAllApns

```TypeScript
function queryAllApns(): Promise<Array<ApnInfo>>
```

Query all APN info.

**Since:** 16

**Required permissions:** ohos.permission.MANAGE_APN_SETTING

<!--Device-data-function queryAllApns(): Promise<Array<ApnInfo>>--><!--Device-data-function queryAllApns(): Promise<Array<ApnInfo>>-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;ApnInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.queryAllApns().then((apnInfos: Array<data.ApnInfo>) => {
    console.info(`queryAllApns success, promise: apnInfos->${JSON.stringify(apnInfos)}`);
}).catch((err: BusinessError) => {
    console.error(`queryAllApns failed. code: ${err.code}, message: ${err.message}`);
});
```
