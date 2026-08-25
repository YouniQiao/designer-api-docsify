# getPermissionUsedTypeInfos（系统接口）

## 导入模块

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## getPermissionUsedTypeInfos

```TypeScript
function getPermissionUsedTypeInfos(
    tokenId?: number | null,
    permissionName?: Permissions): Promise<Array<PermissionUsedTypeInfo>>
```

查询设备上指定应用访问敏感权限时的信息（包括敏感权限名称、敏感权限访问方式）。

**起始版本：** 12

**需要权限：** ohos.permission.PERMISSION_USED_STATS

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenId | number \| null | 否 |
| permissionName | Permissions | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[PermissionUsedTypeInfo](arkts-ability-privacymanager-permissionusedtypeinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100002](../errorcode-access-token.md#12100002-tokenid不存在) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100009](../errorcode-access-token.md#12100009-服务内部错误) |
