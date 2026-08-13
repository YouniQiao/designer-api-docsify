# isDefaultNetMetered

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## isDefaultNetMetered

```TypeScript
function isDefaultNetMetered(callback: AsyncCallback<boolean>): void
```

Checks whether data traffic usage on the current network is metered.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function isDefaultNetMetered(callback: AsyncCallback<boolean>): void--><!--Device-connection-function isDefaultNetMetered(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.isDefaultNetMetered((error: BusinessError, data: boolean) => {
  console.error(JSON.stringify(error));
  console.info('data: ' + data);
});
```


## isDefaultNetMetered

```TypeScript
function isDefaultNetMetered(): Promise<boolean>
```

Checks whether data traffic usage on the current network is metered.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function isDefaultNetMetered(): Promise<boolean>--><!--Device-connection-function isDefaultNetMetered(): Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

connection.isDefaultNetMetered().then((data: boolean) => {
  console.info('data: ' + data);
});
```
