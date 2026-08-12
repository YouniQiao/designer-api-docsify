# getOsAccountSubProfileManager（系统接口）

## getOsAccountSubProfileManager

```TypeScript
function getOsAccountSubProfileManager(): OsAccountSubProfileManager
```

获取系统账号子身份资料管理器。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-osAccount-function getOsAccountSubProfileManager(): OsAccountSubProfileManager--><!--Device-osAccount-function getOsAccountSubProfileManager(): OsAccountSubProfileManager-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [OsAccountSubProfileManager](arkts-basicservices-osaccount-osaccountsubprofilemanager-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
```
