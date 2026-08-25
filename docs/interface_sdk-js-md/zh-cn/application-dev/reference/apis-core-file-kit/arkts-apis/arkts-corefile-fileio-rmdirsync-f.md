# rmdirSync

## 导入模块

```TypeScript
```

## rmdirSync

```TypeScript
declare function rmdirSync(path: string): void
```

以同步方法删除目录。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [rmdirSync](arkts-corefile-file-fs-rmdirsync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**示例**

```TypeScript
let dirPath = pathDir + '/testDir';
fileio.rmdirSync(dirPath);
```
