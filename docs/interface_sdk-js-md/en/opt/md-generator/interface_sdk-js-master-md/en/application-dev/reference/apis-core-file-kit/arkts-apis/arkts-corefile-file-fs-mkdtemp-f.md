# mkdtemp

## Modules to Import

```TypeScript
```

## mkdtemp

```TypeScript
declare function mkdtemp(prefix: string): Promise<string>
```

Creates a temporary directory. This API uses a promise to return the result.

**Since:** 9

<!--Device-unnamed-declare function mkdtemp(prefix: string): Promise<string>--><!--Device-unnamed-declare function mkdtemp(prefix: string): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| prefix | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900018 |
| 13900028 |
| 13900030 |
| 13900025 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |


## mkdtemp

```TypeScript
declare function mkdtemp(prefix: string, callback: AsyncCallback<string>): void
```

Creates a temporary directory. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-unnamed-declare function mkdtemp(prefix: string, callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function mkdtemp(prefix: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| prefix | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900018 |
| 13900028 |
| 13900030 |
| 13900025 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |
