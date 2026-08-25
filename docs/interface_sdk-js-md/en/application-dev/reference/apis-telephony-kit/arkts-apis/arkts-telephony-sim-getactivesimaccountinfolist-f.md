# getActiveSimAccountInfoList

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getActiveSimAccountInfoList

```TypeScript
function getActiveSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void
```

Obtains the list of activated SIM card accounts. This API uses an asynchronous callback to return the result.  
**Required permission**: ohos.permission.GET_TELEPHONY_STATE

> **NOTE：**&gt;
> The **GET_TELEPHONY_STATE** permission is required to obtain the ICCID and phone number. Such information is
> sensitive and not open to third-party applications. When this API is called, the returned ICCID and phone number
> are empty.

**Since:** 10

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |


## getActiveSimAccountInfoList

```TypeScript
function getActiveSimAccountInfoList(): Promise<Array<IccAccountInfo>>
```

Obtains the list of activated SIM card accounts. This API uses a promise to return the result.  
**Required permission**: ohos.permission.GET_TELEPHONY_STATE

> **NOTE：**&gt;
> The **GET_TELEPHONY_STATE** permission is required to obtain the ICCID and phone number. Such information is
> sensitive and not open to third-party applications. When this API is called, the returned ICCID and phone number
> are empty.

**Since:** 10

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
