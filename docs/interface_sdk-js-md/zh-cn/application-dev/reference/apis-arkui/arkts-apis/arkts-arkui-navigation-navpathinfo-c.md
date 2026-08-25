# NavPathInfo

路由页面信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(name: string, param: Object | null | undefined, onPop?: Callback<PopInfo>, isEntry?: boolean)
```

创建NavPathInfo对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [name](#name) | string | 是 |
| [param](#param) | Object \| null \| undefined | 是 |
| [onPop](#onpop) | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PopInfo](arkts-arkui-navigation-popinfo-i.md)&gt; | 否 |
| [isEntry](#isentry) | boolean | 否 |

## isEntry

```TypeScript
set isEntry(isEntry: boolean | undefined)
```

Set whether it is an entry destination, the default value is false, undefined means set to default value.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
set name(name: string)
```

Set the name of NavDestination.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## navDestinationId

```TypeScript
get navDestinationId(): string | undefined
```

获取NavDestination页面唯一标识符。

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onPop

```TypeScript
set onPop(onPop: Callback<PopInfo> | undefined)
```

Set the callback when next page returns, the default value is nullptr, undefined means set to default value.

**类型：** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PopInfo](arkts-arkui-navigation-popinfo-i.md)&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## param

```TypeScript
set param(param: Object | null | undefined)
```

Set the detailed parameter of the NavDestination, default value is undefined, null is also a meaningful input parameter.

**类型：** Object

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
