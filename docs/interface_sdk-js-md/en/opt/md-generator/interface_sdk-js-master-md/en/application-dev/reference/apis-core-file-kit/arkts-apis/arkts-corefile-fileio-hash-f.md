# hash

## hash

```TypeScript
declare function hash(path: string, algorithm: string): Promise<string>
```

Calculates the hash value of a file. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [hash](arkts-file-hash.md#@ohos.file.hash)

<!--Device-unnamed-declare function hash(path: string, algorithm: string): Promise<string>--><!--Device-unnamed-declare function hash(path: string, algorithm: string): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |


## hash

```TypeScript
declare function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void
```

Calculates the hash value of a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [hash](arkts-file-hash.md#@ohos.file.hash)

<!--Device-unnamed-declare function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |
