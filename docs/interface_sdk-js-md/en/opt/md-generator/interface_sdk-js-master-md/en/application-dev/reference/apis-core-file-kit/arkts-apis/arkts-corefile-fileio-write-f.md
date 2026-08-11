# write

## write

```TypeScript
declare function write(
  fd: number,
  buffer: ArrayBuffer | string,
  options?: {
    offset?: number;
    length?: number;
    position?: number;
    encoding?: string;
  }
): Promise<number>
```

Writes data into a file. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:write](arkts-corefile-fileio-write-f.md#write)

<!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): Promise<number>--><!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| buffer | ArrayBuffer \| string | Yes |
| options | {     offset?: number;     length?: number;     position?: number;     encoding?: string;   } | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |


## write

```TypeScript
declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

Writes data to a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:write](arkts-corefile-fileio-write-f.md#write)

<!--Device-unnamed-declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| buffer | ArrayBuffer \| string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |


## write

```TypeScript
declare function write(
  fd: number,
  buffer: ArrayBuffer | string,
  options: {
    offset?: number;
    length?: number;
    position?: number;
    encoding?: string;
  },
  callback: AsyncCallback<number>
): void
```

Writes data to a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:write](arkts-corefile-fileio-write-f.md#write)

<!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  },  callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  },  callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| buffer | ArrayBuffer \| string | Yes |
| options | {     offset?: number;     length?: number;     position?: number;     encoding?: string;   } | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |
