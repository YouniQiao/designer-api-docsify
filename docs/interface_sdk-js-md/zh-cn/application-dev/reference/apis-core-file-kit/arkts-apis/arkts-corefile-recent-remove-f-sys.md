# remove（系统接口）

## 导入模块

```TypeScript
import { recent } from '@kit.CoreFileKit';
```

## remove

```TypeScript
function remove(uri: string): void
```

将uri对应的文件从最近访问列表中移除。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900020 |
| 13900042 |

**示例**

```TypeScript
let uri = 'file://docs/storage/Users/currentUser/<publicPath>';
recent.remove(uri);
```
