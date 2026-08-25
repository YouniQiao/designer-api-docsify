# getUserHomeDir（系统接口）

## 导入模块

```TypeScript
import { Environment } from '@kit.CoreFileKit';
```

## getUserHomeDir

```TypeScript
function getUserHomeDir(): string
```

获取当前用户下应用沙箱路径的内卡目录，该接口仅对具有该系统能力的设备开放。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.File.Environment.FolderObtain

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 13900042 |

**示例**

```TypeScript
function getUserHomeDirExample() {
  try {
    let path = Environment.getUserHomeDir();
    console.info(`Succeeded in getUserHomeDir, path is ${path}`);
  } catch (err) {
    console.error(`Failed to getUserHomeDir. Code: ${err.code}, message: ${err.message}`);
  }
}
```
