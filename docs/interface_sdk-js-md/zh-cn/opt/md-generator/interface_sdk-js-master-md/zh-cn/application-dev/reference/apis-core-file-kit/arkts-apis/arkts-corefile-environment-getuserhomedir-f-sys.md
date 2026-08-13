# getUserHomeDir（系统接口）

## getUserHomeDir

```TypeScript
function getUserHomeDir(): string
```

获取当前用户下应用沙箱路径的内卡目录，该接口仅对具有该系统能力的设备开放。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-Environment-function getUserHomeDir(): string--><!--Device-Environment-function getUserHomeDir(): string-End-->

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
