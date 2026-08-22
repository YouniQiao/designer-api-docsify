# getActiveSimAccountInfoList

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getActiveSimAccountInfoList

```TypeScript
function getActiveSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void
```

Get the list of active SIM card account information.

**Since:** 23

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getActiveSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void--><!--Device-sim-function getActiveSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md)&gt;&gt; | Yes | The callback is used to return the array of [IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md). The ICCID and phone number will be null if has no ohos.permission.GET_TELEPHONY_STATE. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) | No SIM card found. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getActiveSimAccountInfoList((err: BusinessError, data: Array<sim.IccAccountInfo>) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getActiveSimAccountInfoList().then((data: Array<sim.IccAccountInfo>) => {
    console.info(`getActiveSimAccountInfoList success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getActiveSimAccountInfoList failed, promise: err->${JSON.stringify(err)}`);
});
```


## getActiveSimAccountInfoList

```TypeScript
function getActiveSimAccountInfoList(): Promise<Array<IccAccountInfo>>
```

Get the list of active SIM card account information.

**Since:** 23

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getActiveSimAccountInfoList(): Promise<Array<IccAccountInfo>>--><!--Device-sim-function getActiveSimAccountInfoList(): Promise<Array<IccAccountInfo>>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md)&gt;&gt; | Returns the array of { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) | No SIM card found. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |

**Examples**

See [getActiveSimAccountInfoList](#getactivesimaccountinfolist)

