# IStateMgmtFactory

Define IStateMgmtFactory interface.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## makeComputed

```TypeScript
makeComputed<T>(computedCallback: ComputedCallback<T>, computeName: string): IComputedDecoratedVariable<T>
```

Create a computed variable instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| computedCallback | [ComputedCallback](arkts-arkui-computedcallback-t.md)&lt;T&gt; | 是 |
| computeName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [IComputedDecoratedVariable](arkts-arkui-decorator-icomputeddecoratedvariable-i.md)&lt;T&gt; |

## makeConsume

```TypeScript
makeConsume<T>(owner: IVariableOwner, varName: string,
    provideAlias: string, watchFunc?: WatchFuncType): IConsumeDecoratedVariable<T>
```

创建@Consume状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| provideAlias | string | 是 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IConsumeDecoratedVariable](arkts-arkui-decorator-iconsumedecoratedvariable-i.md)&lt;T&gt; |

## makeConsume

```TypeScript
makeConsume<T>(owner: IVariableOwner, varName: string,
    provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): IConsumeDecoratedVariable<T>
```

创建@Consume状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| provideAlias | string | 是 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 |
| consumeOptions | [ConsumeOptions](arkts-arkui-decorator-consumeoptions-i.md)&lt;T&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [IConsumeDecoratedVariable](arkts-arkui-decorator-iconsumedecoratedvariable-i.md)&lt;T&gt; |

## makeConsumer

```TypeScript
makeConsumer<T>(
    owner: IVariableOwner, varName: string, providerAlias: string, defaultValue: T
  ): IConsumerDecoratedVariable<T>
```

创建@Consumer状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| providerAlias | string | 是 |
| defaultValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| [IConsumerDecoratedVariable](arkts-arkui-decorator-iconsumerdecoratedvariable-i.md)&lt;T&gt; |

## makeCustomEnv

```TypeScript
makeCustomEnv<T>(owner: IVariableOwner, envKey: CustomEnvKey<T>, varName: string, localInitValue: T): ICustomEnvDecoratedVariable<T>
```

创建一个CustomEnv变量实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| envKey | [CustomEnvKey](arkts-arkui-decorator-customenvkey-c.md)&lt;T&gt; | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| localInitValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| [ICustomEnvDecoratedVariable](arkts-arkui-decorator-icustomenvdecoratedvariable-i.md)&lt;T&gt; |

## makeEnv

```TypeScript
makeEnv<T>(owner: IVariableOwner, envValue: string | SystemEnvKey<T>, varName: string, envOptions?: EnvOptions<T>): IEnvDecoratedVariable<T>
```

创建一个Env变量实例。 在API 26.0.0及更高版本上，envValue参数支持SystemEnvKey类型。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| envValue | string \| [SystemEnvKey](arkts-arkui-decorator-systemenvkey-c.md)&lt;T&gt; | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| envOptions | [EnvOptions](arkts-arkui-decorator-envoptions-i.md)&lt;T&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [IEnvDecoratedVariable](arkts-arkui-decorator-ienvdecoratedvariable-i.md)&lt;T&gt; |

## makeGlobalReusePool

```TypeScript
makeGlobalReusePool(reusePool: ReusePoolOwnership,
    poolAccepts: Class[], owningView: IVariableOwner): IGlobalReusePoolVariable
```

在自定义组件上创建全局重用池。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reusePool | [ReusePoolOwnership](arkts-arkui-customcomponent-reusepoolownership-e.md) | 是 |
| poolAccepts | [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md)[] | 是 |
| owningView | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [IGlobalReusePoolVariable](arkts-arkui-decorator-iglobalreusepoolvariable-i.md) |

## makeLink

```TypeScript
makeLink<T>(owner: IVariableOwner, varName: string, source: LinkSourceType<T>,
    watchFunc?: WatchFuncType): ILinkDecoratedVariable<T>
```

创建@Link状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| source | [LinkSourceType](arkts-arkui-linksourcetype-t.md)&lt;T&gt; | 是 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ILinkDecoratedVariable](arkts-arkui-decorator-ilinkdecoratedvariable-i.md)&lt;T&gt; |

## makeLocal

```TypeScript
makeLocal<T>(owner: IVariableOwner, varName: string, localInitValue: T): ILocalDecoratedVariable<T>
```

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| localInitValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| [ILocalDecoratedVariable](arkts-arkui-decorator-ilocaldecoratedvariable-i.md)&lt;T&gt; |

## makeLocalStorageLink

```TypeScript
makeLocalStorageLink<T>(owner: IVariableOwner, propName: string,
        varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStorageLinkDecoratedVariable<T>
```

创建@LocalStorageLink状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| propName | string | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| [initValue](arkts-arkui-decorator-envoptions-i.md) | T | 是 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ILocalStorageLinkDecoratedVariable](arkts-arkui-decorator-ilocalstoragelinkdecoratedvariable-i.md)&lt;T&gt; |

## makeLocalStoragePropRef

```TypeScript
makeLocalStoragePropRef<T>(owner: IVariableOwner, propName: string, varName: string, initValue: T, watchFunc?: WatchFuncType): ILocalStoragePropRefDecoratedVariable<T>
```

Create a LocalStoragePropRef variable instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| propName | string | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| [initValue](arkts-arkui-decorator-envoptions-i.md) | T | 是 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ILocalStoragePropRefDecoratedVariable](arkts-arkui-decorator-ilocalstorageproprefdecoratedvariable-i.md)&lt;T&gt; |

## makeMonitor

```TypeScript
makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, owner?: IVariableOwner): IMonitorDecoratedVariable
```

Create a monitored variable instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathInfos | Array&lt;[IMonitorPathInfo](arkts-arkui-decorator-imonitorpathinfo-i.md)&gt; | 是 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | 是 |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) |

## makeMonitor

```TypeScript
makeMonitor(pathInfos: Array<IMonitorPathInfo>, monitorCallback: MonitorCallback, options?: MakeMonitorOptions): IMonitorDecoratedVariable
```

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathInfos | Array&lt;[IMonitorPathInfo](arkts-arkui-decorator-imonitorpathinfo-i.md)&gt; | 是 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | 是 |
| options | [MakeMonitorOptions](arkts-arkui-decorator-makemonitoroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) |

## makeMutableStateMeta

```TypeScript
makeMutableStateMeta(): IMutableStateMeta
```

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [IMutableStateMeta](arkts-arkui-decorator-imutablestatemeta-i.md) |

## makeMutableStateMeta

```TypeScript
makeMutableStateMeta(observedObject: IObservedObject | undefined, propertyName: string): IMutableStateMeta
```

获取可变状态元

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| observedObject | [IObservedObject](arkts-arkui-decorator-iobservedobject-i.md) \| undefined | 是 |
| propertyName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [IMutableStateMeta](arkts-arkui-decorator-imutablestatemeta-i.md) |

## makeObjectLink

```TypeScript
makeObjectLink<T>(owner: IVariableOwner, varName: string,
    initValue: T, watchFunc?: WatchFuncType): IObjectLinkDecoratedVariable<T>
```

创建@ObjectLink状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| [initValue](arkts-arkui-decorator-envoptions-i.md) | T | 是 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IObjectLinkDecoratedVariable](arkts-arkui-decorator-iobjectlinkdecoratedvariable-i.md)&lt;T&gt; |

## makeParam

```TypeScript
makeParam<T>(owner: IVariableOwner, varName: string, initValue: T): IParamDecoratedVariable<T>
```

创建@Param状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| [initValue](arkts-arkui-decorator-envoptions-i.md) | T | 是 |

**返回值：**

| 类型 |
| --- |
| [IParamDecoratedVariable](arkts-arkui-decorator-iparamdecoratedvariable-i.md)&lt;T&gt; |

## makeParamOnce

```TypeScript
makeParamOnce<T>(owner: IVariableOwner, varName: string, initValue: T): IParamOnceDecoratedVariable<T>
```

创建@Once @Param状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| [initValue](arkts-arkui-decorator-envoptions-i.md) | T | 是 |

**返回值：**

| 类型 |
| --- |
| [IParamOnceDecoratedVariable](arkts-arkui-decorator-iparamoncedecoratedvariable-i.md)&lt;T&gt; |

## makePropRef

```TypeScript
makePropRef<T>(owner: IVariableOwner, varName: string, initValue: T,
    watchFunc?: WatchFuncType): IPropRefDecoratedVariable<T>
```

创建@PropRef状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| [initValue](arkts-arkui-decorator-envoptions-i.md) | T | 是 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IPropRefDecoratedVariable](arkts-arkui-decorator-iproprefdecoratedvariable-i.md)&lt;T&gt; |

## makeProvide

```TypeScript
makeProvide<T>(owner: IVariableOwner, varName: string, provideAlias: string, initValue: T, 
      allowOverride: boolean, watchFunc?: WatchFuncType): IProvideDecoratedVariable<T>
```

创建@Provide状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| provideAlias | string | 是 |
| [initValue](arkts-arkui-decorator-envoptions-i.md) | T | 是 |
| allowOverride | boolean | 是 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IProvideDecoratedVariable](arkts-arkui-decorator-iprovidedecoratedvariable-i.md)&lt;T&gt; |

## makeProvider

```TypeScript
makeProvider<T>(owner: IVariableOwner, varName: string, providerAlias: string, 
                  localInitValue: T): IProviderDecoratedVariable<T>
```

创建@Provider 状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| providerAlias | string | 是 |
| localInitValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| [IProviderDecoratedVariable](arkts-arkui-decorator-iproviderdecoratedvariable-i.md)&lt;T&gt; |

## makeState

```TypeScript
makeState<T>(owner: IVariableOwner, varName: string, initValue: T,
    watchFunc?: WatchFuncType): IStateDecoratedVariable<T>
```

创建@State状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| [initValue](arkts-arkui-decorator-envoptions-i.md) | T | 是 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IStateDecoratedVariable](arkts-arkui-decorator-istatedecoratedvariable-i.md)&lt;T&gt; |

## makeStaticLocal

```TypeScript
makeStaticLocal<T>(varName: string, localInitValue: T): ILocalDecoratedVariable<T>
```

Create a static local variable instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| localInitValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| [ILocalDecoratedVariable](arkts-arkui-decorator-ilocaldecoratedvariable-i.md)&lt;T&gt; |

## makeStorageLink

```TypeScript
makeStorageLink<T>(owner: IVariableOwner, propName: string,
    varName: string, initValue: T, watchFunc?: WatchFuncType): IStorageLinkDecoratedVariable<T>
```

创建@StorageLink状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| propName | string | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| [initValue](arkts-arkui-decorator-envoptions-i.md) | T | 是 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IStorageLinkDecoratedVariable](arkts-arkui-decorator-istoragelinkdecoratedvariable-i.md)&lt;T&gt; |

## makeStoragePropRef

```TypeScript
makeStoragePropRef<T>(owner: IVariableOwner, propName: string,
    varName: string, initValue: T, watchFunc?: WatchFuncType): IStoragePropRefDecoratedVariable<T>
```

创建@Storage PropRef状态变量实例

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 是 |
| propName | string | 是 |
| [varName](arkts-arkui-decorator-idecoratedvariable-i.md) | string | 是 |
| [initValue](arkts-arkui-decorator-envoptions-i.md) | T | 是 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IStoragePropRefDecoratedVariable](arkts-arkui-decorator-istorageproprefdecoratedvariable-i.md)&lt;T&gt; |

## makeSubscribedWatches

```TypeScript
makeSubscribedWatches(): ISubscribedWatches
```

get subscribed watches

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [ISubscribedWatches](arkts-arkui-decorator-isubscribedwatches-i.md) |

## makeSyncMonitor

```TypeScript
makeSyncMonitor(pathInfos: IMonitorPathInfo[], monitorCallback: MonitorCallback,
    options?: MakeMonitorOptions): IMonitorDecoratedVariable
```

创建同步监控变量实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathInfos | [IMonitorPathInfo](arkts-arkui-decorator-imonitorpathinfo-i.md)[] | 是 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | 是 |
| options | [MakeMonitorOptions](arkts-arkui-decorator-makemonitoroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) |
