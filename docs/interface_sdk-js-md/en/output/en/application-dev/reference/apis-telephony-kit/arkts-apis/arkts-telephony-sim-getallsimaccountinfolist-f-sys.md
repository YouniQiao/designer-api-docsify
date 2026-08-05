# getAllSimAccountInfoList (System API)

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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;IccAccountInfo&gt;&gt; | Yes | The callback is used to return the array of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. The ICCID and phone number will be null if has no ohos.permission.GET\_\_\_ESCAPED\_UNDERSCORE\_\_\_TELEPHONY\_\_\_ESCAPED\_UNDERSCORE\_\_\_STATE. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) | Do not have sim card. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error code. |

**Example**

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
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) | Do not have sim card. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error code. |

**Example**

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

