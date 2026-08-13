# getExternalStorageDir（系统接口）

## getExternalStorageDir

```TypeScript
function getExternalStorageDir(): string
```

获取外卡根目录的沙箱路径，该接口仅对具有该系统能力的设备开放。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-Environment-function getExternalStorageDir(): string--><!--Device-Environment-function getExternalStorageDir(): string-End-->

**系统能力：** SystemCapability.FileManagement.File.Environment.FolderObtain

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900042 |
