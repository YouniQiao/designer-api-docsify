# getOneCfgFileSync (System API)

## Modules to Import

```TypeScript
import { configPolicy } from 'kits/@kit.BasicServicesKit';
```

## getOneCfgFileSync

```TypeScript
function getOneCfgFileSync(relPath: string, followMode?: FollowXMode, extra?: string): string
```

Obtains the path of the configuration file with the highest priority based on the provided follow mode.

**Since:** 11

<!--Device-configPolicy-function getOneCfgFileSync(relPath: string, followMode?: FollowXMode, extra?: string): string--><!--Device-configPolicy-function getOneCfgFileSync(relPath: string, followMode?: FollowXMode, extra?: string): string-End-->

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
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
