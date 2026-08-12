# readText

## readText

```TypeScript
declare function readText(
  filePath: string,
  options?: {
    position?: number;
    length?: number;
    encoding?: string;
  }
): Promise<string>
```

基于文本方式读取文件（即直接读取文件的文本内容），使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readText](arkts-corefile-file-fs-readtext-f.md#readText)

<!--Device-unnamed-declare function readText(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): Promise<string>--><!--Device-unnamed-declare function readText(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| options | {     position?: number;     length?: number;     encoding?: string;   } | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |


## readText

```TypeScript
declare function readText(
  filePath: string,
  options: {
    position?: number;
    length?: number;
    encoding?: string;
  },
  callback: AsyncCallback<string>
): void
```

基于文本方式读取文件（即直接读取文件的文本内容），使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readText](arkts-corefile-file-fs-readtext-f.md#readText)

<!--Device-unnamed-declare function readText(  filePath: string,  options: {    position?: number;    length?: number;    encoding?: string;  },  callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function readText(  filePath: string,  options: {    position?: number;    length?: number;    encoding?: string;  },  callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| options | {     position?: number;     length?: number;     encoding?: string;   } | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |
