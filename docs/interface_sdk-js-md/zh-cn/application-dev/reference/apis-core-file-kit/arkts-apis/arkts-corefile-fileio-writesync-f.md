# writeSync

## 导入模块

```TypeScript
```

## writeSync

```TypeScript
declare function writeSync(
  fd: number,
  buffer: ArrayBuffer | string,
  options?: {
    offset?: number;
    length?: number;
    position?: number;
    encoding?: string;
  }
): number
```

以同步方法将数据写入文件。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [writeSync](arkts-corefile-file-fs-writesync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| buffer | ArrayBuffer \| string | 是 |
| options | {     offset?: number;     length?: number;     position?: number;     encoding?: string;   } | 否 |

**返回值：**

| 类型 |
| --- |
| number |
