# getAllActiveIfaces (System API)

## Modules to Import

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## getAllActiveIfaces

```TypeScript
function getAllActiveIfaces(callback: AsyncCallback<Array<string>>): void
```

Obtains the active network interface. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |


## getAllActiveIfaces

```TypeScript
function getAllActiveIfaces(): Promise<Array<string>>
```

Obtains the active network interface. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |
