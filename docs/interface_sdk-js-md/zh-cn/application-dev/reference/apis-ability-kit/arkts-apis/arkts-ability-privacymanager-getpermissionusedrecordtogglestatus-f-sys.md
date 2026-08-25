# getPermissionUsedRecordToggleStatus（系统接口）

## 导入模块

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## getPermissionUsedRecordToggleStatus

```TypeScript
function getPermissionUsedRecordToggleStatus(): Promise<boolean>
```

系统应用调用此接口，可以获取当前用户的权限使用记录开关状态，例如在权限管理界面展示当前开关设置状态。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.PERMISSION_USED_STATS

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |


## getPermissionUsedRecordToggleStatus

```TypeScript
function getPermissionUsedRecordToggleStatus(subProfileId: number): Promise<boolean>
```

系统应用调用此接口，可以获取指定子身份资料的权限使用记录开关状态，例如在权限管理界面展示当前开关设置状态。使用Promise异步回调。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.PERMISSION_USED_STATS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [subProfileId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |
