# getDefaultHttpProxy

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getDefaultHttpProxy

```TypeScript
function getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void
```

Obtains the default {@link HttpProxy} proxy settings.

If an application level proxy is set, the application level proxy parameters are returned.If a global proxy is set, the global proxy parameters are returned.If the process is bound to a {@link NetHandle} using {@link setAppNet}, the {@link NetHandle} proxy settings are returned.In other cases, the proxy settings of default network are returned.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-connection-function getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void--><!--Device-connection-function getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HttpProxy&gt; | 是 | Returns the default {@link HttpProxy} settings. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

## 示例

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

Obtains the default {@link HttpProxy} proxy settings.

If an application level proxy is set, the application level proxy parameters are returned.If a global proxy is set, the global proxy parameters are returned.If the process is bound to a {@link NetHandle} using {@link setAppNet}, the {@link NetHandle} proxy settings are returned.In other cases, the proxy settings of default network are returned.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-connection-function getDefaultHttpProxy(): Promise<HttpProxy>--><!--Device-connection-function getDefaultHttpProxy(): Promise<HttpProxy>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HttpProxy&gt; | the promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

## 示例

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultHttpProxy().then((data: connection.HttpProxy) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.error(`Failed to get request. Code:${error.code}, message:${error.message} `);
});
```

