# fdatasync

## fdatasync

```TypeScript
declare function fdatasync(fd: number): Promise<void>
```

Synchronizes the data of a file. This API uses a promise to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:fdatasync](arkts-corefile-fileio-fdatasync-f.md#fdatasync)

<!--Device-unnamed-declare function fdatasync(fd: number): Promise<void>--><!--Device-unnamed-declare function fdatasync(fd: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to synchronize. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |


## fdatasync

```TypeScript
declare function fdatasync(fd: number, callback: AsyncCallback<void>): void
```

Synchronizes the data of a file. This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:fdatasync](arkts-corefile-fileio-fdatasync-f.md#fdatasync)

<!--Device-unnamed-declare function fdatasync(fd: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function fdatasync(fd: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to synchronize. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback invoked when the file data is synchronized in asynchronous mode. |

