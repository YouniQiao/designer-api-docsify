# setVolumeDescription（系统接口）

## 导入模块

```TypeScript
```

## setVolumeDescription

```TypeScript
function setVolumeDescription(uuid: string, description: string, callback: AsyncCallback<void>): void
```

修改指定卷设备描述，使用callback异步回调。当前仅支持修改ntfs和exfat两种文件系统类型的设备描述， 只有处于卸载状态的卷设备可以修改设备描述。

**起始版本：** 23

**需要权限：** ohos.permission.MOUNT_UNMOUNT_MANAGER

<!--Device-volumeManager-function setVolumeDescription(uuid: string, description: string, callback: AsyncCallback<void>): void--><!--Device-volumeManager-function setVolumeDescription(uuid: string, description: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | string | 是 |
| description | string | 是 |
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


## setVolumeDescription

```TypeScript
function setVolumeDescription(uuid: string, description: string): Promise<void>
```

修改指定卷设备描述，使用Promise异步回调。当前仅支持修改ntfs和exfat两种文件系统类型的设备描述， 只有处于卸载状态的卷设备可以修改设备描述。

**起始版本：** 23

**需要权限：** ohos.permission.MOUNT_UNMOUNT_MANAGER

<!--Device-volumeManager-function setVolumeDescription(uuid: string, description: string): Promise<void>--><!--Device-volumeManager-function setVolumeDescription(uuid: string, description: string): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | string | 是 |
| description | string | 是 |

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
