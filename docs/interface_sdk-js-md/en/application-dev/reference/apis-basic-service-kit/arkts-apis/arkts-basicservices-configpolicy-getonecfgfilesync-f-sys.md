# getOneCfgFileSync (System API)

## Modules to Import

```TypeScript
import { configPolicy } from 'kits/@kit.BasicServicesKit';
```

## getOneCfgFileSync

```TypeScript
function getOneCfgFileSync(relPath: string, followMode?: FollowXMode, extra?: string): string
```

根据提供的跟随模式，获取指定文件名优先级最高的配置文件路径。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-configPolicy-function getOneCfgFileSync(relPath: string, followMode?: FollowXMode, extra?: string): string--><!--Device-configPolicy-function getOneCfgFileSync(relPath: string, followMode?: FollowXMode, extra?: string): string-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| relPath | string | Yes | 配置文件名。 |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | No | 跟随模式，不设置时，默认使用 [DEFAULT](arkts-basicservices-configpolicy-followxmode-e-sys.md#default)。 |
| extra | string | No | 用户自定义跟随规则，仅在followMode为 [USER_DEFINED](arkts-basicservices-configpolicy-followxmode-e-sys.md#user_defined)时有效。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回优先级最高的配置文件路径。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types; &lt;br&gt;3.Parameter verification failed. |

