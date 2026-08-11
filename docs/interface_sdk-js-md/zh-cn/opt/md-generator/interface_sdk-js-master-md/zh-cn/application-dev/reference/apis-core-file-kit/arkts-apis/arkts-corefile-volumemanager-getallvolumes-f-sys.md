# getAllVolumes（系统接口）

## getAllVolumes

```TypeScript
function getAllVolumes(callback: AsyncCallback<Array<Volume>>): void
```

获取当前外置存储中所有卷设备信息，使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-volumeManager-function getAllVolumes(callback: AsyncCallback<Array<Volume>>): void--><!--Device-volumeManager-function getAllVolumes(callback: AsyncCallback<Array<Volume>>): void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Volume&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |


## getAllVolumes

```TypeScript
function getAllVolumes(): Promise<Array<Volume>>
```

获取当前外置存储中所有卷设备信息，使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-volumeManager-function getAllVolumes(): Promise<Array<Volume>>--><!--Device-volumeManager-function getAllVolumes(): Promise<Array<Volume>>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;Volume&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |
