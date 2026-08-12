# DLPFile（系统接口）

管理DLPFile的实例，表示一个DLP文件对象，需要通过  
[generateDLPFile](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md#generateDLPFile)/[openDLPFile](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md#openDLPFile)获取DLPFile的实例。DLPFile对象代表一个已打开的DLP文件句柄，封装了对DLP文件的所有操作接口。对象在使用完毕后必须调用[closeDLPFile](#closeDLPFile)方法释放资源，避免文件句柄泄漏。DLPFile对象在跨进程传递时，需要进行授权。

**起始版本：** 10

<!--Device-dlpPermission-export interface DLPFile--><!--Device-dlpPermission-export interface DLPFile-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

## addDLPLinkFile

```TypeScript
addDLPLinkFile(linkFileName: string): Promise<void>
```

在FUSE文件系统(Filesystem in Userspace)添加link文件。FUSE是一种用户空间文件系统框架，允许在用户空间实现自定义文件系统逻辑。link文件是FUSE中映射到DLP密文的虚拟文件，对该文件的读写操作会同步到实际DLP文件。使用Promise异步回调。

在调用addDLPLinkFile后需要调用  
[deleteDLPLinkFile](#deleteDLPLinkFile)移除DLP link文件。

DLP应用需要通过标准文件接口访问加密文件内容时，先添加link文件将DLP文件映射为虚拟明文文件，应用可像操作普通文件一样读写该link文件。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-addDLPLinkFile(linkFileName: string): Promise<void>--><!--Device-DLPFile-addDLPLinkFile(linkFileName: string): Promise<void>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| linkFileName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |

## 示例

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
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // 添加link文件。

  await dlpFile?.closeDLPFile(); // 关闭DLP对象。
  if (file) {
    fileIo.closeSync(file);
  }
}

ExampleFunction();
```

## addDLPLinkFile

```TypeScript
addDLPLinkFile(linkFileName: string, callback: AsyncCallback<void>): void
```

在FUSE文件系统添加link文件。使用callback异步回调。调用成功后，在FUSE文件系统中创建一个映射到DLP文件密文的虚拟文件。

在调用addDLPLinkFile后需要调用  
[deleteDLPLinkFile](#deleteDLPLinkFile)移除DLP link文件。

DLP应用需要通过标准文件接口访问加密文件内容时使用此接口。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-addDLPLinkFile(linkFileName: string, callback: AsyncCallback<void>): void--><!--Device-DLPFile-addDLPLinkFile(linkFileName: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| linkFileName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |

## 示例

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
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  dlpFile.addDLPLinkFile('test.txt.dlp.link', async (err, res) => {
    if (err) {
      console.error('addDLPLinkFile error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
    await dlpFile?.closeDLPFile(); // 关闭DLP对象。
    fileIo.closeSync(file);
  }); // 添加link文件。
}

ExampleFunction();
```

## closeDLPFile

```TypeScript
closeDLPFile(): Promise<void>
```

关闭DLPFile，释放对象。使用Promise异步回调。

调用[openDLPFile](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md#openDLPFile)成功后返回DLPFile对象，必须在使用完毕后调用closeDLPFile()释放资源。

文件所有者决定关闭DLP文件时使用此接口。

> **说明：**
> 
> dlpFile不再使用，应该关闭释放内存，且对象不应继续使用。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-closeDLPFile(): Promise<void>--><!--Device-DLPFile-closeDLPFile(): Promise<void>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |

## 示例

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
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。

  await dlpFile?.closeDLPFile(); // 关闭DLP对象。
  if (file) {
    fileIo.closeSync(file);
  }
}

ExampleFunction();
```

## closeDLPFile

```TypeScript
closeDLPFile(callback: AsyncCallback<void>): void
```

关闭DLPFile，释放对象，使用callback异步回调。

调用openDLPFile()成功后返回DLPFile对象，必须在使用完毕后调用closeDLPFile()释放资源。

文件所有者决定关闭DLP文件时使用此接口。

> **说明：**
> 
> dlpFile不再使用，应该关闭释放内存，且对象不应继续使用。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-closeDLPFile(callback: AsyncCallback<void>): void--><!--Device-DLPFile-closeDLPFile(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |

## 示例

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
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  dlpFile.closeDLPFile((err, res) => { // 关闭DLP文件。
    if (err) {
      console.error('closeDLPFile error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
    fileIo.closeSync(file);
  });
}

ExampleFunction();
```

## deleteDLPLinkFile

```TypeScript
deleteDLPLinkFile(linkFileName: string): Promise<void>
```

删除FUSE文件系统中创建的link文件。使用Promise异步回调。调用成功后，从FUSE文件系统中移除指定的link文件。

在调用deleteDLPLinkFile前需要调用[addDLPLinkFile](#addDLPLinkFile)添加DLP link文件。

DLP文件访问结束后清理link文件映射时使用此接口。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-deleteDLPLinkFile(linkFileName: string): Promise<void>--><!--Device-DLPFile-deleteDLPLinkFile(linkFileName: string): Promise<void>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| linkFileName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |

## 示例

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
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // 添加link文件。
  await dlpFile.deleteDLPLinkFile('test.txt.dlp.link'); // 删除link文件。
  
  await dlpFile?.closeDLPFile(); // 关闭DLP对象。
  if (file) {
    fileIo.closeSync(file);
  }
}

ExampleFunction();
```

## deleteDLPLinkFile

```TypeScript
deleteDLPLinkFile(linkFileName: string, callback: AsyncCallback<void>): void
```

删除FUSE文件系统中创建的link文件，使用callback异步回调。调用成功后，从FUSE文件系统中移除指定的link文件。

在调用deleteDLPLinkFile前需要调用[addDLPLinkFile](#addDLPLinkFile)添加DLP link文件。

DLP文件访问结束后清理link文件映射时使用此接口。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-deleteDLPLinkFile(linkFileName: string, callback: AsyncCallback<void>): void--><!--Device-DLPFile-deleteDLPLinkFile(linkFileName: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| linkFileName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |

## 示例

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
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // 添加link文件。
  dlpFile.deleteDLPLinkFile('test.txt.dlp.link', async (err, res) => { // 删除link文件。
    if (err) {
      console.error('deleteDLPLinkFile error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
    await dlpFile?.closeDLPFile(); // 关闭DLP对象。
    fileIo.closeSync(file);
  });
}

ExampleFunction();
```

## recoverDLPFile

```TypeScript
recoverDLPFile(plaintextFd: number): Promise<void>
```

移除DLP文件的权限控制，恢复成明文文件。使用Promise异步回调。

文件所有者决定取消文件的DLP保护时使用此接口，将其转换为普通文件以便自由分享。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-recoverDLPFile(plaintextFd: number): Promise<void>--><!--Device-DLPFile-recoverDLPFile(plaintextFd: number): Promise<void>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| plaintextFd | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19100003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100003-加解密超时) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100002-加解密出错) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100005-凭据认证服务器错误) |
| [19100004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100004-凭据服务错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [19100010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100010-只读dlp文件) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |
| [19100008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100008-非dlp文件) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let destFile: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  destFile = fileIo.openSync('file://docs/storage/Users/currentUser/Desktop/dest.txt').fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  await dlpFile.recoverDLPFile(destFile); // 还原DLP文件。
  await dlpFile?.closeDLPFile(); // 关闭DLP对象。
  if (file) {
    fileIo.closeSync(file);
  }
  if (destFile) {
    fileIo.closeSync(destFile);
  }
}

ExampleFunction();
```

## recoverDLPFile

```TypeScript
recoverDLPFile(plaintextFd: number, callback: AsyncCallback<void>): void
```

移除DLP文件的权限控制，恢复成明文文件，使用callback异步回调。

文件所有者决定取消文件的DLP保护时使用此接口。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-recoverDLPFile(plaintextFd: number, callback: AsyncCallback<void>): void--><!--Device-DLPFile-recoverDLPFile(plaintextFd: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| plaintextFd | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [19100003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100003-加解密超时) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100002-加解密出错) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100005-凭据认证服务器错误) |
| [19100004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100004-凭据服务错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [19100010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100010-只读dlp文件) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |
| [19100008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100008-非dlp文件) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';

async function ExampleFunction() {
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let file: number | undefined = undefined;
  let destFile: number | undefined = undefined;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  let appId = '';
  let bundleName = 'com.ohos.note';
  let userId = 100;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  destFile = fileIo.openSync('destUri').fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  dlpFile.recoverDLPFile(destFile, async (err, res) => { // 还原DLP文件。
    if (err) {
      console.error('recoverDLPFile error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
    await dlpFile?.closeDLPFile(); // 关闭DLP对象。
    fileIo.closeSync(file);
    fileIo.closeSync(destFile);
  });
}

ExampleFunction();
```

## replaceDLPLinkFile

```TypeScript
replaceDLPLinkFile(linkFileName: string): Promise<void>
```

替换link文件。使用Promise异步回调。调用成功后，使用新的link文件名替换当前link文件。需要先创建link文件并停止FUSE读写，才能执行此操作。

需要切换访问不同的DLP文件时，通过替换link文件实现文件映射的切换。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-replaceDLPLinkFile(linkFileName: string): Promise<void>--><!--Device-DLPFile-replaceDLPLinkFile(linkFileName: string): Promise<void>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| linkFileName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |

## 示例

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
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // 添加link文件。
  await dlpFile.stopFuseLink(); // 暂停link读写。
  await dlpFile.replaceDLPLinkFile('test_new.txt.dlp.link'); // 替换link文件。
  await dlpFile.resumeFuseLink(); // 恢复link读写。
  
  await dlpFile?.closeDLPFile(); // 关闭DLP对象。
  if (file) {
    fileIo.closeSync(file);
  }
}

ExampleFunction();
```

## replaceDLPLinkFile

```TypeScript
replaceDLPLinkFile(linkFileName: string, callback: AsyncCallback<void>): void
```

替换link文件，使用callback异步回调。调用成功后，使用新的link文件名替换当前link文件。

需要切换访问不同的DLP文件时替换link文件。需要先创建link文件并停止FUSE读写，才能执行此操作。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-replaceDLPLinkFile(linkFileName: string, callback: AsyncCallback<void>): void--><!--Device-DLPFile-replaceDLPLinkFile(linkFileName: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| linkFileName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |

## 示例

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
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // 添加link文件。
  await dlpFile.stopFuseLink(); // 暂停link读写。
  dlpFile.replaceDLPLinkFile('test_new.txt.dlp.link', async (err, res) => { // 替换link文件。
    if (err) {
      console.error('replaceDLPLinkFile error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
      await dlpFile?.resumeFuseLink(); // 恢复link读写。
    }
    await dlpFile?.closeDLPFile(); // 关闭DLP对象。
    fileIo.closeSync(file);
  });
}

ExampleFunction();
```

## resumeFuseLink

```TypeScript
resumeFuseLink(): Promise<void>
```

恢复FUSE关联读写。使用Promise异步回调。调用成功后，恢复对link文件的读写操作。 

必须在调用[stopFuseLink](#stopFuseLink)暂停读写后才能调用此方法恢复读写功能。

link文件替换完成后，需要恢复读写关联以继续正常的文件访问。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-resumeFuseLink(): Promise<void>--><!--Device-DLPFile-resumeFuseLink(): Promise<void>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |

## 示例

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
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // 添加link文件。
  await dlpFile.stopFuseLink(); // 暂停link读写。
  await dlpFile.resumeFuseLink(); // 恢复link读写。
  
  await dlpFile?.closeDLPFile(); // 关闭DLP对象。
  if (file) {
    fileIo.closeSync(file);
  }
}

ExampleFunction();
```

## resumeFuseLink

```TypeScript
resumeFuseLink(callback: AsyncCallback<void>): void
```

恢复FUSE关联读写，使用callback异步回调。调用成功后，恢复对link文件的读写操作。

必须在调用[stopFuseLink](#stopFuseLink)暂停读写后才能调用此方法恢复读写功能。

link文件替换完成后需要恢复读写关联。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-resumeFuseLink(callback: AsyncCallback<void>): void--><!--Device-DLPFile-resumeFuseLink(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |

## 示例

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
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // 添加link文件。
  await dlpFile.stopFuseLink(); // 暂停link读写。
  dlpFile.resumeFuseLink(async (err, res) => {
    if (err) {
      console.error('resumeFuseLink error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
    await dlpFile?.closeDLPFile(); // 关闭DLP对象。
    fileIo.closeSync(file);
  }); // 恢复link读写。
}

ExampleFunction();
```

## stopFuseLink

```TypeScript
stopFuseLink(): Promise<void>
```

停止FUSE关联读写。使用Promise异步回调。调用成功后，暂停对link文件的读写操作。

调用stopFuseLink暂停FUSE关联读写后，必须调用[resumeFuseLink](#resumeFuseLink)恢复读写功能。

在删除link文件前，需要先停止关联读写以确保文件操作安全。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-stopFuseLink(): Promise<void>--><!--Device-DLPFile-stopFuseLink(): Promise<void>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |

## 示例

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
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // 添加link文件。
  await dlpFile.stopFuseLink(); // 暂停link读写。
  await dlpFile?.closeDLPFile(); // 关闭DLP对象。
  if (file) {
    fileIo.closeSync(file);
  }
}

ExampleFunction();
```

## stopFuseLink

```TypeScript
stopFuseLink(callback: AsyncCallback<void>): void
```

停止FUSE关联读写。使用callback异步回调。调用成功后，暂停对link文件的读写操作。

调用stopFuseLink暂停FUSE关联读写后，必须调用[resumeFuseLink](#resumeFuseLink)恢复读写功能。

删除link文件前需要暂停读写关联。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-DLPFile-stopFuseLink(callback: AsyncCallback<void>): void--><!--Device-DLPFile-stopFuseLink(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [19100009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100009-操作dlp文件失败) |

## 示例

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
  appId = data.signatureInfo.appId;

  file = fileIo.openSync(uri).fd;
  dlpFile = await dlpPermission.openDLPFile(file, appId); // 打开DLP文件。
  await dlpFile.addDLPLinkFile('test.txt.dlp.link'); // 添加link文件。
  dlpFile.stopFuseLink(async (err, res) => {
    if (err) {
      console.error('stopFuseLink error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
    await dlpFile?.closeDLPFile(); // 关闭DLP对象。
    fileIo.closeSync(file);
  }); // 暂停link读写。
}

ExampleFunction();
```

## dlpProperty

```TypeScript
dlpProperty: DLPProperty
```

表示DLP文件授权相关信息。

**类型：** [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i.md)

**起始版本：** 10

<!--Device-DLPFile-dlpProperty: DLPProperty--><!--Device-DLPFile-dlpProperty: DLPProperty-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。
