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

Reads the text content of a file. This API uses a promise to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:readText](arkts-corefile-fileio-readtext-f.md#readtext)

<!--Device-unnamed-declare function readText(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): Promise<string>--><!--Device-unnamed-declare function readText(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file to read. |
| options | {     position?: number;     length?: number;     encoding?: string;   } | No | The options are as follows:&lt;br&gt;- **position** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position.&lt;br&gt;- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length minus the offset.&lt;br&gt;- **encoding** (string): format of the data to be encoded.&lt;br&gt;It is valid only when the data is of the string type.&lt;br&gt;The default value is **'utf-8'**, which is the only value supported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise that returns the file content read. |


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

Reads the text content of a file. This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:readText](arkts-corefile-fileio-readtext-f.md#readtext)

<!--Device-unnamed-declare function readText(  filePath: string,  options: {    position?: number;    length?: number;    encoding?: string;  },  callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function readText(  filePath: string,  options: {    position?: number;    length?: number;    encoding?: string;  },  callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file to read. |
| options | {     position?: number;     length?: number;     encoding?: string;   } | Yes | The options are as follows:&lt;br&gt;- **position** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position.&lt;br&gt;- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length minus the offset.&lt;br&gt;- **encoding**: format of the data to be encoded. The default value is **'utf-8'**, which is the only value supported. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Callback used to return the file content read. |

