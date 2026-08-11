# readTextSync

## readTextSync

```TypeScript
declare function readTextSync(
  filePath: string,
  options?: {
    position?: number;
    length?: number;
    encoding?: string;
  }
): string
```

以同步方法基于文本方式读取文件（即直接读取文件的文本内容）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [@ohos.file.fs:readTextSync](arkts-corefile-fileio-readtextsync-f.md#readtextsync)

<!--Device-unnamed-declare function readTextSync(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): string--><!--Device-unnamed-declare function readTextSync(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): string-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| options | {     position?: number;     length?: number;     encoding?: string;   } | 否 |

**返回值：**

| 类型 |
| --- |
| string |
