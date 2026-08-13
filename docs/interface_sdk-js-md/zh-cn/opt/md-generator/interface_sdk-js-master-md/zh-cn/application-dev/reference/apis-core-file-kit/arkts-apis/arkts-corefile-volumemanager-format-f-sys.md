# format（系统接口）

## format

```TypeScript
function format(volumeId: string, fsType: string, callback: AsyncCallback<void>): void
```

对指定卷设备进行格式化，使用callback异步回调。当前仅支持vfat和exfat两种文件系统类型的格式化，只有处于卸载状态的 卷设备可以进行格式化，格式化后卷设备的uuid、挂载路径和卷设备描述均会发生变化。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MOUNT_FORMAT_MANAGER

<!--Device-volumeManager-function format(volumeId: string, fsType: string, callback: AsyncCallback<void>): void--><!--Device-volumeManager-function format(volumeId: string, fsType: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeId | string | 是 |
| [fsType](arkts-corefile-volumemanager-volume-i-sys.md) | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600008 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600005 |
| 13600002 |
| 13600001 |
| 13900042 |


## format

```TypeScript
function format(volumeId: string, fsType: string): Promise<void>
```

对指定卷设备进行格式化，使用Promise异步回调。当前仅支持vfat和exfat两种文件系统类型的格式化，只有处于卸载状态的 卷设备可以进行格式化，格式化后卷设备的uuid、挂载路径和卷设备描述均会发生变化。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MOUNT_FORMAT_MANAGER

<!--Device-volumeManager-function format(volumeId: string, fsType: string): Promise<void>--><!--Device-volumeManager-function format(volumeId: string, fsType: string): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeId | string | 是 |
| [fsType](arkts-corefile-volumemanager-volume-i-sys.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600008 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600005 |
| 13600002 |
| 13600001 |
| 13900042 |
