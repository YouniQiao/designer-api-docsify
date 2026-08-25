# listFile（系统接口）

## 导入模块

```TypeScript
import { trash } from 'kits/@kit.CoreFileKit';
```

## listFile

```TypeScript
function listFile(): Array<FileInfo>
```

查询最近删除（回收站）列表中文件/目录信息。

**起始版本：** 10

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array & lt;FileInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900020 |
| 13900042 |
