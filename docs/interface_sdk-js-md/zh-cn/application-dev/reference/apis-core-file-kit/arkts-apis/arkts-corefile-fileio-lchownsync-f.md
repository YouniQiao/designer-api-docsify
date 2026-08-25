# lchownSync

## 导入模块

```TypeScript
```

## lchownSync

```TypeScript
declare function lchownSync(path: string, uid: number, gid: number): void
```

以同步方法基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是更改符号链接所指向的实际文件。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| uid | number | 是 |
| gid | number | 是 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.lchownSync(filePath, stat.uid, stat.gid);
```
