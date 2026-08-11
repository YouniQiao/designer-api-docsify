# getActiveSimAccountInfoList

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getActiveSimAccountInfoList

```TypeScript
function getActiveSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void
```

Get the list of active SIM card account information.

**Since:** 10

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getActiveSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void--><!--Device-sim-function getActiveSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;IccAccountInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getActiveSimAccountInfoList((err: BusinessError, data: Array<sim.IccAccountInfo>) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getActiveSimAccountInfoList

```TypeScript
function getActiveSimAccountInfoList(): Promise<Array<IccAccountInfo>>
```

Get the list of active SIM card account information.

**Since:** 10

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getActiveSimAccountInfoList(): Promise<Array<IccAccountInfo>>--><!--Device-sim-function getActiveSimAccountInfoList(): Promise<Array<IccAccountInfo>>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;IccAccountInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getActiveSimAccountInfoList().then((data: Array<sim.IccAccountInfo>) => {
    console.info(`getActiveSimAccountInfoList success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getActiveSimAccountInfoList failed, promise: err->${JSON.stringify(err)}`);
});
```
