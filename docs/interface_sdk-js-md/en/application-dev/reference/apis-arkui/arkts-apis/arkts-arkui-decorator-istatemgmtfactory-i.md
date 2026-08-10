# IStateMgmtFactory

Define IStateMgmtFactory interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IStateMgmtFactory--><!--Device-unnamed-export declare interface IStateMgmtFactory-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## makeComputed

```TypeScript
makeComputed<T>(computedCallback: ComputedCallback<T>, computeName: string): IComputedDecoratedVariable<T>
```

Create a computed variable instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeComputed<T>(computedCallback: ComputedCallback<T>, computeName: string): IComputedDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeComputed<T>(computedCallback: ComputedCallback<T>, computeName: string): IComputedDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| computedCallback | [ComputedCallback](arkts-arkui-computedcallback-t.md)&lt;T&gt; | Yes | computed callback function |
| computeName | string | Yes | name of the computed function |

**Return value:**

| Type | Description |
| --- | --- |
| [IComputedDecoratedVariable](arkts-arkui-decorator-icomputeddecoratedvariable-i.md)&lt;T&gt; | Computed instance |

## makeConsume

```TypeScript
makeConsume<T>(owner: IVariableOwner, varName: string,
    provideAlias: string, watchFunc?: WatchFuncType): IConsumeDecoratedVariable<T>
```

创建@Consume状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeConsume<T>(owner: IVariableOwner, varName: string,    provideAlias: string, watchFunc?: WatchFuncType): IConsumeDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeConsume<T>(owner: IVariableOwner, varName: string,    provideAlias: string, watchFunc?: WatchFuncType): IConsumeDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| varName | string | Yes | 状态变量的名字 |
| provideAlias | string | Yes | 变量别名 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | No | 监听函数 |

**Return value:**

| Type | Description |
| --- | --- |
| [IConsumeDecoratedVariable](arkts-arkui-decorator-iconsumedecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeConsume

```TypeScript
makeConsume<T>(owner: IVariableOwner, varName: string,
    provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): IConsumeDecoratedVariable<T>
```

创建@Consume状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeConsume<T>(owner: IVariableOwner, varName: string,    provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): IConsumeDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeConsume<T>(owner: IVariableOwner, varName: string,    provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): IConsumeDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| varName | string | Yes | 状态变量的名字 |
| provideAlias | string | Yes | 变量别名 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | No | 监听函数 |
| consumeOptions | [ConsumeOptions](arkts-arkui-decorator-consumeoptions-i.md)&lt;T&gt; | No | 包含开发者设置的初始值的接口 |

**Return value:**

| Type | Description |
| --- | --- |
| [IConsumeDecoratedVariable](arkts-arkui-decorator-iconsumedecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeConsumer

```TypeScript
makeConsumer<T>(
    owner: IVariableOwner, varName: string, providerAlias: string, defaultValue: T
  ): IConsumerDecoratedVariable<T>
```

创建@Consumer状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeConsumer<T>(    owner: IVariableOwner, varName: string, providerAlias: string, defaultValue: T  ): IConsumerDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeConsumer<T>(    owner: IVariableOwner, varName: string, providerAlias: string, defaultValue: T  ): IConsumerDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| varName | string | Yes | 状态变量的名字 |
| providerAlias | string | Yes | 变量别名 |
| defaultValue | T | Yes | 状态变量的初始值 |

**Return value:**

| Type | Description |
| --- | --- |
| [IConsumerDecoratedVariable](arkts-arkui-decorator-iconsumerdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeCustomEnv

```TypeScript
makeCustomEnv<T>(owner: IVariableOwner, envKey: CustomEnvKey<T>, varName: string, localInitValue: T): ICustomEnvDecoratedVariable<T>
```

创建一个CustomEnv变量实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeCustomEnv<T>(owner: IVariableOwner, envKey: CustomEnvKey<T>, varName: string, localInitValue: T): ICustomEnvDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeCustomEnv<T>(owner: IVariableOwner, envKey: CustomEnvKey<T>, varName: string, localInitValue: T): ICustomEnvDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 该变量的自定义组件所有者。 |
| envKey | [CustomEnvKey](../arkts-components/arkts-arkui-customenvkey-c.md)&lt;T&gt; | Yes | 自定义环境变量键。 |
| varName | string | Yes | 被@CustomEnv装饰的变量名。 |
| localInitValue | T | Yes | @CustomEnv本地初始值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ICustomEnvDecoratedVariable](arkts-arkui-decorator-icustomenvdecoratedvariable-i.md)&lt;T&gt; | CustomEnv变量实例。 |

## makeEnv

```TypeScript
makeEnv<T>(owner: IVariableOwner, envValue: string | SystemEnvKey<T>, varName: string, envOptions?: EnvOptions<T>): IEnvDecoratedVariable<T>
```

创建一个Env变量实例。在API 26.0.0及更高版本上，envValue参数支持SystemEnvKey类型。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeEnv<T>(owner: IVariableOwner, envValue: string | SystemEnvKey<T>, varName: string, envOptions?: EnvOptions<T>): IEnvDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeEnv<T>(owner: IVariableOwner, envValue: string | SystemEnvKey<T>, varName: string, envOptions?: EnvOptions<T>): IEnvDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 自定义组件。 |
| envValue | string \| SystemEnvKey&lt;T&gt; | Yes | 支持的环境变量类型 [APi22 - API24] |
| varName | string | Yes | @Env装饰的变量名。 |
| envOptions | [EnvOptions](arkts-arkui-decorator-envoptions-i.md)&lt;T&gt; | No | makeEnv的其他选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| [IEnvDecoratedVariable](arkts-arkui-decorator-ienvdecoratedvariable-i.md)&lt;T&gt; | Env变量实例。 |

## makeGlobalReusePool

```TypeScript
makeGlobalReusePool(reusePool: ReusePoolOwnership,
    poolAccepts: Class[], owningView: IVariableOwner): IGlobalReusePoolVariable
```

在自定义组件上创建全局重用池。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeGlobalReusePool(reusePool: ReusePoolOwnership,    poolAccepts: Class[], owningView: IVariableOwner): IGlobalReusePoolVariable--><!--Device-IStateMgmtFactory-makeGlobalReusePool(reusePool: ReusePoolOwnership,    poolAccepts: Class[], owningView: IVariableOwner): IGlobalReusePoolVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reusePool | [ReusePoolOwnership](arkts-arkui-customcomponent-reusepoolownership-e.md) | Yes | 复用池类型 |
| poolAccepts | [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md)[] | Yes | 重用池接受的自定义组件 |
| owningView | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 拥有全局池的自定义组件 |

**Return value:**

| Type | Description |
| --- | --- |
| [IGlobalReusePoolVariable](arkts-arkui-decorator-iglobalreusepoolvariable-i.md) | 全局重用池句柄。 |

## makeLink

```TypeScript
makeLink<T>(owner: IVariableOwner, varName: string, source: LinkSourceType<T>,
    watchFunc?: WatchFuncType): ILinkDecoratedVariable<T>
```

创建@Link状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeLink<T>(owner: IVariableOwner, varName: string, source: LinkSourceType<T>,    watchFunc?: WatchFuncType): ILinkDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeLink<T>(owner: IVariableOwner, varName: string, source: LinkSourceType<T>,    watchFunc?: WatchFuncType): ILinkDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| varName | string | Yes | 状态变量的名字 |
| source | [LinkSourceType](arkts-arkui-linksourcetype-t.md)&lt;T&gt; | Yes | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | No | 监听函数 |

**Return value:**

| Type | Description |
| --- | --- |
| [ILinkDecoratedVariable](arkts-arkui-decorator-ilinkdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeLocal

```TypeScript
makeLocal<T>(owner: IVariableOwner, varName: string, localInitValue: T): ILocalDecoratedVariable<T>
```

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeLocal<T>(owner: IVariableOwner, varName: string, localInitValue: T): ILocalDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeLocal<T>(owner: IVariableOwner, varName: string, localInitValue: T): ILocalDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| varName | string | Yes | state variable name. |
| localInitValue | T | Yes | state variable initValue. |

**Return value:**

| Type | Description |
| --- | --- |
| [ILocalDecoratedVariable](arkts-arkui-decorator-ilocaldecoratedvariable-i.md)&lt;T&gt; | Local instance |

## makeLocalStorageLink

```TypeScript
makeLocalStorageLink<T>(owner: IVariableOwner, propName: string,
        varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStorageLinkDecoratedVariable<T>
```

创建@LocalStorageLink状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeLocalStorageLink<T>(owner: IVariableOwner, propName: string,        varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStorageLinkDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeLocalStorageLink<T>(owner: IVariableOwner, propName: string,        varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStorageLinkDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| propName | string | Yes | 属性名字 |
| varName | string | Yes | 状态变量的名字 |
| initValue | T | Yes | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | No | 监听函数 |

**Return value:**

| Type | Description |
| --- | --- |
| [ILocalStorageLinkDecoratedVariable](arkts-arkui-decorator-ilocalstoragelinkdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeLocalStoragePropRef

```TypeScript
makeLocalStoragePropRef<T>(owner: IVariableOwner, propName: string, varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStoragePropRefDecoratedVariable<T>
```

Create a LocalStoragePropRef variable instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeLocalStoragePropRef<T>(owner: IVariableOwner, propName: string, varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStoragePropRefDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeLocalStoragePropRef<T>(owner: IVariableOwner, propName: string, varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStoragePropRefDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| propName | string | Yes | property name. |
| varName | string | Yes | state variable name. |
| initValue | T | Yes | init value. |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | No | watch type |

**Return value:**

| Type | Description |
| --- | --- |
| [ILocalStoragePropRefDecoratedVariable](arkts-arkui-decorator-ilocalstorageproprefdecoratedvariable-i.md)&lt;T&gt; | LocalStoragePropRef instance |

## makeMonitor

```TypeScript
makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, owner?: IVariableOwner): IMonitorDecoratedVariable
```

Create a monitored variable instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, owner?: IVariableOwner): IMonitorDecoratedVariable--><!--Device-IStateMgmtFactory-makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, owner?: IVariableOwner): IMonitorDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | Array&lt;IMonitorPathInfo&gt; | Yes | monitor path to its accessor |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | Yes | callback when then monitor triggers |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | No | owner of this monitor |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | Monitor variable instance |

## makeMonitor

```TypeScript
makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, options?: MakeMonitorOptions): IMonitorDecoratedVariable
```

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, options?: MakeMonitorOptions): IMonitorDecoratedVariable--><!--Device-IStateMgmtFactory-makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, options?: MakeMonitorOptions): IMonitorDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | Array&lt;IMonitorPathInfo&gt; | Yes | monitor path to its accessor |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | Yes | callback when the monitor triggers |
| options | [MakeMonitorOptions](arkts-arkui-decorator-makemonitoroptions-i.md) | No | options of this monitor |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | Monitor variable instance |

## makeMutableStateMeta

```TypeScript
makeMutableStateMeta(): IMutableStateMeta
```

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeMutableStateMeta(): IMutableStateMeta--><!--Device-IStateMgmtFactory-makeMutableStateMeta(): IMutableStateMeta-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [IMutableStateMeta](arkts-arkui-decorator-imutablestatemeta-i.md) |  |

## makeMutableStateMeta

```TypeScript
makeMutableStateMeta(observedObject: IObservedObject | undefined, propertyName: string): IMutableStateMeta
```

获取可变状态元

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeMutableStateMeta(observedObject: IObservedObject | undefined, propertyName: string): IMutableStateMeta--><!--Device-IStateMgmtFactory-makeMutableStateMeta(observedObject: IObservedObject | undefined, propertyName: string): IMutableStateMeta-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observedObject | [IObservedObject](arkts-arkui-decorator-iobservedobject-i.md) \| undefined | Yes | 此元的所有者。 |
| propertyName | string | Yes | 元名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| [IMutableStateMeta](arkts-arkui-decorator-imutablestatemeta-i.md) |  |

## makeObjectLink

```TypeScript
makeObjectLink<T>(owner: IVariableOwner, varName: string,
    initValue: T, watchFunc?: WatchFuncType): IObjectLinkDecoratedVariable<T>
```

创建@ObjectLink状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeObjectLink<T>(owner: IVariableOwner, varName: string,    initValue: T, watchFunc?: WatchFuncType): IObjectLinkDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeObjectLink<T>(owner: IVariableOwner, varName: string,    initValue: T, watchFunc?: WatchFuncType): IObjectLinkDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| varName | string | Yes | 状态变量的名字 |
| initValue | T | Yes | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | No | 监听函数 |

**Return value:**

| Type | Description |
| --- | --- |
| [IObjectLinkDecoratedVariable](arkts-arkui-decorator-iobjectlinkdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeParam

```TypeScript
makeParam<T>(owner: IVariableOwner, varName: string, initValue: T): IParamDecoratedVariable<T>
```

创建@Param状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeParam<T>(owner: IVariableOwner, varName: string, initValue: T): IParamDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeParam<T>(owner: IVariableOwner, varName: string, initValue: T): IParamDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| varName | string | Yes | 状态变量的名字 |
| initValue | T | Yes | 状态变量的初始值 |

**Return value:**

| Type | Description |
| --- | --- |
| [IParamDecoratedVariable](arkts-arkui-decorator-iparamdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeParamOnce

```TypeScript
makeParamOnce<T>(owner: IVariableOwner, varName: string, initValue: T): IParamOnceDecoratedVariable<T>
```

创建@Once @Param状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeParamOnce<T>(owner: IVariableOwner, varName: string, initValue: T): IParamOnceDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeParamOnce<T>(owner: IVariableOwner, varName: string, initValue: T): IParamOnceDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| varName | string | Yes | 状态变量的名字 |
| initValue | T | Yes | 状态变量的初始值 |

**Return value:**

| Type | Description |
| --- | --- |
| [IParamOnceDecoratedVariable](arkts-arkui-decorator-iparamoncedecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makePropRef

```TypeScript
makePropRef<T>(owner: IVariableOwner, varName: string, initValue: T,
    watchFunc?: WatchFuncType): IPropRefDecoratedVariable<T>
```

创建@PropRef状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makePropRef<T>(owner: IVariableOwner, varName: string, initValue: T,    watchFunc?: WatchFuncType): IPropRefDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makePropRef<T>(owner: IVariableOwner, varName: string, initValue: T,    watchFunc?: WatchFuncType): IPropRefDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| varName | string | Yes | 状态变量的名字 |
| initValue | T | Yes | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | No | 监听函数 |

**Return value:**

| Type | Description |
| --- | --- |
| [IPropRefDecoratedVariable](arkts-arkui-decorator-iproprefdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeProvide

```TypeScript
makeProvide<T>(owner: IVariableOwner, varName: string, provideAlias: string, initValue: T, 
      allowOverride: boolean, watchFunc?: WatchFuncType): IProvideDecoratedVariable<T>
```

创建@Provide状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeProvide<T>(owner: IVariableOwner, varName: string, provideAlias: string, initValue: T,       allowOverride: boolean, watchFunc?: WatchFuncType): IProvideDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeProvide<T>(owner: IVariableOwner, varName: string, provideAlias: string, initValue: T,       allowOverride: boolean, watchFunc?: WatchFuncType): IProvideDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| varName | string | Yes | 状态变量的名字 |
| provideAlias | string | Yes | 变量别名 |
| initValue | T | Yes | 状态变量的初始值 |
| allowOverride | boolean | Yes | 是否覆盖父组件上的同名@Provide状态变量 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | No | 监听函数 |

**Return value:**

| Type | Description |
| --- | --- |
| [IProvideDecoratedVariable](arkts-arkui-decorator-iprovidedecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeProvider

```TypeScript
makeProvider<T>(owner: IVariableOwner, varName: string, providerAlias: string, 
                  localInitValue: T): IProviderDecoratedVariable<T>
```

创建@Provider 状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeProvider<T>(owner: IVariableOwner, varName: string, providerAlias: string,                   localInitValue: T): IProviderDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeProvider<T>(owner: IVariableOwner, varName: string, providerAlias: string,                   localInitValue: T): IProviderDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| varName | string | Yes | 状态变量的名字 |
| providerAlias | string | Yes | 变量别名 |
| localInitValue | T | Yes | 状态变量的初始值 |

**Return value:**

| Type | Description |
| --- | --- |
| [IProviderDecoratedVariable](arkts-arkui-decorator-iproviderdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeState

```TypeScript
makeState<T>(owner: IVariableOwner, varName: string, initValue: T,
    watchFunc?: WatchFuncType): IStateDecoratedVariable<T>
```

创建@State状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeState<T>(owner: IVariableOwner, varName: string, initValue: T,    watchFunc?: WatchFuncType): IStateDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeState<T>(owner: IVariableOwner, varName: string, initValue: T,    watchFunc?: WatchFuncType): IStateDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| varName | string | Yes | 状态变量的名字 |
| initValue | T | Yes | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | No | 监听函数 |

**Return value:**

| Type | Description |
| --- | --- |
| [IStateDecoratedVariable](arkts-arkui-decorator-istatedecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeStaticLocal

```TypeScript
makeStaticLocal<T>(varName: string, localInitValue: T): ILocalDecoratedVariable<T>
```

Create a static local variable instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeStaticLocal<T>(varName: string, localInitValue: T): ILocalDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeStaticLocal<T>(varName: string, localInitValue: T): ILocalDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| varName | string | Yes | state variable name. |
| localInitValue | T | Yes | state variable initValue. |

**Return value:**

| Type | Description |
| --- | --- |
| [ILocalDecoratedVariable](arkts-arkui-decorator-ilocaldecoratedvariable-i.md)&lt;T&gt; | Local instance |

## makeStorageLink

```TypeScript
makeStorageLink<T>(owner: IVariableOwner, propName: string,
    varName: string, initValue: T, watchFunc?: WatchFuncType): IStorageLinkDecoratedVariable<T>
```

创建@StorageLink状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeStorageLink<T>(owner: IVariableOwner, propName: string,    varName: string, initValue: T, watchFunc?: WatchFuncType): IStorageLinkDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeStorageLink<T>(owner: IVariableOwner, propName: string,    varName: string, initValue: T, watchFunc?: WatchFuncType): IStorageLinkDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| propName | string | Yes | 属性名字 |
| varName | string | Yes | 状态变量的名字 |
| initValue | T | Yes | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | No | 监听函数 |

**Return value:**

| Type | Description |
| --- | --- |
| [IStorageLinkDecoratedVariable](arkts-arkui-decorator-istoragelinkdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeStoragePropRef

```TypeScript
makeStoragePropRef<T>(owner: IVariableOwner, propName: string,
    varName: string, initValue: T, watchFunc?: WatchFuncType): IStoragePropRefDecoratedVariable<T>
```

创建@Storage PropRef状态变量实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeStoragePropRef<T>(owner: IVariableOwner, propName: string,    varName: string, initValue: T, watchFunc?: WatchFuncType): IStoragePropRefDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeStoragePropRef<T>(owner: IVariableOwner, propName: string,    varName: string, initValue: T, watchFunc?: WatchFuncType): IStoragePropRefDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |
| propName | string | Yes | 属性名字 |
| varName | string | Yes | 状态变量的名字 |
| initValue | T | Yes | 状态变量的初始值 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | No | 监听函数 |

**Return value:**

| Type | Description |
| --- | --- |
| [IStoragePropRefDecoratedVariable](arkts-arkui-decorator-istorageproprefdecoratedvariable-i.md)&lt;T&gt; | 状态变量实例 |

## makeSubscribedWatches

```TypeScript
makeSubscribedWatches(): ISubscribedWatches
```

get subscribed watches

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeSubscribedWatches(): ISubscribedWatches--><!--Device-IStateMgmtFactory-makeSubscribedWatches(): ISubscribedWatches-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ISubscribedWatches](arkts-arkui-decorator-isubscribedwatches-i.md) |  |

## makeSyncMonitor

```TypeScript
makeSyncMonitor(pathInfos: IMonitorPathInfo[], monitorCallback: MonitorCallback,
    options?: MakeMonitorOptions): IMonitorDecoratedVariable
```

创建同步监控变量实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeSyncMonitor(pathInfos: IMonitorPathInfo[], monitorCallback: MonitorCallback,    options?: MakeMonitorOptions): IMonitorDecoratedVariable--><!--Device-IStateMgmtFactory-makeSyncMonitor(pathInfos: IMonitorPathInfo[], monitorCallback: MonitorCallback,    options?: MakeMonitorOptions): IMonitorDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [IMonitorPathInfo](arkts-arkui-decorator-imonitorpathinfo-i.md)[] | Yes | 到其访问器的监视器路径。 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | Yes | 监视器触发时的回调。 |
| options | [MakeMonitorOptions](arkts-arkui-decorator-makemonitoroptions-i.md) | No | 此监视器的选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | 监控变量实例 |

