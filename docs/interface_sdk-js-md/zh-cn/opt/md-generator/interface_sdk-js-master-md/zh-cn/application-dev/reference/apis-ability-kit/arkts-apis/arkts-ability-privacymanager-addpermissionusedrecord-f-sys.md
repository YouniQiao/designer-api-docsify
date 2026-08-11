# addPermissionUsedRecord（系统接口）

## addPermissionUsedRecord

```TypeScript
function addPermissionUsedRecord(
    tokenID: number,
    permissionName: Permissions,
    successCount: number,
    failCount: number,
    options?: AddPermissionUsedRecordOptions
  ): Promise<void>
```

受权限保护的应用在被其他服务、应用调用时，可以使用该接口增加一条权限使用记录。建议在访问敏感权限后调用此接口，以便系统记录对应的敏感权限访问事件。使用Promise异步回调。

权限使用记录包括：调用方的应用身份标识、使用的应用权限名称，以及调用方访问本应用成功和失败的次数。

权限使用记录受[setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setpermissionusedrecordtogglestatus)设置的开关状态控制。开关关闭时，调用此接口不会产生权限使用记录。

**起始版本：** 9

**需要权限：** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    options?: AddPermissionUsedRecordOptions  ): Promise<void>--><!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    options?: AddPermissionUsedRecordOptions  ): Promise<void>-End-->

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |
| successCount | number | 是 |
| failCount | number | 是 |
| options | [AddPermissionUsedRecordOptions](arkts-ability-privacymanager-addpermissionusedrecordoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [12100009](../errorcode-access-token.md#12100009-服务内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100002](../errorcode-access-token.md#12100002-tokenid不存在) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

## 示例

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenID: number = 0; // 可以通过应用BundleInfo中的ApplicationInfo的accessTokenId字段获取。
// 添加权限使用记录
privacyManager.addPermissionUsedRecord(tokenID, 'ohos.permission.READ_AUDIO', 1, 0).then(() => {
  console.info('addPermissionUsedRecord success');
}).catch((err: BusinessError): void => {
  console.error(`addPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
});
// with options param
let options: privacyManager.AddPermissionUsedRecordOptions = {
  usedType: privacyManager.PermissionUsedType.PICKER_TYPE,
  enhancedIdentity: 'test'
};
privacyManager.addPermissionUsedRecord(tokenID, 'ohos.permission.READ_AUDIO', 1, 0, options).then(() => {
  console.info('addPermissionUsedRecord success');
}).catch((err: BusinessError): void => {
  console.error(`addPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
});
```


## addPermissionUsedRecord

```TypeScript
function addPermissionUsedRecord(
    tokenID: number,
    permissionName: Permissions,
    successCount: number,
    failCount: number,
    callback: AsyncCallback<void>
  ): void
```

受权限保护的应用在被其他服务、应用调用时，可以使用该接口增加一条权限使用记录。建议在访问敏感权限后调用此接口，以便系统记录对应的敏感权限访问事件。使用callback异步回调。

权限使用记录包括：调用方的应用身份标识、使用的应用权限名称，以及调用方访问本应用成功和失败的次数。

权限使用记录受[setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setpermissionusedrecordtogglestatus)设置的开关状态控制。开关关闭时，调用此接口不会产生权限使用记录。

**起始版本：** 9

**需要权限：** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    callback: AsyncCallback<void>  ): void--><!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    callback: AsyncCallback<void>  ): void-End-->

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |
| successCount | number | 是 |
| failCount | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [12100009](../errorcode-access-token.md#12100009-服务内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100002](../errorcode-access-token.md#12100002-tokenid不存在) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

## 示例

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenID: number = 0; // 可以通过应用BundleInfo中的ApplicationInfo的accessTokenId字段获取。
// 添加权限使用记录
privacyManager.addPermissionUsedRecord(tokenID, 'ohos.permission.READ_AUDIO', 1, 0, (err: BusinessError, data: void) => {
  if (err) {
    console.error(`addPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('addPermissionUsedRecord success');
  }
});
```
