# ResourceManager

提供访问应用资源和系统资源的能力，可访问的资源范围为当前Context对应的HAP/HSP模块中的资源以及所有的系统资源。

> **说明：**&gt;
> - ResourceManager涉及到的方法，仅限基于TS扩展的声明式开发范式使用。&gt;
> - 资源文件在工程的resources目录中定义，通过resName、resId、Resource对象等可以获取对应的字符串、字符串数组、颜色等资源值，resName为资源名称，resId可通过`\$r(资源地址).id`的方式
> 获取，例如`\$r('app.string.test').id`。&gt;
> - 单HAP包获取自身资源、跨HAP/HSP包获取资源，由于入参为Resource的接口相比于入参为resName、resId的接口耗时更长，因此更推荐使用参数为resName或resId的接口。跨HAP/HSP包获取资源，
> **需要先使用[createModuleContext](../../apis-ability-kit/arkts-apis/arkts-ability-application-createmodulecontext-f.md)创建对应module的context**，
> 再调用参数为resName或resId的接口。更多请参考[资源访问](../../../quick-start/resource-categories-and-access.md#资源访问)。&gt;
> - 在API version 22及之前版本，中间码HAR、字节码HAR通过资源ID相关接口访问资源时，因ID无效会抛出异常；从API version 23开始，中间码HAR、字节码HAR通过资源ID相关接口可以正常访问资源，
> 更多请参考[资源访问](../../../quick-start/resource-categories-and-access.md#资源访问)。

**起始版本：** 6

**系统能力：** SystemCapability.Global.ResourceManager

## 导入模块

```TypeScript
import { resourceManager } from 'kits/@kit.LocalizationKit';
```

## addResource

```TypeScript
addResource(path: string) : void
```

应用运行时加载指定的overlay资源，实现主题切换或资源覆盖。

> **说明：**&gt;
> rawfile和resfile目录不支持资源覆盖。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001010](../errorcode-resource-manager.md#9001010-无效的overlay路径) |

## closeRawFd

```TypeScript
closeRawFd(path: string, callback: _AsyncCallback<void>): void
```

关闭resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd）。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | _AsyncCallback & lt;void & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## closeRawFd

```TypeScript
closeRawFd(path: string): Promise<void>
```

关闭resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd）。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## closeRawFdSync

```TypeScript
closeRawFdSync(path: string): void
```

关闭resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd），使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## closeRawFileDescriptor

```TypeScript
closeRawFileDescriptor(path: string, callback: AsyncCallback<void>): void
```

关闭resources/rawfile目录下rawfile文件的文件描述符（fd）。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [closeRawFd](#closerawfd)(path: string, callback: _AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | AsyncCallback & lt;void & gt; | 是 |

## closeRawFileDescriptor

```TypeScript
closeRawFileDescriptor(path: string): Promise<void>
```

关闭resources/rawfile目录下rawfile文件的文件描述符（fd）。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [closeRawFd](#closerawfd)(path: string)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## getBoolean

```TypeScript
getBoolean(resId: number): boolean
```

获取指定资源ID值对应的布尔值，使用同步方式返回。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getBoolean

```TypeScript
getBoolean(resource: Resource): boolean
```

获取指定resource对象对应的布尔值，使用同步方式返回。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getBoolean](#getboolean)(resId: long)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getBooleanByName

```TypeScript
getBooleanByName(resName: string): boolean
```

获取指定资源名称对应的布尔值，使用同步方式返回。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getColor

```TypeScript
getColor(resId: number, callback: _AsyncCallback<number>): void
```

获取指定资源ID对应的颜色值。使用callback异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| callback | _AsyncCallback & lt;number & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getColor

```TypeScript
getColor(resId: number): Promise<number>
```

获取指定资源ID对应的颜色值。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getColor

```TypeScript
getColor(resource: Resource, callback: _AsyncCallback<number>): void
```

获取指定resource对象对应的颜色值。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getColor](#getcolor)(resId: long, callback: _AsyncCallback&lt;long&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| callback | _AsyncCallback & lt;number & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getColor

```TypeScript
getColor(resource: Resource): Promise<number>
```

获取指定resource对象对应的颜色值。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getColor](#getcolor)(resId: long)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getColorByName

```TypeScript
getColorByName(resName: string, callback: _AsyncCallback<number>): void
```

获取指定资源名称对应的颜色值。使用callback异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| callback | _AsyncCallback & lt;number & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getColorByName

```TypeScript
getColorByName(resName: string): Promise<number>
```

获取指定资源名称对应的颜色值。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getColorByNameSync

```TypeScript
getColorByNameSync(resName: string) : number
```

获取指定资源名称对应的颜色值，使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getColorSync

```TypeScript
getColorSync(resId: number) : number
```

获取指定资源ID对应的颜色值，使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getColorSync

```TypeScript
getColorSync(resource: Resource) : number
```

获取指定resource对象对应的颜色值，使用同步方式返回。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getColorSync](#getcolorsync)(resId: long)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getConfiguration

```TypeScript
getConfiguration(callback: _AsyncCallback<Configuration>): void
```

获取设备的Configuration。使用callback异步回调。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | _AsyncCallback & lt;Configuration & gt; | 是 |

## getConfiguration

```TypeScript
getConfiguration(): Promise<Configuration>
```

获取设备的Configuration。使用Promise异步回调。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;Configuration & gt; |

## getConfigurationSync

```TypeScript
getConfigurationSync(): Configuration
```

获取设备的Configuration，使用同步形式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 |
| --- |
| [Configuration](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) |

## getDeviceCapability

```TypeScript
getDeviceCapability(callback: _AsyncCallback<DeviceCapability>): void
```

获取设备的DeviceCapability。使用callback异步回调。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | _AsyncCallback&lt;[DeviceCapability](arkts-localization-resourcemanager-devicecapability-c.md)&gt; | 是 |

## getDeviceCapability

```TypeScript
getDeviceCapability(): Promise<DeviceCapability>
```

获取设备的DeviceCapability。使用Promise异步回调。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DeviceCapability](arkts-localization-resourcemanager-devicecapability-c.md)&gt; |

## getDeviceCapabilitySync

```TypeScript
getDeviceCapabilitySync(): DeviceCapability
```

获取设备的DeviceCapability，使用同步形式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 |
| --- |
| [DeviceCapability](arkts-localization-resourcemanager-devicecapability-c.md) |

## getDoublePluralStringByNameSync

```TypeScript
getDoublePluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string
```

获取指定资源名称对应的[单复数](../../../internationalization/l10n-singular-plural.md)字符串，并使用args参数依次替换字符串中的格式化占位符，使用同步方式返回。

> **说明：**&gt;
> - 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。&gt;
> - 在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本接口仅支持在基数词类型下使用。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| num | number | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |
| [9001008](../errorcode-resource-manager.md#9001008-根据当前名称获取的资源格式化失败) |

## getDoublePluralStringValueSync

```TypeScript
getDoublePluralStringValueSync(resId: number, num: number, ...args: Array<string | number>): string
```

获取指定资源ID对应的[单复数](../../../internationalization/l10n-singular-plural.md)字符串，并使用args参数依次替换字符串中的格式化占位符，使用同步方式返回。

> **说明：**&gt;
> - 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。&gt;
> - 在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本接口仅支持在基数词类型下使用。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| num | number | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |
| [9001007](../errorcode-resource-manager.md#9001007-根据当前id获取的资源格式化失败) |

## getDoublePluralStringValueSync

```TypeScript
getDoublePluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string
```

获取指定resource对象对应的[单复数](../../../internationalization/l10n-singular-plural.md)字符串，并使用args参数依次替换字符串中的格式化占位符，使用同步方式 返回。

> **说明：**&gt;
> - 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 18

**废弃版本：** 20

**替代接口：** [getDoublePluralStringValueSync](#getdoublepluralstringvaluesync)(resId: number, num: number, ...args: Array&lt;string | number&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| num | number | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |
| [9001007](../errorcode-resource-manager.md#9001007-根据当前id获取的资源格式化失败) |

## getDrawableDescriptor

```TypeScript
getDrawableDescriptor(resId: number, density?: number, type?: number): DrawableDescriptor
```

获取指定资源ID对应的DrawableDescriptor对象，用于图标的显示，使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| density | number | 否 |
| type | number | 否 |

**返回值：**

| 类型 |
| --- |
| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getDrawableDescriptor

```TypeScript
getDrawableDescriptor(resource: Resource, density?: number, type?: number): DrawableDescriptor
```

获取指定resource对应的DrawableDescriptor对象，用于图标的显示，使用同步方式返回。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getDrawableDescriptor](#getdrawabledescriptor)(resId: long, density?: int, type?: int)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| density | number | 否 |
| type | number | 否 |

**返回值：**

| 类型 |
| --- |
| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getDrawableDescriptorByName

```TypeScript
getDrawableDescriptorByName(resName: string, density?: number, type?: number): DrawableDescriptor
```

获取指定资源名称对应的DrawableDescriptor对象，用于图标的显示，使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| density | number | 否 |
| type | number | 否 |

**返回值：**

| 类型 |
| --- |
| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |

## getIntPluralStringByNameSync

```TypeScript
getIntPluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string
```

获取指定资源名称对应的[单复数](../../../internationalization/l10n-singular-plural.md)字符串，并使用args参数依次替换字符串中的格式化占位符，使用同步方式返回。

> **说明：**&gt;
> - 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。&gt;
> - 在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本接口仅支持在基数词类型下使用。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| num | number | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |
| [9001008](../errorcode-resource-manager.md#9001008-根据当前名称获取的资源格式化失败) |

## getIntPluralStringValueSync

```TypeScript
getIntPluralStringValueSync(resId: number, num: number,...args: Array<string | number>): string
```

获取指定资源ID对应的[单复数](../../../internationalization/l10n-singular-plural.md)字符串，并使用args参数依次替换字符串中的格式化占位符，使用同步方式返回。

> **说明：**&gt;
> - 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。&gt;
> - 在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本接口仅支持在基数词类型下使用。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| num | number | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |
| [9001007](../errorcode-resource-manager.md#9001007-根据当前id获取的资源格式化失败) |

## getIntPluralStringValueSync

```TypeScript
getIntPluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string
```

获取指定resource对象对应的[单复数](../../../internationalization/l10n-singular-plural.md)字符串，并使用args参数依次替换字符串中的格式化占位符，使用同步方式 返回。

> **说明：**&gt;
> - 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 18

**废弃版本：** 20

**替代接口：** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| num | number | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |
| [9001007](../errorcode-resource-manager.md#9001007-根据当前id获取的资源格式化失败) |

## getLocales

```TypeScript
getLocales(includeSystem?: boolean): Array<string>
```

获取应用的语言列表。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| includeSystem | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getMedia

```TypeScript
getMedia(resId: number, callback: AsyncCallback<Uint8Array>): void
```

获取指定资源ID对应的媒体文件内容。使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getMediaContent](#getmediacontent)(resId: long, callback: _AsyncCallback&lt;Uint8Array&gt;)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| callback | AsyncCallback & lt;Uint8Array & gt; | 是 |

## getMedia

```TypeScript
getMedia(resId: number): Promise<Uint8Array>
```

获取指定资源ID对应的媒体文件内容。使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getMediaContent](#getmediacontent)(resId: long)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

## getMediaBase64

```TypeScript
getMediaBase64(resId: number, callback: AsyncCallback<string>): void
```

获取指定资源ID对应的图片资源Base64编码。使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getMediaContentBase64](#getmediacontentbase64)(resId: long, callback: _AsyncCallback&lt;string&gt;)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| callback | AsyncCallback & lt;string & gt; | 是 |

## getMediaBase64

```TypeScript
getMediaBase64(resId: number): Promise<string>
```

获取指定资源ID对应的图片资源Base64编码。使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getMediaContentBase64](#getmediacontentbase64)(resId: long)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getMediaBase64ByName

```TypeScript
getMediaBase64ByName(resName: string, callback: _AsyncCallback<string>): void
```

获取指定资源名称对应的图片资源Base64编码。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| callback | _AsyncCallback & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |

## getMediaBase64ByName

```TypeScript
getMediaBase64ByName(resName: string, density: number, callback: _AsyncCallback<string>): void
```

获取指定资源名称对应的指定屏幕密度图片资源Base64编码。使用callback异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| density | number | 是 |
| callback | _AsyncCallback & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |

## getMediaBase64ByName

```TypeScript
getMediaBase64ByName(resName: string): Promise<string>
```

获取指定资源名称对应的图片资源Base64编码。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |

## getMediaBase64ByName

```TypeScript
getMediaBase64ByName(resName: string, density: number): Promise<string>
```

获取指定资源名称对应的指定屏幕密度图片资源Base64编码。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| density | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |

## getMediaBase64ByNameSync

```TypeScript
getMediaBase64ByNameSync(resName: string, density?: number): string
```

获取指定资源名称对应的默认或指定的屏幕密度图片资源Base64编码，使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| density | number | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |

## getMediaByName

```TypeScript
getMediaByName(resName: string, callback: _AsyncCallback<Uint8Array>): void
```

获取指定资源名称对应的媒体文件内容。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| callback | _AsyncCallback & lt;Uint8Array & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |

## getMediaByName

```TypeScript
getMediaByName(resName: string, density: number, callback: _AsyncCallback<Uint8Array>): void
```

获取指定资源名称对应的指定屏幕密度媒体文件内容。使用callback异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| density | number | 是 |
| callback | _AsyncCallback & lt;Uint8Array & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |

## getMediaByName

```TypeScript
getMediaByName(resName: string): Promise<Uint8Array>
```

获取指定资源名称对应的媒体文件内容。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |

## getMediaByName

```TypeScript
getMediaByName(resName: string, density: number): Promise<Uint8Array>
```

获取指定资源名称对应的指定屏幕密度媒体文件内容。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| density | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |

## getMediaByNameSync

```TypeScript
getMediaByNameSync(resName: string, density?: number): Uint8Array
```

获取指定资源名称对应的默认或指定的屏幕密度媒体文件内容，使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| density | number | 否 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |

## getMediaContent

```TypeScript
getMediaContent(resource: Resource, callback: _AsyncCallback<Uint8Array>): void
```

获取指定resource对象对应的媒体文件内容。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getMediaContent](#getmediacontent)(resId: long, callback: _AsyncCallback&lt;Uint8Array&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| callback | _AsyncCallback & lt;Uint8Array & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContent

```TypeScript
getMediaContent(resource: Resource, density: number, callback: _AsyncCallback<Uint8Array>): void
```

获取指定resource对象对应的指定屏幕密度媒体文件内容。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getMediaContent](#getmediacontent)(resId: long, density: int, callback: _AsyncCallback&lt;Uint8Array&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| density | number | 是 |
| callback | _AsyncCallback & lt;Uint8Array & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContent

```TypeScript
getMediaContent(resource: Resource): Promise<Uint8Array>
```

获取指定resource对象对应的媒体文件内容。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getMediaContent](#getmediacontent)(resId: long)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContent

```TypeScript
getMediaContent(resource: Resource, density: number): Promise<Uint8Array>
```

获取指定resource对象对应的指定屏幕密度媒体文件内容。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getMediaContent](#getmediacontent)(resId: long, density: int)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| density | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContent

```TypeScript
getMediaContent(resId: number, callback: _AsyncCallback<Uint8Array>): void
```

获取指定资源ID对应的媒体文件内容。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| callback | _AsyncCallback & lt;Uint8Array & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContent

```TypeScript
getMediaContent(resId: number, density: number, callback: _AsyncCallback<Uint8Array>): void
```

获取指定资源ID对应的指定屏幕密度媒体文件内容。使用callback异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| density | number | 是 |
| callback | _AsyncCallback & lt;Uint8Array & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContent

```TypeScript
getMediaContent(resId: number): Promise<Uint8Array>
```

获取指定资源ID对应的媒体文件内容。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContent

```TypeScript
getMediaContent(resId: number, density: number): Promise<Uint8Array>
```

获取指定资源ID对应的指定屏幕密度媒体文件内容。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| density | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resource: Resource, callback: _AsyncCallback<string>): void
```

获取指定resource对象对应的图片资源Base64编码。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getMediaContentBase64](#getmediacontentbase64)(resId: long, callback: _AsyncCallback&lt;string&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| callback | _AsyncCallback & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resource: Resource, density: number, callback: _AsyncCallback<string>): void
```

获取指定resource对象对应的指定屏幕密度图片资源Base64编码。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getMediaContentBase64](#getmediacontentbase64)(resId: long, density: int, callback: _AsyncCallback&lt;string&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| density | number | 是 |
| callback | _AsyncCallback & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resource: Resource): Promise<string>
```

获取指定resource对象对应的图片资源Base64编码。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getMediaContentBase64](#getmediacontentbase64)(resId: long)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resource: Resource, density: number): Promise<string>
```

获取指定resource对象对应的指定屏幕密度图片资源Base64编码。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getMediaContentBase64](#getmediacontentbase64)(resId: long, density: int)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| density | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resId: number, callback: _AsyncCallback<string>): void
```

获取指定资源ID对应的图片资源Base64编码。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| callback | _AsyncCallback & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resId: number, density: number, callback: _AsyncCallback<string>): void
```

获取指定资源ID对应的指定屏幕密度图片资源Base64编码。使用callback异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| density | number | 是 |
| callback | _AsyncCallback & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resId: number): Promise<string>
```

获取指定资源ID对应的图片资源Base64编码。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resId: number, density: number): Promise<string>
```

获取指定资源ID对应的指定屏幕密度图片资源Base64编码。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| density | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContentBase64Sync

```TypeScript
getMediaContentBase64Sync(resId: number, density?: number): string
```

获取指定资源ID对应的默认或指定的屏幕密度图片资源Base64编码，使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| density | number | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContentBase64Sync

```TypeScript
getMediaContentBase64Sync(resource: Resource, density?: number): string
```

获取指定resource对象对应的默认或指定的屏幕密度图片资源Base64编码，使用同步方式返回。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getMediaContentBase64Sync](#getmediacontentbase64sync)(resId: long, density?: int)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| density | number | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContentSync

```TypeScript
getMediaContentSync(resId: number, density?: number): Uint8Array
```

获取指定资源ID对应的默认或指定的屏幕密度媒体文件内容，使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| density | number | 否 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getMediaContentSync

```TypeScript
getMediaContentSync(resource: Resource, density?: number): Uint8Array
```

获取指定resource对象对应的默认或指定的屏幕密度媒体文件内容，使用同步方式返回。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getMediaContentSync](#getmediacontentsync)(resId: long, density?: int)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| density | number | 否 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |

## getNumber

```TypeScript
getNumber(resId: number): number
```

获取指定资源ID对应的integer数值或者float数值，使用同步方式返回。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getNumber

```TypeScript
getNumber(resource: Resource): number
```

获取指定resource对象对应的integer数值或者float数值，使用同步方式返回。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getNumber](#getnumber)(resId: number)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getNumberByName

```TypeScript
getNumberByName(resName: string): number
```

获取指定资源名称对应的integer数值或者float数值，使用同步方式返回。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getOverrideConfiguration

```TypeScript
getOverrideConfiguration(): Configuration
```

获取差异化资源的配置，使用同步方式返回。无论是普通资源管理对象，还是通过[getOverrideResourceManager](#getoverrideresourcemanager)接口获 取的差异化资源管理对象，调用该接口都会返回相同的配置信息。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 |
| --- |
| [Configuration](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) |

## getOverrideResourceManager

```TypeScript
getOverrideResourceManager(configuration?: Configuration): ResourceManager
```

获取可以加载差异化资源的资源管理对象，使用同步方式返回。普通的资源管理对象获取的资源的配置（语言、深浅色、分辨率、横竖屏等）是由系统决定的，而通过该接口返回的对象，应用可以获取符合指定配置的资源，即差异化资源，比如在浅色模式时可以获取深色资源。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| configuration | [Configuration](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getPluralString

```TypeScript
getPluralString(resId: number, num: number, callback: AsyncCallback<string>): void
```

获取指定资源ID，指定资源数量的单复数字符串。使用callback异步回调。

> **说明：**&gt;
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getPluralStringValue](#getpluralstringvalue)(resId: number, num: number, callback: _AsyncCallback&lt;string&gt;)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| num | number | 是 |
| callback | AsyncCallback & lt;string & gt; | 是 |

## getPluralString

```TypeScript
getPluralString(resId: number, num: number): Promise<string>
```

获取指定资源ID，指定资源数量的单复数字符串。使用Promise异步回调。

> **说明：**&gt;
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getPluralStringValue](#getpluralstringvalue)(resId: number, num: number)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| num | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getPluralStringByName

```TypeScript
getPluralStringByName(resName: string, num: number, callback: _AsyncCallback<string>): void
```

获取指定资源名称，指定资源数量的单复数字符串。使用callback异步回调。

> **说明：**&gt;
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [getIntPluralStringByNameSync](#getintpluralstringbynamesync)(resName: string, num: number, ...args: Array&lt;string | number&gt;)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| num | number | 是 |
| callback | _AsyncCallback & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getPluralStringByName

```TypeScript
getPluralStringByName(resName: string, num: number): Promise<string>
```

获取指定资源名称，指定资源数量的单复数字符串。使用Promise异步回调。

> **说明：**&gt;
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [getIntPluralStringByNameSync](#getintpluralstringbynamesync)(resName: string, num: number, ...args: Array&lt;string | number&gt;)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| num | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getPluralStringByNameSync

```TypeScript
getPluralStringByNameSync(resName: string, num: number): string
```

获取指定资源名称，指定资源数量的单复数字符串，使用同步方式返回。

> **说明：**&gt;
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 10

**废弃版本：** 18

**替代接口：** [getIntPluralStringByNameSync](#getintpluralstringbynamesync)(resName: string, num: number, ...args: Array&lt;string | number&gt;)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| num | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getPluralStringValue

```TypeScript
getPluralStringValue(resource: Resource, num: number, callback: _AsyncCallback<string>): void
```

获取指定资源信息，指定资源数量的单复数字符串。使用callback异步回调。

> **说明：**&gt;
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| num | number | 是 |
| callback | _AsyncCallback & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getPluralStringValue

```TypeScript
getPluralStringValue(resource: Resource, num: number): Promise<string>
```

获取指定资源信息，指定资源数量的单复数字符串。使用Promise异步回调。

> **说明：**&gt;
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| num | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getPluralStringValue

```TypeScript
getPluralStringValue(resId: number, num: number, callback: _AsyncCallback<string>): void
```

获取指定资源ID，指定资源数量的单复数字符串。使用callback异步回调。

> **说明：**&gt;
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| num | number | 是 |
| callback | _AsyncCallback & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getPluralStringValue

```TypeScript
getPluralStringValue(resId: number, num: number): Promise<string>
```

获取指定资源ID，指定资源数量的单复数字符串。使用Promise异步回调。

> **说明：**&gt;
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| num | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getPluralStringValueSync

```TypeScript
getPluralStringValueSync(resId: number, num: number): string
```

获取指定资源ID，指定资源数量的单复数字符串，使用同步方式返回。

> **说明：**&gt;
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 10

**废弃版本：** 18

**替代接口：** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| num | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getPluralStringValueSync

```TypeScript
getPluralStringValueSync(resource: Resource, num: number): string
```

获取指定资源信息，指定资源数量的单复数字符串，使用同步方式返回。

> **说明：**&gt;
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考
> [语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**起始版本：** 10

**废弃版本：** 18

**替代接口：** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| num | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getRawFd

```TypeScript
getRawFd(path: string, callback: _AsyncCallback<RawFileDescriptor>): void
```

获取resources/rawfile目录下对应rawfile文件所在HAP的文件描述符（fd）。使用callback异步回调。

> **说明：**&gt;
> 文件描述符（fd）使用完毕后需调用[closeRawFdSync](#closerawfdsync)或
> [closeRawFd](#closerawfd)关闭
> fd，避免资源泄露。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | _AsyncCallback & lt;RawFileDescriptor & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## getRawFd

```TypeScript
getRawFd(path: string): Promise<RawFileDescriptor>
```

获取resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd）。使用Promise异步回调。

> **说明：**&gt;
> 文件描述符（fd）使用完毕后需调用[closeRawFdSync](#closerawfdsync)或
> [closeRawFd](#closerawfd)关闭
> fd，避免资源泄露。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;RawFileDescriptor & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## getRawFdSync

```TypeScript
getRawFdSync(path: string): RawFileDescriptor
```

获取resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd），使用同步方式返回。

> **说明：**&gt;
> 文件描述符（fd）使用完毕后需调用[closeRawFdSync](#closerawfdsync)或
> [closeRawFd](#closerawfd)关闭
> fd，避免资源泄露。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RawFileDescriptor](arkts-localization-resourcemanager-rawfiledescriptor-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## getRawFile

```TypeScript
getRawFile(path: string, callback: AsyncCallback<Uint8Array>): void
```

获取resources/rawfile目录下对应的rawfile文件内容。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getRawFileContent](#getrawfilecontent)(path: string, callback: _AsyncCallback&lt;Uint8Array&gt;)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | AsyncCallback & lt;Uint8Array & gt; | 是 |

## getRawFile

```TypeScript
getRawFile(path: string): Promise<Uint8Array>
```

获取resources/rawfile目录下对应的rawfile文件内容。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getRawFileContent](#getrawfilecontent)(path: string)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

## getRawFileContent

```TypeScript
getRawFileContent(path: string, callback: _AsyncCallback<Uint8Array>): void
```

获取resources/rawfile目录下对应的rawfile文件内容。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | _AsyncCallback & lt;Uint8Array & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## getRawFileContent

```TypeScript
getRawFileContent(path: string): Promise<Uint8Array>
```

获取resources/rawfile目录下对应的rawfile文件内容。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## getRawFileContentSync

```TypeScript
getRawFileContentSync(path: string): Uint8Array
```

获取resources/rawfile目录下对应的rawfile文件内容，使用同步形式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## getRawFileDescriptor

```TypeScript
getRawFileDescriptor(path: string, callback: AsyncCallback<RawFileDescriptor>): void
```

获取resources/rawfile目录下对应rawfile文件的文件描述符（fd）。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getRawFd](#getrawfd)(path: string, callback: _AsyncCallback&lt;RawFileDescriptor&gt;)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | AsyncCallback & lt;RawFileDescriptor & gt; | 是 |

## getRawFileDescriptor

```TypeScript
getRawFileDescriptor(path: string): Promise<RawFileDescriptor>
```

获取resources/rawfile目录下对应rawfile文件的文件描述符（fd）。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getRawFd](#getrawfd)(path: string)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;RawFileDescriptor & gt; |

## getRawFileList

```TypeScript
getRawFileList(path: string, callback: _AsyncCallback<Array<string>>): void
```

获取resources/rawfile下指定子目录中的文件夹及文件列表。使用callback异步回调。

> **说明：**&gt;
> 若文件夹中无文件，则抛出异常；若文件夹中有文件，则返回文件夹及文件列表。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | _AsyncCallback & lt;Array & lt;string & gt; & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## getRawFileList

```TypeScript
getRawFileList(path: string): Promise<Array<string>>
```

获取resources/rawfile下指定子目录中的文件夹及文件列表。使用Promise异步回调。

> **说明：**&gt;
> 若文件夹中无文件，则抛出异常；若文件夹中有文件，则返回文件夹及文件列表。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## getRawFileListSync

```TypeScript
getRawFileListSync(path: string): Array<string>
```

获取resources/rawfile下指定子目录中的文件夹及文件列表，使用同步形式返回。

> **说明：**&gt;
> 若文件夹中无文件，则抛出异常；若文件夹中有文件，则返回文件夹及文件列表。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## getResourceName

```TypeScript
getResourceName(resId: number): string
```

获取指定资源ID对应的资源名称。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |

## getString

```TypeScript
getString(resId: number, callback: AsyncCallback<string>): void
```

获取指定资源ID对应的字符串。使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getStringValue](#getstringvalue)(resId: long, callback: _AsyncCallback&lt;string&gt;)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| callback | AsyncCallback & lt;string & gt; | 是 |

## getString

```TypeScript
getString(resId: number): Promise<string>
```

获取指定资源ID对应的字符串。使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getStringValue](#getstringvalue)(resId: long)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getStringArray

```TypeScript
getStringArray(resId: number, callback: AsyncCallback<Array<string>>): void
```

获取指定资源ID对应的字符串数组。使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getStringArrayValue](#getstringarrayvalue)(resId: long, callback: _AsyncCallback&lt;Array&lt;string&gt;&gt;)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| callback | AsyncCallback & lt;Array & lt;string & gt; & gt; | 是 |

## getStringArray

```TypeScript
getStringArray(resId: number): Promise<Array<string>>
```

获取指定资源ID对应的字符串数组。使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getStringArrayValue](#getstringarrayvalue)(resId: long)

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## getStringArrayByName

```TypeScript
getStringArrayByName(resName: string, callback: _AsyncCallback<Array<string>>): void
```

获取指定资源名称对应的字符串数组。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| callback | _AsyncCallback & lt;Array & lt;string & gt; & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringArrayByName

```TypeScript
getStringArrayByName(resName: string): Promise<Array<string>>
```

获取指定资源名称对应的字符串数组。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringArrayByNameSync

```TypeScript
getStringArrayByNameSync(resName: string): Array<string>
```

获取指定资源名称对应的字符串数组，使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringArrayValue

```TypeScript
getStringArrayValue(resource: Resource, callback: _AsyncCallback<Array<string>>): void
```

获取指定resource对象对应的字符串数组。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getStringArrayValue](#getstringarrayvalue)(resId: long, callback: _AsyncCallback&lt;Array&lt;string&gt;&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| callback | _AsyncCallback & lt;Array & lt;string & gt; & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringArrayValue

```TypeScript
getStringArrayValue(resource: Resource): Promise<Array<string>>
```

获取指定resource对象对应的字符串数组。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getStringArrayValue](#getstringarrayvalue)(resId: long)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringArrayValue

```TypeScript
getStringArrayValue(resId: number, callback: _AsyncCallback<Array<string>>): void
```

获取指定资源ID对应的字符串数组。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| callback | _AsyncCallback & lt;Array & lt;string & gt; & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringArrayValue

```TypeScript
getStringArrayValue(resId: number): Promise<Array<string>>
```

获取指定资源ID对应的字符串数组。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringArrayValueSync

```TypeScript
getStringArrayValueSync(resId: number): Array<string>
```

获取指定资源ID对应的字符串数组，使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringArrayValueSync

```TypeScript
getStringArrayValueSync(resource: Resource): Array<string>
```

获取指定resource对象对应的字符串数组，使用同步方式返回。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getStringArrayValueSync](#getstringarrayvaluesync)(resId: long)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringByName

```TypeScript
getStringByName(resName: string, callback: _AsyncCallback<string>): void
```

获取指定资源名称对应的字符串。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| callback | _AsyncCallback & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringByName

```TypeScript
getStringByName(resName: string): Promise<string>
```

获取指定资源名称对应的字符串。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringByNameSync

```TypeScript
getStringByNameSync(resName: string): string
```

获取指定资源名称对应的字符串，使用同步方式返回。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringByNameSync

```TypeScript
getStringByNameSync(resName: string, ...args: Array<string | number>): string
```

获取指定资源名称对应的字符串，并使用args参数依次替换字符串中的格式化占位符，使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |
| [9001008](../errorcode-resource-manager.md#9001008-根据当前名称获取的资源格式化失败) |

## getStringSync

```TypeScript
getStringSync(resId: number): string
```

获取指定资源ID对应的字符串，使用同步方式返回。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringSync

```TypeScript
getStringSync(resId: number, ...args: Array<string | number>): string
```

获取指定资源ID对应的字符串，并使用args参数依次替换字符串中的格式化占位符。使用同步方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |
| [9001007](../errorcode-resource-manager.md#9001007-根据当前id获取的资源格式化失败) |

## getStringSync

```TypeScript
getStringSync(resource: Resource): string
```

获取指定resource对象对应的字符串，使用同步方式返回。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getStringSync](#getstringsync)(resId: long)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringSync

```TypeScript
getStringSync(resource: Resource, ...args: Array<string | number>): string
```

获取指定resource对象对应的字符串，并使用args参数依次替换字符串中的格式化占位符，使用同步方式返回。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getStringSync](#getstringsync)(resId: number, ...args: Array&lt;string | number&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |
| [9001007](../errorcode-resource-manager.md#9001007-根据当前id获取的资源格式化失败) |

## getStringValue

```TypeScript
getStringValue(resource: Resource, callback: _AsyncCallback<string>): void
```

获取指定resource对象对应的字符串。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getStringValue](#getstringvalue)(resId: long, callback: _AsyncCallback&lt;string&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |
| callback | _AsyncCallback & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringValue

```TypeScript
getStringValue(resource: Resource): Promise<string>
```

获取指定resource对象对应的字符串。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getStringValue](#getstringvalue)(resId: long)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringValue

```TypeScript
getStringValue(resId: number, callback: _AsyncCallback<string>): void
```

获取指定资源ID对应的字符串。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |
| callback | _AsyncCallback & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getStringValue

```TypeScript
getStringValue(resId: number): Promise<string>
```

获取指定资源ID对应的字符串。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getSymbol

```TypeScript
getSymbol(resId: number) : number
```

获取指定资源ID对应的[Symbol字符](https://developer.huawei.com/consumer/cn/design/harmonyos-symbol)Unicode码，使用同步方式返回。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resId | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getSymbol

```TypeScript
getSymbol(resource: Resource) : number
```

获取指定resource对象对应的[Symbol字符](https://developer.huawei.com/consumer/cn/design/harmonyos-symbol)Unicode码，使用同步方式返回。

**起始版本：** 11

**废弃版本：** 20

**替代接口：** [getSymbol](#getsymbol)(resId: long)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001001](../errorcode-resource-manager.md#9001001-无效的资源id) |
| [9001002](../errorcode-resource-manager.md#9001002-根据当前资源id未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## getSymbolByName

```TypeScript
getSymbolByName(resName: string) : number
```

获取指定资源名称对应的[Symbol字符](https://developer.huawei.com/consumer/cn/design/harmonyos-symbol)Unicode码，使用同步方式返回。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resName | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001003](../errorcode-resource-manager.md#9001003-无效的资源名称) |
| [9001004](../errorcode-resource-manager.md#9001004-根据当前资源名称未找到匹配的资源) |
| [9001006](../errorcode-resource-manager.md#9001006-资源存在循环引用) |

## isRawDir

```TypeScript
isRawDir(path: string): boolean
```

判断指定路径是否为rawfile下的目录，使用同步方式返回。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001005](../errorcode-resource-manager.md#9001005-无效的相对路径) |

## release

```TypeScript
release()
```

释放创建的resourceManager。此接口暂不支持，调用后无实际作用。

**起始版本：** 7

**废弃版本：** 12

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

## removeResource

```TypeScript
removeResource(path: string) : void
```

应用运行时移除指定的overlay资源，还原被覆盖前的资源。

> **说明：**&gt;
> rawfile和resfile目录不支持资源覆盖。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9001010](../errorcode-resource-manager.md#9001010-无效的overlay路径) |

## updateOverrideConfiguration

```TypeScript
updateOverrideConfiguration(configuration: Configuration): void
```

更新差异化资源管理对象的配置。无论是普通资源管理对象，还是通过[getOverrideResourceManager](#getoverrideresourcemanager)接口获 取的差异化资源管理对象，调用该方法均可更新差异化资源管理对象的配置。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| configuration | [Configuration](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
