# setAppHttpProxy

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## setAppHttpProxy

```TypeScript
function setAppHttpProxy(httpProxy: HttpProxy): void
```

Set application level http proxy [HttpProxy](arkts-network-connection-httpproxy-i.md#HttpProxy).

**Since:** 11

<!--Device-connection-function setAppHttpProxy(httpProxy: HttpProxy): void--><!--Device-connection-function setAppHttpProxy(httpProxy: HttpProxy): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [httpProxy](arkts-network-ethernet-interfaceconfiguration-i-sys.md) | [HttpProxy](arkts-network-ethernet-httpproxy-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [2100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100001-invalid-parameter-value) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { http } from '@kit.NetworkKit';

let exclusionStr = "192.168,baidu.com";
let exclusionArray = exclusionStr.split(',');
connection.setAppHttpProxy({
  host: "192.168.xx.xxx",
  port: 8080,
  exclusionList: exclusionArray
} as connection.HttpProxy);
let httpRequest = http.createHttp();
let options: http.HttpRequestOptions = {
  usingProxy: true, // This field specifies whether to use the network proxy. It is supported since API version 10.
};
// Initiate an HTTP request.
httpRequest.request("EXAMPLE_URL", options, (err: BusinessError, data: http.HttpResponse) => {
  if (!err) {
   console.info(`Result: ${data.result}`);
   console.info(`code: ${data.responseCode}`);
   console.info(`type: ${JSON.stringify(data.resultType)}`);
   console.info(`header: ${JSON.stringify(data.header)}`);
   console.info(`cookies: ${data.cookies}`); // Cookies are supported since API version 8.
  } else {
   console.error(`error: ${JSON.stringify(err)}`);
  }
});
```
