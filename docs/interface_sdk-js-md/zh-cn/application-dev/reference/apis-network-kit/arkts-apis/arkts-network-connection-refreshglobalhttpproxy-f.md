# refreshGlobalHttpProxy

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## refreshGlobalHttpProxy

```TypeScript
function refreshGlobalHttpProxy(): Promise<HttpProxy>
```

Notifies the system that global proxy re-authentication is required.Upon receiving the notification, the system will reproces the global proxy's authentication status.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function refreshGlobalHttpProxy(): Promise<HttpProxy>--><!--Device-connection-function refreshGlobalHttpProxy(): Promise<HttpProxy>-End-->

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
| 201 | Permission denied. |

## 示例

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.refreshGlobalHttpProxy().then((data: connection.HttpProxy) => {
  console.info(`Succeeded to refresh global http proxy: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to refresh global http proxy. Code:${error.code}, message:${error.message}`);
});
```

