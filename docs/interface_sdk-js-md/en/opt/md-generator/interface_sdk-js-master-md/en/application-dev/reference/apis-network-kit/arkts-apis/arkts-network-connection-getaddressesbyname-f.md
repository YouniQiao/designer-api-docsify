# getAddressesByName

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getAddressesByName

```TypeScript
function getAddressesByName(host: string, callback: AsyncCallback<Array<NetAddress>>): void
```

Resolves the host name to obtain all IP addresses based on the default data network.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERNET

<!--Device-connection-function getAddressesByName(host: string, callback: AsyncCallback<Array<NetAddress>>): void--><!--Device-connection-function getAddressesByName(host: string, callback: AsyncCallback<Array<NetAddress>>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| host | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;NetAddress&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getAddressesByName("xxxx", (error: BusinessError, data: connection.NetAddress[]) => {
  if (error) {
    console.error(`Failed to get addresses. Code:${error.code}, message:${error.message}`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
});
```


## getAddressesByName

```TypeScript
function getAddressesByName(host: string): Promise<Array<NetAddress>>
```

Resolves the host name to obtain all IP addresses based on the default data network.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERNET

<!--Device-connection-function getAddressesByName(host: string): Promise<Array<NetAddress>>--><!--Device-connection-function getAddressesByName(host: string): Promise<Array<NetAddress>>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| host | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;NetAddress & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

connection.getAddressesByName("xxxx").then((data: connection.NetAddress[]) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});
```
