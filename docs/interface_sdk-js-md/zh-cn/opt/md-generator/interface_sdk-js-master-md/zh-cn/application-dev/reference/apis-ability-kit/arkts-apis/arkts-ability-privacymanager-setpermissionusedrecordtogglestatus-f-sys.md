# setPermissionUsedRecordToggleStatus（系统接口）

## 导入模块

```TypeScript
```

## setPermissionUsedRecordToggleStatus

```TypeScript
function setPermissionUsedRecordToggleStatus(status: boolean): Promise<void>
```

设置是否记录当前用户的权限使用情况。系统应用调用此接口，可以设置当前用户的权限使用记录开关状态。使用Promise异步回调。 status为true时，[addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord系统接口)接口可以正常添加使用记录；status为false时， [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord系统接口)接口不产生权限使用记录，并且删除当前用户的历史记录。

**起始版本：** 23

**需要权限：** ohos.permission.PERMISSION_RECORD_TOGGLE

<!--Device-privacyManager-function setPermissionUsedRecordToggleStatus(status: boolean): Promise<void>--><!--Device-privacyManager-function setPermissionUsedRecordToggleStatus(status: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| status | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12100009](../errorcode-access-token.md#12100009-服务内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100006](../errorcode-access-token.md#12100006-指定操作不允许) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

**示例**

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 设置权限使用记录开关状态
privacyManager.setPermissionUsedRecordToggleStatus(true).then(() => {
  console.info('setPermissionUsedRecordToggleStatus success');
}).catch((err: BusinessError): void => {
  console.error(`setPermissionUsedRecordToggleStatus fail, code: ${err.code}, message: ${err.message}`);
});
```


## setPermissionUsedRecordToggleStatus

```TypeScript
function setPermissionUsedRecordToggleStatus(status: boolean, subProfileId: number): Promise<void>
```

设置是否记录指定子身份资料的权限使用情况。系统应用调用此接口，可以设置指定子身份资料的权限使用记录开关状态。使用Promise异步回调。 status为true时，[addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord系统接口)接口可以正常添加使用记录；status为false时，addPermissionUsedRecord][addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord系统接口)接口不产生权限使用记录，并且删除指定子身份资料的历史记录。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.PERMISSION_RECORD_TOGGLE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-privacyManager-function setPermissionUsedRecordToggleStatus(status: boolean, subProfileId: int): Promise<void>--><!--Device-privacyManager-function setPermissionUsedRecordToggleStatus(status: boolean, subProfileId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| status | boolean | 是 |
| [subProfileId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12100009](../errorcode-access-token.md#12100009-服务内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100006](../errorcode-access-token.md#12100006-指定操作不允许) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

**示例**

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileId: number = 100001; // 请替换为当前用户子身份资料的有效id。
privacyManager.setPermissionUsedRecordToggleStatus(true, subProfileId).then(() => {
  console.info('setPermissionUsedRecordToggleStatus success');
}).catch((err: BusinessError): void => {
  console.error(`setPermissionUsedRecordToggleStatus fail, code: ${err.code}, message: ${err.message}`);
});
```
