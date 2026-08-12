# NavPushPathHelper

当跳转的目标[NavDestination](./@internal/component/ets/nav_destination)在不同的hsp分包且未被主包依赖时，首次运行原子化服务只会下载安装主包。此时需要使用NavPushPathHelper先下载安装相应hsp分包，再将指定的[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈或替换当前栈顶页面，从而使[Navigation](./@internal/component/ets/navigation)支持动态加载hsp分包后再跳转。

> **说明：**
> 
> 该组件从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**起始版本：** 12

<!--Device-unnamed-export declare class NavPushPathHelper--><!--Device-unnamed-export declare class NavPushPathHelper-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(navPathStack: NavPathStack)
```

NavPushPathHelper的构造函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPushPathHelper-constructor(navPathStack: NavPathStack)--><!--Device-NavPushPathHelper-constructor(navPathStack: NavPathStack)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| navPathStack | [NavPathStack](../arkts-components/arkts-arkui-navpathstack-c.md) | 是 |

## pushDestination

```TypeScript
pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将info指定的[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈，使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPushPathHelper-pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [100005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#300001-navigation跳转前静默安装hsp分包失败) |
| [100006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## pushDestination

```TypeScript
pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将info指定的[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈，使用Promise异步回调。

具体根据options中指定不同的[LaunchMode](LaunchMode)，有不同的行为。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPushPathHelper-pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPushPathHelper-pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | 是 |
| options | [NavigationOptions](../arkts-components/arkts-arkui-navigationoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [100005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#300001-navigation跳转前静默安装hsp分包失败) |
| [100006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## pushDestinationByName

```TypeScript
pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将name指定的[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈，传递的数据为param，使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPushPathHelper-pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| name | string | 是 |
| param | Object | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [100005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#300001-navigation跳转前静默安装hsp分包失败) |
| [100006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## pushDestinationByName

```TypeScript
pushDestinationByName(moduleName: string, name: string, param: Object,
    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将name指定的[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈，传递的数据为param，添加用于页面出栈时处理返回结果的onPop回调，使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPushPathHelper-pushDestinationByName(moduleName: string, name: string, param: Object,    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushDestinationByName(moduleName: string, name: string, param: Object,    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| name | string | 是 |
| param | Object | 是 |
| onPop | Callback&lt;[PopInfo](../arkts-components/arkts-arkui-popinfo-i.md)&gt; | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [100005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#300001-navigation跳转前静默安装hsp分包失败) |
| [100006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## pushPath

```TypeScript
pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将info指定的[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈，使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPushPathHelper-pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#300001-navigation跳转前静默安装hsp分包失败) |

## pushPath

```TypeScript
pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将info指定的[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈，使用Promise异步回调。

具体根据options中指定的[LaunchMode](LaunchMode)不同，执行不同的跳转行为。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPushPathHelper-pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPushPathHelper-pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | 是 |
| options | [NavigationOptions](../arkts-components/arkts-arkui-navigationoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#300001-navigation跳转前静默安装hsp分包失败) |

## pushPathByName

```TypeScript
pushPathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将name指定的[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈，传递的数据为param，使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPushPathHelper-pushPathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushPathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| name | string | 是 |
| param | Object | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#300001-navigation跳转前静默安装hsp分包失败) |

## pushPathByName

```TypeScript
pushPathByName(moduleName: string, name: string, param: Object,
    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将name指定的[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理，使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPushPathHelper-pushPathByName(moduleName: string, name: string, param: Object,    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushPathByName(moduleName: string, name: string, param: Object,    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| name | string | 是 |
| param | Object | 是 |
| onPop | Callback&lt;[PopInfo](../arkts-components/arkts-arkui-popinfo-i.md)&gt; | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#300001-navigation跳转前静默安装hsp分包失败) |

## replacePath

```TypeScript
replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将当前页面栈栈顶退出，将info指定的  
[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈，使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPushPathHelper-replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#300001-navigation跳转前静默安装hsp分包失败) |

## replacePath

```TypeScript
replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将当前页面栈栈顶退出，将info指定的  
[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈，使用Promise异步回调。

具体根据options中指定不同的[LaunchMode](LaunchMode)，有不同的行为。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPushPathHelper-replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPushPathHelper-replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | 是 |
| options | [NavigationOptions](../arkts-components/arkts-arkui-navigationoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#300001-navigation跳转前静默安装hsp分包失败) |

## replacePathByName

```TypeScript
replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将当前页面栈栈顶退出，将name指定的  
[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈，传递的数据为param，使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPushPathHelper-replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| name | string | 是 |
| param | Object | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#300001-navigation跳转前静默安装hsp分包失败) |
