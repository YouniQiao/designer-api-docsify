# read

## read

```TypeScript
declare function read(
  fd: number,
  buffer: ArrayBuffer,
  options?: {
    offset?: number;
    length?: number;
    position?: number;
  }
): Promise<ReadOut>
```

Reads data from a file. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:read](arkts-corefile-fileio-read-f.md#read)

<!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options?: {    offset?: number;    length?: number;    position?: number;  }): Promise<ReadOut>--><!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options?: {    offset?: number;    length?: number;    position?: number;  }): Promise<ReadOut>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| buffer | ArrayBuffer | Yes |
| options | {     offset?: number;     length?: number;     position?: number;   } | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ReadOut&gt; |


## read

```TypeScript
declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void
```

Reads data from a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:read](arkts-corefile-fileio-read-f.md#read)

<!--Device-unnamed-declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void--><!--Device-unnamed-declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| buffer | ArrayBuffer | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ReadOut&gt; | Yes |


## read

```TypeScript
declare function read(
  fd: number,
  buffer: ArrayBuffer,
  options: {
    offset?: number;
    length?: number;
    position?: number;
  },
  callback: AsyncCallback<ReadOut>
): void
```

Reads data from a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:read](arkts-corefile-fileio-read-f.md#read)

<!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options: {    offset?: number;    length?: number;    position?: number;  },  callback: AsyncCallback<ReadOut>): void--><!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options: {    offset?: number;    length?: number;    position?: number;  },  callback: AsyncCallback<ReadOut>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| buffer | ArrayBuffer | Yes |
| options | {     offset?: number;     length?: number;     position?: number;   } | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ReadOut&gt; | Yes |
