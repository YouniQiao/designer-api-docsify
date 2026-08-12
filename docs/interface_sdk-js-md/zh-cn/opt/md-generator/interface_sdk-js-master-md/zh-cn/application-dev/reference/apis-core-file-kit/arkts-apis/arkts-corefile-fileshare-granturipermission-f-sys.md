# grantUriPermission（系统接口）

## grantUriPermission

```TypeScript
function grantUriPermission(
    uri: string,
    bundleName: string,
    flag: wantConstant.Flags,
    callback: AsyncCallback<void>
  ): void
```

为应用授予公共目录文件URI的临时访问权限，使用Callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.WRITE_MEDIA

<!--Device-fileShare-function grantUriPermission(    uri: string,    bundleName: string,    flag: wantConstant.Flags,    callback: AsyncCallback<void>  ): void--><!--Device-fileShare-function grantUriPermission(    uri: string,    bundleName: string,    flag: wantConstant.Flags,    callback: AsyncCallback<void>  ): void-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| bundleName | string | 是 |
| flag | wantConstant.Flags | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| 14300001 |

## 示例

```TypeScript
import { wantConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

let uri: string =
  'file://docs/storage/Users/currentUser/Document/1.txt'; // 推荐使用系统接口生成URI。fileUri.getUriFromPath('沙箱路径');
let bundleName: string = 'com.demo.test';
try {
  fileShare.grantUriPermission(uri, bundleName, wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION |
    wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION, (err: BusinessError) => {
    if (err) {
      console.error(`grantUriPermission failed with error: ${JSON.stringify(err)}`);
      return;
    }
    console.info('grantUriPermission success!');
  });
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error(`grantUriPermission failed with error: ${JSON.stringify(error)}`);
}
```


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, bundleName: string, flag: wantConstant.Flags): Promise<void>
```

为应用授予公共目录文件URI的临时访问权限，使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.WRITE_MEDIA

<!--Device-fileShare-function grantUriPermission(uri: string, bundleName: string, flag: wantConstant.Flags): Promise<void>--><!--Device-fileShare-function grantUriPermission(uri: string, bundleName: string, flag: wantConstant.Flags): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| bundleName | string | 是 |
| flag | wantConstant.Flags | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| 14300001 |

## 示例

```TypeScript
import { wantConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

let uri: string =
  'file://docs/storage/Users/currentUser/Document/1.txt'; // 推荐使用系统接口生成URI。fileUri.getUriFromPath('沙箱路径');
let bundleName: string = 'com.demo.test';
try {
  fileShare.grantUriPermission(uri, bundleName, wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION |
    wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION).then(() => {
    console.info('grantUriPermission success!');
  }).catch((error: BusinessError) => {
    console.error(`grantUriPermission failed with error: ${JSON.stringify(error)}`);
  });
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error(`grantUriPermission failed with error: ${JSON.stringify(error)}`);
}
```


## grantUriPermission

```TypeScript
function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: number): Promise<void>
```

给应用授予目标文件临时权限，使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-fileShare-function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: int): Promise<void>--><!--Device-fileShare-function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: int): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policies | Array&lt;[PolicyInfo](arkts-corefile-fileshare-policyinfo-i.md)&gt; | 是 |
| targetBundleName | string | 是 |
| appCloneIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| 13900001 |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| 13900011 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

async function grantUriPermissionExample() {
  try {
    let uri = 'file://docs/storage/Users/currentUser/Documents/1.txt';
    let policyInfo: fileShare.PolicyInfo = {
      uri: uri,
      operationMode: fileShare.OperationMode.CREATE_MODE | fileShare.OperationMode.READ_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];

    fileShare.grantUriPermission(policies, 'com.example.myapplicationtest', 0).then(() => {
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error(`grantUriPermission failed. Code: ${err.code}, message: ${err.message}`);
    });
  } catch (error) {
    console.info(`grantUriPermission error, Code: ${error.code}, message: ${error.message}`);
  }
}
```
