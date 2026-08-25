# statSync

## 导入模块

```TypeScript
```

## statSync

```TypeScript
declare function statSync(path: string): Stat
```

以同步方法获取文件的信息。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** [statSync](arkts-corefile-file-fs-statsync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Stat](arkts-corefile-fileio-stat-depr-i.md) |

**示例**

```TypeScript
let stat = fileio.statSync(pathDir);
// example code in Stat
```
