# fdopenStreamSync

## fdopenStreamSync

```TypeScript
declare function fdopenStreamSync(fd: number, mode: string): Stream
```

以同步方法基于文件描述符打开文件流。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:fdopenStreamSync](arkts-corefile-fileio-fdopenstreamsync-f.md#fdopenstreamsync)

<!--Device-unnamed-declare function fdopenStreamSync(fd: number, mode: string): Stream--><!--Device-unnamed-declare function fdopenStreamSync(fd: number, mode: string): Stream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | 待打开文件的文件描述符。 |
| mode | string | Yes | ?r：打开只读文件，该文件必须存在。&lt;br/&gt;-?r+：打开可读写的文件，该文件必须存在。&lt;br/&gt;-?w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则 建立该文件。&lt;br/&gt;-?w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。&lt;br/&gt;-?a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到 文件尾，即文件原先的内容会被保留。&lt;br/&gt;-?a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Stream](arkts-corefile-file-fs-stream-i.md) | 返回文件流的结果。 |

