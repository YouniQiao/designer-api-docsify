# createService

## Modules to Import

```TypeScript
import { omapi } from 'kits/@kit.ConnectivityKit';
```

## createService

```TypeScript
function createService(): Promise<SEService>
```

Creates an **SEService** instance for connecting to all available SEs in the system. The connection is time- consuming. Therefore, only asynchronous APIs are provided. This API uses a promise to return the result.The **SEService** object is available only when [isConnected](arkts-connectivity-omapi-seservice-i.md#isconnected) returns **true**.

**Since:** 12

**System capability:** SystemCapability.Communication.SecureElement

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SEService](arkts-connectivity-omapi-seservice-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
