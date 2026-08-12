# checkPathPermission（系统接口）

## checkPathPermission

```TypeScript
function checkPathPermission(tokenID: number, policies: Array<PathPolicyInfo>, policyType: PolicyType): Promise<Array<boolean>>
```

异步方法校验所选择的多个文件或目录是否有临时或持久化授权，使用Promise异步回调。

**起始版本：** 15

**需要权限：** ohos.permission.CHECK_SANDBOX_POLICY

<!--Device-fileShare-function checkPathPermission(tokenID: int, policies: Array<PathPolicyInfo>, policyType: PolicyType): Promise<Array<boolean>>--><!--Device-fileShare-function checkPathPermission(tokenID: int, policies: Array<PathPolicyInfo>, policyType: PolicyType): Promise<Array<boolean>>-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| policies | Array&lt;[PathPolicyInfo](arkts-corefile-fileshare-pathpolicyinfo-i.md)&gt; | 是 |
| [policyType](../../apis-mdm-kit/arkts-apis/arkts-mdm-systemmanager-otaupdatepolicy-i.md) | [PolicyType](../../apis-mdm-kit/arkts-apis/arkts-mdm-systemmanager-policytype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;boolean & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| 13900042 |

## 示例

```TypeScript
import { fileShare } from '@kit.CoreFileKit';

async function checkPersistentPermissionExample() {
  try {
    let pathPolicyInfo1: fileShare.PathPolicyInfo = {
      path: '/storage/Users/currentUser/Documents/1.txt',
      operationMode: fileShare.OperationMode.READ_MODE,
    }
    let pathPolicyInfo2: fileShare.PathPolicyInfo = {
      path: '/storage/Users/currentUser/Desktop/2.txt',
      operationMode: fileShare.OperationMode.READ_MODE,
    }

    let policies: Array<fileShare.PathPolicyInfo> = [pathPolicyInfo1, pathPolicyInfo2];
    let policyType: fileShare.PolicyType = fileShare.PolicyType.PERSISTENT_TYPE;
    let tokenID = 537688848; // 系统应用可以通过bundleManager.getApplicationInfo获取，普通应用可以通过bundleManager.getBundleInfoForSelf获取。

    fileShare.checkPathPermission(tokenID, policies, policyType).then((result: Array<boolean>) => {
      for (let hasPermission of result) {
        console.info('check permission result is', hasPermission);
      }
    });
    console.info('checkPathPermission finish');
  } catch (error) {
    console.info(`checkPathPermission error, Code: ${error.code}, message: ${error.message}`);
  }
}
```
