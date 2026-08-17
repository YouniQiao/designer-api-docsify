# updateRemindPolicy (System API)

## Modules to Import

```TypeScript
import { policy } from 'policy';
```

## updateRemindPolicy

```TypeScript
function updateRemindPolicy(netType: NetBearType, simId: string, remindType: RemindType, callback: AsyncCallback<void>): void
```

Update the policy when the quota reaches the upper limit.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function updateRemindPolicy(netType: NetBearType, simId: string, remindType: RemindType, callback: AsyncCallback<void>): void--><!--Device-policy-function updateRemindPolicy(netType: NetBearType, simId: string, remindType: RemindType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| netType | NetBearType | Yes | [NetBearType](arkts-network-policy-netbeartype-t.md#netbeartype). |
| simId | string | Yes | Specify the matched simId of quota policy when netType is cellular. |
| remindType | [RemindType](arkts-network-policy-remindtype-e-sys.md) | Yes | [RemindType](arkts-network-policy-remindtype-e-sys.md#remindtype-system-api). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of updateRemindPolicy. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

policy.updateRemindPolicy(
  connection.NetBearType.BEARER_CELLULAR,
  '1',
  policy.RemindType.REMIND_TYPE_WARNING,
  (error: BusinessError) => {
    console.error(JSON.stringify(error));
  }
);
```


## updateRemindPolicy

```TypeScript
function updateRemindPolicy(netType: NetBearType, simId: string, remindType: RemindType): Promise<void>
```

Update the policy when the quota reaches the upper limit.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function updateRemindPolicy(netType: NetBearType, simId: string, remindType: RemindType): Promise<void>--><!--Device-policy-function updateRemindPolicy(netType: NetBearType, simId: string, remindType: RemindType): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| netType | NetBearType | Yes | [NetBearType](arkts-network-policy-netbeartype-t.md#netbeartype). |
| simId | string | Yes | Specify the matched simId of quota policy when netType is cellular. |
| remindType | [RemindType](arkts-network-policy-remindtype-e-sys.md) | Yes | [RemindType](arkts-network-policy-remindtype-e-sys.md#remindtype-system-api). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

policy
  .updateRemindPolicy(
    connection.NetBearType.BEARER_CELLULAR,
    '1',
    policy.RemindType.REMIND_TYPE_WARNING
  )
  .then(() => {
    console.info('updateRemindPolicy success');
  })
  .catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```

