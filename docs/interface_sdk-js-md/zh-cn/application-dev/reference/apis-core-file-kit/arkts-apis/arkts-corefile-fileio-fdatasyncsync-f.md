# fdatasyncSync

## 导入模块

```TypeScript
```

## fdatasyncSync

```TypeScript
declare function fdatasyncSync(fd: number): void
```

以同步方法实现文件内容数据同步。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [fdatasyncSync](arkts-corefile-file-fs-fdatasyncsync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.fdatasyncSync(fd);
```
