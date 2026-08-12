# revokePermission（系统接口）

## revokePermission

```TypeScript
function revokePermission(tokenID: number): Promise<void>
```

撤销指定应用的全部持久化文件授权，使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.REVOKE_FILE_ACCESS_PERSIST

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-fileShare-function revokePermission(tokenID: int): Promise<void>--><!--Device-fileShare-function revokePermission(tokenID: int): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| 13900001 |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

async function revokeAllPermissionExample() {
  try {
    let tokenID = 537688848; // 系统应用可以通过bundleManager.getApplicationInfo获取，普通应用可以通过bundleManager.getBundleInfoForSelf获取。
    fileShare.revokePermission(tokenID).then(() => {
      console.info('revoke persist permission successfully.');
    }).catch((err: BusinessError) => {
      console.error(`revoke persist permission failed, Code: ${err.code}, message: ${err.message}`);
    });
  } catch (error) {
    console.error(`revoke persist permission failed error, Code: ${error.code}, message: ${error.message}`);
  }
}
```


## revokePermission

```TypeScript
function revokePermission(tokenID: number, policies: Array<PolicyInfo>): Promise<void>
```

撤销指定应用对URI的持久化授权，使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.REVOKE_FILE_ACCESS_PERSIST

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-fileShare-function revokePermission(tokenID: int, policies: Array<PolicyInfo>): Promise<void>--><!--Device-fileShare-function revokePermission(tokenID: int, policies: Array<PolicyInfo>): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| policies | Array&lt;[PolicyInfo](arkts-corefile-fileshare-policyinfo-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| 13900001 |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| 13900011 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

async function revokeSpecificPermissionExample() {
  try {
    let tokenID = 537688848; // 系统应用可以通过bundleManager.getApplicationInfo获取，普通应用可以通过bundleManager.getBundleInfoForSelf获取。
    let policyInfo: fileShare.PolicyInfo = {
      uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
      operationMode: fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.revokePermission(tokenID, policies).then(() => {
      console.info('revoke persist permission successfully.');
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error(`revoke persist permission failed. Code: ${err.code}, message: ${err.message}`);
      if (err.code === 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error(`error code: ${JSON.stringify(err.data[i].code)}`);
          console.error(`error URI: ${JSON.stringify(err.data[i].uri)}`);
          console.error(`error reason: ${JSON.stringify(err.data[i].message)}`);
        }
      }
    });
  } catch (error) {
    console.error(`revokePermission error, Code: ${error.code}, message: ${error.message}`);
  }
}
```
