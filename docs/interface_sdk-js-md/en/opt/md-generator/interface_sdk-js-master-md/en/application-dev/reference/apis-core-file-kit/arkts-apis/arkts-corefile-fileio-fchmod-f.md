# fchmod

## fchmod

```TypeScript
declare function fchmod(fd: number, mode: number): Promise<void>
```

Changes file permissions based on the file descriptor. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

<!--Device-unnamed-declare function fchmod(fd: number, mode: number): Promise<void>--><!--Device-unnamed-declare function fchmod(fd: number, mode: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| mode | number | Yes | Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (\|

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |


## fchmod

```TypeScript
declare function fchmod(fd: number, mode: number, callback: AsyncCallback<void>): void
```

Changes file permissions based on the file descriptor. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

<!--Device-unnamed-declare function fchmod(fd: number, mode: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function fchmod(fd: number, mode: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| mode | number | Yes | Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (\|
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
