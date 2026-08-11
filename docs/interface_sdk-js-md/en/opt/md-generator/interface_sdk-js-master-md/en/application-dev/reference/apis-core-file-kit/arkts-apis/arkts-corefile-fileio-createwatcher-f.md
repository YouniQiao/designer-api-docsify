# createWatcher

## createWatcher

```TypeScript
declare function createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher
```

Listens for file or directory changes. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [@ohos.file.fs:createWatcher](arkts-corefile-fileio-createwatcher-f.md#createwatcher)

<!--Device-unnamed-declare function createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher--><!--Device-unnamed-declare function createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filename | string | Yes |
| events | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Watcher](arkts-corefile-file-fs-watcher-i.md) |
