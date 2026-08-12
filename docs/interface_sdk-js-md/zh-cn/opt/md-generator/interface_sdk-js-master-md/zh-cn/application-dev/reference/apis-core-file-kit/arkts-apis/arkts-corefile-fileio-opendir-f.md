# opendir

## opendir

```TypeScript
declare function opendir(path: string): Promise<Dir>
```

打开文件目录，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md#listFile)

<!--Device-unnamed-declare function opendir(path: string): Promise<Dir>--><!--Device-unnamed-declare function opendir(path: string): Promise<Dir>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Dir](arkts-corefile-fileio-dir-depr-i.md)&gt; |


## opendir

```TypeScript
declare function opendir(path: string, callback: AsyncCallback<Dir>): void
```

打开文件目录，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md#listFile)

<!--Device-unnamed-declare function opendir(path: string, callback: AsyncCallback<Dir>): void--><!--Device-unnamed-declare function opendir(path: string, callback: AsyncCallback<Dir>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Dir](arkts-corefile-fileio-dir-depr-i.md)&gt; | 是 |
