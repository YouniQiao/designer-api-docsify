# listFile（系统接口）

## 导入模块

```TypeScript
import { recent } from '@kit.CoreFileKit';
```

## listFile

```TypeScript
function listFile(): Array<FileInfo>
```

查询最近访问列表中文件信息。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

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

**示例**

```TypeScript
let fileinfos = recent.listFile();
for(let i = 0; i < fileinfos.length; i++){
  console.info('uri: ' + fileinfos[i].uri);
  console.info('srcPath: ' + fileinfos[i].srcPath);
  console.info('fileName: ' + fileinfos[i].fileName);
  console.info('mode: ' + fileinfos[i].mode);
  console.info('size: ' + fileinfos[i].size);
  console.info('mtime: ' + fileinfos[i].mtime);
  console.info('ctime: ' + fileinfos[i].ctime);
}
```
