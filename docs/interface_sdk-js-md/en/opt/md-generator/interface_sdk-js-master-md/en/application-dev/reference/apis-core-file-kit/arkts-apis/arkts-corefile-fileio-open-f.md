# open

## open

```TypeScript
declare function open(path: string, flags?: number, mode?: number): Promise<number>
```

Opens a file. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:open](arkts-corefile-fileio-open-f.md#open)

<!--Device-unnamed-declare function open(path: string, flags?: number, mode?: number): Promise<number>--><!--Device-unnamed-declare function open(path: string, flags?: number, mode?: number): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| flags | number | No | Option for opening the file. You must specify one of the following options. By default, the file is opened in read-only mode.&lt;br&gt;- **0o0**: Open the file in read-only mode.&lt;br&gt;- **0o1**: Open the file in write-only mode.&lt;br&gt;- **0o2**: Open the file in read/write mode.&lt;br&gt;In addition, you can specify the following options, separated using a bitwise OR operator (\|
| mode | number | No | Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (\|

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |


## open

```TypeScript
declare function open(path: string, callback: AsyncCallback<number>): void
```

Opens a file. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:open](arkts-corefile-fileio-open-f.md#open)

<!--Device-unnamed-declare function open(path: string, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function open(path: string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |


## open

```TypeScript
declare function open(path: string, flags: number, callback: AsyncCallback<number>): void
```

Opens a file. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:open](arkts-corefile-fileio-open-f.md#open)

<!--Device-unnamed-declare function open(path: string, flags: number, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function open(path: string, flags: number, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| flags | number | Yes | Option for opening the file. You must specify one of the following options. By default, the file is opened in read-only mode.&lt;br&gt;- **0o0**: Open the file in read-only mode.&lt;br&gt;- **0o1**: Open the file in write-only mode.&lt;br&gt;- **0o2**: Open the file in read/write mode.&lt;br&gt;In addition, you can specify the following options, separated using a bitwise OR operator (\|
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |


## open

```TypeScript
declare function open(path: string, flags: number, mode: number, callback: AsyncCallback<number>): void
```

Opens a file. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:open](arkts-corefile-fileio-open-f.md#open)

<!--Device-unnamed-declare function open(path: string, flags: number, mode: number, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function open(path: string, flags: number, mode: number, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| flags | number | Yes | Option for opening the file. You must specify one of the following options. By default, the file is opened in read-only mode.&lt;br&gt;- **0o0**: Open the file in read-only mode.&lt;br&gt;- **0o1**: Open the file in write-only mode.&lt;br&gt;- **0o2**: Open the file in read/write mode.&lt;br&gt;In addition, you can specify the following options, separated using a bitwise OR operator (\|
| mode | number | Yes | Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (\|
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |
