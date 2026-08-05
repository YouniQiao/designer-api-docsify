# getDefaultHttpProxy

## getDefaultHttpProxy

```TypeScript
function getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void
```

Obtains the default \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ proxy settings. If an application level proxy is set, the application level proxy parameters are returned. If a global proxy is set, the global proxy parameters are returned. If the process is bound to a \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ using \_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, the \_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ proxy settings are returned. In other cases, the proxy settings of default network are returned.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-connection-function getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void--><!--Device-connection-function getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;HttpProxy&gt; | Yes | Returns the default \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ settings. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |

**Example**

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultHttpProxy((error: BusinessError, data: connection.HttpProxy) => {
  if (error) {
    console.error(`Failed to get default http proxy. Code:${error.code}, message:${error.message}`);
    return;
  }
  console.info("Succeeded to get data" + JSON.stringify(data));
});
```


## getDefaultHttpProxy

```TypeScript
function getDefaultHttpProxy(): Promise<HttpProxy>
```

Obtains the default \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ proxy settings. If an application level proxy is set, the application level proxy parameters are returned. If a global proxy is set, the global proxy parameters are returned. If the process is bound to a \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ using \_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, the \_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ proxy settings are returned. In other cases, the proxy settings of default network are returned.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-connection-function getDefaultHttpProxy(): Promise<HttpProxy>--><!--Device-connection-function getDefaultHttpProxy(): Promise<HttpProxy>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HttpProxy&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |

**Example**

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultHttpProxy().then((data: connection.HttpProxy) => {
  console.info(JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.info(JSON.stringify(error));
});
```

