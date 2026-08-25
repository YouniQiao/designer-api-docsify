# getCfgFiles（系统接口）

## 导入模块

```TypeScript
import { configPolicy } from 'kits/@kit.BasicServicesKit';
```

## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string, callback: AsyncCallback<Array<string>>): void
```

获取指定文件名的所有文件列表，按优先级从低到高。使用callback异步回调。 例如，config.xml在设备中的路径按优先级升序排列为：/system/etc/config.xml、/sys_pod/etc/config.xml。 最终返回的是：/system/etc/config.xml, /sys_pod/etc/config.xml。

**起始版本：** 8

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relPath | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string, followMode: FollowXMode, callback: AsyncCallback<Array<string>>): void
```

根据提供的跟随模式获取指定文件名所有的文件列表，按优先级从低到高。使用callback异步回调。 例如，config.xml在设备中的路径按优先级升序排列为：/system/etc/config.xml、/sys_pod/etc/config.xml、 /sys_pod/etc/carrier/46060/etc/config.xml。设备默认卡opkey为46060，设置的followMode为 configPolicy.FollowXMode.SIM_DEFAULT。最终返回的是：/system/etc/config.xml, /sys_pod/etc/config.xml, /sys_pod/etc/carrier/46060/etc/config.xml。

**起始版本：** 11

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relPath | string | 是 |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string, followMode: FollowXMode, extra: string, callback: AsyncCallback<Array<string>>): void
```

根据提供的跟随模式获取指定文件名所有的文件列表，按优先级从低到高。使用callback异步回调。 例如，config.xml在设备中的路径按优先级升序排列为：/system/etc/config.xml、/sys_pod/etc/config.xml、 /sys_pod/etc/carrier/46060/etc/config.xml。设备卡1的opkey为46060，设置的followMode为 configPolicy.FollowXMode.USER_DEFINED，自定义跟随规则为"etc/carrier/\${telephony.sim.opkey0}"。 最终返回的是：/system/etc/config.xml, /sys_pod/etc/config.xml, /sys_pod/etc/carrier/46060/etc/config.xml。

**起始版本：** 11

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relPath | string | 是 |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | 是 |
| extra | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string): Promise<Array<string>>
```

获取指定文件名的所有文件列表，按优先级从低到高。使用Promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relPath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getCfgFiles

```TypeScript
function getCfgFiles(relPath: string, followMode: FollowXMode, extra?: string): Promise<Array<string>>
```

根据提供的跟随模式获取指定文件名所有的文件列表，按优先级从低到高。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relPath | string | 是 |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | 是 |
| extra | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
