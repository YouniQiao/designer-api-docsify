# getAllSimAccountInfoList (System API)

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getAllSimAccountInfoList

```TypeScript
function getAllSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void
```

Get the list of all SIM card account information.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getAllSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void--><!--Device-sim-function getAllSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;IccAccountInfo&gt;&gt; | Yes | The callback is used to return the array of {@link IccAccountInfo}. The ICCID and phone number will be null if has no ohos.permission.GET_TELEPHONY_STATE. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300004 | Do not have sim card. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getAllSimAccountInfoList((err: BusinessError) => {
    console.info(`callback: err->${JSON.stringify(err)}`);
});
```


## getAllSimAccountInfoList

```TypeScript
function getAllSimAccountInfoList(): Promise<Array<IccAccountInfo>>
```

Get the list of all SIM card account information.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getAllSimAccountInfoList(): Promise<Array<IccAccountInfo>>--><!--Device-sim-function getAllSimAccountInfoList(): Promise<Array<IccAccountInfo>>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;IccAccountInfo&gt;&gt; | Returns the array of { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300004 | Do not have sim card. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

async getAllSimAccountInfoList(): Promise<ResponseData<sim.IccAccountInfo[] | null>> {
    try {
      const accountInfoList: sim.IccAccountInfo[] =
        await sim.getAllSimAccountInfoList();
      return { success: true, code: CommonConstant.DEFAULT_SUCCESS_CODE, data: accountInfoList };
    } catch (err) {
      return this.handleError(this.getAllSimAccountInfoList.name, err);
    }
  }
```

