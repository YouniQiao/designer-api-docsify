# getOneCfgFile（系统接口）

## 导入模块

```TypeScript
```

## getOneCfgFile

```TypeScript
function getOneCfgFile(relPath: string, callback: AsyncCallback<string>): void
```

获取指定文件名优先级最高的配置文件路径。使用callback异步回调。 例如，config.xml在设备中的路径按优先级升序排列为：/system/etc/config.xml、/sys_pod/etc/config.xml， 最终返回优先级最高的是：/sys_pod/etc/config.xml。

**起始版本：** 23

<!--Device-configPolicy-function getOneCfgFile(relPath: string, callback: AsyncCallback<string>): void--><!--Device-configPolicy-function getOneCfgFile(relPath: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relPath | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getOneCfgFile

```TypeScript
function getOneCfgFile(relPath: string, followMode: FollowXMode, callback: AsyncCallback<string>): void
```

根据提供的跟随模式获取指定文件名优先级最高的配置文件路径。使用callback异步回调。 例如，config.xml在设备中的路径按优先级升序排列为：/system/etc/config.xml、/sys_pod/etc/config.xml、 /sys_pod/etc/carrier/46060/etc/ config.xml。设备默认卡opkey为46060，设置的followMode为configPolicy.FollowXMode.SIM_DEFAULT。最终返回的是： /sys_pod/etc/carrier/46060/etc/config.xml。

**起始版本：** 23

<!--Device-configPolicy-function getOneCfgFile(relPath: string, followMode: FollowXMode, callback: AsyncCallback<string>): void--><!--Device-configPolicy-function getOneCfgFile(relPath: string, followMode: FollowXMode, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relPath | string | 是 |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getOneCfgFile

```TypeScript
function getOneCfgFile(relPath: string, followMode: FollowXMode, extra: string, callback: AsyncCallback<string>): void
```

根据跟随模式获取指定文件优先级最高的配置文件路径。使用callback异步回调。 例如，config.xml在设备中的路径按优先级升序排列为：/system/etc/config.xml、/sys_pod/etc/config.xml、 /sys_pod/etc/carrier/46060/etc/config.xml。设备卡1的opkey为46060，设置的followMode为 configPolicy.FollowXMode.USER_DEFINED，自定义跟随规则为"etc/carrier/\${telephony.sim.opkey0}"。 最终返回的是：/sys_pod/etc/carrier/46060/etc/config.xml。

**起始版本：** 23

<!--Device-configPolicy-function getOneCfgFile(relPath: string, followMode: FollowXMode, extra: string, callback: AsyncCallback<string>): void--><!--Device-configPolicy-function getOneCfgFile(relPath: string, followMode: FollowXMode, extra: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relPath | string | 是 |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | 是 |
| extra | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getOneCfgFile

```TypeScript
function getOneCfgFile(relPath: string): Promise<string>
```

获取指定文件名优先级最高的配置文件路径。使用Promise异步回调。

**起始版本：** 23

<!--Device-configPolicy-function getOneCfgFile(relPath: string): Promise<string>--><!--Device-configPolicy-function getOneCfgFile(relPath: string): Promise<string>-End-->

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relPath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getOneCfgFile

```TypeScript
function getOneCfgFile(relPath: string, followMode: FollowXMode, extra?: string): Promise<string>
```

根据提供的跟随模式，获取指定文件名优先级最高的配置文件路径。使用Promise异步回调。

**起始版本：** 23

<!--Device-configPolicy-function getOneCfgFile(relPath: string, followMode: FollowXMode, extra?: string): Promise<string>--><!--Device-configPolicy-function getOneCfgFile(relPath: string, followMode: FollowXMode, extra?: string): Promise<string>-End-->

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
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
