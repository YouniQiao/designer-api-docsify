# opendirSync

## 导入模块

```TypeScript
```

## opendirSync

```TypeScript
declare function opendirSync(path: string): Dir
```

以同步方法打开文件目录。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** [listFileSync](arkts-corefile-file-fs-listfilesync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Dir](arkts-corefile-fileio-dir-depr-i.md) |

**示例**

```TypeScript
let dir = fileio.opendirSync(pathDir);
// example code in Dir struct
// use read/readSync/close
```
