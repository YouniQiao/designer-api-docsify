# createStream

## createStream

```TypeScript
declare function createStream(path: string, mode: string): Promise<Stream>
```

基于文件路径打开文件流，使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:createStream](arkts-corefile-fileio-createstream-f.md#createstream)

<!--Device-unnamed-declare function createStream(path: string, mode: string): Promise<Stream>--><!--Device-unnamed-declare function createStream(path: string, mode: string): Promise<Stream>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待打开文件的应用沙箱路径。 |
| mode | string | Yes | ?r：打开只读文件，该文件必须存在。&lt;br/&gt;-?r+：打开可读写的文件，该文件必须存在。&lt;br/&gt;-?w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则 建立该文件。&lt;br/&gt;-?w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。&lt;br/&gt;-?a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到 文件尾，即文件原先的内容会被保留。&lt;br/&gt;-?a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Stream&gt; | Promise对象。返回文件流的结果。 |


## createStream

```TypeScript
declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void
```

基于文件路径打开文件流，使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:createStream](arkts-corefile-fileio-createstream-f.md#createstream)

<!--Device-unnamed-declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void--><!--Device-unnamed-declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待打开文件的应用沙箱路径。 |
| mode | string | Yes | ?r：打开只读文件，该文件必须存在。&lt;br/&gt;-?r+：打开可读写的文件，该文件必须存在。&lt;br/&gt;-?w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则 建立该文件。&lt;br/&gt;-?w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。&lt;br/&gt;-?a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到 文件尾，即文件原先的内容会被保留。&lt;br/&gt;-?a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Stream&gt; | Yes | 异步打开文件流之后的回调。 |

