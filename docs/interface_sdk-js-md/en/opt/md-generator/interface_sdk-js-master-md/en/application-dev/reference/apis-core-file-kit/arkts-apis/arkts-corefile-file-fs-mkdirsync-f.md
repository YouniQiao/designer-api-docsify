# mkdirSync

## Modules to Import

```TypeScript
```

## mkdirSync

```TypeScript
declare function mkdirSync(path: string): void
```

Creates a directory. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function mkdirSync(path: string): void--><!--Device-unnamed-declare function mkdirSync(path: string): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

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


## mkdirSync

```TypeScript
declare function mkdirSync(path: string, recursion: boolean): void
```

Creates a directory. This API returns the result synchronously. The value **true** means to create a directory recursively.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function mkdirSync(path: string, recursion: boolean): void--><!--Device-unnamed-declare function mkdirSync(path: string, recursion: boolean): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| recursion | boolean | Yes |

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
