# getCfgFiles (System API)

## Modules to Import

```TypeScript
import { configPolicy } from '@kit.BasicServicesKit';
```

## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string, callback: AsyncCallback<Array<string>>): void
```

Obtains a list of all files with the specified names, in ascending order of priority. This API uses an asynchronous callback to return the result. For example, if the paths of **config.xml** on the device are **\/system/etc/config.xml** and **\/sys_pod/etc/config.xml** in ascending order of priority, **\/system/etc/config.xml, /sys_pod/etc/config.xml** is returned.

**Since:** 8

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| relPath | string | Yes | Name of the configuration file. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | Callback used to return the result. If the file list is successfully obtained, **err** is **undefined**, and **data** is the obtained file list. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified;  2.Incorrect parameter types. |

**Examples**

```TypeScript
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

configPolicy.getCfgFiles('etc/config.xml', (err: BusinessError, data: Array<string>) => {
  if (err == null) {
    console.info('data is ' + data);
  } else {
    console.error('err: ' + err.code + ', ' + err.message);
  }
});
```


## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string, followMode: FollowXMode, callback: AsyncCallback<Array<string>>): void
```

Obtains a list of all files of a specified file name based on the provided follow mode, in ascending order of priority. This API uses an asynchronous callback to return the result. For example, if the paths of **config.xml** on the device are **\/system/etc/config.xml**, **\/sys_pod/etc/config.xml**, and **\/sys_pod/etc/carrier/46060/etc/config.xml** in ascending order of priority, the default opkey of the device is **46060**, and **followMode** is set to **configPolicy.FollowXMode.SIM_DEFAULT**, the return value is **\/system/etc/config.xml, /sys_pod/etc/config.xml, /sys_pod/etc/carrier/46060/etc/config.xml**.

**Since:** 11

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| relPath | string | Yes | Name of the configuration file. |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | Yes | Follow mode. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | Callback used to return the result. If the file list is successfully obtained, **err** is **undefined**, and **data** is the obtained file list. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified;  2.Incorrect parameter types. |

**Examples**

```TypeScript
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

let relpath: string = 'etc/config.xml';
configPolicy.getCfgFiles(relpath, configPolicy.FollowXMode.SIM_DEFAULT,
  (err: BusinessError, data: Array<string>) => {
    if (err == null) {
      console.info('data is ' + data);
    } else {
      console.error('err: ' + err.code + ', ' + err.message);
    }
  });
```


## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string, followMode: FollowXMode, extra: string, callback: AsyncCallback<Array<string>>): void
```

Obtains a list of all files of a specified file name based on the provided follow mode, in ascending order of priority. This API uses an asynchronous callback to return the result. For example, if the paths of **config.xml** on the device are **\/system/etc/config.xml**, **\/sys_pod/etc/config.xml**, and **\/sys_pod/etc/carrier/46060/etc/config.xml** in ascending order of priority, the opkey of the device card 1 is **46060**, **followMode** is set to **configPolicy.FollowXMode.USER_DEFINED**, and the custom follow rule is **"etc/carrier/\${telephony.sim.opkey0}"**, the return value is **\/system/etc/config.xml, /sys_pod/etc/config.xml, /sys_pod/etc/carrier/46060/etc/config.xml**.

**Since:** 11

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| relPath | string | Yes | Name of the configuration file. |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | Yes | Follow mode. |
| extra | string | Yes | Custom follow rule. This parameter is valid only when **followMode** is set to [USER_DEFINED](arkts-basicservices-configpolicy-followxmode-e-sys.md#user_defined). |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | Callback used to return the result. If the file list is successfully obtained, **err** is **undefined**, and **data** is the obtained file list. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified;  2.Incorrect parameter types. |

**Examples**

```TypeScript
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

let relpath: string = 'etc/config.xml';
let extra: string = 'etc/carrier/${telephony.sim.opkey0}';
configPolicy.getCfgFiles(relpath, configPolicy.FollowXMode.SIM_DEFAULT, extra,
  (err: BusinessError, data: Array<string>) => {
    if (err == null) {
      console.info('data is ' + data);
    } else {
      console.error('err: ' + err.code + ', ' + err.message);
    }
  });
```


## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string): Promise<Array<string>>
```

Obtains a list of all files with the specified names, in ascending order of priority. This API uses a promise to return the result.

**Since:** 8

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| relPath | string | Yes | Name of the configuration file. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise used to return the file list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified;  2.Incorrect parameter types. |

**Examples**

```TypeScript
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

async function fetchCfgFiles() {
  try {
    let relpath: string = 'etc/config.xml';
    let value: Array<string> = await configPolicy.getCfgFiles(relpath);
    console.info('value is ' + value);
  } catch (error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    console.error('error:' + code + ', ' + message);
  }
}

fetchCfgFiles();
```


## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string, followMode: FollowXMode, extra?: string): Promise<Array<string>>
```

Obtains a list of all files of a specified file name based on the provided follow mode, in ascending order of priority. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| relPath | string | Yes | Name of the configuration file. |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | Yes | Follow mode. |
| extra | string | No | Custom follow rule. This parameter is valid only when **followMode** is set to [USER_DEFINED](arkts-basicservices-configpolicy-followxmode-e-sys.md#user_defined). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise used to return the file list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified;  2.Incorrect parameter types;  3.Parameter verification failed. |

**Examples**

```TypeScript
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

async function fetchCfgFiles() {
  try {
    let relpath: string = 'etc/config.xml';
    let extra: string = 'etc/carrier/${telephony.sim.opkey0}';
    let value: Array<string> = await configPolicy.getCfgFiles(relpath, configPolicy.FollowXMode.SIM_DEFAULT, extra);
    console.info('value is ' + value);
  } catch (error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    console.error('error:' + code + ', ' + message);
  }
}

fetchCfgFiles();
```
