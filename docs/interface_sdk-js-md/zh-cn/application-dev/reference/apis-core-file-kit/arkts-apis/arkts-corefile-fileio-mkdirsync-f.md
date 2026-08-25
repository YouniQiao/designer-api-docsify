# mkdirSync

## 导入模块

```TypeScript
```

## mkdirSync

```TypeScript
declare function mkdirSync(path: string, mode?: number): void
```

以同步方法创建目录。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** [mkdirSync](arkts-corefile-file-fs-mkdirsync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | number | 否 |

**示例**

```TypeScript
let dirPath = pathDir + '/testDir';
fileio.mkdirSync(dirPath);
```
