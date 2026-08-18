# readText

## Modules to Import

```TypeScript
```

## readText

```TypeScript
declare function readText(
  filePath: string,
  options?: ReadTextOptions
): Promise<string>
```

Reads the text content of a file. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function readText(  filePath: string,  options?: ReadTextOptions): Promise<string>--><!--Device-unnamed-declare function readText(  filePath: string,  options?: ReadTextOptions): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| options | [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900019 |
| 13900024 |
| 13900025 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900044 |
| 13900013 |
| 13900008 |
| 13900041 |
| 13900010 |
| 13900042 |


## readText

```TypeScript
declare function readText(filePath: string, callback: AsyncCallback<string>): void
```

Reads the text content of a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function readText(filePath: string, callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function readText(filePath: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900019 |
| 13900024 |
| 13900025 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900013 |
| 13900008 |
| 13900041 |
| 13900010 |
| 13900042 |


## readText

```TypeScript
declare function readText(
  filePath: string,
  options: ReadTextOptions,
  callback: AsyncCallback<string>
): void
```

Reads the text content of a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function readText(  filePath: string,  options: ReadTextOptions,  callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function readText(  filePath: string,  options: ReadTextOptions,  callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| options | [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900019 |
| 13900024 |
| 13900025 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900013 |
| 13900008 |
| 13900041 |
| 13900010 |
| 13900042 |
