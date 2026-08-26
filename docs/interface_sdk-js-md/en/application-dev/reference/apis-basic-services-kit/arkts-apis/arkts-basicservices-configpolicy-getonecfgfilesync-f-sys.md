# getOneCfgFileSync (System API)

## Modules to Import

```TypeScript
import configPolicy from '@kit.BasicServicesKit';
```

## getOneCfgFileSync

```TypeScript
function getOneCfgFileSync(relPath: string, followMode?: FollowXMode, extra?: string): string
```

Obtains the path of the configuration file with the highest priority based on the provided follow mode.

**Since:** 11

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| relPath | string | Yes | Name of the configuration file. |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | No | Follow mode. The default value is [DEFAULT](arkts-basicservices-configpolicy-followxmode-e-sys.md#default) if this parameter is not set. |
| extra | string | No | Custom follow rule. This parameter is valid only when **followMode** is set to [USER_DEFINED](arkts-basicservices-configpolicy-followxmode-e-sys.md#user_defined). |

**Return value:**

| Type | Description |
| --- | --- |
| string | The path of the configuration file with the highest priority obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified;  2.Incorrect parameter types;  3.Parameter verification failed. |

**Examples**

```TypeScript
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

try {
  let relpath: string = 'etc/config.xml';
  let extra: string = 'etc/carrier/${telephony.sim.opkey0}';
  let result: string = configPolicy.getOneCfgFileSync(relpath, configPolicy.FollowXMode.USER_DEFINED, extra);
  console.info('result is ' + result);
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error('error:' + code + ', ' + message);
}
```
