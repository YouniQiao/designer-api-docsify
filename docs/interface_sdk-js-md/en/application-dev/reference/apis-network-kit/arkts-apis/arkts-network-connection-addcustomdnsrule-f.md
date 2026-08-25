# addCustomDnsRule

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## addCustomDnsRule

```TypeScript
function addCustomDnsRule(host: string, ip: Array<string>, callback: AsyncCallback<void>): void
```

Adds custom DNS rules for the specified host of the current application. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> You can call [removeCustomDnsRule](arkts-network-connection-removecustomdnsrule-f.md) to delete a custom DNS rule or call
> [clearCustomDnsRules](arkts-network-connection-clearcustomdnsrules-f.md) to delete all custom DNS rules of the current
> application.

**Since:** 11

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| host | string | Yes |
| ip | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |


## addCustomDnsRule

```TypeScript
function addCustomDnsRule(host: string, ip: Array<string>): Promise<void>
```

Adds custom DNS rules for the specified host of the current application. This API uses a promise to return the result.

> **NOTE：**&gt;
> You can call [removeCustomDnsRule](arkts-network-connection-removecustomdnsrule-f.md) to delete a custom DNS rule or call
> [clearCustomDnsRules](arkts-network-connection-clearcustomdnsrules-f.md) to delete all custom DNS rules of the current
> application.

**Since:** 11

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| host | string | Yes |
| ip | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
