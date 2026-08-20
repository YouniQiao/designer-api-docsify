# IStateMgmtFactory

Define IStateMgmtFactory interface.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface IStateMgmtFactory--><!--Device-unnamed-export declare interface IStateMgmtFactory-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## makeComputed

```TypeScript
makeComputed<T>(computedCallback: ComputedCallback<T>, computeName: string): IComputedDecoratedVariable<T>
```

Create a computed variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeComputed<T>(computedCallback: ComputedCallback<T>, computeName: string): IComputedDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeComputed<T>(computedCallback: ComputedCallback<T>, computeName: string): IComputedDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| computedCallback | [ComputedCallback](arkts-computedcallback-t.md)&lt;T&gt; | Yes | computed callback function |
| computeName | string | Yes | name of the computed function |

**Return value:**

| Type | Description |
| --- | --- |
| [IComputedDecoratedVariable](arkts-decorator-icomputeddecoratedvariable-i.md)&lt;T&gt; | Computed instance |

## makeConsume

```TypeScript
makeConsume<T>(owner: IVariableOwner, varName: string,
    provideAlias: string, watchFunc?: WatchFuncType): IConsumeDecoratedVariable<T>
```

Create a Consume variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeConsume<T>(owner: IVariableOwner, varName: string,    provideAlias: string, watchFunc?: WatchFuncType): IConsumeDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeConsume<T>(owner: IVariableOwner, varName: string,    provideAlias: string, watchFunc?: WatchFuncType): IConsumeDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| varName | string | Yes | state variable name. |
| provideAlias | string | Yes | provide alias. |
| watchFunc | [WatchFuncType](arkts-watchfunctype-t.md) | No | watch type |

**Return value:**

| Type | Description |
| --- | --- |
| [IConsumeDecoratedVariable](arkts-decorator-iconsumedecoratedvariable-i.md)&lt;T&gt; | Consume instance |

## makeConsume

```TypeScript
makeConsume<T>(owner: IVariableOwner, varName: string,
    provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): IConsumeDecoratedVariable<T>
```

Create a Consume variable instance. It is used to establish two-way data binding with @Provide.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeConsume<T>(owner: IVariableOwner, varName: string,    provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): IConsumeDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeConsume<T>(owner: IVariableOwner, varName: string,    provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): IConsumeDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | instance of the custom component where this state variable is located. |
| varName | string | Yes | state variable name. |
| provideAlias | string | Yes | provide alias. |
| watchFunc | [WatchFuncType](arkts-watchfunctype-t.md) | No | watch callback function type. |
| consumeOptions | [ConsumeOptions](arkts-decorator-consumeoptions-i.md)&lt;T&gt; | No | interface containing default value set by developer. |

**Return value:**

| Type | Description |
| --- | --- |
| [IConsumeDecoratedVariable](arkts-decorator-iconsumedecoratedvariable-i.md)&lt;T&gt; | Consume instance. |

## makeConsumer

```TypeScript
makeConsumer<T>(
    owner: IVariableOwner, varName: string, providerAlias: string, defaultValue: T
  ): IConsumerDecoratedVariable<T>
```

Create a consumer variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeConsumer<T>(    owner: IVariableOwner, varName: string, providerAlias: string, defaultValue: T  ): IConsumerDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeConsumer<T>(    owner: IVariableOwner, varName: string, providerAlias: string, defaultValue: T  ): IConsumerDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| varName | string | Yes | consumer variable name. |
| providerAlias | string | Yes | consumer alias. |
| defaultValue | T | Yes | consumer default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [IConsumerDecoratedVariable](arkts-decorator-iconsumerdecoratedvariable-i.md)&lt;T&gt; | Consumer instance |

## makeCustomEnv

```TypeScript
makeCustomEnv<T>(owner: IVariableOwner, envKey: CustomEnvKey<T>, varName: string, localInitValue: T, customEnvOptions?: CustomEnvOptions<T>): ICustomEnvDecoratedVariable<T>
```

Create a CustomEnv variable instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeCustomEnv<T>(owner: IVariableOwner, envKey: CustomEnvKey<T>, varName: string, localInitValue: T, customEnvOptions?: CustomEnvOptions<T>): ICustomEnvDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeCustomEnv<T>(owner: IVariableOwner, envKey: CustomEnvKey<T>, varName: string, localInitValue: T, customEnvOptions?: CustomEnvOptions<T>): ICustomEnvDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | custom component owner. |
| envKey | [CustomEnvKey](arkts-decorator-customenvkey-c.md)&lt;T&gt; | Yes | custom env key. |
| varName | string | Yes | variable name that is decorated by @CustomEnv. |
| localInitValue | T | Yes | custom env variable initValue. |
| customEnvOptions | [CustomEnvOptions](arkts-decorator-customenvoptions-i.md)&lt;T&gt; | No | additional options for makeCustomEnv. |

**Return value:**

| Type | Description |
| --- | --- |
| [ICustomEnvDecoratedVariable](arkts-decorator-icustomenvdecoratedvariable-i.md)&lt;T&gt; | CustomEnv variable instance |

## makeEnv

```TypeScript
makeEnv<T>(owner: IVariableOwner, envValue: string | SystemEnvKey<T>, varName: string, envOptions?: EnvOptions<T>): IEnvDecoratedVariable<T>
```

Create a Env variable instance. On API 26.0.0 and above, it can also support SystemEnvKey type for envValue.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeEnv<T>(owner: IVariableOwner, envValue: string | SystemEnvKey<T>, varName: string, envOptions?: EnvOptions<T>): IEnvDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeEnv<T>(owner: IVariableOwner, envValue: string | SystemEnvKey<T>, varName: string, envOptions?: EnvOptions<T>): IEnvDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | custom component owner |
| envValue | string \| [SystemEnvKey](arkts-decorator-systemenvkey-c.md)&lt;T&gt; | Yes | system environment key<br>**Since:** 26.0.0 |
| varName | string | Yes | variable name that is decorated by @Env |
| envOptions | [EnvOptions](arkts-decorator-envoptions-i.md)&lt;T&gt; | No | additional options for makeEnv |

**Return value:**

| Type | Description |
| --- | --- |
| [IEnvDecoratedVariable](arkts-decorator-ienvdecoratedvariable-i.md)&lt;T&gt; | Env variable instance |

## makeGlobalReusePool

```TypeScript
makeGlobalReusePool(reusePool: ReusePoolOwnership,
    poolAccepts: Class[], owningView: IVariableOwner): IGlobalReusePoolVariable
```

Create global reuse pool on a custom component.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeGlobalReusePool(reusePool: ReusePoolOwnership,    poolAccepts: Class[], owningView: IVariableOwner): IGlobalReusePoolVariable--><!--Device-IStateMgmtFactory-makeGlobalReusePool(reusePool: ReusePoolOwnership,    poolAccepts: Class[], owningView: IVariableOwner): IGlobalReusePoolVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reusePool | [ReusePoolOwnership](arkts-customcomponent-reusepoolownership-e.md) | Yes | reuse pool type. |
| poolAccepts | [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md)[] | Yes | custom components that reuse pool accepts. |
| owningView | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | custom component that owns the global pool. |

**Return value:**

| Type | Description |
| --- | --- |
| [IGlobalReusePoolVariable](arkts-decorator-iglobalreusepoolvariable-i.md) | global reuse pool handle. |

## makeLink

```TypeScript
makeLink<T>(owner: IVariableOwner, varName: string, source: LinkSourceType<T>,
    watchFunc?: WatchFuncType): ILinkDecoratedVariable<T>
```

Create a Link variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeLink<T>(owner: IVariableOwner, varName: string, source: LinkSourceType<T>,    watchFunc?: WatchFuncType): ILinkDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeLink<T>(owner: IVariableOwner, varName: string, source: LinkSourceType<T>,    watchFunc?: WatchFuncType): ILinkDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| varName | string | Yes | state variable name. |
| source | [LinkSourceType](arkts-linksourcetype-t.md)&lt;T&gt; | Yes | state variable sync source. |
| watchFunc | [WatchFuncType](arkts-watchfunctype-t.md) | No | watch type |

**Return value:**

| Type | Description |
| --- | --- |
| [ILinkDecoratedVariable](arkts-decorator-ilinkdecoratedvariable-i.md)&lt;T&gt; | PropRef instance |

## makeLocal

```TypeScript
makeLocal<T>(owner: IVariableOwner, varName: string, localInitValue: T): ILocalDecoratedVariable<T>
```

Create a Local variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeLocal<T>(owner: IVariableOwner, varName: string, localInitValue: T): ILocalDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeLocal<T>(owner: IVariableOwner, varName: string, localInitValue: T): ILocalDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| varName | string | Yes | state variable name. |
| localInitValue | T | Yes | state variable initValue. |

**Return value:**

| Type | Description |
| --- | --- |
| [ILocalDecoratedVariable](arkts-decorator-ilocaldecoratedvariable-i.md)&lt;T&gt; | Local instance |

## makeLocalStorageLink

```TypeScript
makeLocalStorageLink<T>(owner: IVariableOwner, propName: string,
        varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStorageLinkDecoratedVariable<T>
```

Create a LocalStorageLink variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeLocalStorageLink<T>(owner: IVariableOwner, propName: string,        varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStorageLinkDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeLocalStorageLink<T>(owner: IVariableOwner, propName: string,        varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStorageLinkDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| propName | string | Yes | property name. |
| varName | string | Yes | state variable name. |
| initValue | T | Yes | init value. |
| watchFunc | [WatchFuncType](arkts-watchfunctype-t.md) | No | watch type |

**Return value:**

| Type | Description |
| --- | --- |
| [ILocalStorageLinkDecoratedVariable](arkts-decorator-ilocalstoragelinkdecoratedvariable-i.md)&lt;T&gt; | LocalStorageLink instance |

## makeLocalStoragePropRef

```TypeScript
makeLocalStoragePropRef<T>(owner: IVariableOwner, propName: string, varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStoragePropRefDecoratedVariable<T>
```

Create a LocalStoragePropRef variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeLocalStoragePropRef<T>(owner: IVariableOwner, propName: string, varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStoragePropRefDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeLocalStoragePropRef<T>(owner: IVariableOwner, propName: string, varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStoragePropRefDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| propName | string | Yes | property name. |
| varName | string | Yes | state variable name. |
| initValue | T | Yes | init value. |
| watchFunc | [WatchFuncType](arkts-watchfunctype-t.md) | No | watch type |

**Return value:**

| Type | Description |
| --- | --- |
| [ILocalStoragePropRefDecoratedVariable](arkts-decorator-ilocalstorageproprefdecoratedvariable-i.md)&lt;T&gt; | LocalStoragePropRef instance |

## makeMonitor

```TypeScript
makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, owner?: IVariableOwner): IMonitorDecoratedVariable
```

Create a monitored variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, owner?: IVariableOwner): IMonitorDecoratedVariable--><!--Device-IStateMgmtFactory-makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, owner?: IVariableOwner): IMonitorDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | Array&lt;[IMonitorPathInfo](arkts-decorator-imonitorpathinfo-i.md)&gt; | Yes | monitor path to its accessor |
| monitorCallback | [MonitorCallback](arkts-monitorcallback-t.md) | Yes | callback when then monitor triggers |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | No | owner of this monitor |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-decorator-imonitordecoratedvariable-i.md) | Monitor variable instance |

## makeMonitor

```TypeScript
makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, options?: MakeMonitorOptions): IMonitorDecoratedVariable
```

Create a monitored variable instance.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, options?: MakeMonitorOptions): IMonitorDecoratedVariable--><!--Device-IStateMgmtFactory-makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, options?: MakeMonitorOptions): IMonitorDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | Array&lt;[IMonitorPathInfo](arkts-decorator-imonitorpathinfo-i.md)&gt; | Yes | monitor path to its accessor |
| monitorCallback | [MonitorCallback](arkts-monitorcallback-t.md) | Yes | callback when the monitor triggers |
| options | [MakeMonitorOptions](arkts-decorator-makemonitoroptions-i.md) | No | options of this monitor |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-decorator-imonitordecoratedvariable-i.md) | Monitor variable instance |

## makeMutableStateMeta

```TypeScript
makeMutableStateMeta(): IMutableStateMeta
```

get mutable state meta

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeMutableStateMeta(): IMutableStateMeta--><!--Device-IStateMgmtFactory-makeMutableStateMeta(): IMutableStateMeta-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [IMutableStateMeta](arkts-decorator-imutablestatemeta-i.md) |  |

## makeMutableStateMeta

```TypeScript
makeMutableStateMeta(observedObject: IObservedObject | undefined, propertyName: string): IMutableStateMeta
```

get mutable state meta

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeMutableStateMeta(observedObject: IObservedObject | undefined, propertyName: string): IMutableStateMeta--><!--Device-IStateMgmtFactory-makeMutableStateMeta(observedObject: IObservedObject | undefined, propertyName: string): IMutableStateMeta-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observedObject | [IObservedObject](arkts-decorator-iobservedobject-i.md) \| undefined | Yes | owner of this meta. |
| propertyName | string | Yes | meta name. |

**Return value:**

| Type | Description |
| --- | --- |
| [IMutableStateMeta](arkts-decorator-imutablestatemeta-i.md) |  |

## makeObjectLink

```TypeScript
makeObjectLink<T>(owner: IVariableOwner, varName: string,
    initValue: T, watchFunc?: WatchFuncType): IObjectLinkDecoratedVariable<T>
```

Create a ObjectLink variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeObjectLink<T>(owner: IVariableOwner, varName: string,    initValue: T, watchFunc?: WatchFuncType): IObjectLinkDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeObjectLink<T>(owner: IVariableOwner, varName: string,    initValue: T, watchFunc?: WatchFuncType): IObjectLinkDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| varName | string | Yes | state variable name. |
| initValue | T | Yes | init value. |
| watchFunc | [WatchFuncType](arkts-watchfunctype-t.md) | No | watch type |

**Return value:**

| Type | Description |
| --- | --- |
| [IObjectLinkDecoratedVariable](arkts-decorator-iobjectlinkdecoratedvariable-i.md)&lt;T&gt; | ObjectLink instance |

## makeParam

```TypeScript
makeParam<T>(owner: IVariableOwner, varName: string, initValue: T): IParamDecoratedVariable<T>
```

Create a Param variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeParam<T>(owner: IVariableOwner, varName: string, initValue: T): IParamDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeParam<T>(owner: IVariableOwner, varName: string, initValue: T): IParamDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| varName | string | Yes | state variable name. |
| initValue | T | Yes | param variable initValue. |

**Return value:**

| Type | Description |
| --- | --- |
| [IParamDecoratedVariable](arkts-decorator-iparamdecoratedvariable-i.md)&lt;T&gt; | Param instance |

## makeParamOnce

```TypeScript
makeParamOnce<T>(owner: IVariableOwner, varName: string, initValue: T): IParamOnceDecoratedVariable<T>
```

Create a param once variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeParamOnce<T>(owner: IVariableOwner, varName: string, initValue: T): IParamOnceDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeParamOnce<T>(owner: IVariableOwner, varName: string, initValue: T): IParamOnceDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| varName | string | Yes | state variable name. |
| initValue | T | Yes | param once variable initValue. |

**Return value:**

| Type | Description |
| --- | --- |
| [IParamOnceDecoratedVariable](arkts-decorator-iparamoncedecoratedvariable-i.md)&lt;T&gt; | Param Once instance |

## makePropRef

```TypeScript
makePropRef<T>(owner: IVariableOwner, varName: string, initValue: T,
    watchFunc?: WatchFuncType): IPropRefDecoratedVariable<T>
```

Create a PropRef variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makePropRef<T>(owner: IVariableOwner, varName: string, initValue: T,    watchFunc?: WatchFuncType): IPropRefDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makePropRef<T>(owner: IVariableOwner, varName: string, initValue: T,    watchFunc?: WatchFuncType): IPropRefDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| varName | string | Yes | state variable name. |
| initValue | T | Yes | state variable initValue. |
| watchFunc | [WatchFuncType](arkts-watchfunctype-t.md) | No | watch type |

**Return value:**

| Type | Description |
| --- | --- |
| [IPropRefDecoratedVariable](arkts-decorator-iproprefdecoratedvariable-i.md)&lt;T&gt; | PropRef instance |

## makeProvide

```TypeScript
makeProvide<T>(owner: IVariableOwner, varName: string, provideAlias: string, initValue: T, 
      allowOverride: boolean, watchFunc?: WatchFuncType): IProvideDecoratedVariable<T>
```

Create a Provide variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeProvide<T>(owner: IVariableOwner, varName: string, provideAlias: string, initValue: T,       allowOverride: boolean, watchFunc?: WatchFuncType): IProvideDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeProvide<T>(owner: IVariableOwner, varName: string, provideAlias: string, initValue: T,       allowOverride: boolean, watchFunc?: WatchFuncType): IProvideDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| varName | string | Yes | state variable name. |
| provideAlias | string | Yes | provide alias. |
| initValue | T | Yes | init value. |
| allowOverride | boolean | Yes | Override the @Provide of any parent |
| watchFunc | [WatchFuncType](arkts-watchfunctype-t.md) | No | watch type |

**Return value:**

| Type | Description |
| --- | --- |
| [IProvideDecoratedVariable](arkts-decorator-iprovidedecoratedvariable-i.md)&lt;T&gt; | Provide instance |

## makeProvider

```TypeScript
makeProvider<T>(owner: IVariableOwner, varName: string, providerAlias: string, 
                  localInitValue: T): IProviderDecoratedVariable<T>
```

Create a provider variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeProvider<T>(owner: IVariableOwner, varName: string, providerAlias: string,                   localInitValue: T): IProviderDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeProvider<T>(owner: IVariableOwner, varName: string, providerAlias: string,                   localInitValue: T): IProviderDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| varName | string | Yes | provider variable name. |
| providerAlias | string | Yes | provider alias. |
| localInitValue | T | Yes | provider local variable value. |

**Return value:**

| Type | Description |
| --- | --- |
| [IProviderDecoratedVariable](arkts-decorator-iproviderdecoratedvariable-i.md)&lt;T&gt; | Provider instance |

## makeState

```TypeScript
makeState<T>(owner: IVariableOwner, varName: string, initValue: T,
    watchFunc?: WatchFuncType): IStateDecoratedVariable<T>
```

Create a State variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeState<T>(owner: IVariableOwner, varName: string, initValue: T,    watchFunc?: WatchFuncType): IStateDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeState<T>(owner: IVariableOwner, varName: string, initValue: T,    watchFunc?: WatchFuncType): IStateDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| varName | string | Yes | state variable name. |
| initValue | T | Yes | state variable initValue. |
| watchFunc | [WatchFuncType](arkts-watchfunctype-t.md) | No | watch type |

**Return value:**

| Type | Description |
| --- | --- |
| [IStateDecoratedVariable](arkts-decorator-istatedecoratedvariable-i.md)&lt;T&gt; | State instance |

## makeStaticLocal

```TypeScript
makeStaticLocal<T>(varName: string, localInitValue: T): ILocalDecoratedVariable<T>
```

Create a static local variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

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
| [ILocalDecoratedVariable](arkts-decorator-ilocaldecoratedvariable-i.md)&lt;T&gt; | Local instance |

## makeStorageLink

```TypeScript
makeStorageLink<T>(owner: IVariableOwner, propName: string,
    varName: string, initValue: T, watchFunc?: WatchFuncType): IStorageLinkDecoratedVariable<T>
```

Create a StorageLink variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeStorageLink<T>(owner: IVariableOwner, propName: string,    varName: string, initValue: T, watchFunc?: WatchFuncType): IStorageLinkDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeStorageLink<T>(owner: IVariableOwner, propName: string,    varName: string, initValue: T, watchFunc?: WatchFuncType): IStorageLinkDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| propName | string | Yes | property name. |
| varName | string | Yes | state variable name. |
| initValue | T | Yes | init value. |
| watchFunc | [WatchFuncType](arkts-watchfunctype-t.md) | No | watch type |

**Return value:**

| Type | Description |
| --- | --- |
| [IStorageLinkDecoratedVariable](arkts-decorator-istoragelinkdecoratedvariable-i.md)&lt;T&gt; | StorageLink instance |

## makeStoragePropRef

```TypeScript
makeStoragePropRef<T>(owner: IVariableOwner, propName: string,
    varName: string, initValue: T, watchFunc?: WatchFuncType): IStoragePropRefDecoratedVariable<T>
```

Create a StoragePropRef variable instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeStoragePropRef<T>(owner: IVariableOwner, propName: string,    varName: string, initValue: T, watchFunc?: WatchFuncType): IStoragePropRefDecoratedVariable<T>--><!--Device-IStateMgmtFactory-makeStoragePropRef<T>(owner: IVariableOwner, propName: string,    varName: string, initValue: T, watchFunc?: WatchFuncType): IStoragePropRefDecoratedVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-decorator-ivariableowner-i.md) | Yes | owner of this variable. |
| propName | string | Yes | property name. |
| varName | string | Yes | state variable name. |
| initValue | T | Yes | init value. |
| watchFunc | [WatchFuncType](arkts-watchfunctype-t.md) | No | watch type |

**Return value:**

| Type | Description |
| --- | --- |
| [IStoragePropRefDecoratedVariable](arkts-decorator-istorageproprefdecoratedvariable-i.md)&lt;T&gt; | StoragePropRef instance |

## makeSubscribedWatches

```TypeScript
makeSubscribedWatches(): ISubscribedWatches
```

get subscribed watches

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeSubscribedWatches(): ISubscribedWatches--><!--Device-IStateMgmtFactory-makeSubscribedWatches(): ISubscribedWatches-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ISubscribedWatches](arkts-decorator-isubscribedwatches-i.md) |  |

## makeSyncMonitor

```TypeScript
makeSyncMonitor(pathInfos: IMonitorPathInfo[], monitorCallback: MonitorCallback,
    options?: MakeMonitorOptions): IMonitorDecoratedVariable
```

Create a synchronous monitored variable instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IStateMgmtFactory-makeSyncMonitor(pathInfos: IMonitorPathInfo[], monitorCallback: MonitorCallback,    options?: MakeMonitorOptions): IMonitorDecoratedVariable--><!--Device-IStateMgmtFactory-makeSyncMonitor(pathInfos: IMonitorPathInfo[], monitorCallback: MonitorCallback,    options?: MakeMonitorOptions): IMonitorDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [IMonitorPathInfo](arkts-decorator-imonitorpathinfo-i.md)[] | Yes | monitor path to its accessor. |
| monitorCallback | [MonitorCallback](arkts-monitorcallback-t.md) | Yes | callback when the monitor triggers. |
| options | [MakeMonitorOptions](arkts-decorator-makemonitoroptions-i.md) | No | options of this monitor. |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-decorator-imonitordecoratedvariable-i.md) | Monitor variable instance |

