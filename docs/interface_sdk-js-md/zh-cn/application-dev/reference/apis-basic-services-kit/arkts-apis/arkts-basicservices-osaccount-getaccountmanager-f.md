# getAccountManager

## 导入模块

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## getAccountManager

```TypeScript
function getAccountManager(): AccountManager
```

获取系统账号管理对象。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| [AccountManager](arkts-basicservices-osaccount-accountmanager-i.md) |

**示例**

```TypeScript
let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
```
