# isDomainAccountSupported

## 导入模块

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## isDomainAccountSupported

```TypeScript
function isDomainAccountSupported(): Promise<boolean>
```

检查是否支持域账号。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
