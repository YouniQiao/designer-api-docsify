# enableCloud（系统接口）

## enableCloud

```TypeScript
function enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>
```

异步方法使能端云协同能力。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-cloudSyncManager-function enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>--><!--Device-cloudSyncManager-function enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| switches | Record & lt;string, boolean & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountId: string = "testAccount";
let switches: Record<string, boolean> = {
  'com.example.bundleName1': true,
  'com.example.bundleName2': false
}
cloudSyncManager.enableCloud(accountId, switches).then(() => {
  console.info("enableCloud successfully.");
}).catch((err: BusinessError) => {
  console.error(`enableCloud failed with error message: ${err.message}, error code: ${err.code}`);
});
```


## enableCloud

```TypeScript
function enableCloud(
    accountId: string,
    switches: Record<string, boolean>,
    callback: AsyncCallback<void>
  ): void
```

异步方法使能端云协同能力。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-cloudSyncManager-function enableCloud(    accountId: string,    switches: Record<string, boolean>,    callback: AsyncCallback<void>  ): void--><!--Device-cloudSyncManager-function enableCloud(    accountId: string,    switches: Record<string, boolean>,    callback: AsyncCallback<void>  ): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| switches | Record & lt;string, boolean & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountId: string = "testAccount";
let switches: Record<string, boolean> = {
  'com.example.bundleName1': true,
  'com.example.bundleName2': false
}
cloudSyncManager.enableCloud(accountId, switches, (err: BusinessError) => {
  if (err) {
    console.error(`enableCloud failed with error message: ${err.message}, error code: ${err.code}`);
  } else {
    console.info("enableCloud successfully");
  }
});
```
