# mkdir

## Modules to Import

```TypeScript
```

## mkdir

```TypeScript
declare function mkdir(path: string, mode?: number): Promise<void>
```

Creates a directory. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [mkdir](arkts-corefile-file-fs-mkdir-f.md#mkdir)

<!--Device-unnamed-declare function mkdir(path: string, mode?: number): Promise<void>--><!--Device-unnamed-declare function mkdir(path: string, mode?: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | number | No | Permission on the directory to create. You can specify multiple permissions, separated using a bitwise OR operator (\|

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |


## mkdir

```TypeScript
declare function mkdir(path: string, callback: AsyncCallback<void>): void
```

Creates a directory. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [mkdir](arkts-corefile-file-fs-mkdir-f.md#mkdir)

<!--Device-unnamed-declare function mkdir(path: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function mkdir(path: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## mkdir

```TypeScript
declare function mkdir(path: string, mode: number, callback: AsyncCallback<void>): void
```

Creates a directory. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [mkdir](arkts-corefile-file-fs-mkdir-f.md#mkdir)

<!--Device-unnamed-declare function mkdir(path: string, mode: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function mkdir(path: string, mode: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | number | Yes | Permission on the directory to create. You can specify multiple permissions, separated using a bitwise OR operator (\|
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
