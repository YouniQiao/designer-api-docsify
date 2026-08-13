# getDLPPermissionInfo

## getDLPPermissionInfo

```TypeScript
function getDLPPermissionInfo(): Promise<DLPPermissionInfo>
```

查询当前DLP沙箱的权限信息，包括文件授权类型及可执行操作（如查看、编辑、复制等）。仅支持在DLP沙箱应用中调用，使用Promise异步回调。 在DLP沙箱中处理文件时，可根据权限信息判断当前用户可以执行哪些操作，避免调用无权限的功能。

**起始版本：** 10

**废弃版本：** -1

<!--Device-dlpPermission-function getDLPPermissionInfo(): Promise<DLPPermissionInfo>--><!--Device-dlpPermission-function getDLPPermissionInfo(): Promise<DLPPermissionInfo>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DLPPermissionInfo](arkts-dataprotection-dlppermission-dlppermissioninfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100006](../errorcode-dlp.md#19100006-非dlp沙箱应用) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.isInSandbox().then(async (inSandbox) => { // 是否在沙箱内。
  if (inSandbox) {
    dlpPermission.getDLPPermissionInfo().then((permissionInfo: dlpPermission.DLPPermissionInfo) => {
      console.info('permissionInfo', JSON.stringify(permissionInfo));
    }).catch((error: BusinessError)=> {
      console.error(JSON.stringify(error));
    })
  }
});
```


## getDLPPermissionInfo

```TypeScript
function getDLPPermissionInfo(callback: AsyncCallback<DLPPermissionInfo>): void
```

查询当前DLP沙箱的权限信息。返回的权限信息包括文件的授权类型和可执行的操作权限（如查看、编辑、复制等）。仅支持在DLP沙箱应用中调用。使用callback异步回调。 在DLP沙箱中处理文件时，可根据权限信息判断当前用户可以执行哪些操作，避免调用无权限的功能。

**起始版本：** 10

**废弃版本：** -1

<!--Device-dlpPermission-function getDLPPermissionInfo(callback: AsyncCallback<DLPPermissionInfo>): void--><!--Device-dlpPermission-function getDLPPermissionInfo(callback: AsyncCallback<DLPPermissionInfo>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DLPPermissionInfo](arkts-dataprotection-dlppermission-dlppermissioninfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100006](../errorcode-dlp.md#19100006-非dlp沙箱应用) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.isInSandbox().then((inSandbox) => { // 是否在沙箱内。
  if (inSandbox) {
    dlpPermission.getDLPPermissionInfo((err, permissionInfo) => { 
      if (err) {
        console.error(`Failed to get DLP permission info. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.info('permissionInfo', JSON.stringify(permissionInfo));
      }
    }); // 获取当前权限信息。
  }
});
```
