# getCfgFilesSync (System API)

## Modules to Import

```TypeScript
```

## getCfgFilesSync

```TypeScript
function getCfgFilesSync(relPath: string, followMode?: FollowXMode, extra?: string): Array<string>
```

Obtains a list of all files of a specified file name based on the provided follow mode, in ascending order of priority.

**Since:** 23

<!--Device-configPolicy-function getCfgFilesSync(relPath: string, followMode?: FollowXMode, extra?: string): Array<string>--><!--Device-configPolicy-function getCfgFilesSync(relPath: string, followMode?: FollowXMode, extra?: string): Array<string>-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| relPath | string | Yes |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | No |
| extra | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
