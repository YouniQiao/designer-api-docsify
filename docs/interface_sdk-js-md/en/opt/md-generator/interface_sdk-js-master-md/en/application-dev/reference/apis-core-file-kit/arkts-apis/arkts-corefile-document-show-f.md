# show

## Modules to Import

```TypeScript
```

## show

```TypeScript
declare function show(uri: string, type: string): Promise<void>
```

Opens a file. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

<!--Device-unnamed-declare function show(uri: string, type: string): Promise<void>--><!--Device-unnamed-declare function show(uri: string, type: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| type | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |


## show

```TypeScript
declare function show(uri: string, type: string, callback: AsyncCallback<void>): void
```

Opens a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

<!--Device-unnamed-declare function show(uri: string, type: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function show(uri: string, type: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| type | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
