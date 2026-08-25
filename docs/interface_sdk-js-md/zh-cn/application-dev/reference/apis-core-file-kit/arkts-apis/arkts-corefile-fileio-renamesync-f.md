# renameSync

## 导入模块

```TypeScript
```

## renameSync

```TypeScript
declare function renameSync(oldPath: string, newPath: string): void
```

以同步方法重命名文件。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [renameSync](arkts-corefile-file-fs-renamesync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| oldPath | string | 是 |
| newPath | string | 是 |

**示例**

```TypeScript
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/new.txt';
fileio.renameSync(srcFile, dstFile);
```
