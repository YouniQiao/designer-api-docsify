# getVolumeById（系统接口）

## getVolumeById

```TypeScript
function getVolumeById(volumeId: string, callback: AsyncCallback<Volume>): void
```

通过指定卷设备id获得卷设备信息，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-volumeManager-function getVolumeById(volumeId: string, callback: AsyncCallback<Volume>): void--><!--Device-volumeManager-function getVolumeById(volumeId: string, callback: AsyncCallback<Volume>): void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Volume](arkts-corefile-volumemanager-volume-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600008 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |


## getVolumeById

```TypeScript
function getVolumeById(volumeId: string): Promise<Volume>
```

通过卷设备id获得指定卷设备信息，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-volumeManager-function getVolumeById(volumeId: string): Promise<Volume>--><!--Device-volumeManager-function getVolumeById(volumeId: string): Promise<Volume>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Volume](arkts-corefile-volumemanager-volume-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600008 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |
