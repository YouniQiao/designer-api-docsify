# getCfgFiles (System API)

## Modules to Import

```TypeScript
import { configPolicy } from 'kits/@kit.BasicServicesKit';
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| relPath | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string, followMode: FollowXMode, callback: AsyncCallback<Array<string>>): void
```

Obtains a list of all files of a specified file name based on the provided follow mode, in ascending order of priority. This API uses an asynchronous callback to return the result. For example, if the paths of **config.xml** on the device are **\/system/etc/config.xml**, **\/sys_pod/etc/config.xml**, and **\/sys_pod/etc/carrier/46060/etc/config.xml** in ascending order of priority, the default opkey of the device is **46060**, and **followMode** is set to **configPolicy.FollowXMode.SIM_DEFAULT**, the return value is **\/system/etc/config.xml, /sys_pod/etc/config.xml, /sys_pod/etc/carrier/46060/etc/config.xml**.

**Since:** 11

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| relPath | string | Yes |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string, followMode: FollowXMode, extra: string, callback: AsyncCallback<Array<string>>): void
```

Obtains a list of all files of a specified file name based on the provided follow mode, in ascending order of priority. This API uses an asynchronous callback to return the result. For example, if the paths of **config.xml** on the device are **\/system/etc/config.xml**, **\/sys_pod/etc/config.xml**, and **\/sys_pod/etc/carrier/46060/etc/config.xml** in ascending order of priority, the opkey of the device card 1 is **46060**, **followMode** is set to **configPolicy.FollowXMode.USER_DEFINED**, and the custom follow rule is **"etc/carrier/\${telephony.sim.opkey0}"**, the return value is **\/system/etc/config.xml, /sys_pod/etc/config.xml, /sys_pod/etc/carrier/46060/etc/config.xml**.

**Since:** 11

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| relPath | string | Yes |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | Yes |
| extra | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string): Promise<Array<string>>
```

Obtains a list of all files with the specified names, in ascending order of priority. This API uses a promise to return the result.

**Since:** 8

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| relPath | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string, followMode: FollowXMode, extra?: string): Promise<Array<string>>
```

Obtains a list of all files of a specified file name based on the provided follow mode, in ascending order of priority. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| relPath | string | Yes |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | Yes |
| extra | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
