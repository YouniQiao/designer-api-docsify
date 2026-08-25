# fsyncSync

## 导入模块

```TypeScript
```

## fsyncSync

```TypeScript
declare function fsyncSync(fd: number): void
```

以同步方法同步文件数据。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [fsyncSync](arkts-corefile-file-fs-fsyncsync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fsyncSync(fd);
```
