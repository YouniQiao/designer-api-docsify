# refreshGlobalHttpProxy

## 导入模块

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## refreshGlobalHttpProxy

```TypeScript
function refreshGlobalHttpProxy(): Promise<HttpProxy>
```

通知系统需要重新验证全局代理。 收到通知后，系统将重新处理全局代理的认证状态。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;HttpProxy & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |

**示例**

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.refreshGlobalHttpProxy().then((data: connection.HttpProxy) => {
  console.info(`Succeeded to refresh global http proxy: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to refresh global http proxy. Code:${error.code}, message:${error.message}`);
});
```
