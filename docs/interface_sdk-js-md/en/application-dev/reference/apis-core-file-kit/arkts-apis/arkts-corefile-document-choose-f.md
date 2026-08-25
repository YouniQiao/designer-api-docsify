# choose

## Modules to Import

```TypeScript
```

## choose

```TypeScript
declare function choose(types?: string[]): Promise<string>
```

Chooses files of the specified types. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | string[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |


## choose

```TypeScript
declare function choose(callback: AsyncCallback<string>): void
```

Chooses a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |


## choose

```TypeScript
declare function choose(types: string[], callback: AsyncCallback<string>): void
```

Chooses files of the specified types. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | string[] | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |
