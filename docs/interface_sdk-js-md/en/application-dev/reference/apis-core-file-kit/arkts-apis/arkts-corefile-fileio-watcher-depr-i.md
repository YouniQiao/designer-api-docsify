# Watcher

Listens for file change. You can call the **Watcher.stop()** method synchronously or asynchronously to stop the listening.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [Watcher](arkts-corefile-file-fs-watcher-i.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
```

## stop

```TypeScript
stop(): Promise<void>
```

Stops the **watcher** instance. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [stop](arkts-corefile-file-fs-watcher-i.md#stop)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops the **watcher** instance. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [stop](arkts-corefile-file-fs-watcher-i.md#stop)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
