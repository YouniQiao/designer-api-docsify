# IStateMgmtFactory

Define IStateMgmtFactory interface.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface IStateMgmtFactory--><!--Device-unnamed-export declare interface IStateMgmtFactory-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## makeComputed

```TypeScript
makeComputed<T>(computedCallback: ComputedCallback<T>, computeName: string): IComputedDecoratedVariable<T>
```

Create a computed variable instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeComputed<T>(computedCallback: ComputedCallback<T>, computeName: string): IComputedDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeComputed<T>(computedCallback: ComputedCallback<T>, computeName: string): IComputedDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| computedCallback | [ComputedCallback](arkts-arkui-computedcallback-t.md)&lt;T&gt; | 是 | computed callback function |
| computeName | string | 是 | name of the computed function |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IComputedDecoratedVariable](arkts-arkui-decorator-icomputeddecoratedvariable-i.md)&lt;T&gt; | Computed instance |

## makeConsume

```TypeScript
makeConsume<T>(owner: IVariableOwner, varName: string,
    provideAlias: string, watchFunc?: WatchFuncType): IConsumeDecoratedVariable<T>
```

创建@Consume状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeConsume<T>(owner: IVariableOwner, varName: string,    provideAlias: string, watchFunc?: WatchFuncType): IConsumeDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeConsume<T>(owner: IVariableOwner, varName: string,    provideAlias: string, watchFunc?: WatchFuncType): IConsumeDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| varName | string | 是 | 状态变量的名字 |
| provideAlias | string | 是 | 变量别名 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 | 监听函数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IConsumeDecoratedVariable](arkts-arkui-decorator-iconsumedecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeConsume

```TypeScript
makeConsume<T>(owner: IVariableOwner, varName: string,
    provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): IConsumeDecoratedVariable<T>
```

创建@Consume状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeConsume<T>(owner: IVariableOwner, varName: string,    provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): IConsumeDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeConsume<T>(owner: IVariableOwner, varName: string,    provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): IConsumeDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| varName | string | 是 | 状态变量的名字 |
| provideAlias | string | 是 | 变量别名 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 | 监听函数 |
| consumeOptions | [ConsumeOptions](arkts-arkui-decorator-consumeoptions-i.md)&lt;T&gt; | 否 | 包含开发者设置的初始值的接口 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IConsumeDecoratedVariable](arkts-arkui-decorator-iconsumedecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeConsumer

```TypeScript
makeConsumer<T>(
    owner: IVariableOwner, varName: string, providerAlias: string, defaultValue: T
  ): IConsumerDecoratedVariable<T>
```

创建@Consumer状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeConsumer<T>(    owner: IVariableOwner, varName: string, providerAlias: string, defaultValue: T  ): IConsumerDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeConsumer<T>(    owner: IVariableOwner, varName: string, providerAlias: string, defaultValue: T  ): IConsumerDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| varName | string | 是 | 状态变量的名字 |
| providerAlias | string | 是 | 变量别名 |
| defaultValue | T | 是 | 状态变量的初始值 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IConsumerDecoratedVariable](arkts-arkui-decorator-iconsumerdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeCustomEnv

```TypeScript
makeCustomEnv<T>(owner: IVariableOwner, envKey: CustomEnvKey<T>, varName: string, localInitValue: T): ICustomEnvDecoratedVariable<T>
```

创建一个CustomEnv变量实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeCustomEnv<T>(owner: IVariableOwner, envKey: CustomEnvKey<T>, varName: string, localInitValue: T): ICustomEnvDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeCustomEnv<T>(owner: IVariableOwner, envKey: CustomEnvKey<T>, varName: string, localInitValue: T): ICustomEnvDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 该变量的自定义组件所有者。 |
| envKey | [CustomEnvKey](../arkts-components/arkts-arkui-customenvkey-c.md)&lt;T&gt; | 是 | 自定义环境变量键。 |
| varName | string | 是 | 被@CustomEnv装饰的变量名。 |
| localInitValue | T | 是 | @CustomEnv本地初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ICustomEnvDecoratedVariable](arkts-arkui-decorator-icustomenvdecoratedvariable-i.md)&lt;T&gt; | CustomEnv变量实例。 |

## makeEnv

```TypeScript
makeEnv<T>(owner: IVariableOwner, envValue: string | SystemEnvKey<T>, varName: string, envOptions?: EnvOptions<T>): IEnvDecoratedVariable<T>
```

创建一个Env变量实例。在API 26.0.0及更高版本上，envValue参数支持SystemEnvKey类型。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeEnv<T>(owner: IVariableOwner, envValue: string | SystemEnvKey<T>, varName: string, envOptions?: EnvOptions<T>): IEnvDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeEnv<T>(owner: IVariableOwner, envValue: string | SystemEnvKey<T>, varName: string, envOptions?: EnvOptions<T>): IEnvDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 自定义组件。 |
| envValue | string \| SystemEnvKey&lt;T&gt; | 是 | 支持的环境变量类型 [APi22 - API24] |
| varName | string | 是 | @Env装饰的变量名。 |
| envOptions | [EnvOptions](arkts-arkui-decorator-envoptions-i.md)&lt;T&gt; | 否 | makeEnv的其他选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IEnvDecoratedVariable](arkts-arkui-decorator-ienvdecoratedvariable-i.md)&lt;T&gt; | Env变量实例。 |

## makeGlobalReusePool

```TypeScript
makeGlobalReusePool(reusePool: ReusePoolOwnership,
    poolAccepts: Class[], owningView: IVariableOwner): IGlobalReusePoolVariable
```

在自定义组件上创建全局重用池。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeGlobalReusePool(reusePool: ReusePoolOwnership,    poolAccepts: Class[], owningView: IVariableOwner): IGlobalReusePoolVariable--><!--Device-IStateMgmtFactory-makeGlobalReusePool(reusePool: ReusePoolOwnership,    poolAccepts: Class[], owningView: IVariableOwner): IGlobalReusePoolVariable-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reusePool | [ReusePoolOwnership](arkts-arkui-customcomponent-reusepoolownership-e.md) | 是 | 复用池类型 |
| poolAccepts | Class[] | 是 | 重用池接受的自定义组件 |
| owningView | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 拥有全局池的自定义组件 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IGlobalReusePoolVariable](arkts-arkui-decorator-iglobalreusepoolvariable-i.md) | 全局重用池句柄。 |

## makeLink

```TypeScript
makeLink<T>(owner: IVariableOwner, varName: string, source: LinkSourceType<T>,
    watchFunc?: WatchFuncType): ILinkDecoratedVariable<T>
```

创建@Link状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeLink<T>(owner: IVariableOwner, varName: string, source: LinkSourceType<T>,    watchFunc?: WatchFuncType): ILinkDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeLink<T>(owner: IVariableOwner, varName: string, source: LinkSourceType<T>,    watchFunc?: WatchFuncType): ILinkDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| varName | string | 是 | 状态变量的名字 |
| source | [LinkSourceType](arkts-arkui-linksourcetype-t.md)&lt;T&gt; | 是 | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 | 监听函数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ILinkDecoratedVariable](arkts-arkui-decorator-ilinkdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeLocal

```TypeScript
makeLocal<T>(owner: IVariableOwner, varName: string, localInitValue: T): ILocalDecoratedVariable<T>
```

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeLocal<T>(owner: IVariableOwner, varName: string, localInitValue: T): ILocalDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeLocal<T>(owner: IVariableOwner, varName: string, localInitValue: T): ILocalDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | owner of this variable. |
| varName | string | 是 | state variable name. |
| localInitValue | T | 是 | state variable initValue. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ILocalDecoratedVariable](arkts-arkui-decorator-ilocaldecoratedvariable-i.md)&lt;T&gt; | Local instance |

## makeLocalStorageLink

```TypeScript
makeLocalStorageLink<T>(owner: IVariableOwner, propName: string,
        varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStorageLinkDecoratedVariable<T>
```

创建@LocalStorageLink状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeLocalStorageLink<T>(owner: IVariableOwner, propName: string,        varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStorageLinkDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeLocalStorageLink<T>(owner: IVariableOwner, propName: string,        varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStorageLinkDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| propName | string | 是 | 属性名字 |
| varName | string | 是 | 状态变量的名字 |
| initValue | T | 是 | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 | 监听函数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ILocalStorageLinkDecoratedVariable](arkts-arkui-decorator-ilocalstoragelinkdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeLocalStoragePropRef

```TypeScript
makeLocalStoragePropRef<T>(owner: IVariableOwner, propName: string, varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStoragePropRefDecoratedVariable<T>
```

Create a LocalStoragePropRef variable instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeLocalStoragePropRef<T>(owner: IVariableOwner, propName: string, varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStoragePropRefDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeLocalStoragePropRef<T>(owner: IVariableOwner, propName: string, varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStoragePropRefDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | owner of this variable. |
| propName | string | 是 | property name. |
| varName | string | 是 | state variable name. |
| initValue | T | 是 | init value. |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 | watch type |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ILocalStoragePropRefDecoratedVariable](arkts-arkui-decorator-ilocalstorageproprefdecoratedvariable-i.md)&lt;T&gt; | LocalStoragePropRef instance |

## makeMonitor

```TypeScript
makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, owner?: IVariableOwner): IMonitorDecoratedVariable
```

Create a monitored variable instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, owner?: IVariableOwner): IMonitorDecoratedVariable--><!--Device-IStateMgmtFactory-makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, owner?: IVariableOwner): IMonitorDecoratedVariable-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pathInfos | Array&lt;IMonitorPathInfo&gt; | 是 | monitor path to its accessor |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | 是 | callback when then monitor triggers |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 否 | owner of this monitor |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | Monitor variable instance |

## makeMonitor

```TypeScript
makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, options?: MakeMonitorOptions): IMonitorDecoratedVariable
```

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, options?: MakeMonitorOptions): IMonitorDecoratedVariable--><!--Device-IStateMgmtFactory-makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, options?: MakeMonitorOptions): IMonitorDecoratedVariable-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pathInfos | Array&lt;IMonitorPathInfo&gt; | 是 | monitor path to its accessor |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | 是 | callback when the monitor triggers |
| options | [MakeMonitorOptions](arkts-arkui-decorator-makemonitoroptions-i.md) | 否 | options of this monitor |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | Monitor variable instance |

## makeMutableStateMeta

```TypeScript
makeMutableStateMeta(): IMutableStateMeta
```

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeMutableStateMeta(): IMutableStateMeta--><!--Device-IStateMgmtFactory-makeMutableStateMeta(): IMutableStateMeta-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IMutableStateMeta](arkts-arkui-decorator-imutablestatemeta-i.md) |  |

## makeMutableStateMeta

```TypeScript
makeMutableStateMeta(observedObject: IObservedObject | undefined, propertyName: string): IMutableStateMeta
```

获取可变状态元

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeMutableStateMeta(observedObject: IObservedObject | undefined, propertyName: string): IMutableStateMeta--><!--Device-IStateMgmtFactory-makeMutableStateMeta(observedObject: IObservedObject | undefined, propertyName: string): IMutableStateMeta-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| observedObject | [IObservedObject](arkts-arkui-decorator-iobservedobject-i.md) \| undefined | 是 | 此元的所有者。 |
| propertyName | string | 是 | 元名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IMutableStateMeta](arkts-arkui-decorator-imutablestatemeta-i.md) |  |

## makeObjectLink

```TypeScript
makeObjectLink<T>(owner: IVariableOwner, varName: string,
    initValue: T, watchFunc?: WatchFuncType): IObjectLinkDecoratedVariable<T>
```

创建@ObjectLink状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeObjectLink<T>(owner: IVariableOwner, varName: string,    initValue: T, watchFunc?: WatchFuncType): IObjectLinkDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeObjectLink<T>(owner: IVariableOwner, varName: string,    initValue: T, watchFunc?: WatchFuncType): IObjectLinkDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| varName | string | 是 | 状态变量的名字 |
| initValue | T | 是 | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 | 监听函数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IObjectLinkDecoratedVariable](arkts-arkui-decorator-iobjectlinkdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeParam

```TypeScript
makeParam<T>(owner: IVariableOwner, varName: string, initValue: T): IParamDecoratedVariable<T>
```

创建@Param状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeParam<T>(owner: IVariableOwner, varName: string, initValue: T): IParamDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeParam<T>(owner: IVariableOwner, varName: string, initValue: T): IParamDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| varName | string | 是 | 状态变量的名字 |
| initValue | T | 是 | 状态变量的初始值 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IParamDecoratedVariable](arkts-arkui-decorator-iparamdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeParamOnce

```TypeScript
makeParamOnce<T>(owner: IVariableOwner, varName: string, initValue: T): IParamOnceDecoratedVariable<T>
```

创建@Once @Param状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeParamOnce<T>(owner: IVariableOwner, varName: string, initValue: T): IParamOnceDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeParamOnce<T>(owner: IVariableOwner, varName: string, initValue: T): IParamOnceDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| varName | string | 是 | 状态变量的名字 |
| initValue | T | 是 | 状态变量的初始值 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IParamOnceDecoratedVariable](arkts-arkui-decorator-iparamoncedecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makePropRef

```TypeScript
makePropRef<T>(owner: IVariableOwner, varName: string, initValue: T,
    watchFunc?: WatchFuncType): IPropRefDecoratedVariable<T>
```

创建@PropRef状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makePropRef<T>(owner: IVariableOwner, varName: string, initValue: T,    watchFunc?: WatchFuncType): IPropRefDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makePropRef<T>(owner: IVariableOwner, varName: string, initValue: T,    watchFunc?: WatchFuncType): IPropRefDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| varName | string | 是 | 状态变量的名字 |
| initValue | T | 是 | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 | 监听函数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IPropRefDecoratedVariable](arkts-arkui-decorator-iproprefdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeProvide

```TypeScript
makeProvide<T>(owner: IVariableOwner, varName: string, provideAlias: string, initValue: T, 
      allowOverride: boolean, watchFunc?: WatchFuncType): IProvideDecoratedVariable<T>
```

创建@Provide状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeProvide<T>(owner: IVariableOwner, varName: string, provideAlias: string, initValue: T,       allowOverride: boolean, watchFunc?: WatchFuncType): IProvideDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeProvide<T>(owner: IVariableOwner, varName: string, provideAlias: string, initValue: T,       allowOverride: boolean, watchFunc?: WatchFuncType): IProvideDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| varName | string | 是 | 状态变量的名字 |
| provideAlias | string | 是 | 变量别名 |
| initValue | T | 是 | 状态变量的初始值 |
| allowOverride | boolean | 是 | 是否覆盖父组件上的同名@Provide状态变量 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 | 监听函数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IProvideDecoratedVariable](arkts-arkui-decorator-iprovidedecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeProvider

```TypeScript
makeProvider<T>(owner: IVariableOwner, varName: string, providerAlias: string, 
                  localInitValue: T): IProviderDecoratedVariable<T>
```

创建@Provider 状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeProvider<T>(owner: IVariableOwner, varName: string, providerAlias: string,                   localInitValue: T): IProviderDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeProvider<T>(owner: IVariableOwner, varName: string, providerAlias: string,                   localInitValue: T): IProviderDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| varName | string | 是 | 状态变量的名字 |
| providerAlias | string | 是 | 变量别名 |
| localInitValue | T | 是 | 状态变量的初始值 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IProviderDecoratedVariable](arkts-arkui-decorator-iproviderdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeState

```TypeScript
makeState<T>(owner: IVariableOwner, varName: string, initValue: T,
    watchFunc?: WatchFuncType): IStateDecoratedVariable<T>
```

创建@State状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeState<T>(owner: IVariableOwner, varName: string, initValue: T,    watchFunc?: WatchFuncType): IStateDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeState<T>(owner: IVariableOwner, varName: string, initValue: T,    watchFunc?: WatchFuncType): IStateDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| varName | string | 是 | 状态变量的名字 |
| initValue | T | 是 | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 | 监听函数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IStateDecoratedVariable](arkts-arkui-decorator-istatedecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeStaticLocal

```TypeScript
makeStaticLocal<T>(varName: string, localInitValue: T): ILocalDecoratedVariable<T>
```

Create a static local variable instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeStaticLocal<T>(varName: string, localInitValue: T): ILocalDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeStaticLocal<T>(varName: string, localInitValue: T): ILocalDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| varName | string | 是 | state variable name. |
| localInitValue | T | 是 | state variable initValue. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ILocalDecoratedVariable](arkts-arkui-decorator-ilocaldecoratedvariable-i.md)&lt;T&gt; | Local instance |

## makeStorageLink

```TypeScript
makeStorageLink<T>(owner: IVariableOwner, propName: string,
    varName: string, initValue: T, watchFunc?: WatchFuncType): IStorageLinkDecoratedVariable<T>
```

创建@StorageLink状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeStorageLink<T>(owner: IVariableOwner, propName: string,    varName: string, initValue: T, watchFunc?: WatchFuncType): IStorageLinkDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeStorageLink<T>(owner: IVariableOwner, propName: string,    varName: string, initValue: T, watchFunc?: WatchFuncType): IStorageLinkDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| propName | string | 是 | 属性名字 |
| varName | string | 是 | 状态变量的名字 |
| initValue | T | 是 | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 | 监听函数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IStorageLinkDecoratedVariable](arkts-arkui-decorator-istoragelinkdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeStoragePropRef

```TypeScript
makeStoragePropRef<T>(owner: IVariableOwner, propName: string,
    varName: string, initValue: T, watchFunc?: WatchFuncType): IStoragePropRefDecoratedVariable<T>
```

创建@Storage PropRef状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeStoragePropRef<T>(owner: IVariableOwner, propName: string,    varName: string, initValue: T, watchFunc?: WatchFuncType): IStoragePropRefDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeStoragePropRef<T>(owner: IVariableOwner, propName: string,    varName: string, initValue: T, watchFunc?: WatchFuncType): IStoragePropRefDecoratedVariable<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 | 状态变量的所有者 |
| propName | string | 是 | 属性名字 |
| varName | string | 是 | 状态变量的名字 |
| initValue | T | 是 | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 | 监听函数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IStoragePropRefDecoratedVariable](arkts-arkui-decorator-istorageproprefdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeSubscribedWatches

```TypeScript
makeSubscribedWatches(): ISubscribedWatches
```

get subscribed watches

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeSubscribedWatches(): ISubscribedWatches--><!--Device-IStateMgmtFactory-makeSubscribedWatches(): ISubscribedWatches-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ISubscribedWatches](arkts-arkui-decorator-isubscribedwatches-i.md) |  |

## makeSyncMonitor

```TypeScript
makeSyncMonitor(pathInfos: IMonitorPathInfo[], monitorCallback: MonitorCallback,
    options?: MakeMonitorOptions): IMonitorDecoratedVariable
```

创建同步监控变量实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IStateMgmtFactory-makeSyncMonitor(pathInfos: IMonitorPathInfo[], monitorCallback: MonitorCallback,    options?: MakeMonitorOptions): IMonitorDecoratedVariable--><!--Device-IStateMgmtFactory-makeSyncMonitor(pathInfos: IMonitorPathInfo[], monitorCallback: MonitorCallback,    options?: MakeMonitorOptions): IMonitorDecoratedVariable-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pathInfos | [IMonitorPathInfo](arkts-arkui-decorator-imonitorpathinfo-i.md)[] | 是 | 到其访问器的监视器路径。 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | 是 | 监视器触发时的回调。 |
| options | [MakeMonitorOptions](arkts-arkui-decorator-makemonitoroptions-i.md) | 否 | 此监视器的选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | 监控变量实例 |

