# closeSync

## 导入模块

```TypeScript
```

## closeSync

```TypeScript
declare function closeSync(fd: number): void
```

以同步方法关闭文件。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** [closeSync](arkts-corefile-file-fs-closesync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.closeSync(fd);
```

```TypeScript
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.closeSync();
```

```TypeScript
dir.closeSync();
```
