# NavPushPathHelper

当跳转的目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)在不同的hsp分包且未被主包依赖时，首次运行原子化服务只会下载安装主包。此时需要使用NavPushPathHelper先下载安装相应hsp分包，再将指定的[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈或替换当前栈顶页面，从而使[Navigation](../../apis-arkui/arkts-components/arkts-arkui-navigation-i)支持动态加载hsp分包后再跳转。

> **说明：**
> 
> 该组件从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export declare class NavPushPathHelper--><!--Device-unnamed-export declare class NavPushPathHelper-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { NavPushPathHelper } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(navPathStack: NavPathStack)
```

NavPushPathHelper的构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-constructor(navPathStack: NavPathStack)--><!--Device-NavPushPathHelper-constructor(navPathStack: NavPathStack)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| navPathStack | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | Yes | [Navigation](../../apis-arkui/arkts-components/arkts-arkui-navigation-i)路由栈。 |

## pushDestination

```TypeScript
pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将info指定的[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈，使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)所在分包的moduleName。 |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面的信息。 |
| animated | boolean | No | 是否支持转场动画。 &lt;br&gt;默认值：true。 &lt;br&gt;true：支持转场动画。 &lt;br&gt;false：不支持转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100005 | Builder function not registered. |
| 300001 | hsp silent install fail. |
| 100006 | NavDestination not found. |

## pushDestination

```TypeScript
pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将info指定的[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈，使用Promise异步回调。

具体根据options中指定不同的[LaunchMode](arkts-arkui-navigation-launchmode-e.md)，有不同的行为。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPushPathHelper-pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)所在分包的moduleName。 |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面的信息。 |
| options | [NavigationOptions](arkts-arkui-navigation-navigationoptions-i.md) | No | 页面栈操作选项。默认值为{ launchMode: LaunchMode.STANDARD, animated: true }。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100005 | Builder function not registered. |
| 300001 | hsp silent install fail. |
| 100006 | NavDestination not found. |

## pushDestinationByName

```TypeScript
pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将name指定的[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈，传递的数据为param，使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)所在分包的moduleName。 |
| name | string | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面名称。 |
| param | Object | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面详细参数。 |
| animated | boolean | No | 是否支持转场动画。 &lt;br&gt;默认值：true。 &lt;br&gt;true：支持转场动画。 &lt;br&gt;false：不支持转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100005 | Builder function not registered. |
| 300001 | hsp silent install fail. |
| 100006 | NavDestination not found. |

## pushDestinationByName

```TypeScript
pushDestinationByName(moduleName: string, name: string, param: Object,
    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将name指定的[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈，传递的数据为param，添加用于页面出栈时处理返回结果的onPop回调，使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushDestinationByName(moduleName: string, name: string, param: Object,    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushDestinationByName(moduleName: string, name: string, param: Object,    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)所在分包的moduleName。 |
| name | string | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面名称。 |
| param | Object | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面的参数对象，用于向目标页面传递数据。 |
| onPop | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;PopInfo&gt; | Yes | Callback回调，用于页面出栈时处理返回结果。 |
| animated | boolean | No | 是否支持转场动画。 &lt;br&gt;默认值：true。 &lt;br&gt;true：支持转场动画。 &lt;br&gt;false：不支持转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100005 | Builder function not registered. |
| 300001 | hsp silent install fail. |
| 100006 | NavDestination not found. |

## pushPath

```TypeScript
pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将info指定的[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈，使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)所在分包的moduleName。 |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面的信息。 |
| animated | boolean | No | 是否支持转场动画。 &lt;br&gt;默认值：true。 &lt;br&gt;true：支持转场动画。 &lt;br&gt;false：不支持转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 300001 | hsp silent install fail. |

## pushPath

```TypeScript
pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将info指定的[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈，使用Promise异步回调。

具体根据options中指定的[LaunchMode](arkts-arkui-navigation-launchmode-e.md)不同，执行不同的跳转行为。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPushPathHelper-pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)所在分包的moduleName。 |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面的信息。 |
| options | [NavigationOptions](arkts-arkui-navigation-navigationoptions-i.md) | No | 页面栈操作选项。默认值为{ launchMode: LaunchMode.STANDARD, animated: true }。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 300001 | hsp silent install fail. |

## pushPathByName

```TypeScript
pushPathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将name指定的[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈，传递的数据为param，使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushPathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushPathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)所在分包的moduleName。 |
| name | string | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面名称。 |
| param | Object | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面详细参数。 |
| animated | boolean | No | 是否支持转场动画。 &lt;br&gt;默认值：true。 &lt;br&gt;true：支持转场动画。 &lt;br&gt;false：不支持转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 300001 | hsp silent install fail. |

## pushPathByName

```TypeScript
pushPathByName(moduleName: string, name: string, param: Object,
    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将name指定的[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理，使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushPathByName(moduleName: string, name: string, param: Object,    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushPathByName(moduleName: string, name: string, param: Object,    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)所在分包的moduleName。 |
| name | string | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面名称。 |
| param | Object | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面详细参数。 |
| onPop | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;PopInfo&gt; | Yes | Callback回调，用于页面出栈时处理返回结果。 |
| animated | boolean | No | 是否支持转场动画。 &lt;br&gt;默认值：true。 &lt;br&gt;true：支持转场动画。 &lt;br&gt;false：不支持转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 300001 | hsp silent install fail. |

## replacePath

```TypeScript
replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将当前页面栈栈顶退出，将info指定的  
[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈，使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)所在分包的moduleName。 |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | 新栈顶页面参数信息。 |
| animated | boolean | No | 是否支持转场动画。 &lt;br&gt;默认值：true。 &lt;br&gt;true：支持转场动画。 &lt;br&gt;false：不支持转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 300001 | hsp silent install fail. |

## replacePath

```TypeScript
replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将当前页面栈栈顶退出，将info指定的  
[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈，使用Promise异步回调。

具体根据options中指定不同的[LaunchMode](arkts-arkui-navigation-launchmode-e.md)，有不同的行为。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPushPathHelper-replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)所在分包的moduleName。 |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | 新栈顶页面参数信息。 |
| options | [NavigationOptions](arkts-arkui-navigation-navigationoptions-i.md) | No | 页面栈操作选项。默认值为{ launchMode: LaunchMode.STANDARD, animated: true }。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 300001 | hsp silent install fail. |

## replacePathByName

```TypeScript
replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>
```

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将当前页面栈栈顶退出，将name指定的  
[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈，传递的数据为param，使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)所在分包的moduleName。 |
| name | string | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面名称。 |
| param | Object | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面详细参数。 |
| animated | boolean | No | 是否支持转场动画。 &lt;br&gt;默认值：true。 &lt;br&gt;true：支持转场动画。 &lt;br&gt;false：不支持转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 300001 | hsp silent install fail. |

