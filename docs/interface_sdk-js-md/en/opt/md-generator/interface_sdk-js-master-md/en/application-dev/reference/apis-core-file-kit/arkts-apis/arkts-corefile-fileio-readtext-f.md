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

**Deprecated since:** 9

**Substitutes:** [readText](arkts-corefile-file-fs-readtext-f.md#readText)

<!--Device-unnamed-declare function readText(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): Promise<string>--><!--Device-unnamed-declare function readText(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| options | {     position?: number;     length?: number;     encoding?: string;   } | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
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

Reads the text content of a file. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readText](arkts-corefile-file-fs-readtext-f.md#readText)

<!--Device-unnamed-declare function readText(  filePath: string,  options: {    position?: number;    length?: number;    encoding?: string;  },  callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function readText(  filePath: string,  options: {    position?: number;    length?: number;    encoding?: string;  },  callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| options | {     position?: number;     length?: number;     encoding?: string;   } | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |
