# readSync

## 导入模块

```TypeScript
```

## readSync

```TypeScript
declare function readSync(
  fd: number,
  buffer: ArrayBuffer,
  options?: {
    offset?: number;
    length?: number;
    position?: number;
  }
): number
```

以同步方法从文件读取数据。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [readSync](arkts-corefile-file-fs-readsync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| buffer | ArrayBuffer | 是 |
| options | {     offset?: number;     length?: number;     position?: number;   } | 否 |

**返回值：**

| 类型 |
| --- |
| number |
