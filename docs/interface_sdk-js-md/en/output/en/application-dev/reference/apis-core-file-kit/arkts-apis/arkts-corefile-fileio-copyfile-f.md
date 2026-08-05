# copyFile

## copyFile

```TypeScript
declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>
```

Copies a file. This API uses a promise to return the result.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:copyFile](arkts-corefile-fileio-copyfile-f.md#copyfile)

<!--Device-unnamed-declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>--><!--Device-unnamed-declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string \| number | Yes | Path or file descriptor of the source file to copy. |
| dest | string \| number | Yes | Path or file descriptor of the destination file. |
| mode | number | No | Option for overwriting the destination file. The default value is **0**, which is the only value supported.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_**0**: Overwrite the file with the same name completely and truncate the part that is not overwritten. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |


## copyFile

```TypeScript
declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void
```

Copies a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:copyFile](arkts-corefile-fileio-copyfile-f.md#copyfile)

<!--Device-unnamed-declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string \| number | Yes | Path or file descriptor of the source file to copy. |
| dest | string \| number | Yes | Path or file descriptor of the destination file. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback invoked when the file is copied asynchronously. |


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

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:copyFile](arkts-corefile-fileio-copyfile-f.md#copyfile)

<!--Device-unnamed-declare function copyFile(  src: string | number,  dest: string | number,  mode: number,  callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copyFile(  src: string | number,  dest: string | number,  mode: number,  callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string \| number | Yes | Path or file descriptor of the source file to copy. |
| dest | string \| number | Yes | Path or file descriptor of the destination file. |
| mode | number | Yes | Option for overwriting the destination file. The default value is **0**, which is the only value supported.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_**0**: Overwrite the file with the same name completely and truncate the part that is not overwritten. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback invoked when the file is copied asynchronously. |

