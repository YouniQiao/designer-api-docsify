# openDLPFile（系统接口）

## 导入模块

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## openDLPFile

```TypeScript
function openDLPFile(ciphertextFd: number, appId: string): Promise<DLPFile>
```

DLP管理应用调用该接口，打开DLP文件。调用成功后返回DLPFile管理对象，可用于管理DLP文件的权限和进行相关操作。使用Promise异步回调。调用openDLPFile()成功后返回DLPFile对象，必须在使用完毕后调用[closeDLPFile](arkts-dataprotection-dlppermission-dlpfile-i-sys.md#closedlpfile)释放资源。DLP管理应用或授权应用需要访问受保护的DLP文件内容时，先打开文件获取管理对象。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**需要权限：** ohos.permission.ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ciphertextFd | number | 是 |
| appId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DLPFile](arkts-dataprotection-dlppermission-dlpfile-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100002](../errorcode-dlp.md#19100002-加解密出错) |
| [19100003](../errorcode-dlp.md#19100003-加解密超时) |
| [19100004](../errorcode-dlp.md#19100004-凭据服务错误) |
| [19100005](../errorcode-dlp.md#19100005-凭据认证服务器错误) |
| [19100008](../errorcode-dlp.md#19100008-非dlp文件) |
| [19100009](../errorcode-dlp.md#19100009-操作dlp文件失败) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |
| [19100018](../errorcode-dlp.md#19100018-应用未授权) |
| [19100019](../errorcode-dlp.md#19100019-dlp文件已过期) |
| [19100020](../errorcode-dlp.md#19100020-网络未连接) |

**示例**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
  appId = data.signatureInfo.appId; // appId通过应用包信息获取

  file = fileIo.openSync(uri).fd; // file通过文件打开获取fd
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  await dlpFile?.closeDLPFile(); // 关闭DLP对象。

  if (file) {
    fileIo.closeSync(file);
  }
}

ExampleFunction();
```

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';

let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
let file: number | undefined = undefined;
let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
let appId = '';
let bundleName = 'com.ohos.note';
let userId = 100;

let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
appId = data.signatureInfo.appId; // appId通过应用包信息获取

file = fileIo.openSync(uri).fd; // file通过文件打开获取fd
dlpPermission.openDLPFile(file, appId, async (err, res) => { // 打开DLP文件。
  if (err) {
    console.error(`Failed to open DLPFile. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('res', JSON.stringify(res));
  }
  await res?.closeDLPFile(); // 关闭DLP对象。
  if (file) {
    fileIo.closeSync(file);
  }
});
```


## openDLPFile

```TypeScript
function openDLPFile(ciphertextFd: number, appId: string, callback: AsyncCallback<DLPFile>): void
```

DLP管理应用调用该接口，打开DLP文件。使用callback异步回调。调用成功后返回DLPFile管理对象，可用于管理DLP文件的权限和进行相关操作。使用完DLPFile对象后，应调用closeDLPFile释放对象，避免资 源泄露。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**需要权限：** ohos.permission.ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ciphertextFd | number | 是 |
| appId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DLPFile](arkts-dataprotection-dlppermission-dlpfile-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100002](../errorcode-dlp.md#19100002-加解密出错) |
| [19100003](../errorcode-dlp.md#19100003-加解密超时) |
| [19100004](../errorcode-dlp.md#19100004-凭据服务错误) |
| [19100005](../errorcode-dlp.md#19100005-凭据认证服务器错误) |
| [19100008](../errorcode-dlp.md#19100008-非dlp文件) |
| [19100009](../errorcode-dlp.md#19100009-操作dlp文件失败) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |
| [19100018](../errorcode-dlp.md#19100018-应用未授权) |
| [19100019](../errorcode-dlp.md#19100019-dlp文件已过期) |
| [19100020](../errorcode-dlp.md#19100020-网络未连接) |

**示例**

参见 [openDLPFile](#opendlpfile)
