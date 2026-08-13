# setNetQuotaPolicies (System API)

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## setNetQuotaPolicies

```TypeScript
function setNetQuotaPolicies(quotaPolicies: Array<NetQuotaPolicy>, callback: AsyncCallback<void>): void
```

Set metered network quota policies.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function setNetQuotaPolicies(quotaPolicies: Array<NetQuotaPolicy>, callback: AsyncCallback<void>): void--><!--Device-policy-function setNetQuotaPolicies(quotaPolicies: Array<NetQuotaPolicy>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| quotaPolicies | Array&lt;[NetQuotaPolicy](arkts-network-policy-netquotapolicy-i-sys.md)&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netQuotaPolicyList: Array<policy.NetQuotaPolicy> = [];
let netQuotaPolicy: policy.NetQuotaPolicy = {
  networkMatchRule: {
    netType: connection.NetBearType.BEARER_CELLULAR,
    identity: '',
    simId: '1'
  },
  quotaPolicy: {
    periodDuration: 'M1',
    warningBytes: 40000,
    limitBytes: 50000,
    metered: true,
    limitAction: policy.LimitAction.LIMIT_ACTION_NONE
  }
}
netQuotaPolicyList.push(netQuotaPolicy);

policy.setNetQuotaPolicies(netQuotaPolicyList, (error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```


## setNetQuotaPolicies

```TypeScript
function setNetQuotaPolicies(quotaPolicies: Array<NetQuotaPolicy>): Promise<void>
```

Set metered network quota policies.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function setNetQuotaPolicies(quotaPolicies: Array<NetQuotaPolicy>): Promise<void>--><!--Device-policy-function setNetQuotaPolicies(quotaPolicies: Array<NetQuotaPolicy>): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| quotaPolicies | Array&lt;[NetQuotaPolicy](arkts-network-policy-netquotapolicy-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netQuotaPolicyList: Array<policy.NetQuotaPolicy> = [];
let netQuotaPolicy: policy.NetQuotaPolicy = {
  networkMatchRule: {
    netType: connection.NetBearType.BEARER_CELLULAR,
    identity: '',
    simId: '1'
  },
  quotaPolicy: {
    periodDuration: 'M1',
    warningBytes: 40000,
    limitBytes: 50000,
    metered: true,
    limitAction: policy.LimitAction.LIMIT_ACTION_NONE
  }
}
netQuotaPolicyList.push(netQuotaPolicy);

policy
  .setNetQuotaPolicies(netQuotaPolicyList)
  .then(() => {
    console.info('setNetQuotaPolicies success');
  })
  .catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```
