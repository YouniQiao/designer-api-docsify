# truncateSync

## 导入模块

```TypeScript
```

## truncateSync

```TypeScript
declare function truncateSync(path: string, len?: number): void
```

以同步方法基于文件路径截断文件。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [truncateSync](arkts-corefile-file-fs-truncatesync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| len | number | 否 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let len = 5;
fileio.truncateSync(filePath, len);
```
