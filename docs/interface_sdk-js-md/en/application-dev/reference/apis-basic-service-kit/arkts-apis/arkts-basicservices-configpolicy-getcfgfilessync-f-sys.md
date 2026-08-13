# getCfgFilesSync (System API)

## Modules to Import

```TypeScript
import { configPolicy } from '@kit.BasicServicesKit';
```

## getCfgFilesSync

```TypeScript
function getCfgFilesSync(relPath: string, followMode?: FollowXMode, extra?: string): Array<string>
```

Obtains a list of all files of a specified file name based on the provided follow mode, in ascending order of priority.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-configPolicy-function getCfgFilesSync(relPath: string, followMode?: FollowXMode, extra?: string): Array<string>--><!--Device-configPolicy-function getCfgFilesSync(relPath: string, followMode?: FollowXMode, extra?: string): Array<string>-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| relPath | string | Yes | Name of the configuration file. |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | No | Follow mode. The default value is [DEFAULT](arkts-basicservices-configpolicy-followxmode-e-sys.md#DEFAULT) if this parameter is not set. |
| extra | string | No | Custom follow rule. This parameter is valid only when **followMode** is set to [USER_DEFINED](arkts-basicservices-configpolicy-followxmode-e-sys.md#USER_DEFINED). |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | List of configuration files obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types; &lt;br&gt;3.Parameter verification failed. |

