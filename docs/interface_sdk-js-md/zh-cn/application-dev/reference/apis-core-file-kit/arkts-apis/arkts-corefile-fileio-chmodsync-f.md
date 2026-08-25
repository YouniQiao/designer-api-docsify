# chmodSync

## 导入模块

```TypeScript
```

## chmodSync

```TypeScript
declare function chmodSync(path: string, mode: number): void
```

以同步方法改变文件权限。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | number | 是 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
fileio.chmodSync(filePath, 0o700);
```
