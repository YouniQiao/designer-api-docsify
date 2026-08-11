# copyFile

## copyFile

```TypeScript
declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>
```

Copies a file. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:copyFile](arkts-corefile-fileio-copyfile-f.md#copyfile)

<!--Device-unnamed-declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>--><!--Device-unnamed-declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string \| number | Yes |
| dest | string \| number | Yes |
| mode | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |


## copyFile

```TypeScript
declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void
```

Copies a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:copyFile](arkts-corefile-fileio-copyfile-f.md#copyfile)

<!--Device-unnamed-declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string \| number | Yes |
| dest | string \| number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## copyFile

```TypeScript
declare function copyFile(
  src: string | number,
  dest: string | number,
  mode: number,
  callback: AsyncCallback<void>
): void
```

Copies a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:copyFile](arkts-corefile-fileio-copyfile-f.md#copyfile)

<!--Device-unnamed-declare function copyFile(  src: string | number,  dest: string | number,  mode: number,  callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copyFile(  src: string | number,  dest: string | number,  mode: number,  callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string \| number | Yes |
| dest | string \| number | Yes |
| mode | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
