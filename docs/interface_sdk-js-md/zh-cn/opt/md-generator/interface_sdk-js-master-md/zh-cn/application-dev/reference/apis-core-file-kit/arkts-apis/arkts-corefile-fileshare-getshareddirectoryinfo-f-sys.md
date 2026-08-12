# getSharedDirectoryInfo（系统接口）

## getSharedDirectoryInfo

```TypeScript
function getSharedDirectoryInfo(): Promise<Array<SharedDirectoryInfo>>
```

获取所有应用捐献的沙箱目录。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_SHARED_FILE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-fileShare-function getSharedDirectoryInfo(): Promise<Array<SharedDirectoryInfo>>--><!--Device-fileShare-function getSharedDirectoryInfo(): Promise<Array<SharedDirectoryInfo>>-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[SharedDirectoryInfo](arkts-corefile-fileshare-shareddirectoryinfo-i-sys.md)&gt;&gt; |

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

async function getSharedDirectoryInfo() {
  try {
    fileShare.getSharedDirectoryInfo().then((infos: Array<fileShare.SharedDirectoryInfo>) => {
      infos.forEach((info: fileShare.SharedDirectoryInfo) => {
        console.info(`bundleName=${info.bundleName} path=${info.path} mode=${info.permissionMode}`);
      });
    }).catch((err: BusinessError) => {
      console.error(`getSharedDirectoryInfo err: ${JSON.stringify(err)}`);
    });
  } catch (error) {
    console.error(`getSharedDirectoryInfo error, Code: ${error.code}, message: ${error.message}`);
  }
}
```
